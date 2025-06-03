# FlaskでAPIを作るならSwagger自動生成したい

[flask-openapi3](https://luolingchun.github.io/flask-openapi3/v4.x/) がとても良い

## 例外のとき

Validationに失敗したときは、一律で 422 を返す

## 他に検討した手段

### flagger

引数でValidateしたいのでやめた

```python
@app.route('/api/user', methods=['POST'])
def user_profile():

    try:
        data = request.get_json()
    ...
```

### flask_restx

flaggerよりはよさそうだが、やっぱり `get_json()`したくないのでやめた

```python
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
```