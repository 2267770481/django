from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
import dev

app = dev.create_app()
manage = Manager(app)
Migrate(app, dev.db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
