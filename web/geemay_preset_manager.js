/**
 * Geemay Preset Manager 前端扩展
 * 实现主类、功能类和模版的动态联动
 */

import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

// 定义主类和功能类的映射关系
const CATEGORY_MAPPING = {
    "室内平面专项": [
        "平面布置图",
        "住宅彩平图",
        "智能家居分析",
        "住宅空间动线分析",
        "住宅空气质量分析",
        "住宅室内光环境分析",
        "住宅通风分析",
        "室内平面出立体鸟瞰"
    ],
    "室内效果图": [
        "模型出效果图",
        "毛坯加参考出图",
        "根据参考换风格",
        "空间多角度",
        "提取立面造型",
        "提取软装配饰",
        "三图联动出图",
        "一键转夜景",
        "硬装材料表",
        "软装配饰表",
        "施工工艺图",
        "出软装搭配图",
        "空间色彩搭配分析",
        "空间材料搭配分析",
        "户型手办模型",
        "定制柜立面加参考出图",
        "定制柜拆单图",
        "参考出展厅概念"
    ],
    "建筑景观庭院专项": [
        "模型出效果图",
        "一键转夜景",
        "庭院平面出立体鸟瞰",
        "庭院立体鸟瞰出多角度",
        "建筑CAD立面出效果图",
        "建筑图转多角度",
        "景观四季变换",
        "景观植物分析图",
        "天气转变"
    ],
    "市政规划专项": [
        "平面图出立体鸟瞰",
        "鸟瞰转写实低空视角",
        "低空视角转局部特写",
        "低空视角转全方位分析"
    ],
    "国学分析": [
        "住宅平面国学分析",
        "建筑庭院环境国学分析"
    ]
};

// 定义功能类和模版的映射关系
// 注意：使用 "主类|功能类" 的格式作为键，避免重复键名问题
const TEMPLATE_MAPPING = {
    // 室内平面专项
    "室内平面专项|平面布置图": ["住宅"],
    "室内平面专项|住宅彩平图": ["现代", "轻奢", "莫兰迪", "手绘"],
    "室内平面专项|智能家居分析": ["启用模版"],
    "室内平面专项|住宅空间动线分析": ["启用模版"],
    "室内平面专项|住宅空气质量分析": ["启用模版"],
    "室内平面专项|住宅室内光环境分析": ["启用模版"],
    "室内平面专项|住宅通风分析": ["启用模版"],
    "室内平面专项|室内平面出立体鸟瞰": ["启用模版"],
    
    // 室内效果图
    "室内效果图|模型出效果图": ["白天", "夜晚"],
    "室内效果图|毛坯加参考出图": ["客厅", "餐厅", "卧室", "书房"],
    "室内效果图|根据参考换风格": ["启用模版"],
    "室内效果图|空间多角度": ["启用模版"],
    "室内效果图|提取立面造型": ["启用模版"],
    "室内效果图|提取软装配饰": ["启用模版"],
    "室内效果图|三图联动出图": ["启用模版"],
    "室内效果图|一键转夜景": ["启用模版"],
    "室内效果图|硬装材料表": ["启用模版"],
    "室内效果图|软装配饰表": ["启用模版"],
    "室内效果图|施工工艺图": ["启用模版"],
    "室内效果图|出软装搭配图": ["启用模版"],
    "室内效果图|空间色彩搭配分析": ["启用模版"],
    "室内效果图|空间材料搭配分析": ["启用模版"],
    "室内效果图|户型手办模型": ["启用模版"],
    "室内效果图|定制柜立面加参考出图": ["启用模版"],
    "室内效果图|定制柜拆单图": ["启用模版"],
    "室内效果图|参考出展厅概念": ["启用模版"],
    
    // 建筑景观庭院专项
    "建筑景观庭院专项|模型出效果图": ["建筑", "景观", "庭院"],
    "建筑景观庭院专项|一键转夜景": ["建筑", "景观", "庭院"],
    "建筑景观庭院专项|庭院平面出立体鸟瞰": ["启用模版"],
    "建筑景观庭院专项|庭院立体鸟瞰出多角度": ["启用模版"],
    "建筑景观庭院专项|建筑CAD立面出效果图": ["启用模版"],
    "建筑景观庭院专项|建筑图转多角度": ["启用模版"],
    "建筑景观庭院专项|景观四季变换": ["春", "夏", "秋", "冬"],
    "建筑景观庭院专项|景观植物分析图": ["启用模版"],
    "建筑景观庭院专项|天气转变": ["晴", "雨", "雪", "雾"],
    
    // 市政规划专项
    "市政规划专项|平面图出立体鸟瞰": ["启用模版"],
    "市政规划专项|鸟瞰转写实低空视角": ["启用模版"],
    "市政规划专项|低空视角转局部特写": ["启用模版"],
    "市政规划专项|低空视角转全方位分析": ["启用模版"],
    
    // 国学分析
    "国学分析|住宅平面国学分析": ["启用模版"],
    "国学分析|建筑庭院环境国学分析": ["启用模版"]
};

