from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import monday

app = monday.create_app()

CSRFProtect(app)  # 增加csrf校验

db = SQLAlchemy(app)
manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    from monday.modles import UserInfo

    db.create_all()  # 需要先导入modles模块中的类 才能在执行 python manage.py db init 的时候生成表
    manage.run()
