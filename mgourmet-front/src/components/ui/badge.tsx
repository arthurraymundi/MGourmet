import type { HTMLAttributes } from 'react'
import { cn } from '@/utils/cn'

export function Badge({ className, ...props }: HTMLAttributes<HTMLSpanElement>) {
  return (
    <span
      className={cn(
        'inline-flex items-center rounded-full bg-orange-100 px-3 py-1 text-xs font-medium text-orange-700',
        className,
      )}
      {...props}
    />
  )
}
