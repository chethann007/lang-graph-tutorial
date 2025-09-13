# This is a simple example which demonstrates how to create an AgentState which is a shared data structure
# that keeps a track of information as your application runs.

from typing import TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict): # State schema
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """A simple node that adds a greeting message to the state."""

    state['message'] = "Hey " + state['message'] + " how are you doing?"
    return state

graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result = app.invoke({"message": "Bob"})

print(result["message"])