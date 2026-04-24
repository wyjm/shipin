# 🎬 Seko AI 视频创作工具集

> 通过 Python 脚本调用 Seko API 生成视频策划案和视频的 CLI 工具集

## 📖 简介

这是一个**本地命令行工具**，不是需要部署的 Web 服务。用户在自己的电脑上按需执行脚本，调用 Seko AI (seko.sensetime.com) 的 API 来生成视频策划案和 AI 视频。

**核心用途**：
- 📝 在本地生成影视策划案（故事、角色、场景、分镜）
- 🎬 生成 AI 视频
- 🖼️ 下载角色和场景素材图片

## 🔧 环境要求

- Python 3.7+
- 网络连接（访问 seko.sensetime.com）
- Seko API Key

## ⚙️ 配置步骤

### 1. 获取 SEKO API Key

1. 登录 [https://seko.sensetime.com](https://seko.sensetime.com)
2. 首页**左下角**点击 🦞 **Openclaw 入口**
3. 复制 API Key（格式：`Seko-xxxxxxxx`）

### 2. 配置 API Key

```bash
# 方式1：设置环境变量
export SEKO_API_KEY=Seko-xxxxxxxx

# 方式2：运行脚本时传入
python3 gen_proposal.py --prompt "主题" --seko_api_key "Seko-xxxxxxxx"
```

## 🚀 使用方法

### 1. 克隆仓库

```bash
git clone https://github.com/wyjm/shipin.git
cd shipin
```

### 2. 生成策划案

```bash
# 设置 API Key
export SEKO_API_KEY=Seko-xxxxxxxx

# 生成策划案
python3 scripts/gen_proposal.py --prompt "体检报告怎么看？科普小视频，可爱Q版3D画风"
```

输出示例：
```json
{"code":200,"data":{"taskId":"2047525792706523139","taskStatus":"RUNNING"}}
```

### 3. 查询策划案结果

```bash
python3 scripts/get_proposal.py \
  --taskid "2047525792706523139" \
  --wait \
  --download ./assets \
  --output proposal_result.json
```

### 4. 生成视频（需要先有策划案 docId）

```bash
python3 scripts/gen_video.py --docid "策划案ID"
```

### 5. 查询视频结果

```bash
python3 scripts/get_video.py \
  --taskid "视频任务ID" \
  --wait \
  --download ./output \
  --output video_result.json
```

## 📂 脚本说明

| 脚本 | 功能 |
|------|------|
| `gen_proposal.py` | 提交策划案生成任务 |
| `get_proposal.py` | 查询策划案结果，下载素材 |
| `gen_video.py` | 提交视频生成任务 |
| `get_video.py` | 查询视频结果，下载视频 |
| `modify_proposal.py` | 修改已有策划案 |
| `download_img.py` | 下载图片素材 |
| `download_video.py` | 下载视频文件 |

## 📁 输出结构

```
shipin/
├── assets/              # 角色/场景图片素材
│   ├── Q版小人.png
│   ├── 机器人医生.png
│   └── ...
├── outputs/             # 策划案和视频结果
│   ├── proposal_result.json
│   └── video_result.json
├── scripts/             # 工具脚本
└── README.md
```

## ⚠️ 注意事项

1. **本地使用**：这是本地 CLI 工具，不需要部署到服务器
2. **按需执行**：需要生成视频时运行脚本，不是持续运行的服务
3. **积分消耗**：视频生成会消耗 Seko 平台积分
4. **网络要求**：运行脚本时需要联网

## ❓ 常见问题

**Q: 这是一个 Web 服务吗？**
A: 不是，这是本地 CLI 工具集，下载到本地后运行脚本使用。

**Q: 需要部署到服务器吗？**
A: 不需要，直接在本地 Python 环境中运行脚本即可。

**Q: GitHub Actions 有什么用？**
A: 可选的 CI/CD 配置，不是必需的。不部署服务时可以忽略。

**Q: 积分不足怎么办？**
A: 登录 seko.sensetime.com 充值积分。

## 📄 许可证

MIT License

## 👤 作者

- GitHub: https://github.com/wyjm
- 官网: https://seko.sensetime.com