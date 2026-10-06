from config import llm


def suggest_allocation(state):

    profile = state["profile"]

    prompt = f"""
Role:
You are a financial planning assistant with expertise in long-term investing
and portfolio construction.

Your job is to provide simple, educational asset-allocation guidance.

Do not present the recommendation as guaranteed or as a substitute for
advice from a qualified financial professional.

User Profile:
- Age: {profile['age']}
- Goal: {profile['goal']}
- Investment Horizon: {profile['horizon']} years
- Risk Tolerance: {profile['risk']}

Task:
Suggest an educational asset allocation across:

- Stocks
- Bonds
- Cash

Important:
- Percentages must add up to exactly 100%.
- Consider age, goal, investment horizon and risk tolerance.
- Keep the explanation simple.

Output:
Return the allocation in a simple table followed by a brief explanation.
"""

    suggestion = llm.invoke(prompt)

    state["allocation"] = suggestion.content

    return state