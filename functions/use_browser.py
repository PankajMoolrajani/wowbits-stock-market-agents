import asyncio
import select
import sys

from dotenv import load_dotenv
from browser_use import Agent, Browser, ChatOpenAI

load_dotenv()

PAUSED = False

async def run():
    print("\n=== BrowserUse CLI Agent ===\n")
    task = input("Enter task for the browser agent:\n> ")

    browser = Browser(
        headless=False  # IMPORTANT: visible browser so user trusts it
    )

    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser=browser,
    )

    print("\nAgent started.")
    print("Commands during run:")
    print("  [p] pause")
    print("  [r] resume")
    print("  [i] add instruction")
    print("  [q] quit\n")

    agent_task = asyncio.create_task(agent.run())

    while not agent_task.done():
        await asyncio.sleep(1)

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            cmd = sys.stdin.readline().strip().lower()

            if cmd == "p":
                print("\n⏸ Pausing agent...")
                agent.pause()
                print("Agent paused.")

            elif cmd == "r":
                print("\n▶️ Resuming agent...")
                agent.resume()
                print("Agent resumed.")

            elif cmd == "i":
                extra = input("\nEnter additional instruction:\n> ")
                print(f"📌 Injecting instruction: {extra}")
                agent.add_new_task(extra)

            elif cmd == "q":
                print("\n🛑 Stopping agent...")
                agent.stop()
                break

    print("\n✅ Agent finished.")
    await browser.stop()

if __name__ == "__main__":
    asyncio.run(run())
