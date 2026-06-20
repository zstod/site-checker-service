from models import Users, Target, Result
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel

sqlite_url = f'postgresql+asyncpg://user:password193@db:5432/database'
engine = create_async_engine(sqlite_url, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_tables():
    async with engine.begin() as con:
        await con.run_sync(SQLModel.metadata.create_all)

async def start_session():
    async with async_session() as session:
        yield session