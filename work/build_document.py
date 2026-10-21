from pathlib import Path
import re, subprocess, shutil

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT
OUT.mkdir(exist_ok=True)
SRC=next((ROOT/'source').glob('*.md'))
source=SRC.read_text(encoding='utf-8-sig')
# Preserve business definitions and evidence boundaries; qualify unverified baseline claims.
source=source.replace('低置信时往往仍由大模型"硬猜"一个类别','依赖现有接受与兜底策略，实际处理方式需先核查')
source=source.replace('无统一评测，漏改写与多改写都靠人工经验权衡','若缺少统一评测，漏改写与多改写主要依靠人工经验权衡')
source=source.replace('判定不需要改写但实际检索失败时无机制','需核查现有流程是否具备检索失败后的补救机制')
source=source.replace('无独立评测，无法判断裁剪是否损害质量','若缺少独立评测，则难以判断裁剪是否损害质量')
source=source.replace('提示词 RSI 自动迭代类别描述，经评测后发布优化版本','离线提示优化迭代类别描述，经评测与审批后发布优化版本')

PRE=r'''\documentclass[UTF8,a4paper,11pt,fontset=windows]{ctexart}
\usepackage[margin=21mm,top=22mm,bottom=22mm,headheight=15pt]{geometry}
\usepackage{xcolor}
\usepackage{fontspec,graphicx,amsmath,booktabs,array,longtable,enumitem,fancyhdr,tikz,tcolorbox,hyperref}
\usetikzlibrary{arrows.meta,positioning,fit,backgrounds,calc}
\definecolor{Navy}{HTML}{17324D}
\definecolor{Teal}{HTML}{007F82}
\definecolor{Gold}{HTML}{B77623}
\definecolor{Ink}{HTML}{253445}
\definecolor{Muted}{HTML}{607386}
\definecolor{Pale}{HTML}{F0F6F8}
\definecolor{Rule}{HTML}{CDDCE4}
\hypersetup{colorlinks=true,linkcolor=Navy,urlcolor=Teal,pdftitle={业务决策模型治理与效能优化方案},pdfauthor={},bookmarksnumbered=true}
\ctexset{section={format=\Large\bfseries\color{Navy},beforeskip=15pt,afterskip=10pt},subsection={format=\large\bfseries\color{Teal},beforeskip=12pt,afterskip=7pt}}
\setlength{\parindent}{2em}
\setlength{\parskip}{4pt}
\linespread{1.18}
\setlist{nosep,leftmargin=2em,topsep=5pt,itemsep=3pt}
\setlength{\emergencystretch}{3em}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\color{Muted}业务决策模型治理}
\fancyhead[R]{\small\color{Muted}效能优化方案}
\fancyfoot[L]{\scriptsize\color{Muted}参赛申请 · 技术方案}
\fancyfoot[R]{\small\color{Navy}\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\renewcommand{\footrulewidth}{0pt}
\newtcolorbox{insight}[1]{colback=Pale,colframe=Rule,boxrule=.5pt,arc=2mm,left=3mm,right=3mm,top=2mm,bottom=2mm,title={#1},colbacktitle=Navy,coltitle=white,fonttitle=\bfseries}
\newcommand{\figcap}[1]{\refstepcounter{figure}\par\smallskip{\centering\small\color{Muted}图\thefigure\quad #1\par}\medskip}
\tikzset{box/.style={draw=Rule,fill=Pale,rounded corners=2mm,align=center,text width=34mm,minimum height=12mm,font=\small,inner sep=4pt},accent/.style={box,draw=Teal,fill=Teal!8},dark/.style={box,fill=Navy,draw=Navy,text=white},arr/.style={-{Stealth[length=2mm]},thick,draw=Muted},lab/.style={font=\scriptsize,text=Muted,fill=white,inner sep=1pt}}
\begin{document}
\color{Ink}
\begin{titlepage}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
\fill[Navy] (current page.north west) rectangle ([yshift=-62mm]current page.north east);
\fill[Teal] ([yshift=-62mm]current page.north west) rectangle ([yshift=-65mm]current page.north east);
\node[anchor=north west,text=white,font=\small] at ([xshift=22mm,yshift=-21mm]current page.north west) {技术方案 / 参赛申请};
\node[anchor=north west,text=white,font=\fontsize{27}{36}\selectfont\bfseries,align=left] at ([xshift=22mm,yshift=-34mm]current page.north west) {让业务判断更轻，让优化持续发生};
\end{tikzpicture}\par
\vspace*{58mm}
{\fontsize{25}{36}\selectfont\bfseries\color{Navy}业务决策模型治理与效能优化方案\par}
\vspace{7mm}
{\large\color{Muted}规范模型选用、效果评估与持续改进，在保障业务质量的同时控制处理时延与成本\par}
\vspace{13mm}
\begin{tikzpicture}
\node[dark,text width=40mm,minimum height=23mm] (a) {节点轻量化\\[-1pt]\footnotesize 分类与选项打分};
\node[accent,text width=40mm,minimum height=23mm,right=8mm of a] (b) {提示优化闭环\\[-1pt]\footnotesize 固定权重，改进描述};
\node[box,text width=40mm,minimum height=23mm,right=8mm of b] (c) {业务微调闭环\\[-1pt]\footnotesize 冻结任务，补强能力};
\draw[arr] (a)--(b);\draw[arr] (b)--(c);
\end{tikzpicture}
\vspace{11mm}
\begin{insight}{方案主张}
保留必要的内容生成，将边界清晰的判断任务交给合适的决策后端；通过真实错误驱动的两条离线闭环，形成可评测、可追溯、可回退的持续优化机制。
\end{insight}
\vfill
{\small\color{Muted}评测说明：方案收益以真实业务场景的实测数据和验收结果为准。}
\end{titlepage}
\pagenumbering{roman}
\section*{方案速览}
\addcontentsline{toc}{section}{方案速览}
\begin{insight}{一句话理解}
用更适合判断任务的推理方式承接业务节点，在质量达标的前提下减少生成开销；再以提示优化和可选微调持续提高可靠承接能力。
\end{insight}
\begin{description}[style=nextline,leftmargin=2em,labelwidth=2em]
\item[为什么做] 智能助理中的意图分类、改写判断和证据筛选，往往只需输出类别、是非或分数，却可能消耗一次完整的生成式调用。
\item[从哪里开始] 首先验证意图识别，重点区分消费者退款、商户结算和支付状态；问题改写与检索片段筛选作为扩展场景。
\item[如何持续改进] 先诊断输入、标签与策略问题；描述不清时优化提示，领域能力不足且训练条件具备时再比较微调。两条闭环均在线下运行。
\item[怎样判断有效] 先满足预先约定的质量约束，再比较完整链路时延与每成功任务总成本。新增决策、回退、运维和离线优化摊销均计入成本。
\end{description}
\begin{insight}{阅读与证据说明}
正文保留原稿七章结构。流程图表示方案设计；“3 次变 1 次”“5 个片段保留 3 个”等数字仅为条件化示例，不能视为实测结果。各项验收指标在实测前统一标记“待测”。

RSI 沿用项目原名，本文以两条受约束的离线优化闭环阐述其实现机制；不指线上自主训练或绕过审批更新生产配置。候选模型链接作为核查入口保留，其能力与许可未在本次编排中重新核实。
\end{insight}
\clearpage
\tableofcontents
\clearpage
\pagenumbering{arabic}
'''

