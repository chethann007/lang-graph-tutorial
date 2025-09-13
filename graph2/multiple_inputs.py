from typing import TypedDict, List
from langgraph.graph import StateGraph
from IPython.display import Image, display

class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str

def process_values(state: AgentState) -> AgentState:
    """This is a function which handles diffrent input"""

    state["result"] = f"Hi there {state["name"]}! Your sum = {sum(state["values"])}"
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process_values)
graph.set_entry_point("process")
graph.set_finish_point("process")
app = graph.compile()
result = app.invoke({"values": [1, 2, 3, 4], "name": "John"})
print(result["result"])

#You can comment this out if you don't have the need to generate the image of the state graph
graph_image = app.get_graph().draw_mermaid_png()
with open("graph_output.png", "wb") as f:
    f.write(graph_image)
print("Graph image saved as graph_output.png")