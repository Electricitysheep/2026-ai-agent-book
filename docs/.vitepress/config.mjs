import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/2026-ai-agent-book/',
  title: "Agentic OS 2026",
  description: "重构工作流：2026 中国 AI Agent 终极进化史",
  themeConfig: {
    search: {
      provider: 'local'
    },
    logo: '/niche-lain.png',
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/intro' },
      { text: 'About', link: '/about' }
    ],
    sidebar: [
      {
        text: '序章',
        items: [
          { text: 'Agentic OS 的崛起', link: '/intro' },
          { text: '关于本项目', link: '/about' }
        ]
      },
      {
        text: '核心阵营',
        items: [
          { text: '1. DeepSeek 终端的反叛', link: '/vol1' },
          { text: '2. ByteDance Trae & Coze', link: '/vol2' },
          { text: '3. Alibaba Tongyi Lingma', link: '/vol3' },
          { text: '4. Zhipu GLM-PC', link: '/vol4' },
          { text: '5. Hardware & Open Source', link: '/vol5' },
          { text: '6. Tencent WorkBuddy', link: '/vol6' },
          { text: '7. Kimi Agent Swarm', link: '/vol7' },
          { text: '8. Baidu Comate', link: '/vol8' },
          { text: '9. MiniMax Hailuo', link: '/vol9' }
        ]
      },
      {
        text: '终章',
        items: [
          { text: '国际对抗与未来展望', link: '/vol10' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/10k-ai-agent-book' }
    ]
  }
})
