# 🎬 Seko AI 视频创作工具集

> 通过 Python 脚本调用 Seko API 生成视频策划案和视频

## 📖 简介

支持两种使用方式：

1. **本地 CLI 工具**：直接运行 Python 脚本
2. **API 服务**：部署为 FastAPI 服务

## ⚙️ 配置步骤

### 1. 获取 SEKO API Key

1. 登录 [https://seko.sensetime.com](https://seko.sensetime.com)
2. 首页**左下角**点击 🦞 **Openclaw 入口**
3. 复制 API Key（格式：`Seko-xxxxxxxx`）

### 2. 配置环境变量

```bash
export SEKO_API_KEY=Seko-xxxxxxxx
```

## 🚀 使用方法

### 方式一：本地 CLI 工具

```bash
# 克隆仓库
git clone https://github.com/wyjm/shipin.git
cd shipin

# 生成策划案
python3 scripts/gen_proposal.py --prompt "体检报告科普视频"

# 查询策划案
python3 scripts/get_proposal.py --taskid "任务ID" --wait

# 生成视频
python3 scripts/gen_video.py --docid "策划案ID"

# 查询视频
python3 scripts/get_video.py --taskid "任务ID" --wait
```

### 方式二：API 服务部署

```bash
# 1. 安装依赖
pip install fastapi uvicorn requests

# 2. 配置环境变量
export SEKO_API_KEY=Seko-xxxxxxxx

# 3. 启动服务
uvicorn api:app --host 0.0.0.0 --port 8000
```

#### API 端点

| 方法 | 端点 | 说明 |
|------|------|------|
| GET | `/` | 健康检查 |
| GET | `/api/health` | 服务状态 |
| POST | `/api/generate_proposal` | 生成策划案 |

#### 调用示例

```bash
# 生成策划案
curl -X POST http://localhost:8000/api/generate_proposal \
  -H "Content-Type: application/json" \
  -d '{"prompt": "体检报告科普视频", "api_key": "Seko-xxxxxxxx"}'
```

## 📂 项目结构

```
shipin/
├── api.py                   # FastAPI 服务入口
├── scripts/
│   ├── gen_proposal.py      # 生成策划案
│   ├── get_proposal.py      # 查询策划案
│   ├── gen_video.py         # 生成视频
│   ├── get_video.py         # 查询视频
│   └── ...
├── references/
│   └── config.md            # 配置指南
└── README.md
```

## ⚠️ 注意事项

- 视频生成会消耗 Seko 平台积分
- API 服务需要持续运行
- 本地 CLI 可按需执行

## 📄 许可证

MIT License

## 👤 作者

- GitHub: https://github.com/wyjm
- 官网: https://seko.sensetime.com