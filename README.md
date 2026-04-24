# 🎬 零克云 AI 应用视频制作工具

> 一站式 AI 视频创作工具，从剧本到成片全流程自动化

## ✨ 功能特点

- 📝 **自动生成策划案**：故事梗概、美术风格、角色场景、分镜剧本
- 🎬 **AI 视频生成**：支持 3D卡通、Q版、真实风格
- 🖼️ **角色场景设计**：自动生成角色和场景图片
- 📋 **完整项目管理体系**：任务队列、进度跟踪

## 🚀 快速开始

### 1. 获取 SEKO API Key

1. 登录 [https://seko.sensetime.com](https://seko.sensetime.com)
2. 首页**左下角**点击 🦞 **Openclaw 入口**
3. 复制你的 **API Key**（格式：`Seko-xxxxxxxx`）

### 2. 配置环境变量

在 零克云 AI应用 中配置：

```
SEKO_API_KEY = Seko-xxxxxxxx
```

> ⚠️ 将 `xxxxxxxx` 替换为你的实际 API Key

### 3. 本地开发配置

```bash
# 设置环境变量
export SEKO_API_KEY=Seko-xxxxxxxx

# 安装依赖（如需要）
pip install requests
```

## 📖 使用流程

### 完整创作流程

```
用户输入主题
    ↓
【Step 1】生成策划案
    ↓
确认策划案 → 修改（如需要）
    ↓
【Step 2】生成视频
    ↓
下载视频 → 完成
```

### 示例命令

#### 1. 生成策划案

```bash
python3 scripts/gen_proposal.py --prompt "体检报告怎么看？科普小视频，可爱Q版3D画风"
```

**成功响应**：
```json
{
  "code": 200,
  "data": {
    "taskId": "2047525792706523139",
    "taskStatus": "RUNNING"
  }
}
```

#### 2. 查询策划案结果

```bash
python3 scripts/get_proposal.py \
  --taskid "2047525792706523139" \
  --wait \
  --interval 20 \
  --download ./assets \
  --output ./proposal_result.json
```

#### 3. 生成视频

```bash
python3 scripts/gen_video.py --docid "策划案ID"
```

#### 4. 查询视频结果

```bash
python3 scripts/get_video.py \
  --taskid "视频任务ID" \
  --wait \
  --interval 30 \
  --download ./outputs \
  --output ./video_result.json
```

## 📂 项目结构

```
shipin/
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 部署
├── references/
│   └── config.md           # 配置指南
├── scripts/
│   ├── gen_proposal.py     # 生成策划案
│   ├── get_proposal.py     # 查询策划案
│   ├── gen_video.py        # 生成视频
│   ├── get_video.py        # 查询视频
│   ├── modify_proposal.py  # 修改策划案
│   ├── download_img.py     # 下载图片
│   └── download_video.py   # 下载视频
├── SKILL.md                # 技能文档
└── README.md                # 本文件
```

## 🎨 创作示例

### 示例1：生成科普视频

**输入**：
```
创作一个体检报告怎么看 的科普小视频，可爱Q版3D画风
```

**输出**：
- 完整策划案（故事、角色、场景、分镜）
- 55秒 AI 生成视频
- 11张角色/场景素材图片

### 示例2：生成短剧

**输入**：
```
创作一个关于亲情的科幻短剧，时长2分钟
```

## ⚠️ 常见问题

### Q1: API Key 怎么获取？

A: 登录 [seko.sensetime.com](https://seko.sensetime.com)，点击左下角 🦞 Openclaw 入口

### Q2: 提示"积分不足"怎么办？

A: 登录 Seko 平台充值积分

### Q3: 任务一直显示 RUNNING 怎么办？

A: 使用 `--wait` 参数等待任务完成

### Q4: 如何查看生成的素材？

A: 素材保存在 `{PROJECT_DIR}/assets/` 目录下

## 📞 获取支持

- **Seko 平台**：https://seko.sensetime.com
- **GitHub**：https://github.com/wyjm/shipin
- **零克云**：https://zerke.cloud

## 📄 许可证

MIT License

---

**Made with ❤️ for AI Video Creation**