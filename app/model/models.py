from sqlalchemy import Column, DateTime, Integer, text
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

Base: Any = declarative_base()


class House(Base):
    __tablename__ = "house"

    id = Column(Integer, primary_key=True, comment="房屋id")
    name = Column(VARCHAR(100), comment="房屋名稱")
    city = Column(VARCHAR(50), comment="城市")
    region = Column(VARCHAR(50), comment="地區")
    address = Column(VARCHAR(200), comment="地址")
    is_elevator = Column(TINYINT(1), server_default=text("'0'"), comment="是否有電梯")
    is_trailer = Column(TINYINT(1), server_default=text("'0'"), comment="是否有子母車")
    memo = Column(VARCHAR(100), comment="備註")
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    create_user = Column(Integer, nullable=False, server_default=text("'0'"))
    update_time = Column(DateTime)
    update_user = Column(Integer)
    is_cancel = Column(TINYINT, nullable=False, server_default=text("'0'"), comment="軟刪")
