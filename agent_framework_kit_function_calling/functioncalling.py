import openai
import time
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1 : Create an Assistant
# Assistants API is deprecated
# assistant = client.beta.assistants.create(
#    name="Business Analyst Agent",
#    instructions = "You are a Business Analyst agent "
#)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get stock price for the stock symbol for the company requested",
            "parameters": {
                "type": "object",
                "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker symbol for the company. e.g. AAPL or Apple"
                }
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia"
                    }
                },
                "required": [
                    "location"
                ],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

#completion = client.chat.completions.create(
#    model="gpt-4.1",
#    messages=[{"role": "user", "content": "Can you please provide the stock price of MSFT"}],
#    tools=tools
#)

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Can you please tell me the weather in San Francisco"}],
    tools=tools
)

print(completion.choices[0].message.tool_calls)