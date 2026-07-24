import { useState } from 'react'
import { ChevronDown } from 'lucide-react'
import type { FaqItem as FaqItemType } from '@/types/domain'
import { cn } from '@/utils/cn'

interface FaqItemProps {
  item: FaqItemType
}

export function FAQItem({ item }: FaqItemProps) {
  const [open, setOpen] = useState(false)

  return (
    <div className="rounded-2xl border border-[var(--color-border)] bg-white p-4">
      <button
        type="button"
        className="flex w-full items-center justify-between gap-3 text-left"
        onClick={() => setOpen((prev) => !prev)}
      >
        <span className="font-medium">{item.question}</span>
        <ChevronDown className={cn('h-4 w-4 transition-transform', open && 'rotate-180')} />
      </button>
      {open ? <p className="pt-3 text-sm text-[var(--color-text-secondary)]">{item.answer}</p> : null}
    </div>
  )
}
