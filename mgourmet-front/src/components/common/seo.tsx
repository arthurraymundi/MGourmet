import { useEffect } from 'react'
import { SITE_URL } from '@/data/seo'
import type { SeoMeta } from '@/types/domain'

interface SeoProps {
  meta: SeoMeta
  schema?: Record<string, unknown>
}

function upsertMeta(selector: string, attrs: Record<string, string>) {
  const existing = document.head.querySelector(selector)
  const node = existing ?? document.createElement('meta')
  Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value))
  if (!existing) document.head.appendChild(node)
}

export function Seo({ meta, schema }: SeoProps) {
  useEffect(() => {
    const url = `${SITE_URL}${meta.path}`
    document.title = meta.title
    upsertMeta('meta[name="description"]', { name: 'description', content: meta.description })
    upsertMeta('meta[property="og:title"]', { property: 'og:title', content: meta.title })
    upsertMeta('meta[property="og:description"]', {
      property: 'og:description',
      content: meta.description,
    })
    upsertMeta('meta[property="og:url"]', { property: 'og:url', content: url })
    if (meta.image) {
      upsertMeta('meta[property="og:image"]', { property: 'og:image', content: meta.image })
      upsertMeta('meta[name="twitter:image"]', { name: 'twitter:image', content: meta.image })
    }
    upsertMeta('meta[name="twitter:title"]', { name: 'twitter:title', content: meta.title })
    upsertMeta('meta[name="twitter:description"]', {
      name: 'twitter:description',
      content: meta.description,
    })

    const scriptId = 'localbusiness-schema'
    const current = document.getElementById(scriptId)
    if (current) current.remove()
    if (schema) {
      const script = document.createElement('script')
      script.id = scriptId
      script.type = 'application/ld+json'
      script.text = JSON.stringify(schema)
      document.head.appendChild(script)
    }
  }, [meta, schema])

  return null
}
