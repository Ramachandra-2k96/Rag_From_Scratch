from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b

@tool
def subtract(a: int, b: int) -> int:
    """Subtracts a and b."""
    return a - b

@tool
def devide(a: float, b: float) -> float:
    """Devides a and b."""
    return a / b

def use_Internet(a:str)->str:
    """ Use internet if there is a shortage of information or anything related to upto date information"""
    return a

def date(a:str)->str:
    """ Tells todays date and time """
    return a

tools = [add, subtract, multiply, devide, use_Internet, date]

from langchain_ollama.chat_models import ChatOllama
model =ChatOllama(model="llama3.1")
llm_with_tools = model.bind_tools(tools)

query = "What is 3 * 12 + 11 - 49?"

print(llm_with_tools.invoke(query).tool_calls)