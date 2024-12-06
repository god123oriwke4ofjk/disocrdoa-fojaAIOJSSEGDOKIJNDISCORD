import asyncio
import nest_asyncio
import botResponses

nest_asyncio.apply()

async def main():
    await botResponses.run_discord_bot()

if __name__ == "__main__":
    asyncio.run(main())
