def collect_profile(state):
    state["profile"] = {
        "age": state.get("age", 30),
        "goal": state.get("goal", "retirement"),
        "horizon": state.get("horizon", 25),
        "risk": state.get("risk", "medium")
    }

    return state