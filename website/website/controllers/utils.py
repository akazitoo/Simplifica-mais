from website import db
from website.models.tables import Data

def insert_data(city, gender, initials) -> None:

    insert_data = Data(city.lower(), gender.lower(), initials.lower())
    db.session.add(insert_data)
    db.session.commit()
    