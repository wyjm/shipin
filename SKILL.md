---
name: seko-ai-video
description: 一站式AI视频创作技能 - 从剧本到成片全流程自动化。通过 Seko AI (seko.sensetime.com) 实现影视策划案生成、AI视频生成、角色场景设计、分镜剧本等功能。支持3D卡通、Q版风格，适合科普视频、短剧、广告等创作。零克云 AI应用视频制作工具。
metadata:
  {
    "openclaw": {
      "requires": {
        "bins": ["python3"],
        "env": ["SEKO_API_KEY"]
      },
      "primaryEnv": "SEKO_API_KEY"
    },
    "zerke": {
      "version": "1.0.0",
      "category": "视频创作",
      "tags": ["AI视频", "一站式创作", "短剧生成", "科普视频", "SEKO"]
    }
  }
---

# Seko AI 视频创作技能

## 🎯 简介

一站式 AI 视频创作工具，通过 Seko AI (seko.sensetime.com) 实现从剧本到成片的全流程自动化。

**核心能力**：
- 📝 自动生成完整策划案（故事梗概、美术风格、角色场景、分镜剧本）
- 🎬 AI 视频生成（支持3D卡通、Q版、真实风格）
- 🖼️ 角色和场景图片生成
- 📋 完整的项目管理体系

## ⚙️ 配置步骤

### 第一步：获取 SEKO API Key

1. 登录 **https://seko.sensetime.com**
2. 首页**左下角**点击 🦞 **Openclaw 入口**
3. 复制你的 **API Key**（格式：`Seko-xxxxxxxx`）

### 第二步：配置环境变量

在 零克云 AI应用 中配置环境变量：

```
SEKO_API_KEY = Seko-xxxxxxxx
```

> ⚠️ 将 `xxxxxxxx` 替换为你的实际 API Key

### 第三步：完善设置

确保 零克云 平台已安装：
- Python 3 环境
- requests 库（`pip install requests`）

## 📁 项目结构

### 工作目录约定

- **PROJECT_DIR**：`{WORKSPACE}/$项目名`（项目文件存放处）
- **SKILL_DIR**：技能脚本路径

### 必需文件

1. **PLAN.md** - 项目骨干任务/里程碑（必需）
2. **TASK_QUEUE.md** - 异步任务队列（可选）

## 📜 工作流程

### 完整创作流程

```
用户输入主题
    ↓
【任务1】影视策划案生成
    ↓
策划案确认 → 修改（如需要）
    ↓
【任务2】AI视频生成
    ↓
视频确认 → 完成
```

### 任务1：影视策划案

#### Step 1 - 提交策划案任务

```bash
python3 {SKILL_DIR}/scripts/gen_proposal.py --prompt "你的创作主题"
```

**示例**：
```bash
python3 seko-ai-video/scripts/gen_proposal.py --prompt "体检报告怎么看？科普小视频，可爱Q版3D画风"
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

**失败响应**（如积分不足）：
```json
{"code": 500, "msg": "无效操作，积分不足"}
```

#### Step 2 - 查询策划案结果

```bash
python3 {SKILL_DIR}/scripts/get_proposal.py \
  --taskid "任务ID" \
  --wait \
  --interval 20 \
  --download {PROJECT_DIR}/assets \
  --output {PROJECT_DIR}/outputs/结果.json
```

**参数说明**：
| 参数 | 必填 | 默认值 | 说明 |
|------|------|--------|------|
| --taskid | ✅ | - | 任务ID |
| --seko_api_key | ❌ | 环境变量 | API密钥 |
| --interval | ❌ | 10 | 轮询间隔（秒） |
| --wait | ❌ | - | 持续等待直到完成 |
| --download | ❌ | ./assets | 资产下载目录 |
| --output | ❌ | $taskid_result.json | 结果保存文件 |

#### Step 3 - 阅读并确认策划案

策划案包含：
- **故事梗概**：核心剧情和亮点设计
- **美术风格**：画风、色彩、光影描述
- **主体列表**：角色及其生图提示词
- **场景列表**：场景及其生图提示词
- **分镜剧本**：完整镜头列表（含台词、构图、运镜）

### 任务2：AI视频生成

#### 提交视频生成任务

```bash
python3 {SKILL_DIR}/scripts/gen_video.py --docid "策划案ID"
```

**成功响应**：
```json
{
  "code": 200,
  "data": {
    "taskId": "2047527659272945666",
    "taskStatus": "RUNNING",
    "taskPhase": "SCRIPT_GEN"
  }
}
```

#### 查询视频结果

```bash
python3 {SKILL_DIR}/scripts/get_video.py \
  --taskid "任务ID" \
  --wait \
  --interval 30 \
  --download {PROJECT_DIR}/outputs \
  --output {PROJECT_DIR}/outputs/视频结果.json
```

## 🎨 使用示例

### 示例1：生成科普视频

**用户输入**：
```
创作一个体检报告怎么看 的科普小视频，可爱Q版3D画风
```

**执行流程**：
1. 生成策划案 → 用户确认
2. 生成视频 → 完成

### 示例2：生成短剧

**用户输入**：
```
创作一个关于亲情的科幻短剧，时长2分钟
```

## 📋 策划案数据结构

策划案返回的 `result` 结构：

```
data
├── taskId          # 任务ID
├── taskStatus      # 任务状态
├── result
│   ├── docId       # 策划案文档ID（生成视频用）
│   ├── docStatus   # 文档状态
│   ├── steps[]     # 策划步骤
│   │   ├── step          # 步骤名（outline/style_design/character_design/scene_design/storyboard）
│   │   ├── stepStatus    # 步骤状态（10=完成）
│   │   └── stepOutput    # 步骤输出内容
│   └── elements[]   # 资产元素
│       ├── elementType   # 类型（CHARACTER/SCENE）
│       ├── elementName   # 名称
│       ├── elementUrl    # 资产URL
│       └── transStatus   # 状态
```

## ⚠️ 注意事项

1. **API Key 配置**：必须正确配置 `SEKO_API_KEY`，否则无法使用
2. **积分管理**：视频生成需要积分，积分不足时会失败
3. **路径规范**：必须使用绝对路径，禁止相对路径
4. **任务队列**：异步任务需轮询查询结果，使用 `--wait` 参数自动等待
5. **策划案确认**：每个策划案步骤完成后需用户确认，再执行下一步

## 🔧 故障排除

### 问题1：SEKO_API_KEY 未设置

**错误**：
```
Error: SEKO_API_KEY not found
```

**解决**：配置环境变量 `SEKO_API_KEY=Seko-xxxxxxxx`

### 问题2：积分不足

**错误**：
```
{"code": 500, "msg": "无效操作，积分不足"}
```

**解决**：登录 Seko 平台充值积分

### 问题3：任务超时

**解决**：增加轮询间隔或使用更长等待时间

## 📞 获取支持

- Seko 平台：https://seko.sensetime.com
- API Key 获取：首页左下角 🦞 Openclaw 入口