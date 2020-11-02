from . import db


class UserInfo(db.Model):
    __tablename__ = 'db_UserInfo'

    id = db.column(db.Integer, primary_key=True, autoincrement=True)
    username = db.column(db.String(40), nullabled=False)
    password = db.column(db.String(128), nullabled=False)
    state = db.column(db.String(4), nullabled=False)
    permit = db.column(db.Integer)
    phone = db.column(db.Integer)
    mail = db.column(db.String(40))
    free1 = db.column(db.Integer)
    free2 = db.column(db.String(20))
    free3 = db.column(db.String(60))

