from website import db


class Data(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    gender = db.Column(db.String)
    lgbtqia_plus = db.Column(db.String)

    def __init__(self, city, gender, lgbtqia_plus):
        self.city = city
        self.gender = gender
        self.lgbtqia_plus = lgbtqia_plus

    def __repr__(self):
        return "<Data %r>" % self.id


class Traffic(db.Model):
    __tablename__ = "traffics"

    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String)
    url_route = db.Column(db.String)

    def __init__(self, section, url_route):
        self.section = section
        self.url_route = url_route

    def __repr__(self):
        return "<Traffic %r>" % self.id
        