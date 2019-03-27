import os
from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Role


app = create_app(os.getenv('SAFP_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
