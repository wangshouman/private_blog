from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import DevelopementConfig
from info import db, create_app
from info import models

app = create_app(DevelopementConfig)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()