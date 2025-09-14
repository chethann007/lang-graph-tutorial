from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    number1: int
    operation: str
    number2: int
    result: str

def add_node(state: AgentState) -> AgentState:
    """This node is for adding the numbers"""

    state['result'] = f"The sum of the numbers are: {state['number1'] + state['number2']}"
    return state


def subtract_node(state: AgentState) -> AgentState:
    """This node is for subtracting the numbers"""

    state['result'] = f"The difference of the numbers are: {state['number1'] - state['number2']}"
    return state

def decision_node(state: AgentState) -> AgentState:
    """This is a router node"""

    if state['operation'] == "+":
        return "addition_node"
    
    elif state['operation'] == "-":
        return "subtraction_node"
    
graph = StateGraph(AgentState)
graph.add_node("add_node", add_node)
graph.add_node("subtract_node", subtract_node)
graph.add_node("router", lambda state: state) #This is a pass through function
graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router",
    decision_node,
    {
        "addition_node": "add_node",
        "subtraction_node": "subtract_node"
    }
    )
graph.add_edge("add_node", END)
graph.add_edge("subtract_node", END)

app = graph.compile()
result1 = app.invoke({"number1": 10, "operation": "+", "number2": 20})
result2 = app.invoke({"number1": 30, "operation": "-", "number2": 20})
print(result1['result'])
print(result2['result'])

#You can comment this out if you don't have the need to generate the image of the state graph
graph_image = app.get_graph().draw_mermaid_png()
with open("conditional_graph.png", "wb") as f:
    f.write(graph_image)
print("The graph image is generated")