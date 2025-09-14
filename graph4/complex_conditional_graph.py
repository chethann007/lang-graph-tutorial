from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    number1: int
    operation1: str
    number2: int
    finalNumber1: int
    number3: int
    operation2: str
    number4: int
    finalNumber2: int

def add_node1(state: AgentState) -> AgentState:
    """This node is for adding the numbers"""

    state['finalNumber1'] = state['number1'] + state['number2']
    return state

def add_node2(state: AgentState) -> AgentState:
    """This node is for adding the numbers"""

    state['finalNumber2'] = state['number3'] + state['number4']
    return state


def subtract_node1(state: AgentState) -> AgentState:
    """This node is for subtracting the numbers"""

    state['finalNumber1'] = state['number1'] - state['number2']
    return state


def subtract_node2(state: AgentState) -> AgentState:
    """This node is for subtracting the numbers"""

    state['finalNumber2'] = state['number3'] - state['number4']
    return state

def decision_node1(state: AgentState) -> AgentState:
    """This is a router node"""

    if state['operation1'] == "+":
        return "addition_operation1"

    elif state['operation1'] == "-":
        return "subtraction_operation1"
    
def decision_node2(state: AgentState) -> AgentState:
    """This is a router node"""

    if state['operation2'] == "+":
        return "addition_operation2"

    elif state['operation2'] == "-":
        return "subtraction_operation2"
    
graph = StateGraph(AgentState)
graph.add_node("add_node1", add_node1)
graph.add_node("add_node2", add_node2)
graph.add_node("subtract_node1", subtract_node1)
graph.add_node("subtract_node2", subtract_node2)
graph.add_node("router1", lambda state: state)
graph.add_node("router2", lambda state: state)
graph.add_edge(START, "router1")
graph.add_conditional_edges(
    "router1",
    decision_node1,
    {
        "addition_operation1": "add_node1",
        "subtraction_operation1": "subtract_node1"
    }
)
graph.add_edge("add_node1", "router2")
graph.add_edge("subtract_node1", "router2")
graph.add_conditional_edges(
    "router2",
    decision_node2,
    {
        "addition_operation2": "add_node2",
        "subtraction_operation2": "subtract_node2"
    }
)
graph.add_edge("add_node2", END)
graph.add_edge("subtract_node2", END)

app = graph.compile()
result = app.invoke({"number1": 20, "operation1": "+", "number2": 20, "number3": 30, "operation2": "-", "number4": 30})
print(result["finalNumber1"])
print(result["finalNumber2"])


#You can comment this out if you don't have the need to generate the image of the state graph
graph_image = app.get_graph().draw_mermaid_png()
with open("conditional_graph2.png", "wb") as f:
    f.write(graph_image)
print("The graph image is generated")