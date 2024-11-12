from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

# 定義泛型 T
T = TypeVar("T")


# 定義泛型 BaseAPIResponse 類別，繼承 Generic[T]
class BaseAPIResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    msg: Optional[str] = None