// 注册节点扩展
app.registerExtension({
    name: "Geemay.PresetManager",
    
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        // 只处理我们的节点
        if (nodeData.name === "GeemayPresetManager") {
            
            // 保存原始的onNodeCreated方法
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            
            // 重写onNodeCreated方法
            nodeType.prototype.onNodeCreated = function() {
                // 调用原始方法
                const result = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;
                
                // 获取所有widgets
                const mainCategoryWidget = this.widgets.find(w => w.name === "main_category");
                const functionCategoryWidget = this.widgets.find(w => w.name === "function_category");
                const templateWidget = this.widgets.find(w => w.name === "template");
                
                if (!mainCategoryWidget || !functionCategoryWidget || !templateWidget) {
                    console.error("Geemay: 无法找到必需的widgets");
                    return result;
                }
                
                // 保存原始的callback
                const originalMainCallback = mainCategoryWidget.callback;
                const originalFunctionCallback = functionCategoryWidget.callback;
                
                // 定义更新模版选项的函数
                const updateTemplates = (mainCategory, functionCategory) => {
                    // 使用 "主类|功能类" 的格式作为键
                    const key = `${mainCategory}|${functionCategory}`;
                    // 获取对应的模版列表
                    const templates = TEMPLATE_MAPPING[key] || ["启用模版"];
                    
                    // 更新模版widget的选项
                    templateWidget.options.values = templates;
                    
                    // 如果当前值不在新列表中，设置为第一个选项
                    if (!templates.includes(templateWidget.value)) {
                        templateWidget.value = templates[0];
                    }
                    
                    console.log(`Geemay: 主类="${mainCategory}", 功能类="${functionCategory}"，模版更新为:`, templates);
                };
                
                // 定义更新功能类选项的函数
                const updateFunctionCategories = (mainCategory) => {
                    // 获取对应的功能类列表
                    const functionCategories = CATEGORY_MAPPING[mainCategory] || [];
                    
                    if (functionCategories.length > 0) {
                        // 更新功能类widget的选项
                        functionCategoryWidget.options.values = functionCategories;
                        
                        // 如果当前值不在新列表中，设置为第一个选项
                        if (!functionCategories.includes(functionCategoryWidget.value)) {
                            functionCategoryWidget.value = functionCategories[0];
                        }
                        
                        console.log(`Geemay: 主类切换到 "${mainCategory}"，功能类更新为:`, functionCategories);
                        
                        // 更新模版选项（传入主类和功能类）
                        updateTemplates(mainCategory, functionCategoryWidget.value);
                    }
                };
                
                // 设置主类widget的回调函数
                mainCategoryWidget.callback = function(value) {
                    // 调用原始callback（如果存在）
                    if (originalMainCallback) {
                        originalMainCallback.apply(this, arguments);
                    }
                    
                    // 更新功能类选项
                    updateFunctionCategories(value);
                };
                
                // 设置功能类widget的回调函数
                functionCategoryWidget.callback = function(value) {
                    // 调用原始callback（如果存在）
                    if (originalFunctionCallback) {
                        originalFunctionCallback.apply(this, arguments);
                    }
                    
                    // 更新模版选项（传入主类和功能类）
                    updateTemplates(mainCategoryWidget.value, value);
                };
                
                // 初始化时也要更新一次功能类和模版选项
                updateFunctionCategories(mainCategoryWidget.value);
                
                return result;
            };
        }
    }
});

