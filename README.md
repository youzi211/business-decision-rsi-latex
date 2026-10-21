# 模型治理与决策节点优化

本目录为可独立移动的 LaTeX 项目，包含已修正图 3 连线的最终版本。

- 根目录 `.tex`：可直接编辑的 LaTeX 主文档，所有示意图均由 TikZ 绘制。
- 根目录 `模型治理与决策节点优化.pdf`：编译后的文档。
- `build.ps1`：编译现有 LaTeX 文档的入口，不覆盖源码。
- `source/`：用户提供的 Markdown 原稿副本，外部原件保留在原处。
- `preview/`：图 3 修正版预览。
- `work/`：原有编译中间文件、排版检查图片及 Markdown 转换脚本。

## 编译

环境：Windows、XeLaTeX（MiKTeX 或 TeX Live）、ctex 和 Windows 中文字体；需要 TikZ、tcolorbox 等文档中列出的宏包。

在 PowerShell 中执行：

```powershell
.\build.ps1
```

编译两次以更新目录，PDF 以 `模型治理与决策节点优化.pdf` 为名更新至项目根目录，中间文件留在 `work/latex-build/`。

## 从 Markdown 重新生成

```powershell
python .\work\build_document.py
```

该命令根据 `source/` 原稿重新生成 LaTeX 并编译，会覆盖手动编辑过的主文档。日常修改 LaTeX 后请使用 `build.ps1`。

## 协作约定

- 以根目录 `.tex` 为当前文档的唯一编辑入口；图表使用内嵌 TikZ，无需额外图片依赖。
- `source/` 保留最初的 Markdown 原稿，供对照与追溯，不代表当前 LaTeX 的后续修订。
- `work/build_document.py` 是最初的转换与构建工具。重新运行会覆盖 `.tex`，协作修订后请谨慎使用；日常编译使用 `build.ps1`。
- 修改后编译两次并检查排版，将更新的 `.tex` 和 `.pdf` 一起提交；图 3 变化时相应更新 `preview/` 中的预览。
- `work/` 下的缓存、日志、历史检查截图由 `.gitignore` 排除，仅转换脚本入库。
- 推荐通过功能分支和 Pull Request 合并修改。私有仓库协作者须由仓库所有者授予写入权限。

## 同步文件清单

| 文件 | 用途 |
| --- | --- |
| 根目录 `.tex` | 可编辑主文档和 TikZ 图形 |
| 根目录 `.pdf` | 已编译、可直接阅读的版本 |
| `build.ps1` | 编译现有 LaTeX 的入口 |
| `README.md` | 环境、构建与协作说明 |
| `.gitignore`、`.gitattributes` | 忽略中间文件并统一换行规则 |
| `source/*.md` | 原始材料副本 |
| `work/build_document.py` | Markdown 转换与构建脚本 |
| `preview/*.png` | 图 3 修正版预览 |
