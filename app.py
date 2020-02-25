from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import ItemList, Item
from resources.store import StoreList, Store
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK__MODIFICATIONS'] = False
app.secret_key = 'aadi'

#create new end point /auth
# when we give credential its give to the authenticate and identity function
# jwt token
jwt = JWT(app, authenticate, identity)
api = Api(app)





api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList,'/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
