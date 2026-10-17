// astro.config.mjs
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://byjunyoung.github.io',
  i18n: { defaultLocale: 'ko', locales: ['ko', 'en'], routing: { prefixDefaultLocale: false } },
  // 2026-09-24 메뉴 이름을 work·activity·play로 바꾸면서 옛 주소를 새 주소로 넘긴다(밖에 걸린 링크 보호)
  redirects: {
    '/works/[slug]': '/work/[slug]',
    '/en/works/[slug]': '/en/work/[slug]',
    '/activities': '/activity',
    '/activities/[slug]': '/activity/[slug]',
    '/en/activities': '/en/activity',
    '/en/activities/[slug]': '/en/activity/[slug]',
    '/playground': '/play',
    '/playground/[slug]': '/play/[slug]',
    '/en/playground': '/en/play',
    '/en/playground/[slug]': '/en/play/[slug]',
    // doan(옛 design-core)은 2026-10-17 폐기 — 옛 링크는 플레이 목록으로
    '/play/doan': '/play',
    '/en/play/doan': '/en/play',
    '/play/design-core': '/play',
    '/en/play/design-core': '/en/play',
    '/playground/design-core': '/play',
    '/en/playground/design-core': '/en/play',
  },
  integrations: [sitemap({ i18n: { defaultLocale: 'ko', locales: { ko: 'ko-KR', en: 'en-US' } } })],
});
