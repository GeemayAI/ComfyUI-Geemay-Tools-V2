# ComfyUI-Geemay-Tools-V2

## 简介
ComfyUI_Geemay_Tools 是一个专为建筑、室内、景观设计领域打造的高集成度、可视化提示词预设管理器。

## 安装方法
1. 手动安装
#1. Clone the repo克隆仓库
git clone https://github.com/GeemayAI/ComfyUI-Geemay-Tools-V2
 #2. Install the requirements安装依赖
pip install -r ComfyUI-Geemay-Tools-V2\requirements.txt

2. 完全重启ComfyUI

## 使用方法
1. 在ComfyUI工作流中添加 "Geemay Preset Manager" 节点（在节点菜单中找到 "Geemay Tools" → "Geemay Preset Manager" 节点）
2. 选择"预设主类"（室内专项/景观专项/建筑专项/GM国学分析）
3. 功能类会自动更新，选择需要的功能类
4. 模版会自动更新，选择具体的模版
5. （可选）在混合输入区添加额外提示词
6. （可选）开启专家模式，完全自定义提示词
7. 运行节点，从GM_prompt输出端获取生成的提示词


## 更新日志

### v1.0.2 (2026-02-7)
- ✨ 初始版本发布

## 许可证
Apache-2.0 license
