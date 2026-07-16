import requests

# 测试：获取第一篇文章，验证状态码和 ID
def test_get_single_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    # 断言 1：HTTP 状态码为 200（成功）
    assert response.status_code == 200
    # 将返回的 JSON 字符串转为 Python 字典
    data = response.json()
    # 断言 2：返回的数据中，id 字段等于 1
    assert data['id'] == 1

# 测试：创建一个新帖子，验证返回的数据
def test_create_post():
    # 准备要发送的数据（Python 字典）
    new_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    # 发送 POST 请求，json 参数会自动序列化字典
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_data)

    # 断言：创建成功通常返回 201 Created
    assert response.status_code == 201
    # 验证返回的数据中包含我们发送的 title
    response_data = response.json()
    assert response_data['title'] == "foo"
    import pytest

    # 参数化：给 test_get_post 传入不同的 post_id (1, 2, 3)
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_multiple_posts(post_id):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        assert response.status_code == 200
        data = response.json()
        # 验证返回的文章 ID 是否和传入的一致
        assert data['id'] == post_id