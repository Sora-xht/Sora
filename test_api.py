# test_api.py
import requests

def test_get_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200  # 验证状态码
    data = response.json()
    assert data['id'] == 1  # 验证返回数据的ID