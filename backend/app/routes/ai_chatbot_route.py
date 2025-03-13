import os
from fastapi import APIRouter
import requests  # or any other library to call the Gemini API
from google import genai
import httpx
from dotenv import load_dotenv
from app.models.ChatAiContent import ChatContent

app = APIRouter()

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@app.post("/chat-ai")
async def generate_test_cases(request: ChatContent):

    async with httpx.AsyncClient() as client:
        prompt = f"""
                    If any user asks about you or greets you with Hi or Hello 
                    then You are TestGenie a Chat AI developed by 
                    prakhar kabra (a software engineer) and if user is asking another question then answer normally 
                    don't include your introduction in your response, the message by user is enclosed 
                    under ***user message***. 
                    Here is the user message: ***Explain the following : {request.message} ***"

                """

        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-1.5-flash", contents=prompt
        )
        print(response.text)
        return response.text
