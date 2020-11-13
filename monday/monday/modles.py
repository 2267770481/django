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


class Company(db.Model):
    __tablename__ = "company"

    name = db.Column(db.String(20), primary_key=True)
    location = db.Column(db.String(20))

    def __repr__(self):
        return "name:{0} location:{1}".format(self.name, self.location)


class Phone(db.Model):
    __tablename__ = "phone"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(32))
    price = db.Column(db.String(32))
    company_name = db.Column(db.String(20), db.ForeignKey('company.name'))  # 创建与company.name关联的外键
    company = db.relationship("Company", backref="phone_of_company")  # 使用orm查询是可通过 正向查询和反向查询 直接获取类外一张表的数据
