from flask import jsonify
import secrets
from werkzeug.security import check_password_hash
from flask_security import login_user
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


from application.data.model import db,User, Role, UserRoles

user_post_args = reqparse.RequestParser()
user_post_args.add_argument('user_mail', type = str, required = True, help="User mail is required")
user_post_args.add_argument('password', type=str, required = True, help= "password is required")


class LoginAPI(Resource):
    def post(resource):
        args = user_post_args.parse_args()
        user_mail = args.get("user_mail")
        password = args.get("password")
        
        user = User.query.filter_by(user_mail = user_mail).first()
        
        if user is None:
            return jsonify({'status': 'failed', 'message': ' Mail is not registered'})
        
        
        if not check_password_hash(user.password, password):
            print("user password wrong")
            return jsonify({'status': 'failed', 'message': 'password is wrong'})
        
        refresh_token = create_refresh_token(identity= user.user_id)
        access_token = create_access_token(identity=user.user_id)
        
        
        
        login_user(user)
        
        # user_role = UserRoles.get.join(User, UserRoles.user_id == user.user_id).join(Role, UserRoles.role_id == Role.role_id).add_columns(Role.name)
        
        return jsonify({'status': 'sucess', 'message': 'Sucessfully logged in', "refresh_token": refresh_token, "access_token":access_token, "user_id": user.user_id, "user_mail": user.user_mail, "role": user.roles[0].name})
        
        
        
class RefreshTokenAPI(Resource):
    @jwt_required(refresh=True)
    def post(resource):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {'access_token':access_token}, 200