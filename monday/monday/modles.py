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


class SqlHelper:
    """
        sql = f"SELECT id, name from db_userinfo where username={'abc'}"
    """

    @staticmethod
    def fetch_one(sql, args=None):
        obj = db.session.execute(sql, args)
        return obj.fetchone()

    @staticmethod
    def fetch_all(sql, args=None):
        obj = db.session.execute(sql, args)
        return obj.fetchall()

    @staticmethod
    def update(sql, args):
        try:
            # 这里有问题， 不能检查错误
            res = db.session.execute(sql, args)
            print(res)
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def delete(self, sql, args):
        pass

    @staticmethod
    def insert(sql, args=None):
        try:
            res = db.session.execute(sql, args)
            db.session.commit()
        except:
            db.session.rollback()
