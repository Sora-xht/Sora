import pytest
import requests
import json


# 读取外部数据
def load_test_data():
    with open('test_data.json', 'r') as f:
        return json.load(f)


# 动态生成参数
@pytest.mark.parametrize("post_data", load_test_data())
def test_get_post_from_json(post_data):
    """从 JSON 文件加载数据，验证文章信息"""
    post_id = post_data['id']
    expected_title = post_data['title']
    expected_user_id = post_data['userId']

    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200
    data = response.json()

    assert data['title'] == expected_title
    assert data['userId'] == expected_user_id