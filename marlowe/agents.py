from dotenv import load_dotenv
from langchain.agents import create_agent
from utils.tools import tools
from utils.prompts import SYSTEM_PROMPT
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START
import uuid
import asyncio
import random


load_dotenv()

MODEL = "openai:gpt-5.5"
EVIDENCE_PHRASES = [
    "Gathering evidence...",
    "Digging for clues...",
    "Chasing a lead...",
    "Combing through the data...",
    "Following a hunch...",
]
checkpointer = InMemorySaver()

print(f"Starting agent... (model={MODEL}, tools={[t.name for t in tools]})")
agent = create_agent(
        model=MODEL, 
        tools=tools, system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer
    )


print("Agent ready. Ctrl+C to quit.")


async def ask(question: str, thread_id: str):
    
    async for chunk in agent.astream(
        {"messages": [{"role": "user", "content": question}]},
        {"configurable": {"thread_id": thread_id}}, stream_mode="updates"):
        node_name, data = next(iter(chunk.items()))

        if "messages" in data:
            latest_message = data["messages"][-1]
            if node_name == "model":
                if latest_message.content:
                    yield latest_message.content + "\n"
                for _ in latest_message.tool_calls:
                    random_number = random.randint(0, 4)
                    phrase = EVIDENCE_PHRASES[random_number]
                    yield f"{phrase}\n"


        else:
            yield f"[{node_name}] {data}\n"

async def main():
    thread_id = str(uuid.uuid4())
    while True:
        user_input = input("\nYou: ")

        async for event in ask(user_input, thread_id):
            print(event)


if __name__ == "__main__":
    asyncio.run(main())


    # print(f"\nAgent: {asyncio.run(ask(user_input, thread_id))}\n")