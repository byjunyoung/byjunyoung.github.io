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
    // design-core 레포가 doan(도안)으로 이름을 바꿨다
    '/play/design-core': '/play/doan',
    '/en/play/design-core': '/en/play/doan',
    '/playground/design-core': '/play/doan',
    '/en/playground/design-core': '/en/play/doan',
  },
  integrations: [sitemap({ i18n: { defaultLocale: 'ko', locales: { ko: 'ko-KR', en: 'en-US' } } })],
});
