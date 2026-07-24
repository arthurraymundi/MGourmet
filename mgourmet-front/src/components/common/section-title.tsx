import type { ReactNode } from 'react'

interface SectionTitleProps {
  eyebrow?: string
  title: string
  description?: ReactNode
}

export function SectionTitle({ eyebrow, title, description }: SectionTitleProps) {
  return (
    <header className="mx-auto mb-8 max-w-2xl text-center md:mb-10">
      {eyebrow ? (
        <p className="mb-3 text-sm font-semibold uppercase tracking-widest text-orange-600">{eyebrow}</p>
      ) : null}
      <h2 className="text-3xl font-semibold md:text-4xl">{title}</h2>
      {description ? <p className="mt-3 text-base text-[var(--color-text-secondary)]">{description}</p> : null}
    </header>
  )
}
