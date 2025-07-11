import os
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
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


agent = Agent(
    name="Binte Sheilk's Cafe",
    instructions="Create a strategy for opening a cafe in easy english. The owner's name is Fatima Sheikh.",
    model=model
)


async def main():
    # await the run_streamed call
    stream = Runner.run_streamed(agent, "Create a complete plan to open a cafe.")

    print("\n🟡 Streaming Output:\n")
    async for event in stream.stream_events():
        if hasattr(event, 'data') and hasattr(event.data, 'delta'):
            print(event.data.delta, end="", flush=True)

    # After the stream is complete, just access .final_output
    print("\n\n✅ Final Output:\n")
    print(stream.final_output)

# Run the async function
asyncio.run(main())
