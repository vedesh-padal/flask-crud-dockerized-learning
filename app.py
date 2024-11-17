from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disabling event system to save memory
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
          return {'id': self.id, 'username': self.username, 'email': self.email}
    

with app.app_context():
    db.create_all()

def create_response(data=None, message=None, status=200):
    response = {'status': 'success' if status < 400 else 'error'}
    if data is not None:
        response['data'] = data
    if message is not None:
        response['message'] = message
    return make_response(jsonify(response), status)


# create a test route
@app.route('/test', methods=['GET'])
def test():
    return create_response(message='Test route')

# create a user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email'):
        return create_response(message='Invalid input', status=400)

    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        return create_response(message='User with this username or email already exists', status=409)

    try:
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return create_response(message='User created', status=201, data=new_user.to_dict())
    except Exception as e:
        db.session.rollback()
        return create_response(message='Error creating user', status=500)
  
# get all users
@app.route('/users', methods=['GET'])
def get_users():
  try:
    users = User.query.all()
    return  make_response(jsonify({ 'users': [ user.json() for user in users]}), 200)
  
  except e:
    return make_response(jsonify({ 'message': 'error getting users'}), 500)
  
# get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({ 'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({ 'message': 'error getting user'}), 500)

# update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = request.get_json()
      user.username = data['username']
      user.email = data['email']
      db.session.commit()
      return make_response(jsonify({ 'message': 'user updated'}), 200)
    return make_response(jsonify({ 'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({ 'message': 'error updating user'}), 500)
  
# delete a user
@app.route('/users.<int:id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      db.session.delete(user)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({ 'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({ 'message': 'error deleting user'}), 500)
  
