from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
import json
json_schema = {
    "title":"Person",
    "description":"Identify information about a person",
    "type":"object",
    "properties":{
        "name":{"title":"Name","description":"the person's name","type":"string"},
        "age":{"title":"Age","description":"the person's age","type":"integer"},
        "fav_food":{
            "title":"Fav_Food",
            "description":"the person's favorite food",
            "type":"string"
            },
    },
    "required":['name','age','fav_food'],
}

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    format="json",
    max_new_tokens =512
)
messages = [
    HumanMessage(
        content="Please tell me about a person using the following Json schema: "
    ),
    HumanMessage(content="{schema}"),
    HumanMessage(
        content="tell me  about a person named Jhon who is 35 years old and loves pizza."
    )
]

prompt = ChatPromptTemplate.from_messages(messages=messages)
dumps = json.dumps(json_schema,indent=2)
chain = prompt | llm | JsonOutputParser()
result = chain.invoke({"schema":dumps})
print(result)