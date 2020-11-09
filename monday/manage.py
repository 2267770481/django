from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from monday import create_app, db

app = create_app()
manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    with app.app_context():     # 这个是为了解决在表单中使用了数据库查询
        from monday import modles  # 需要先导入modles模块中的类 才能在执行 python manage.py db init 的时候生成表
        db.create_all()
    manage.run()
