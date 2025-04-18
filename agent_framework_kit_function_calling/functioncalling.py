import openai
import time
import json
from dotenv import load_dotenv
import os
from yfinance import Ticker

# Load environment variables from .env file
load_dotenv()

def get_stock_price(ticker: str) -> float:
    try: 
        print(f"Fetching stock data for {ticker}...")
        stock = Ticker(ticker)
        # Get historical data - use a longer period to ensure we get data
        hist = stock.history(period="5d")
        print(f"Data received: {hist.shape[0]} rows")

        if hist.empty:
            print("No data returned from endpoint")
            return None
        
        # Get the most recent closing price
        price = hist['Close'].iloc[-1]
        print(f"Raw price: {price}")
        return round(float(price), 2)
    except Exception as e:
        print(f"Error getting stock price: {e}")
        return None    

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
            "description": "Get stock price for the stock ticker for the company requested",
            "parameters": {
                "type": "object",
                "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker for the company. e.g. AAPL or Apple"
                }
                },
                "required": [
                    "ticker"
                ]
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

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Can you please provide the stock price of AAPL"}],
    tools=tools
)

# Process the response
response_message = completion.choices[0].message


# Check if there are any tool calls
if response_message.tool_calls:
    # Extract the tool calls
    tool_call = response_message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
    
    print(f"Function called: {function_name}")
    print(f"Arguments: {function_args}")
    
    # Execute the function
    if function_name == "get_stock_price":
        # Note: The parameter name in your tool definition is 'ticker' but in required you listed 'symbol'
        # Make sure these match or handle both cases
        ticker = function_args.get("ticker", "")
        if ticker:
            result = get_stock_price(ticker)
            print(f"The stock price of {ticker} is ${result}")
        else:
            print("No ticker symbol provided")
    elif function_name == "get_weather":
        # Implement weather function if needed
        location = function_args.get("location", "")
        print(f"Would get weather for {location} (not implemented)")


#completion = client.chat.completions.create(
#    model="gpt-4.1",
#    messages=[{"role": "user", "content": "Can you please tell me the weather in San Francisco"}],
#    tools=tools
#)

# print(completion.choices[0].message.tool_calls)