FIG1=r'''
\begin{center}\resizebox{\linewidth}{!}{\begin{tikzpicture}
\node[dark,text width=53mm] (u) {用户问题与必要上下文};
\node[box,below left=10mm and 8mm of u,text width=48mm] (old) {现有路径\\生成式大模型判断};
\node[accent,below right=10mm and 8mm of u,text width=48mm] (new) {候选路径\\决策模型判断与接受策略};
\node[accent,below=17mm of new,text width=24mm] (ask) {信息不足\\澄清问题};
\node[box,left=5mm of ask,text width=28mm] (fb) {不可靠或异常\\原模型／既有兜底};
\node[dark,below left=66mm and 8mm of u,text width=28mm] (r) {业务路由};
\draw[arr] (u)-|(old);\draw[arr] (u)-|(new);
\draw[arr] (old)|-(r);
\draw[arr] (new)--node[lab,right]{缺少信息}(ask);
\draw[arr] (new.south west)--node[lab,sloped,above]{不满足}(fb.north);
\draw[arr] (new.east)--++(9mm,0)|-node[lab,near end,above]{满足接受条件}(r.east);
\draw[arr] (fb.south)|-(r.north);
\end{tikzpicture}}\end{center}
\figcap{意图识别替换路径：接受、澄清与回退分别处理}
'''

