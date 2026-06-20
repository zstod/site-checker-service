from db import create_db_tables
from scanner import start_scan
import asyncio

async def main():
    await start_scan()

if __name__ == "__main__":
    asyncio.run(main())