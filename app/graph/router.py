def route_decision(state):

    plan = state["plan"]

    if plan.get("route") == "retriever":
        return "retriever"

    return "validator"