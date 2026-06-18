import os
import re

with open('C:/Users/24835/.gemini/antigravity/brain/476bb426-700e-432e-8578-7f1cf7d9344b/2026_the_ultimate_ai_agent_history_book_v9.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by headers (e.g., # 第一卷)
parts = re.split(r'\n(?=# 第[一二三四五六七八九十]+卷|# 序章)', content)

docs_dir = 'C:/Users/24835/.gemini/antigravity/scratch/10k-ai-agent-book/docs'
if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)

# Create index.md
index_content = '''---
layout: home

hero:
  name: "Agentic OS 2026"
  text: "重构工作流：中国 AI Agent 终极进化史"
  tagline: "一份真实字数过万的极客圣经。全图床 200 OK 真实校验。"
  actions:
    - theme: brand
      text: 开始阅读
      link: /intro
    - theme: alt
      text: GitHub Repo
      link: https://github.com/10k-ai-agent-book

features:
  - title: 全景解析十家巨头
    details: DeepSeek、字节、阿里、腾讯等最强 Agent 架构大解密。
  - title: 底层生态位剖析
    details: 从 CLI 到 IDE，从云端沙盒到操作系统底层接管。
  - title: 国际基准对比
    details: SWE-bench 2026 极限算力碰撞，全网独家收录。
---
'''

with open(os.path.join(docs_dir, 'index.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

for part in parts:
    if not part.strip(): continue
    fname = 'part.md'
    if '# 序章' in part or '# 《重构' in part: fname = 'intro.md'
    elif '# 第一卷' in part: fname = 'vol1.md'
    elif '# 第二卷' in part: fname = 'vol2.md'
    elif '# 第三卷' in part: fname = 'vol3.md'
    elif '# 第四卷' in part: fname = 'vol4.md'
    elif '# 第五卷' in part: fname = 'vol5.md'
    elif '# 第六卷' in part: fname = 'vol6.md'
    elif '# 第七卷' in part: fname = 'vol7.md'
    elif '# 第八卷' in part: fname = 'vol8.md'
    elif '# 第九卷' in part: fname = 'vol9.md'
    elif '# 第十卷' in part: fname = 'vol10.md'
    elif '# 第十一卷' in part: fname = 'epilogue.md'

    with open(os.path.join(docs_dir, fname), 'w', encoding='utf-8') as f:
        f.write(part.strip() + '\n\n')

print('VitePress docs split successfully.')