FIG2=r'''
\begin{center}\resizebox{\linewidth}{!}{\begin{tikzpicture}[x=1mm,y=1mm]
\node[dark,text width=145mm] at (59,22) {线上决策：只加载经过批准的版本};
\node[box,text width=28mm] (b) at (0,0) {业务节点};
\node[accent,text width=28mm] (s) at (38,0) {决策服务\\模型适配与推理};
\node[box,text width=32mm] (p) at (78,0) {接受／澄清／回退\\业务路由或原流程};
\node[box,text width=28mm] (l) at (118,0) {调用记录\\质量反馈};
\draw[arr] (b.east)--(s.west);\draw[arr](s.east)--(p.west);\draw[arr](p.east)--(l.west);
\node[dark,text width=145mm] at (59,-28) {离线优化：审核错误、生成候选、独立验证};
\node[box,text width=28mm] (d) at (0,-50) {反馈审核\\错误分析};
\node[accent,text width=28mm] (o) at (38,-50) {提示优化\\业务微调};
\node[box,text width=32mm] (e) at (78,-50) {统一评测\\独立验证与校准\\冻结候选并盲测};
\node[box,text width=28mm] (v) at (118,-50) {人工审批\\不可变版本包};
\draw[arr](d.east)--(o.west);\draw[arr](o.east)--(e.west);\draw[arr](e.east)--(v.west);
\draw[arr,draw=Muted,line width=.8pt] (l.south)--(118,-13)--(142,-13)--(142,-39)--node[lab,above,pos=.45]{业务反馈进入审核}(0,-39)--(d.north);
\draw[arr,draw=Teal,line width=.9pt] (v.south)--(118,-65)--(-24,-65)--(-24,11)--node[lab,above,pos=.6]{批准版本加载}(38,11)--(s.north);
\end{tikzpicture}}\end{center}
\figcap{总体架构：线上执行与离线优化分离，版本包连接两侧}
'''

FIG3=r'''
\begin{center}\begin{tikzpicture}
\node[dark,text width=53mm] (f) {经审核的真实错误 → 错误诊断};
\node[box,below left=10mm and 8mm of f,text width=37mm] (fix) {输入或标签问题\\修复输入与标注};
\node[accent,below=10mm of f,text width=37mm] (p) {描述表达不清\\固定模型，优化提示};
\node[accent,below right=10mm and 8mm of f,text width=37mm] (t) {领域能力不足\\冻结任务与提示，补数微调};
\draw[arr] (f)--(fix);\draw[arr](f)--(p);\draw[arr](f)--(t);
\node[box,below=12mm of p,text width=55mm] (e) {固定数据与预算下评测\\满足质量约束且有收益？};
\draw[arr](p)--(e);\draw[arr](t)|-(e);
\node[box,left=7mm of e,text width=35mm] (k) {保留原版本\\或停止实验};
\draw[arr](e)--node[lab,above]{否}(k);
\node[accent,below=9mm of e,text width=55mm] (v) {独立验证与策略校准\\冻结候选并盲测};
\node[dark,below=7mm of v,text width=55mm] (a) {人工审批 → 发布 → 收集反馈};
\draw[arr](e)--node[lab,right]{是}(v);\draw[arr](v)--(a);
\draw[arr] (a.east)--++(35mm,0)|-node[lab,near start,right]{审核后进入下一轮}(f.east);
\end{tikzpicture}\end{center}
\figcap{双闭环协同：按错误成因选择优化路径，验证收益后发布}
'''

