import { Card } from '@/components/ui/card'
import type { Testimonial } from '@/types/domain'

interface TestimonialCardProps {
  testimonial: Testimonial
}

export function TestimonialCard({ testimonial }: TestimonialCardProps) {
  return (
    <Card className="h-full">
      <p className="text-sm leading-relaxed text-[var(--color-text-secondary)]">"{testimonial.quote}"</p>
      <p className="mt-4 text-sm font-semibold">{testimonial.name}</p>
      <p className="text-xs text-[var(--color-text-secondary)]">{testimonial.role}</p>
    </Card>
  )
}
