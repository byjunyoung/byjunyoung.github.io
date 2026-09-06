// src/lib/i18n.ts
export type Lang = 'ko' | 'en';
export const LANGS: readonly Lang[] = ['ko', 'en'];
export const langOf = (id: string): Lang => (id.startsWith('en/') ? 'en' : 'ko');
export const slugOf = (id: string): string => id.replace(/^en\//, '');
export const counterpartId = (id: string): string => (langOf(id) === 'en' ? slugOf(id) : `en/${id}`);
export const localePath = (lang: Lang, path: string): string => (lang === 'en' ? `/en${path}` : path); // path starts with '/'
export function byLang<T extends { id: string; data: { draft: boolean; order: number } }>(entries: T[], lang: Lang): T[] {
  return entries.filter((e) => langOf(e.id) === lang && !e.data.draft).sort((a, b) => a.data.order - b.data.order);
}
