from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app import Base




class User(Base):
    __bind_key__ = "User"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    nickname: Mapped[str] = mapped_column(String(24), nullable=False)
    password: Mapped[str] = mapped_column(String(48), nullable=False)
    email: Mapped[str] = mapped_column(String(48), nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    __tablename__ = "User"
    
    def __init__(self, id: int, nickname: str, password: str, email: str, is_superuser: bool):
        self.id: int = id
        self.nickname: str = nickname
        self.password: str = password
        self.email: str = email
        self.is_superuser: bool = is_superuser
    
    def __repr__(self) -> str:
        return f"[USER][id: {self.id}][nickname: {self.nickname}][password: {self.password}][email: {self.email}][is_superuser: {self.is_superuser}]"
    
    
class Post(Base):
    __bind_key__ = "Post"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(24), nullable=False)
    date: Mapped['datetime'] = mapped_column(DateTime, nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    __tablename__ = "Post"
    
    def __init__(self, id: int, title: str, date: datetime, text: str):
        self.id: int = id
        self.title: str = title
        self.date: datetime = date
        self.text: str = text
        
    def __repr__(self) -> str:
        return f"[POST][id: {self.id}][title: {self.title}][date: {self.date}][text: {self.text}]"
       
        
class Tag(Base):
    __bind_key__ = "Tag"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String(24), nullable=False)
    __tablename__ = "Tag"
    
    def __init__(self, id: int, title: str):
        self.id: int = id
        self.title: str = title
    
    def __repr__(self) -> str:
        return f"[TAG][id: {self.id}][title: {self.title}]"


class ItemTag(Base):
    __bind_key__ = "ItemTag"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, nullable=False, unique=True)
    item_id: Mapped[int]
    tag_id: Mapped[int]
    __tablename__ = "ItemTag"
    
    def __init__(self, id: int, item_id: int, tag_id: int):
        self.id: int = id
        self.item_id: int = item_id
        self.tag_id: int = tag_id
        
    def __repr__(self) -> str:
        return f"[ITEM TAG][id: {self.id}][item id: {self.item_id}][tag id {self.tag_id}]"
        