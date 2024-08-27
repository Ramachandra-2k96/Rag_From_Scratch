from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.llms.ollama_functions import OllamaFunctions

class Person(BaseModel):
    name : str = Field(description="""Name of the person""",required = True)
    hieght : float = Field(description="""the person's hieght in floating type""",required = True)
    hair_color : str = Field(description="""the person's hair color""")

context = """
Alex is a 5 feet tall.
Claudia is five times taller than Alex and jumps higher than he does.
Cludia is brunette and Alex is blonde."""

llama3_template =  '''<|begin_of_text|><|start_header_id|>system<|end_header_id|>
    you are a smart assistant take the following context and and question below and retrun answer in JSON.
    <|eot_id|> 
    <|start_header_id|>user<|end_header_id|>
    QUESTION:{question}\n
    CONTEXT:{context}\n
    JSON:
    <|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>'''

phi3_template = """<|user|>{context}
QUESTION:{question}<|end|>
<|assistant|>AI:"""
Prompt= PromptTemplate.from_template(# change this one according to model [ current one is for only llama family,Hermis family
   llama3_template)

llm = OllamaFunctions(
    model="hermes3",
    temperature=0,
    format = 'json',
)
structured_llm= llm.with_structured_output(Person)
chain = Prompt | structured_llm

response = chain.invoke({
    "question":"Who is taller?",
    "context":context
})    
for chunk in response:
    print(chunk,flush=True,end="")