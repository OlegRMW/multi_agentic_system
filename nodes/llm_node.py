from states.chatstate import ChatState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage
import os  
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

def llm_node(state: ChatState) -> dict:
    
    load_dotenv()
            
    llm = ChatOpenAI(
        model="openai/gpt-4o-mini",
        api_key=os.getenv("ROUTERAI_API_KEY"),
        base_url="https://routerai.ru/api/v1",
        temperature=0
    )
    
    response = llm.invoke(state["messages"])
    
    print(response.content)
    print("-" * 50)
    
    new_messages = state["messages"] + [AIMessage(content=response.content)]
    
    return {"messages": new_messages}