import type { InputHTMLAttributes } from 'react'
import { cn } from '@/utils/cn'

export function Input({ className, ...props }: InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={cn(
        'h-11 w-full rounded-xl border border-[var(--color-border)] bg-white px-3 text-sm text-[var(--color-text-primary)] placeholder:text-[var(--color-text-secondary)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-primary-500)]',
        className,
      )}
      {...props}
    />
  )
}
