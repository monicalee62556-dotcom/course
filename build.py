import json,re,pathlib,hashlib
ROOT=pathlib.Path(__file__).resolve().parent
data_path=ROOT/'source-data.json'
if data_path.exists():
    data=json.loads(data_path.read_text(encoding='utf-8'))
    topics,questions=data['topics'],data['questions']
else:
    source=pathlib.Path(r'C:\Users\18259\Downloads\mba-course-fixed.html').read_text(encoding='utf-8-sig')
    decoder=json.JSONDecoder()
    def array(name):
        match=re.search(r'\b'+name+r'\s*=\s*(\[)',source)
        if not match: raise ValueError('Missing complete source array: '+name)
        value,_=decoder.raw_decode(source[match.start(1):])
        return value
    topics,questions=array('TOPICS'),array('QUESTIONS')
assert len(topics)==52 and len(questions)==234
(ROOT/'source-data.json').write_text(json.dumps({'topics':topics,'questions':questions},ensure_ascii=False,indent=2),encoding='utf-8')
scripts='const TOPICS='+json.dumps(topics,ensure_ascii=False)+';\nconst QUESTIONS='+json.dumps(questions,ensure_ascii=False)+';\n'
for name in ['lessons.js','lessons-bearing-gear.js','lessons-robot-validation.js','glossary.js','diagrams.js','app.js']:
    scripts+='\n'+(ROOT/name).read_text(encoding='utf-8')+'\n'
scripts=scripts.replace('</script','<\\/script')
(ROOT/'compiled.js').write_text(scripts,encoding='utf-8')
html='''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="哆啦A胡的机械研发入门课程：8节零基础先修、52个逐步图解专题、234道复习题，带术语解释、完整例题和自测。"><meta name="theme-color" content="#123c44"><title>机械研发 · 从零开始 | 哆啦A胡的学习室</title><style>'''+(ROOT/'style.css').read_text(encoding='utf-8')+'''</style></head><body>
<div class="shell"><aside class="sidebar"><a class="brand" href="#home"><span class="brandmark">机</span><span><b>从零学机械研发</b><small>哆啦A胡的学习室</small></span></a><nav class="nav" aria-label="主导航"><button data-nav="home">学习首页</button><button data-nav="intro">零基础先修</button><button data-nav="topics">52个专题</button><button data-nav="bank">234道题库</button><button data-nav="terms">术语词典</button><button data-nav="progress">我的进度</button></nav><div class="sidecard"><b>不用着急，一课一课来</b><p id="side-progress">0 / 60 课已完成</p><div class="meter"><i id="side-meter" style="width:0%"></i></div><p>建议先学先修课，再进入感兴趣的专题。先理解，再计算。</p><p>进度保存在当前浏览器。</p></div></aside><main class="work" id="main"><header class="topbar"><span>从原理到计算，再到工程判断</span><span class="version">零基础详解版 · v3</span></header><div id="storage-warning"></div><div id="content"></div><footer class="pagefooter">60节课程＝8节先修＋52个专题。原题库作为进阶复习材料保留；例题数据为题内假设，不代表具体产品额定值。<br>查证入口：<a href="https://www.skf.com/" target="_blank" rel="noopener noreferrer">SKF 轴承资料</a><a href="https://khkgears.net/" target="_blank" rel="noopener noreferrer">KHK 齿轮资料</a><a href="https://www.iso.org/" target="_blank" rel="noopener noreferrer">ISO 标准信息</a>具体选型应查制造商完整型号与适用标准。</footer></main></div>
<dialog id="detail-dialog" class="dialog" aria-label="学习帮助"><div id="dialog-content"></div></dialog><div id="toast" class="toast" hidden role="status"></div><noscript><p>课程需要启用 JavaScript 才能显示。完整内容和图解已包含在本文件内，无需另外加载题库。</p></noscript><script>'''+scripts+'''</script></body></html>'''
(ROOT/'index.html').write_text(html,encoding='utf-8')
print(json.dumps({'topics':len(topics),'questions':len(questions),'bytes':len(html.encode()),'characters':len(html),'sha256':hashlib.sha256(html.encode()).hexdigest()},ensure_ascii=False))
