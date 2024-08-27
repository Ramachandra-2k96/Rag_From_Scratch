from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model = "hermes3",
    keep_alive = -1,
    temparature = 0.7,
    max_tokens = 2048)
prompt  = ChatPromptTemplate.from_template("Write a 100 letter essay on {topic} from the perspective of a {profession}. ")

chain = prompt | llm | StrOutputParser()
stream = chain.stream({"topic":"LLMs","profession":"shipping magnate"})
for c in stream:
    print(c,flush=True,end="")