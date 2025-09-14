from typing import TypedDict, List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: int
    skills: List[str]
    result: str

def first_node(state: AgentState) -> AgentState:
    """This is a simple function which process the name"""

    state['result'] = f"{state['name']}, welcome to the system!\n"
    return state

def second_node(state: AgentState) -> AgentState:
    """This is a simple function which process the age"""

    state['result'] = state['result'] + f"You are {state['age']} years old!\n"
    return state

def thrid_node(state: AgentState) -> AgentState:
    """This is a simple function which process the skills"""

    skills = state['skills']
    if len(skills) > 1:
        skill_str = ", ".join(skills[:-1]) + ", and " + skills[-1]
    elif skills:
        skill_str = skills[0]
    else:
        skill_str = "none"
    
    state['result'] = state['result'] + f"You have skills in: {skill_str}"
    return state

graph = StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("thrid_node", thrid_node)
graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "thrid_node")
graph.set_finish_point("thrid_node")

app = graph.compile()
result = app.invoke({"name": "Jack", "age": 23, "skills": ["Python", "AI/ML", "LangGraph"]})
print(result['result'])