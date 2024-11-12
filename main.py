from fastapi import FastAPI
from app.router.house import router

app = FastAPI()

# 路由註冊
app.include_router(router, prefix="/house", tags=["house"])
