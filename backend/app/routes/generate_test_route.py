# main.py
import os
from fastapi import APIRouter
import requests  # or any other library to call the Gemini API
from google import genai
import httpx
from dotenv import load_dotenv
from app.models.PromptRequest import PromptRequest

app = APIRouter()

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@app.post("/gemini-prompt")
async def generate_test_cases(request: PromptRequest):

    async with httpx.AsyncClient() as client:
        prompt = f"""
                    Based on the following swagger contract, generate comprehensive test cases in {request.language} and dont give me any extra text just the test cases so that i can just copy and paste into a file.:
                    Give the response in markdown.
                    
                    {request.contract}

                    Please include:
                    1. Input validation tests
                    2. Edge case scenarios
                    3. Expected responses
                    4. Error handling cases

                    Make sure to not give anything such as ``` python ``` at the start or the end of the response. 

                """
        # if you have a gpt model key use this code
        # insert the gpt key in a env file and load it here
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        # response = openai.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=prompt,
        #     temperature=0.5,
        #     stream=True,
        # )
        # print(response.choices[0].message.content)

        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-1.5-flash", contents=prompt
        )

        return response.text.removeprefix(f"```{request.language}\n").removesuffix(
            "\n```\n"
        )
