from app.query.house import HouseQuery
from app.schema.house import HouseSchema
from app.schema.base_response import BaseAPIResponse


class HouseLogic:
    @staticmethod
    def get_house(session):

        house = HouseQuery.get_house(session)
        result = [HouseSchema.model_validate(h).model_dump() for h in house]
        return BaseAPIResponse(success=True, data=result)
