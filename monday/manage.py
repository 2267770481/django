from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from dev.modles import UserInfo
import dev


app = dev.create_app()
manage = Manager(app)
Migrate(app, dev.db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    dev.db.create_all()     # 需要先导入modles模块中的类 才能在执行 python manage.py db init 的时候生成表
    manage.run()
