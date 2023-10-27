from .. import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
        }