from typing import TypedDict, List
from langgraph.graph import StateGraph
import math

class AgentState(TypedDict):
    name: str
    operation: str
    values: List[int]
    result: str
    

def operation_process_node(state: AgentState) -> AgentState:
    """This simple function process the list in accordance with the operation value"""

    if state["operation"] == "+":
        state["result"] = f"Hi {state['name']}! The operand that you provided is {state['operation']} and the sum is {sum(state["values"])}"
    elif state["operation"] == "*":
        state["result"] = f"Hi {state['name']}! The operand that you provided is {state['operation']} and the product is {math.prod(state["values"])}"
    return state
    
graph = StateGraph(AgentState)
graph.add_node("process_operation", operation_process_node)
graph.set_entry_point("process_operation")
graph.set_finish_point("process_operation")
app = graph.compile()

result = app.invoke({"name": "Jack", "operation": "*", "values": [1, 2, 3, 4]})
print(result["result"])