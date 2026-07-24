import { CheckCircle2 } from 'lucide-react'
import { Card } from '@/components/ui/card'

interface BenefitCardProps {
  text: string
}

export function BenefitCard({ text }: BenefitCardProps) {
  return (
    <Card className="flex items-center gap-3 p-5">
      <CheckCircle2 className="h-5 w-5 text-orange-500" aria-hidden="true" />
      <p className="text-sm text-[var(--color-text-secondary)]">{text}</p>
    </Card>
  )
}
