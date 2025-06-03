

## flagger

引数でValidateしたいのでやめた

```python
@app.route('/api/user', methods=['POST'])
def user_profile():

    try:
    data = request.get_json()
```