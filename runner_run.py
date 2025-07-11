import os
import asyncio
from agents import Agent , Runner , OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.0-flash"

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
        model=MODEL_NAME,
        openai_client=external_client,
    )

assistant = Agent(
    name="Help for education",
    instructions="Explain in detailed",
    model=model
)

async def main():
    result = await Runner.run(assistant, "What is the Education")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())