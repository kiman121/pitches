from app import create_app, db
from flask_script import Manager, Server
from app.models import User,Category,Post,Comment
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')
manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.before_first_request
def create_tables():
    db.create_all()

@manager.command
def test():
    '''
    Run the unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    '''
    Function that allows us to pass properties into the shell context.
    '''
    return dict(app=app, db=db, User=User, Category=Category, Comment=Comment, Post = Post)

if __name__ == '__main__':
    manager.run()
