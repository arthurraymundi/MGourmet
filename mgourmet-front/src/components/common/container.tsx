import type { PropsWithChildren } from 'react'
import { cn } from '@/utils/cn'

interface ContainerProps extends PropsWithChildren {
  className?: string
}

export function Container({ className, children }: ContainerProps) {
  return <div className={cn('mx-auto w-full max-w-[1200px] px-4 md:px-6', className)}>{children}</div>
}
