# Seko AI 视频创作 - 配置指南

## 零克云 AI应用视频制作工具 部署指南

### 一、Seko 平台注册与 API Key 获取

#### 1. 登录 Seko 官网
访问 **https://seko.sensetime.com** 并登录账户

#### 2. 获取 API Key
1. 登录后，在首页**左下角**找到 🦞 **Openclaw 入口**
2. 点击进入，即可看到你的 **API Key**
3. 复制 API Key（格式：`Seko-xxxxxxxx`）

> ⚠️ **注意**：API Key ，请勿泄露给他人

### 二、零克云环境变量配置

在 零克云 AI应用 部署时，需要配置以下环境变量：

| 环境变量 | 说明 | 必填 |
|----------|------|------|
| `SEKO_API_KEY` | Seko 平台 API Key | ✅ |

#### 配置示例：

```
SEKO_API_KEY = Seko-9b191eac04
```

### 三、本地开发配置

如果需要在本地测试，可以：

```bash
# 方式1：设置环境变量
export SEKO_API_KEY=Seko-xxxxxxxx

# 方式2：写入 .env 文件
echo 'SEKO_API_KEY=Seko-xxxxxxxx' > .env

# 方式3：在调用脚本时传入
python3 gen_proposal.py --prompt "主题" --seko_api_key "Seko-xxxxxxxx"
```

### 四、依赖安装

```bash
# 安装 Python 依赖（如果需要）
pip install requests
```

### 五、验证配置

配置完成后，可以运行测试：

```bash
python3 scripts/gen_proposal.py --prompt "测试"
```

正常情况下会返回：
```json
{
  "code": 200,
  "data": {
    "taskId": "xxx",
    "taskStatus": "RUNNING"
  }
}
```

### 六、积分说明

- Seko 平台采用积分制
- 策划案生成：消耗较少积分
- 视频生成：消耗较多积分
- 积分不足时，会返回错误：`{"code": 500, "msg": "积分不足"}`

**充值方式**：登录 Seko 平台 → 账户管理 → 积分充值

### 七、常见问题

#### Q1：API Key 怎么获取？
A: 登录 seko.sensetime.com，点击左下角 🦞 Openclaw 入口

#### Q2：提示"积分不足"怎么办？
A: 登录 Seko 平台充值积分

#### Q3：任务一直显示 RUNNING 怎么办？
A: 使用 `--wait` 参数等待任务完成，或手动轮询查询

#### Q4：如何查看生成的素材？
A: 素材保存在 `{PROJECT_DIR}/assets/` 目录下

#### Q5：视频生成失败怎么办？
A: 检查策划案是否完整，确认积分充足，查看错误信息

### 八、GitHub 部署

#### 1. 克隆仓库
```bash
git clone https://github.com/你的仓库/seko-ai-video.git
```

#### 2. 配置环境变量
在 零克云 或 Vercel 等平台配置：
- `SEKO_API_KEY` = 你的 API Key

#### 3. 使用方式
参考 SKILL.md 中的工作流程调用脚本

---

**技术支持**：
- Seko 官网：https://seko.sensetime.com
- 零克云：https://zerke.cloud