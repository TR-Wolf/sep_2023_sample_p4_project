#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Login (Resource) :
    def post (self) :
        username = request.get_json().get('username')
        password = request.get_json().get('password')

        user = User.query.filter( User.username.like( f'{ username }' ) ).first()

        if user and user.authenticate( password ) :
            session[ 'user_id' ] = user.id
            # print( session[ 'user_id' ] )
            return user.to_dict(), 200
        else :
            return { 'errors':['Invalid username or password.'] }, 401

class Logout (Resource) :
    def delete (self) :
        session[ 'user_id' ] = None
        return {}, 204

class SignUp (Resource) :
    def post (self):
        username = request.get_json().get('username')
        password = request.get_json().get('password')

        try:
            new_user = User(
                username = username,
                password_hash = password
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(), 201
        except:
            return {"Validation Error":"Recieved info was malformed" }, 204

api.add_resource( Login, '/login')
api.add_resource( Logout, '/logout')
api.add_resource( SignUp, '/signup')

# api.add_resource( Login, '/login', endpoint = 'login' )
# api.add_resource( Login, '/logout', endpoint = 'logout' )


if __name__ == '__main__':
    app.run(port=5555, debug=True)

