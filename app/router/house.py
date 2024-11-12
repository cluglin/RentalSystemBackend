from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.logic.core.db_manager import create_session
from app.logic.house import HouseLogic
from app.schema.base_response import BaseAPIResponse
from app.router.router_tag import RouterTags

router = APIRouter()


@router.get("/", description="取得房屋列表", response_model=BaseAPIResponse, tags=[RouterTags.house])
def get_house(session: Session = Depends(create_session)):
    try:
        return HouseLogic.get_house(session)
    except Exception as e:
        print("取得房屋列表失敗: ", e)
        return BaseAPIResponse(success=False, msg="取得房屋列表失敗")
