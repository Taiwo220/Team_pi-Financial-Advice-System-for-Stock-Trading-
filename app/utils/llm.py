import openai
import os
import logging
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    logging.error("❌ OpenAI API Key is missing! Make sure it's set in the .env file.")

def generate_financial_advice(query, retrieved_news):
    """
    Uses an LLM to generate financial advice based on retrieved news.
    """
    prompt = f"""
    You are a financial analyst providing stock trading advice.
    
    User Query: "{query}"
    
    Here are the latest stock news articles relevant to the query:
    {retrieved_news}

    Based on this, analyze whether the user should buy, sell, or hold the stock.
    Provide clear reasons, advantages, and risks.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use GPT-4 or another model
            messages=[{"role": "system", "content": "You are a financial expert."},
                      {"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        logging.error(f"❌ LLM Error: {e}")
        return "Sorry, I couldn't generate advice due to an error."
