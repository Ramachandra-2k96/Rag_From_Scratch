import ollama

def call_Function(name):
    match name:
        case 1:
            return "Case 1"
        case 2:
            return "Case 2"
        case 3:
            return "Case 3"
        case _:
            return "Default Case"

tools = [
    {   
        'type': 'function',
        'function': {
            "name": "perform_math_operation",
            "description": "Perform a mathematical operation between two numbers",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": 'string',
                        "enum": ['add', 'subtract', 'multiply', 'divide'],
                        "description": "The mathematical operation to perform"
                    },
                    "a": {
                        "type": 'number',
                        "description": "The first number"
                    },
                    "b": {
                        "type": 'number',
                        "description": "The second number"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        }
    },
    {
        'type': 'function',
        'function': {
            "name": "search_recent_news",
            "description": "Search for recent news or get the current date, or information unknown to the LLM",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": 'string',
                        "description": "The search query for the news or information"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        'type': 'function',
        'function': {
            "name": "process_image",
            "description": "Process an image if the query is related to image tasks",
            "parameters": {
                "type": "object",
                "properties": {
                    "image_path": {
                        "type": 'string',
                        "description": "The file path to the image"
                    },
                    "operation": {
                        "type": 'string',
                        "enum": ['analyze', 'resize', 'filter'],
                        "description": "The operation to perform on the image"
                    }
                },
                "required": ["image_path", "operation"]
            }
        }
    },
    {
        'type': 'function',
        'function': {
            "name": "read_file",
            "description": "Read the content of a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": 'string',
                        "description": "The path to the file"
                    }
                },
                "required": ["file_path"]
            }
        }
    },
    {
        'type': 'function',
        'function': {
            "name": "simple_chat",
            "description": "Have a simple chat without invoking any special tools",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": 'string',
                        "description": "The message to respond to"
                    }
                },
                "required": ["message"]
            }
        }
    }
]
while True:
    querry = input("Your message => ")
    if querry.strip().lower() == 'exit':
        break
    response = ollama.chat(
        model = 'llama3.1',
        messages = [{'role':'user',"content":querry}],
        tools = tools,
        keep_alive=1   
    )
    print(response['message']['tool_calls'])