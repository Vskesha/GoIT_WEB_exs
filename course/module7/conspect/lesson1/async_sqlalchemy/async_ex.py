from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    AsyncEngine,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, select

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    articles = relationship("Article", back_populates="author")


engine: AsyncEngine = create_async_engine(
    "postgresql+asyncpg://user:password@host/database", echo=True
)
AsyncDBSession = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_user_by_name(name: str) -> User:
    async with AsyncDBSession() as session:
        result = await session.execute(select(User).where(User.name == name))
        user = result.scalars().first()
