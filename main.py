import os
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
    name="Fatima's Assistant",
    instructions="Write a story about this topic",
    model=model
)

if __name__ == "__main__":
    result = Runner.run_sync(assistant, "What is Skills?")
    print(result)

