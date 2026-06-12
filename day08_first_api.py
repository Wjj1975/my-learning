# 导入 FastAPI 类
from fastapi import FastAPI

# 创建 FastAPI 实例，app 是应用的核心对象
app = FastAPI()

# 使用装饰器 @app.get 定义一个 GET 请求的接口
# 路径为 "/"，即根路径，例如 http://127.0.0.1:8000/
@app.get("/")
def read_root():
    # 返回一个字典，FastAPI 会自动转换成 JSON 格式
    return {"message": "Hello, World!"}

# 定义带路径参数的接口
# 例如访问 http://127.0.0.1:8000/items/5
# {item_id} 是路径中的变量部分
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # item_id 从路径中提取，类型注解为 int
    return {"item_id": item_id, "description": "这是一个测试物品"}