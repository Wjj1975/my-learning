# 导入 FastAPI 核心
from fastapi import FastAPI, Query, HTTPException
# 从 Pydantic 导入 BaseModel 和 Field（Field 用于给字段添加验证规则）
from pydantic import BaseModel, Field
# 从 typing 导入 Optional，用于声明可选字段（可以是 None）
from typing import Optional

# 创建应用实例
app = FastAPI()


# ========== 1. 定义请求体模型（使用 Field 添加字段级验证）==========
class Item(BaseModel):
    # Field(..., min_length=2) 表示：这个字段必须传，且字符串长度至少为 2
    name: str = Field(..., min_length=2, description="商品名称，至少2个字符")

    # Field(..., gt=0) 表示：必须传，且数值必须大于 0（gt = greater than）
    price: float = Field(..., gt=0, description="商品价格，必须大于0")

    # Field(None, ge=0) 表示：可选（默认 None），但如果传了，必须大于等于 0（ge = greater or equal）
    tax: Optional[float] = Field(None, ge=0, description="税费，可选，必须大于等于0")

    # 字符串类型，有默认值，且长度限制在 1 到 20 之间
    category: str = Field("未分类", min_length=1, max_length=20, description="商品类别")


# ========== 2. 实现大纲要求的 /create_item 接口（POST）==========
@app.post("/create_item/")
def create_item(item: Item):
    """
    接收一个 Item 类型的 JSON 请求体。
    如果数据不符合 Field 定义的规则（如 name 太短、price 为负数），
    FastAPI 会自动返回 422 错误，并告诉用户哪里错了。
    """
    # 计算总价（包含税费）
    total = item.price + (item.tax if item.tax else 0.0)

    # 返回创建成功的信息
    return {
        "message": f"商品 '{item.name}' 创建成功！",
        "category": item.category,
        "price": item.price,
        "tax": item.tax,
        "total_price": total,
        "status": "success"
    }


# ========== 3. GET 接口：演示查询参数验证 ==========
@app.get("/search_items/")
def search_items(
        # Query(...) 表示这是一个查询参数，必须传
        # min_length=3 表示 q 字符串长度至少为 3
        q: str = Query(..., min_length=3, max_length=50, description="搜索关键词"),

        # Query(1) 表示可选参数，默认值为 1，ge=1 表示必须大于等于 1
        page: int = Query(1, ge=1, description="页码，从1开始"),

        # Query(10) 表示可选，默认 10，le=100 表示最多 100 条
        size: int = Query(10, le=100, description="每页条数，最大100")
):
    """
    搜索商品接口。
    访问示例：/search_items/?q=电脑&page=2&size=5
    如果 q 少于 3 个字符，FastAPI 会自动返回错误提示。
    """
    # 模拟搜索逻辑
    results = [f"商品 {q} 的第 {i + 1} 条结果" for i in range(size)]
    return {
        "query": q,
        "page": page,
        "size": size,
        "total_results": len(results),
        "results": results
    }


# ========== 4. 额外演示：路径参数与查询参数混合 ==========
@app.get("/items_demo/{item_id}")
def get_item_by_id(
        item_id: int,  # 路径参数，没有验证装饰器时默认就是整数
        # 可选查询参数，用于是否显示详细信息
        include_details: bool = Query(False, description="是否显示详细描述")
):
    """
    演示路径参数 + 查询参数混合。
    访问示例：/items_demo/5?include_details=true
    """
    # 模拟数据库查询
    fake_item = {"id": item_id, "name": f"商品{item_id}"}

    if include_details:
        fake_item["details"] = "这是商品的详细描述信息"

    return fake_item