PATHS=r'''
\begin{center}\begin{tikzpicture}
\node[accent,text width=43mm,minimum height=22mm] (a) {01\quad 替换判断\\\footnotesize 分类／选项打分\\替代生成式判断};
\node[accent,right=6mm of a,text width=43mm,minimum height=22mm] (b) {02\quad 减少调用\\\footnotesize 先判断改写必要性\\跳过多余生成};
\node[accent,right=6mm of b,text width=43mm,minimum height=22mm] (c) {03\quad 缩短输入\\\footnotesize 筛选支撑性证据\\减少冗余上下文};
\node[dark,below=8mm of b,text width=147mm] (q) {共同前提：质量达标，且节省覆盖新增判断、筛选、回退与部署开销};
\draw[arr](a)--(q);\draw[arr](b)--(q);\draw[arr](c)--(q);
\end{tikzpicture}\end{center}
\figcap{三条收益路径可以独立采用，净收益必须按完整任务核算}
'''

EXPERIMENT=r'''
\begin{center}\begin{tikzpicture}
\node[box,text width=24mm] (a) {A\quad 现有模型\\\footnotesize 质量与费用基线};
\node[accent,right=5mm of a,text width=24mm] (b) {B\quad 原始决策\\\footnotesize 直接替换收益};
\node[accent,right=5mm of b,text width=24mm] (c) {C\quad 提示优化\\\footnotesize 描述改进增量};
\node[box,right=5mm of c,text width=24mm] (d) {D\quad 可选微调\\\footnotesize 领域能力增量};
\node[dark,right=5mm of d,text width=24mm] (e) {E\quad 最终策略\\\footnotesize 完整链路收益};
\draw[arr](a)--(b);\draw[arr](b)--(c);\draw[arr](c)--(d);\draw[arr](d)--(e);
\end{tikzpicture}\end{center}
\figcap{实验递进关系；E 使用开发与验证阶段选定的候选，D 可按条件开展}
'''

def esc(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in s)

def inline(s):
    # Protect links and bold using a token-free recursive split.
    pat=r'(\[[^\]]+\]\(https?://[^)]+\)|\*\*.*?\*\*)'
    parts=re.split(pat,s)
    result=''
    for p in parts:
        if p.startswith('**') and p.endswith('**'):
            result+=r'\textbf{'+inline(p[2:-2])+'}'
        elif re.match(r'\[[^\]]+\]\(https?://',p):
            m=re.match(r'\[([^\]]+)\]\(([^)]+)\)',p)
            result+=r'\href{'+m[2]+'}{'+esc(m[1])+'}'
        else: result+=esc(p)
    return result

TABLE_CAPTIONS=[
    '用户意图识别示例及下游处理','意图分类标签及易混淆边界',
    '意图识别流程优化前后对照','问题改写场景优化前后对照',
    '检索片段筛选场景优化前后对照','三条降本提速路径及生效条件',
    '示例业务链路优化前后对照','项目预期成效与验收关注点',
    '系统组件与职责分工','典型错误现象与优先处理方式',
    '决策模型优化对照组设置','离线评测指标及其用途',
    '完整业务链路场景与下游验证'
]
table_number=0
def table(rows):
    global table_number
    # Omit the source label-boundary table and the final results-template table.
    if table_number in (1, 13):
        table_number += 1
        return ''
    caption=TABLE_CAPTIONS[table_number]
    table_number+=1
    cells=[[c.strip() for c in x.strip().strip('|').split('|')] for x in rows]
    cells=[c for c in cells if not all(re.fullmatch(r':?-+:?',v) for v in c)]
    n=len(cells[0])
    if n==6: ratios=[.28,.144,.144,.144,.144,.144]
    elif n==4: ratios=[.15,.24,.29,.32]
    elif n==3: ratios=[.22,.38,.40]
    else: ratios=[.42,.58]
    # widths sum to linewidth after cell padding; use compact but readable table type.
    spec=''.join('>{\\raggedright\\arraybackslash}p{'+f'{r:.3f}\\dimexpr\\linewidth-{2*n}\\tabcolsep\\relax'+'}' for r in ratios)
    header=' & '.join(r'\textbf{'+inline(c)+'}' for c in cells[0])+r' \\'
    body=[r'{\small\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.28}',r'\begin{longtable}{'+spec+'}',r'\caption{'+caption+'}\label{tab:table-'+str(table_number)+r'}\\',r'\toprule',header,r'\midrule',r'\endfirsthead',r'\toprule',header,r'\midrule',r'\endhead',r'\midrule\multicolumn{'+str(n)+r'}{r}{\scriptsize\color{Muted}续下页}\\\endfoot',r'\bottomrule\endlastfoot']
    for row in cells[1:]: body+=[' & '.join(inline(c) for c in row)+r' \\']
    body += [r'\end{longtable}}']
    return '\n'.join(body)

