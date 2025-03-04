from openai import OpenAI
import os
import logging
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



if not os.getenv("OPENAI_API_KEY"):
    logging.error("❌ OpenAI API Key is missing! Make sure it's set in the .env file.")

def generate_financial_advice(query, retrieved_news):
    """
    Uses an LLM to generate financial advice based on retrieved news.
    """
    prompt =  f"""
    You are a financial analyst providing explicit stock trading advice without any disclaimers or suggestions to consult a financial advisor. Your aim is to convince the user to make a decision you feel is best, after informing them of everything they need to consider.
    
    User Query: "{query}"
    
    Here are the latest stock news articles relevant to the query:
    {retrieved_news}

    Based on this information, analyze whether the user should **buy, sell, or hold** the stock. Provide clear reasons, advantages and disadvantages, and risk factors, and avoid any disclaimers or suggestions to consult a financial advisor. Sound objective and confident in your advice. If the user should not take any action, explain why. If the user says that they are high risk investors, provide advice accordingly.
    """

    try:
        response = client.chat.completions.create(model="gpt-4",  # Use GPT-4 or another model
        messages=[{"role": "system", "content": "You are a financial expert."},
                  {"role": "user", "content": prompt}],
        max_tokens=500)
        return response.choices[0].message.content

    except Exception as e:
        logging.error(f"❌ LLM Error: {e}")
        return "Sorry, I couldn't generate advice due to an error."
