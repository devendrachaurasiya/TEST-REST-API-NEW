from app import app
from db import db

db.init_app(app)

# flask decorator
@app.before_first_request
def create_table():
    db.create_all()
	
	
	
	# This Code is not running pr
	# I did all changes