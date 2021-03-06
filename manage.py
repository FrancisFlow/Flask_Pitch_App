from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Comment, Pitch
from flask_migrate import Migrate, MigrateCommand


app= create_app('test')

manager = Manager(app)
manager.add_command('server', Server)

migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Running the Unittests"""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

#creating shell context

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Comment=Comment, Pitch=Pitch)


if __name__ == '__main__':
    manager.run()