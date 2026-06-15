# 导入 FastAPI 和 HTTPException（用于返回错误状态码）
from fastapi import FastAPI, HTTPException
# 从 pydantic 导入 BaseModel，用于定义请求体的数据结构
from pydantic import BaseModel

# 创建 FastAPI 应用实例
app = FastAPI()

# ========== 1. 定义一个 GET 接口（无参数）==========
# @app.get 表示这个接口只接受 HTTP GET 方法
@app.get("/hello")
def say_hello():
    """
    一个简单的 GET 接口，返回一句问候。
    """
    return {"message": "Hello, GET request!"}

# ========== 2. 定义一个 GET 接口，带查询参数 ==========
# 查询参数：URL 中 ?key=value 的部分，例如 /search?q=python&page=2
@app.get("/search")
def search_items(q: str, page: int = 1):
    """
    查询参数 q 是必需的（没有默认值），page 可选，默认值为 1。
    FastAPI 会自动从 URL 中提取同名参数。
    访问示例：/search?q=fastapi&page=3
    """
    return {"query": q, "page": page, "result": [f"结果1 for {q}", f"结果2 for {q}"]}

# ========== 3. 定义一个 Pydantic 模型（用于 POST 请求体）==========
# 继承 BaseModel，定义 JSON 请求体应该包含哪些字段及其类型
class Item(BaseModel):
    # 字段名: 类型 = 默认值（如果有默认值则为可选）
    name: str          # 必填，字符串
    price: float       # 必填，浮点数
    tax: float = None  # 可选，如果没有传则默认为 None

# ========== 4. 定义一个 POST 接口，接收 JSON 请求体 ==========
# @app.post 表示只接受 POST 方法
@app.post("/items/")
def create_item(item: Item):
    """
    请求体必须是 JSON 格式，且包含 name 和 price 字段（tax 可选）。
    FastAPI 会自动解析 JSON 并验证类型，然后赋值给 item 参数。
    """
    # 计算总价（价格 + 税费，如果 tax 存在）
    total = item.price + (item.tax if item.tax else 0)
    return {
        "message": f"商品 '{item.name}' 创建成功！",
        "price": item.price,
        "tax": item.tax,
        "total_price": total
    }

# ========== 5. 带路径参数 + 请求体的混合接口 ==========
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    路径参数 item_id 从 URL 中提取，请求体从 JSON body 中解析。
    演示混合使用。
    """
    # 模拟更新数据库中的商品
    return {
        "item_id": item_id,
        "updated_item": {
            "name": item.name,
            "price": item.price,
            "tax": item.tax
        }
    }

# ========== 6. 异常处理示例：当找不到资源时返回 404 ==========
# 这是一个模拟的数据库
fake_db = {
    1: {"name": "Laptop", "price": 5000},
    2: {"name": "Mouse", "price": 100}
}

@app.get("/items_db/{item_id}")
def get_item_from_db(item_id: int):
    """
    根据 ID 从模拟数据库中获取商品，如果不存在则返回 404 错误。
    """
    if item_id not in fake_db:
        # HTTPException 可以指定状态码和详细消息
        raise HTTPException(status_code=404, detail=f"商品 ID {item_id} 不存在")
    return fake_db[item_id]