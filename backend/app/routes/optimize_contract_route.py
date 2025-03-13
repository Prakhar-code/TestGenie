import os
from fastapi import APIRouter
import requests  # or any other library to call the Gemini API
from google import genai
import httpx
from dotenv import load_dotenv
from app.models.OpmitizeContent import OptimizeContract

app = APIRouter()

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@app.post("/optimize-contract")
async def generate_test_cases(request: OptimizeContract):

    async with httpx.AsyncClient() as client:
        prompt = f"""
                    Based on the following swagger contract, generate optimized contract which i can just copy and paste into a file.:
                    json or yaml format
                    
                    Following is the swagger contract:

                    {request.contract}

                    Please include:
                    1. Versioning in the Endpoints
                    2. Missing Status codes which increases the contract score
                    3. Security 
                    4. Endpoint naming convention accorting to best practices
                    5. Include any necessary vaidation

                """

        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-1.5-flash", contents=prompt
        )

        return response.text
