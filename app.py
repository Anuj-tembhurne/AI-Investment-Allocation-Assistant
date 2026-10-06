from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Literal

from langgraph.graph import StateGraph

from collector import collect_profile
from suggest import suggest_allocation
from rec import recommend_assets


app = FastAPI(
    title="AI Investment Allocation Assistant",
    description="Educational investment allocation assistant using LangGraph and Groq",
    version="1.0"
)


templates = Jinja2Templates(directory="templates")


# -----------------------------
# LangGraph
# -----------------------------

graph = StateGraph(dict)

graph.add_node("profile", collect_profile)
graph.add_node("allocate", suggest_allocation)
graph.add_node("recommend", recommend_assets)

graph.set_entry_point("profile")

graph.add_edge("profile", "allocate")
graph.add_edge("allocate", "recommend")

graph.set_finish_point("recommend")

runnable = graph.compile()


# -----------------------------
# Request Model
# -----------------------------

class UserProfile(BaseModel):

    age: int
    goal: str
    horizon: int
    risk: Literal["low", "medium", "high"]


# -----------------------------
# Home Page
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

# -----------------------------
# Investment Recommendation API
# -----------------------------

@app.post("/recommend")
async def recommend(profile: UserProfile):

    state = {
        "age": profile.age,
        "goal": profile.goal,
        "horizon": profile.horizon,
        "risk": profile.risk
    }

    result = runnable.invoke(state)

    return {
        "profile": result["profile"],
        "allocation": result["allocation"],
        "recommendations": result["recommendations"]
    }