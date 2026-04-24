# 🎬 Seko AI 视频创作工具

> 通过 FastAPI 提供 REST API 服务，支持视频策划案和视频生成

## 🚀 快速部署

### 方式一：Docker 部署（推荐）

```bash
# 1. 克隆仓库
git clone https://github.com/wyjm/shipin.git
cd shipin

# 2. 配置环境变量
export SEKO_API_KEY=Seko-xxxxxxxx

# 3. 构建并运行
docker build -t seko-ai-video .
docker run -d -p 8000:8000 -e SEKO_API_KEY=Seko-xxxxxxxx seko-ai-video
```

### 方式二：直接运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
export SEKO_API_KEY=Seko-xxxxxxxx

# 3. 启动服务
uvicorn api:app --host 0.0.0.0 --port 8000
```

## 📡 API 端点

### 健康检查
```bash
GET /api/health
```

### 生成策划案
```bash
POST /api/generate_proposal
Content-Type: application/json

{
  "prompt": "体检报告科普视频，可爱Q版3D画风",
  "api_key": "Seko-xxxxxxxx"  // 可选，使用环境变量则不需要
}
```

### 查询策划案
```bash
POST /api/get_proposal
Content-Type: application/json

{
  "task_id": "任务ID",
  "wait": true,
  "interval": 20
}
```

### 生成视频
```bash
POST /api/generate_video
Content-Type: application/json

{
  "doc_id": "策划案ID"
}
```

### 查询视频
```bash
POST /api/get_video
Content-Type: application/json

{
  "task_id": "任务ID",
  "wait": true,
  "interval": 30
}
```

## 📂 项目结构

```
shipin/
├── api.py              # FastAPI 服务
├── Dockerfile          # Docker 配置
├── requirements.txt    # Python 依赖
├── scripts/            # 核心脚本
│   ├── gen_proposal.py
│   ├── get_proposal.py
│   ├── gen_video.py
│   └── get_video.py
└── README.md
```

## ⚠️ 重要配置

- **SEKO_API_KEY**：必须配置，可在环境变量或请求中提供
- **端口**：默认 8000，可通过 PORT 环境变量修改
- **项目目录**：默认 `./project`，可通过 project_dir 参数修改

## 📄 许可证

MIT License