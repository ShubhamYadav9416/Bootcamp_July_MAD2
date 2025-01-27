from flask import jsonify
import secrets
from werkzeug.security import generate_password_hash
from flask_restful import Resource, reqparse


from application.data.model import db,User, Role, UserRoles

user_post_args = reqparse.RequestParser()
user_post_args.add_argument('user_mail', type = str, required = True, help="User mail is required")
user_post_args.add_argument('password', type=str, required = True, help= "password is required")
user_post_args.add_argument('role', type= str, required = True, help= "role is required")


class RegisterAPI(Resource):
    def post(resource):
        print("hello")
        args = user_post_args.parse_args()
        user_mail = args.get("user_mail")
        password = args.get("password")
        role = args.get("role")
        
        user = User.query.filter_by(user_mail = user_mail).first()
        if user:
            return jsonify({'status': 'failed', 'message': ' Mail is already registered'})
        user_role = Role.query.filter_by(name = role).first()
        if user_role is None:
            return jsonify({'status': 'failed', 'message': ' Role is not there'})
        
        hash_password = generate_password_hash(password)
        
        new_user = User(user_mail = user_mail, password = hash_password)
        new_user.roles.append(user_role)
        new_user.fs_uniquifier = secrets.token_hex(16)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'status': 'success', 'message': 'Successfully created a new user'})
        


# {
#   "user_mail": "user1@gmail.com",
#   "password": "1234",
#   "role":"watcher" 
# }
        