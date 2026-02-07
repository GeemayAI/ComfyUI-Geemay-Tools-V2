# ComfyUI Registry 发布准备检查脚本
# 这个脚本会检查你的项目是否准备好发布到 ComfyUI Registry

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ComfyUI Registry 发布准备检查" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$allGood = $true

# 检查必需文件
Write-Host "1. 检查必需文件..." -ForegroundColor Yellow

$requiredFiles = @(
    "pyproject.toml",
    "README.md",
    "LICENSE",
    "__init__.py",
    "requirements.txt"
)

foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "   ✓ $file 存在" -ForegroundColor Green
    } else {
        Write-Host "   ✗ $file 缺失" -ForegroundColor Red
        $allGood = $false
    }
}

Write-Host ""

# 检查 Git 状态
Write-Host "2. 检查 Git 状态..." -ForegroundColor Yellow

try {
    $gitStatus = git status --porcelain
    if ($gitStatus) {
        Write-Host "   ⚠ 有未提交的更改" -ForegroundColor Yellow
        Write-Host "   提示: 运行 'git add .' 和 'git commit' 来提交更改" -ForegroundColor Gray
    } else {
        Write-Host "   ✓ 所有更改已提交" -ForegroundColor Green
    }
} catch {
    Write-Host "   ✗ 无法检查 Git 状态" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

# 检查远程仓库
Write-Host "3. 检查远程仓库..." -ForegroundColor Yellow

try {
    $remote = git remote get-url origin
    if ($remote) {
        Write-Host "   ✓ 远程仓库: $remote" -ForegroundColor Green
    }
} catch {
    Write-Host "   ✗ 未配置远程仓库" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

# 读取版本号
Write-Host "4. 检查版本信息..." -ForegroundColor Yellow

if (Test-Path "pyproject.toml") {
    $content = Get-Content "pyproject.toml" -Raw
    if ($content -match 'version\s*=\s*"([^"]+)"') {
        $version = $matches[1]
        Write-Host "   ✓ pyproject.toml 版本: $version" -ForegroundColor Green
        Write-Host "   提示: GitHub Release 标签应该是: v$version" -ForegroundColor Gray
    } else {
        Write-Host "   ✗ 无法读取版本号" -ForegroundColor Red
        $allGood = $false
    }
}

Write-Host ""

# 总结
Write-Host "========================================" -ForegroundColor Cyan
if ($allGood) {
    Write-Host "✓ 所有检查通过！准备发布" -ForegroundColor Green
    Write-Host ""
    Write-Host "下一步操作:" -ForegroundColor Yellow
    Write-Host "1. 提交并推送代码到 GitHub" -ForegroundColor White
    Write-Host "   git add ." -ForegroundColor Gray
    Write-Host "   git commit -m '准备发布 v$version'" -ForegroundColor Gray
    Write-Host "   git push origin main" -ForegroundColor Gray
    Write-Host ""
    Write-Host "2. 在 GitHub 上创建 Release" -ForegroundColor White
    Write-Host "   访问: $remote/releases/new" -ForegroundColor Gray
    Write-Host "   标签: v$version" -ForegroundColor Gray
    Write-Host ""
    Write-Host "3. 提交到 ComfyUI Registry" -ForegroundColor White
    Write-Host "   查看详细指南: 发布到ComfyUI_Registry指南.md" -ForegroundColor Gray
} else {
    Write-Host "✗ 发现问题，请修复后再发布" -ForegroundColor Red
}
Write-Host "========================================" -ForegroundColor Cyan

