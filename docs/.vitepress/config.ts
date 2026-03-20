import { defineConfig } from "vitepress";

const repo = "https://github.com/Sunwood-ai-labs/timberborn-modding-skill";

export default defineConfig({
  base: "/timberborn-modding-skill/",
  cleanUrls: true,
  lang: "en-US",
  title: "Timberborn Modding Skill",
  description: "Turn GLB assets into placeable Timberborn buildings with Codex.",
  head: [["link", { rel: "icon", href: "/skillmark.svg" }]],
  lastUpdated: true,
  themeConfig: {
    logo: "/skillmark.svg",
    search: {
      provider: "local",
    },
    socialLinks: [{ icon: "github", link: repo }],
  },
  locales: {
    root: {
      label: "English",
      lang: "en-US",
      title: "Timberborn Modding Skill",
      description: "Turn GLB assets into placeable Timberborn buildings with Codex.",
      themeConfig: {
        nav: [
          { text: "Guide", link: "/guide/getting-started" },
          { text: "Routes", link: "/guide/workflow-routes" },
          { text: "Troubleshooting", link: "/guide/troubleshooting" },
        ],
        sidebar: [
          {
            text: "Guide",
            items: [
              { text: "Getting Started", link: "/guide/getting-started" },
              { text: "Route Guide", link: "/guide/workflow-routes" },
              { text: "Repository Structure", link: "/guide/repository-structure" },
              { text: "Troubleshooting", link: "/guide/troubleshooting" },
            ],
          },
        ],
        footer: {
          message: "Released under the MIT License.",
          copyright: "Copyright (c) 2026 Sunwood-ai-labs",
        },
        editLink: {
          pattern: "https://github.com/Sunwood-ai-labs/timberborn-modding-skill/edit/main/docs/:path",
          text: "Edit this page on GitHub",
        },
      },
    },
    ja: {
      label: "日本語",
      lang: "ja-JP",
      link: "/ja/",
      title: "Timberborn Modding Skill",
      description: "GLB アセットを Timberborn の建物 MOD に落とし込むための Codex スキル。",
      themeConfig: {
        nav: [
          { text: "ガイド", link: "/ja/guide/getting-started" },
          { text: "ルート選定", link: "/ja/guide/workflow-routes" },
          { text: "トラブルシュート", link: "/ja/guide/troubleshooting" },
        ],
        sidebar: [
          {
            text: "ガイド",
            items: [
              { text: "はじめに", link: "/ja/guide/getting-started" },
              { text: "ルート選定", link: "/ja/guide/workflow-routes" },
              { text: "リポジトリ構成", link: "/ja/guide/repository-structure" },
              { text: "トラブルシュート", link: "/ja/guide/troubleshooting" },
            ],
          },
        ],
        outlineTitle: "目次",
        footer: {
          message: "MIT License のもとで公開しています。",
          copyright: "Copyright (c) 2026 Sunwood-ai-labs",
        },
        editLink: {
          pattern: "https://github.com/Sunwood-ai-labs/timberborn-modding-skill/edit/main/docs/:path",
          text: "GitHub でこのページを編集",
        },
      },
    },
  },
});
