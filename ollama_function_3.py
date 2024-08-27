from langchain_experimental.llms.ollama_functions import OllamaFunctions

# Initialize the model with the appropriate format
model = OllamaFunctions(
    model="mistral:instruct",
    format='json',
)

# Define the tools
tools = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": 'string',
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {
                    'type': 'string',
                    "enum": ['celsius', 'fahrenheit'],
                },
            },
            "required": ["location", "unit"],
        }
    },
    {
        "name": "simple_chat",
        "description": "Have a simple chat without invoking any special tools",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": 'string',
                    "description": "The message to respond to",
                }
            },
            "required": ["message"],
        }
    }
]

# Bind the tools to the model
model = model.bind_tools(tools=tools)

# Example: Asking about the weather in Singapore
response = model.invoke("What is the weather in Singapore?")

# Check if a tool was invoked and print the result
if response.tool_calls:
    print(f"Tool called: {response.tool_calls[0]['name']}")
    print(f"With arguments: {response.tool_calls[0]['args']}")
else:
    print(f"Model response: {response}")

# Example: Simple chat without invoking a tool
chat_response = model.invoke("How are you today?")

# Check if a tool was invoked and print the result
if chat_response.tool_calls:
    print(f"Tool called: {chat_response.tool_calls[0]['name']}")
    print(f"With arguments: {chat_response.tool_calls[0]['args']}")
else:
    print(f"Model response: {chat_response}")
