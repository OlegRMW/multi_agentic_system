from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage
from langgraph.graph import StateGraph, START, END
from states.chatstate import ChatState

from nodes.user_input_node import user_input_node
from nodes.check_interrupt_node import check_interrupt_node
from nodes.llm_node import llm_node


def main(): 
    
    print('Привет! Это ассистент по математике. Задавай вопросы и получай понятное объяснение.')
    print("-" * 50)
    
    graph = StateGraph(ChatState)
    
    graph.add_node("user_input_node", user_input_node)
    graph.add_node("check_interrupt_node", check_interrupt_node)
    graph.add_node("llm_node", llm_node)
  
    graph.add_edge(START, "user_input_node")
    graph.add_edge("user_input_node", "llm_node")
    graph.add_conditional_edges(
        "llm_node",
        check_interrupt_node,
        {
            "continue": "user_input_node",
            "end": END 
        }
    )
    graph.add_edge("llm_node", END)
    
    app = graph.compile()   
    
    initial_state = {
        "messages": [
            SystemMessage(
                '''Ты ассистент по математике. Твоя задача по условию задачи 
                последовательно расписывать план её решения по пунктам. Не стоит 
                углубляться в формулы, просто словестно описывай содержание каждого 
                пункта решения. На вопросы по задаче отвечай опираясь на ее условия не 
                выдумывая факты. Отвечай коротко и по делу. 
                '''
            )
        ],
        "should_continue": True 
    }
    
    try: 
        final_state = app.invoke(initial_state)
    except KeyboardInterrupt:
        print("\n\nЧат прерван пользователем (Ctrl+C)")
    except Exception as e:
        print(f"\nОшибка в работе чата: {e}")
    
if __name__ == "__main__":
    main()  