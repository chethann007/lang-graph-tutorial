from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    message: str

def compliment_node(state: AgentState) -> AgentState:
    """A simple node which adds a compliment message to the state."""

    state["message"] = state['name'] + " you're doing an amazing job learning LangGraph!"
    return state

graph = StateGraph(AgentState)
graph.add_node("compliment", compliment_node)
graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

result = app.invoke({"name": "Bob", "message": ""})

print(result["message"])