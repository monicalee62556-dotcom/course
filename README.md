# 从零学机械研发

哆啦A胡的图文学习室：8节先修课、52个原有专题、16个新增进阶专题、扩展术语词典与234道原题复习笔记。

在线地址：https://monicalee62556-dotcom.github.io/course/?v=advanced16

## 学习方式

先走完“零基础先修”，再选专题。每课依次为术语、白话原理与图解、四步讲解、完整例题、自测。点击术语可看解释，图解可放大；小屏放大后可左右滑动。部分计算课有可修改输入的计算器。

题库是保留的历史复习笔记，未将234道题逐题重写为入门课。新手优先学习8节先修课；完成后可学习原有52个专题和新增16个进阶专题，共76节课程。自测答对或手动标记会记录进度；数据只在当前浏览器 localStorage 保存，不自动跨设备同步。

## 文件与构建

页面无第三方运行依赖，不需要数据库、账号或外部题库请求。GitHub Pages直接发布仓库根目录 `index.html`。直接下载该文件也可离线学习。

- `source-data.json`：从完整本地原稿保留的52个主题元数据和234道题。
- `lessons.js`：8节先修课与T01～T13。
- `lessons-bearing-gear.js`：T14～T32。
- `lessons-robot-validation.js`：T33～T52。
- `glossary.js`、`diagrams.js`：术语与SVG图解。
- `advanced-16/advanced-lessons.js`、`advanced-16/advanced-diagrams.js`：新增16节进阶课程数据和中文SVG图解。
- `app.js`、`style.css`：界面、交互、进度和自测。
- `build.py`：把以上内容完整打包到单个HTML。

使用Python 3生成页面：

```sh
python build.py
```

构建会另外生成 `compiled.js`，可用 `node --check compiled.js` 检查语法；发布只需 `index.html`。本地预览可运行 `python -m http.server 8765`。

所有教学算例明确给出假设。效率、配合示例、虚构样本参数不能作为具体型号额定值或生产图样。真实选型应查制造商完整型号、适用标准与试验记录。


## 进阶课程：16个机械研发专题

新增的进阶课程源文件位于 [advanced-16/](./advanced-16/README.md)，包括16个独立专题 Markdown、统一课程规范和 Codex 开发指南。内容覆盖材料热处理、压铸、钛合金表面处理、CNC、水下密封、公差尺寸链、轴承、减速器、机器人关节、电机功率、轻量化、热管理、有限元、可靠性、量产及 BOM 成本。

**给 Codex 的入口：** 先读 [advanced-16/CODEX_GUIDE.md](./advanced-16/CODEX_GUIDE.md)，再按专题文件逐个实现网页模块。要求保留现有课程，新增专题统一使用中文结构图、详细讲解、可交互计算器、失效分析和面试练习。16个进阶专题已集成到网站课程导航、专题列表、中文流程图、术语解释、自测和计算器中。静态入口 `index.html` 已同步；本地可用 `python build.py` 重新构建。
