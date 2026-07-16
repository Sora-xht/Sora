import requests  # ✅ 所有 import 必须放在文件最顶部
import pytest

# 测试：获取第一篇文章，验证状态码和 ID
def test_get():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1

# 测试：创建一个新帖子，验证返回的数据
def test_post():
    new_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['title'] == "foo"

# ✅ 修正：将参数化测试移到了 import 之后，现在它可以被正确识别和执行了
@pytest.mark.parametrize("post_id", [1, 2, 3,11])
def test_get_posts(post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == post_id


