# 发布到 ComfyUI Registry 完整指南

## 📋 前提条件检查清单

在开始发布之前，请确保：

- ✅ 你的代码已经上传到 GitHub
- ✅ GitHub 仓库是公开的（public）
- ✅ 你有 GitHub 账号并已登录
- ✅ 项目包含必要的文件：
  - `pyproject.toml` （已完善）
  - `README.md` （已有）
  - `LICENSE` 文件（需要检查）
  - `__init__.py` （已有）
  - `requirements.txt` （已有）

---

## 🚀 发布步骤

### 第一步：检查并创建 LICENSE 文件

你的 `pyproject.toml` 中引用了 LICENSE 文件，需要确保它存在。

**操作：**
1. 在项目根目录检查是否有 `LICENSE` 文件
2. 如果没有，需要创建一个 Apache-2.0 许可证文件

我可以帮你创建这个文件，或者你可以：
- 访问 https://www.apache.org/licenses/LICENSE-2.0.txt
- 复制内容并保存为 `LICENSE` 文件（无扩展名）

---

### 第二步：确保代码已推送到 GitHub

**操作：**
```bash
# 1. 检查当前状态
git status

# 2. 添加所有更改
git add .

# 3. 提交更改
git commit -m "准备发布到 ComfyUI Registry v1.0.1"

# 4. 推送到 GitHub
git push origin main
```

**注意：** 如果你的主分支叫 `master` 而不是 `main`，请使用 `git push origin master`

---

### 第三步：创建 GitHub Release（发布版本）

这是**最重要**的一步！ComfyUI Registry 需要通过 GitHub Release 来识别你的版本。

**操作步骤：**

1. **访问你的 GitHub 仓库**
   - 打开浏览器，访问：https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2

2. **进入 Releases 页面**
   - 点击右侧的 "Releases"（发布）
   - 或直接访问：https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2/releases

3. **创建新的 Release**
   - 点击 "Create a new release"（创建新发布）或 "Draft a new release"（起草新发布）

4. **填写 Release 信息**
   
   **Tag version（标签版本）：** 
   ```
   v1.0.1
   ```
   ⚠️ **重要：** 版本号必须以 `v` 开头，并且与 `pyproject.toml` 中的版本号一致！
   
   **Release title（发布标题）：**
   ```
   ComfyUI Geemay Tools V2 - v1.0.1
   ```
   
   **Description（描述）：**
   ```markdown
   ## ✨ 首次发布

   ComfyUI_Geemay_Tools 是一个专为建筑、室内、景观设计领域打造的高集成度、可视化提示词预设管理器。

   ### 主要功能
   - 🏗️ 建筑专项提示词预设
   - 🏠 室内设计提示词预设
   - 🌳 景观设计提示词预设
   - 📚 GM国学分析功能
   - 🎨 可视化预设管理界面
   - 🔧 专家模式支持自定义提示词

   ### 安装方法
   通过 ComfyUI Manager 搜索 "Geemay Tools" 安装，或手动克隆仓库。

   ### 依赖
   - Python >= 3.9
   - cryptography >= 41.0.0

   ---

   **完整文档：** [README.md](https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2/blob/main/README.md)
   ```

5. **选择目标分支**
   - Target: `main` （或 `master`，取决于你的主分支名称）

6. **发布**
   - 点击 "Publish release"（发布版本）

---

### 第四步：提交到 ComfyUI Registry

**方法一：通过 GitHub（推荐）**

1. **访问 ComfyUI Registry 仓库**
   - 打开：https://github.com/comfyanonymous/ComfyUI-Registry

2. **Fork 这个仓库**
   - 点击右上角的 "Fork" 按钮

3. **在你 Fork 的仓库中添加你的节点**
   - 进入 `registry` 文件夹
   - 找到或创建对应的分类文件
   - 添加你的节点信息

4. **创建 Pull Request**
   - 提交更改
   - 创建 Pull Request 到原仓库
   - 等待审核

**方法二：通过 ComfyUI Manager（更简单）**

1. **在 ComfyUI 中安装 ComfyUI Manager**
   - 如果还没安装，访问：https://github.com/ltdrdata/ComfyUI-Manager

2. **使用 Manager 提交**
   - 打开 ComfyUI Manager
   - 找到 "Submit Custom Node" 或类似选项
   - 填写你的 GitHub 仓库地址：`https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2`
   - 提交申请

