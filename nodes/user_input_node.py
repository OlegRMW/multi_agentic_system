from states.chatstate import ChatState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage


def user_input_node(state: ChatState) -> dict:
    
    user_input = input() 
    
    if user_input.lower() in ["выход", "quit", "exit", "пока", "bye"]:
        return {"should_continue": False}
    
    new_messages = state["messages"] + [HumanMessage(content=user_input)]
    
    return {"messages": new_messages, "should_continue": True}

