from dotenv import load_dotenv
from langchain.agents import create_agent
from utils.tools import tools
from utils.prompts import SYSTEM_PROMPT
from langgraph.checkpoint.memory import InMemorySaver
import uuid

load_dotenv()

MODEL = "openai:gpt-5.5"
checkpointer = InMemorySaver()

print(f"Starting agent... (model={MODEL}, tools={[t.name for t in tools]})")
agent = create_agent(
        model=MODEL, 
        tools=tools, system_prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer
    )


print("Agent ready. Ctrl+C to quit.")


def ask(question: str, thread_id: str):
    raw_result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        {"configurable": {"thread_id": thread_id}},
    )
    return raw_result["messages"][-1].content


if __name__ == "__main__":
    thread_id = str(uuid.uuid4())
    while True:
        user_input = input("\nYou: ")

        print(f"\nAgent: {ask(user_input, thread_id)}\n")
