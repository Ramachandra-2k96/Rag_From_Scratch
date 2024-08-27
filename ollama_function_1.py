"""
This module demonstrates the use of Langchain to generate a response based on a given context and question.

It uses the Ollama model to process the input and return a structured output in JSON format.
"""

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

# This block of code sets up the OllamaFunctions object with specific settings for the "hermes3" model.
# It also customizes the output format to be JSON and sets a structured output schema using the Person class defined earlier.
# Finally, it combines these settings with the PromptTemplate and uses them to create a chain that can be used to get answers from the OllamaFunctions object.

llm = OllamaFunctions(
    model="hermes3",
    temperature=0,
    format = 'json',
)
# The structured_llm variable is assigned an object of type llm.with_structured_output, where we're using the Person schema for structured output.
structured_llm= llm.with_structured_output(Person)

# Now, this PromptTemplate is used to create a chain that can be used to generate answers from the llm object
chain = Prompt | structured_llm

response = chain.invoke({
    "question":"Who is taller?",
    "context":context
})    
print(response)
