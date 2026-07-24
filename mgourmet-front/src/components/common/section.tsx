import type { PropsWithChildren } from 'react'
import { cn } from '@/utils/cn'
import { Container } from './container'

interface SectionProps extends PropsWithChildren {
  className?: string
  containerClassName?: string
}

export function Section({ className, containerClassName, children }: SectionProps) {
  return (
    <section className={cn('py-12 md:py-16', className)}>
      <Container className={containerClassName}>{children}</Container>
    </section>
  )
}
