from flask import Flask, request, jsonify
from flask_restx_sample import Api, Resource, fields
from pydantic import BaseModel, Field, ValidationError



app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='A simple User API')
ns = api.namespace('api', description='User operations')



# Pydanticモデル定義
class UserProfile(BaseModel):
    name: str = Field(..., min_length=2, max_length=40, example='very_important_user')
    age: int = Field(..., ge=1, le=149, example=42)



# Flask-RESTXモデル（Swagger用、バリデーションはPydanticで行う）
user_profile_model = api.model('UserProfile', {
    'name': fields.String(required=True, min_length=2, max_length=40, example='very_important_user', description='User name'),
    'age': fields.Integer(required=True, min=1, max=149, example=42, description='User age'),
})



@ns.route('/user')
class UserProfileResource(Resource):
    @ns.expect(user_profile_model)
    @ns.response(200, '成功時のメッセージ', model=api.model('Success', {'text': fields.String(example='it works')}))
    @ns.response(400, 'バリデーションエラー', model=api.model('ValidationError', {'error': fields.String(example='Validation error')}))
    def post(self):
        """verify user profile (summary of this endpoint)
        user's name, user's age, ... (long description)
        """
        try:
            data = request.get_json()
            user = UserProfile(**data)
            return {'text': 'it works'}, 200
        except ValidationError as e:
            return {'error': e.errors()}, 400



if __name__ == "__main__":
    app.run(port=8000)