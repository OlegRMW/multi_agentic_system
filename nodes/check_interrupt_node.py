from states.chatstate import ChatState

def check_interrupt_node(state: ChatState) -> str:
    
    if state["should_continue"]:
        return "continue"
    
    return "end"


    