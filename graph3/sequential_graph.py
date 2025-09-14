from typing import TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image

class AgentState(TypedDict):
    name: str
    age: int
    final: str

def first_node(state: AgentState) -> AgentState:
    """This is the first node of the sequence"""

    state['final'] =  f"Hello {state['name']}! "
    return state

def second_node(state: AgentState) -> AgentState:
    """This is the second node of the sequence"""

    state['final'] =  state['final'] + f"You are {state['age']} years old!"
    return state

graph = StateGraph(AgentState)
graph.add_node("first_node",first_node)
graph.add_node("second_node", second_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.set_finish_point("second_node")

app = graph.compile()
result = app.invoke({"name": "Bob", "age": 20})
print(result['final'])

#You can comment this out if you don't have the need to generate the image of the state graph
graph_image = app.get_graph().draw_mermaid_png()
with open("sequential_graph.png", "wb") as f:
    f.write(graph_image)
print("The graph image is generated")