from app.model.models import House
from sqlalchemy.orm import Session


class HouseQuery:
    @staticmethod
    def get_house(session: Session):
        result = session.query(House).where(House.is_cancel == 0).all()
        return result
