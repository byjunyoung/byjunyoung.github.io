// src/content.config.ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const link = z.object({ label: z.string().min(1), url: z.string().url() });
const localeId = ({ entry }: { entry: string }) => {
  const [slug, file] = entry.split('/');
  return file === 'index.en.md' ? `en/${slug}` : slug;
};

const works = defineCollection({
  loader: glob({ pattern: ['*/index.md', '*/index.en.md'], base: './src/content/works', generateId: localeId }),
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1),
      subtitle: z.string().min(1),
      org: z.string().min(1),
      year: z.string().min(1),
      role: z.string().min(1),
      responsibilities: z.array(z.string()).min(1),
      with: z.string().optional(),
      keywords: z.array(z.string()).default([]),
      link: link.optional(),
      tags: z.array(z.string()).min(1),
      kind: z.enum(['case-study', 'note']),
      cover: image(),
      loop: z.string().regex(/^\/media\/works\/[a-z0-9-]+\/[a-z0-9-]+\.mp4$/).optional(),
      order: z.number().int(),
      draft: z.boolean().default(false),
      press: z.array(link).default([]),
      awards: z.array(z.string()).default([]),
    }),
});

const activities = defineCollection({
  loader: glob({ pattern: ['*/index.md', '*/index.en.md'], base: './src/content/activities', generateId: localeId }),
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1),
      subtitle: z.string().min(1),
      role: z.string().min(1),
      period: z.string().min(1),
      links: z.array(link).default([]),
      cover: image().optional(),
      order: z.number().int(),
      draft: z.boolean().default(false),
    }),
});

export const collections = { works, activities };
