from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
# from config import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from config import db, bcrypt
# Models go here!


class User (db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    username = db.Column( db.String, nullable = False )

    # ✅ Add a column _password_hash
    _password_hash = db.Column( db.String, nullable = False )
        # Note: When an underscore is used, it's a sign that the variable or method is for internal use.

    serialize_rules = ( '-_password_hash', )

    validation_errors = []

    @classmethod
    def clear_val_err(self):
        self.validation_errors.clear()
    # Password stuff for user model!
    # ✅ Create a hybrid_property that will protect the hash from being viewed
    @hybrid_property
    def password_hash ( self ) :
        return self._password_hash
    
    # ✅ Create a setter method called password_hash that takes self and a password.
        # Use bcyrpt to generate the password hash with bcrypt.generate_password_hash
        # Set the _password_hash to the hashed password
    @password_hash.setter
    def password_hash ( self, password ) :
        # from app import bcrypt
        if type( password ) is str and len( password ) in range( 6, 17 ) :
            password_hash = bcrypt.generate_password_hash( password.encode( 'utf-8' ) )
            self._password_hash = password_hash.decode( 'utf-8' )
        else :
            raise ValueError( "Password must be between 6-16 characters long." )

    # ✅ Create an authenticate method that uses bcyrpt to verify the password against the hash in the DB with bcrypt.check_password_hash 
    def authenticate ( self, password ) :
        # from app import bcrypt
        return bcrypt.check_password_hash( self._password_hash, password.encode( 'utf-8' ) )
    
    @validates( 'username' )
    def validate_username ( self, key, username ) :
        if type( username ) is str and username :
            return username
        else :
            raise ValueError( 'Username cannot be blank.' )

    # ✅ Navigate to app

    def __repr__(self):
        return f'< username:{self.username}'
