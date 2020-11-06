from manage import db


class UserInfo(db.Model):
    __tablename__ = 'db_UserInfo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(3), nullable=False)
    permit = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(40))
    free1 = db.Column(db.Integer)
    free2 = db.Column(db.String(20))
    free3 = db.Column(db.String(60))