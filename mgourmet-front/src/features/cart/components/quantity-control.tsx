import { Minus, Plus } from 'lucide-react'
import { Button } from '@/components/ui/button'

interface QuantityControlProps {
  quantity: number
  label: string
  onIncrement: () => void
  onDecrement: () => void
}

export function QuantityControl({ quantity, label, onIncrement, onDecrement }: QuantityControlProps) {
  return (
    <div className="flex items-center rounded-lg border border-[var(--color-border)]" aria-label={`Quantidade de ${label}`}>
      <Button variant="ghost" size="sm" type="button" onClick={onDecrement} aria-label={`Diminuir quantidade de ${label}`}>
        <Minus className="h-4 w-4" />
      </Button>
      <span className="min-w-7 text-center text-sm font-semibold" aria-live="polite">{quantity}</span>
      <Button variant="ghost" size="sm" type="button" onClick={onIncrement} aria-label={`Aumentar quantidade de ${label}`}>
        <Plus className="h-4 w-4" />
      </Button>
    </div>
  )
}
