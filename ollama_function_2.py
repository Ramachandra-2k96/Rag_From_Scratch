from langchain_experimental.llms.ollama_functions import OllamaFunctions

model = OllamaFunctions(
        model="mistral:instruct",
        format='json',
    )
model = model.bind_tools(
    tools=[
        {
            "name":"get_current_weather",
            "description":"Get the current weather in a give location",
            "parameters":{
                "type":"object",
                "properties":{
                    "location":{
                        "type":'string',
                        "description":"The city and state, e.g. San Francisco, CA",
                    },
                    "unit":{
                        'type':'string',
                        "enum":['celsius','fahrenheit'],
                    },
                },
                "required":["location","unit"],
            }
        }
    ],
)

response = model.invoke(" what is the weather in Singapore?")
print(response.tool_calls[0]['name'],"with arguments",response.tool_calls[0]['args'])