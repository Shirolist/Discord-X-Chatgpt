from dotenv import load_dotenv
import discord 
import os
import asyncio
import openai

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 1,
        max_token=2048
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
