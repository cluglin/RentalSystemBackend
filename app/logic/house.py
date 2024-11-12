from app.query.house import HouseQuery
from app.schema.house import HouseSchema


class HouseLogic:
    @staticmethod
    def get_house(session):

        house = HouseQuery.get_house(session)

        return [HouseSchema.model_validate(h).model_dump() for h in house]