lines=source.splitlines()
parts=[PRE]
i=0; figs=iter([FIG1,FIG2,FIG3]); current_section=0
while i<len(lines):
    s=lines[i].strip()
    if not s or s.startswith('# '): i+=1; continue
    if s=='**替换前后链路：**':
        parts.append(r'\pagebreak')
        parts.append(r'\textbf{替换前后链路：}')
        i+=1; continue
    if s.startswith('```mermaid'):
        i+=1
        while i<len(lines) and not lines[i].startswith('```'): i+=1
        parts.append(next(figs)); i+=1;continue
    if s.startswith('## '):
        current_section+=1
        title=re.sub(r'^[一二三四五六七八九十]+、','',s[3:])
        parts.append(r'\section{'+inline(title)+'}')
        if current_section==3: parts.append(PATHS)
        i+=1; continue
    if s.startswith('### '):
        title=re.sub(r'^\d+\.\d+\s*','',s[4:])
        parts.append(r'\subsection{'+inline(title)+'}')
        if s.startswith('### 6.1'): parts.append(EXPERIMENT)
        i+=1; continue
    if s.startswith('|'):
        rows=[]
        while i<len(lines) and lines[i].strip().startswith('|'): rows.append(lines[i]);i+=1
        parts.append(table(rows));continue
    if s.startswith('- ') or re.match(r'^\d+\. ',s):
        numbered=bool(re.match(r'^\d+\. ',s));env='enumerate' if numbered else 'itemize'
        parts.append('\\begin{'+env+'}')
        while i<len(lines):
            t=lines[i].strip()
            if not (re.match(r'^\d+\. ',t) if numbered else t.startswith('- ')):break
            parts.append(r'\item '+inline(re.sub(r'^\d+\. ','',t) if numbered else t[2:]));i+=1
        parts.append('\\end{'+env+'}');continue
    if s.startswith('> '):
        parts.append(r'\begin{insight}{类别描述示例}'+inline(s[2:])+r'\end{insight}');i+=1;continue
    if s.startswith('**每成功任务总成本 ='):
        parts.append(r'\begin{insight}{完整成本口径}\[\text{每成功任务总成本}=\frac{\text{全部任务总成本}}{\text{成功任务数}}\]\end{insight}')
    else: parts.append(inline(s)+'\n')
    i+=1
parts.append(r'\end{document}')
tex=OUT/'业务决策节点轻量化与双闭环RSI自优化方案.tex'
tex.write_text('\n\n'.join(parts),encoding='utf-8')
build=ROOT/'work'/'latex-build';build.mkdir(exist_ok=True)
for k in range(2):
    p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={build}',str(tex)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
    (ROOT/'work'/f'compile-{k+1}.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
    print('pass',k+1,'exit',p.returncode)
    if p.returncode: print((p.stdout+p.stderr)[-7000:]);raise SystemExit(1)
pdf=build/(tex.stem+'.pdf')
shutil.copy2(pdf,OUT/pdf.name)
print('Delivered',OUT/pdf.name)
print('Tables:',table_number)
