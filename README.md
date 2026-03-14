# FastAPI Demo Project

一个简单的 FastAPI REST API 示例项目，包含完整的 CI/CD 配置。

## 功能

- `/health` - 健康检查端点
- `/api/hello` - Hello 端点（支持 `name` 参数）

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务
uvicorn main:app --reload

# 或直接运行
python main.py
```

访问 http://localhost:8000/docs 查看 API 文档。

## 运行测试

```bash
pytest tests/ -v
```

## Docker

```bash
# 构建镜像
docker build -t fastapi-demo .

# 运行容器
docker run -p 8000:8000 fastapi-demo
```

## CI/CD 流程

1. **Test**: 每次 push/PR 自动运行测试
2. **Build**: main 分支合并后构建 Docker 镜像
3. **Deploy**: 自动部署到生产环境

## 项目结构

```
fastapi-demo/
├── main.py              # FastAPI 应用
├── requirements.txt     # Python 依赖
├── Dockerfile          # Docker 配置
├── README.md           # 项目说明
├── tests/
│   └── test_main.py    # 单元测试
└── .github/
    └── workflows/
        └── ci.yml      # CI/CD 配置
```
