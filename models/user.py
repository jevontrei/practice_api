# MODEL AREA
class User(db.Model):
    id = db.Column(db.Integer, primarykey=True)
    first_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = 
    is_admin = db.Column(db.Boolean, default=False)


# SCHEMA AREA
class UserSchema(db.Schema):
    ...
    # id = 


user_schema = UserSchema()
users_schema = UserSchema(many=True)