**方法三：直接提交 Issue（最简单）**

1. **访问 ComfyUI Registry Issues**
   - 打开：https://github.com/comfyanonymous/ComfyUI-Registry/issues

2. **创建新 Issue**
   - 点击 "New Issue"
   - 标题：`[New Node] ComfyUI Geemay Tools V2`
   - 内容模板：
   ```markdown
   ## 节点信息
   
   - **名称：** ComfyUI Geemay Tools V2
   - **GitHub 仓库：** https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2
   - **描述：** 专为建筑、室内、景观设计领域打造的高集成度、可视化提示词预设管理器
   - **分类：** prompt, text, design
   - **作者：** GeemayAI
   
   ## 功能特点
   - 建筑、室内、景观设计专业提示词预设
   - 可视化预设管理界面
   - 支持专家模式自定义
   
   ## 已完成
   - [x] 创建了 pyproject.toml
   - [x] 创建了 README.md
   - [x] 上传到 GitHub
   - [x] 创建了 Release v1.0.1
   
   请将此节点添加到 ComfyUI Registry，谢谢！
   ```

3. **提交 Issue**
   - 点击 "Submit new issue"
   - 等待维护者回复

---

## 📝 重要注意事项

### 1. 版本号规范
- `pyproject.toml` 中的版本：`1.0.1`
- GitHub Release 标签：`v1.0.1`（必须加 `v` 前缀）
- 两者必须对应！

### 2. 文件结构要求
```
ComfyUI-Geemay-Tools-V2/
├── __init__.py              # 必需：节点入口文件
├── pyproject.toml           # 必需：项目配置
├── README.md                # 必需：说明文档
├── LICENSE                  # 必需：许可证文件
├── requirements.txt         # 推荐：依赖列表
├── icon.png                 # 可选：节点图标
├── nodes/                   # 节点代码
│   ├── __init__.py
│   └── geemay_preset_manager.py
└── web/                     # 前端代码
    └── geemay_preset_manager.js
```

### 3. pyproject.toml 关键字段
- `name`: 包名（小写，用连字符）
- `version`: 版本号（与 Release 对应）
- `description`: 简短描述
- `dependencies`: Python 依赖
- `[tool.comfy]`: ComfyUI 特定配置
  - `PublisherId`: 发布者 ID（你的 GitHub 用户名）
  - `DisplayName`: 显示名称
  - `Icon`: 图标文件路径

### 4. 常见问题

**Q: 我的节点没有出现在 ComfyUI Manager 中？**
A: 
- 检查是否创建了 GitHub Release
- 确认版本号格式正确（Release 标签要加 `v`）
- 等待 Registry 更新（可能需要几小时到一天）

**Q: 如何更新已发布的节点？**
A:
1. 修改代码
2. 更新 `pyproject.toml` 中的版本号（如 `1.0.2`）
3. 提交并推送到 GitHub
4. 创建新的 Release（如 `v1.0.2`）
5. Registry 会自动检测更新

**Q: 需要什么权限？**
A:
- 你必须是 GitHub 仓库的所有者或有写入权限
- 仓库必须是公开的（public）

---

## 🎯 快速检查清单

发布前请确认：

- [ ] ✅ `pyproject.toml` 已完善（版本号、描述、依赖）
- [ ] ✅ `README.md` 包含安装和使用说明
- [ ] ✅ `LICENSE` 文件存在
- [ ] ✅ 代码已推送到 GitHub
- [ ] ✅ 创建了 GitHub Release（标签格式：`v1.0.1`）
- [ ] ✅ 提交到 ComfyUI Registry（通过 Issue 或 PR）

---

## 📞 需要帮助？

如果遇到问题：
1. 查看 ComfyUI Registry 文档：https://github.com/comfyanonymous/ComfyUI-Registry
2. 查看 ComfyUI Manager 文档：https://github.com/ltdrdata/ComfyUI-Manager
3. 在 ComfyUI Discord 社区寻求帮助
4. 在你的仓库 Issues 中提问

---

## 🎉 发布成功后

发布成功后，用户可以通过以下方式安装你的节点：

1. **通过 ComfyUI Manager**
   - 打开 ComfyUI Manager
   - 搜索 "Geemay Tools"
   - 点击安装

2. **手动安装**
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2
   cd ComfyUI-Geemay-Tools-V2
   pip install -r requirements.txt
   ```

祝发布顺利！🚀

