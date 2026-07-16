import json

# Python 字典
data = {
    "title": "My Post",
    "body": "Content",
    "userId": 1
}

# 序列化为 JSON 字符串
json_string = json.dumps(data)
print(json_string)  # {"title": "My Post", "body": "Content", "userId": 1}
print(type(json_string))  # <class 'str'>