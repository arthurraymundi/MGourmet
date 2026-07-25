import { memo } from 'react'
import { Minus, Plus } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import type { Product } from '@/types/domain'
import { formatCurrency } from '@/utils/currency'

interface ProductCardProps {
  product: Product
  quantity?: number
  onAdd?: (product: Product) => void
  onIncrement?: (productId: string) => void
  onDecrement?: (productId: string) => void
}

export const ProductCard = memo(function ProductCard({
  product,
  quantity = 0,
  onAdd,
  onIncrement,
  onDecrement,
}: ProductCardProps) {
  return (
    <Card className="h-full overflow-hidden p-0">
      <img
        src={product.imageUrl}
        alt={product.name}
        className="h-44 w-full object-cover sm:h-48"
        loading="lazy"
      />
      <div className="space-y-4 p-5">
        <div className="flex items-center justify-between gap-3">
          <h3 className="text-lg font-semibold">{product.name}</h3>
          <Badge>{product.category}</Badge>
        </div>
        <p className="text-sm text-[var(--color-text-secondary)]">{product.description}</p>

        <div>
          <h4 className="mb-2 text-sm font-medium">Ingredientes</h4>
          <ul className="flex flex-wrap gap-2">
            {product.ingredients.slice(0, 5).map((ingredient) => (
              <li
                key={ingredient}
                className="rounded-full bg-[var(--color-bg-subtle)] px-2 py-1 text-xs text-[var(--color-text-secondary)]"
              >
                {ingredient}
              </li>
            ))}
          </ul>
        </div>

        <dl className="grid grid-cols-2 gap-2 text-xs text-[var(--color-text-secondary)]">
          <div>Cal: {product.nutrition.calories}</div>
          <div>Prot: {product.nutrition.protein}g</div>
          <div>Carb: {product.nutrition.carbs}g</div>
          <div>Gord: {product.nutrition.fat}g</div>
        </dl>
        <p className="text-lg font-semibold text-orange-600">{formatCurrency(product.price)}</p>
        {onAdd && onIncrement && onDecrement ? (
          quantity > 0 ? (
            <div className="flex h-11 items-center justify-between rounded-xl border border-[var(--color-border)]" aria-label={`Quantidade de ${product.name}`}>
              <Button variant="ghost" size="sm" type="button" onClick={() => onDecrement(product.id)} aria-label={`Remover uma unidade de ${product.name}`}>
                <Minus className="h-4 w-4" />
              </Button>
              <span className="text-sm font-semibold" aria-live="polite">{quantity}</span>
              <Button variant="ghost" size="sm" type="button" onClick={() => onIncrement(product.id)} aria-label={`Adicionar uma unidade de ${product.name}`}>
                <Plus className="h-4 w-4" />
              </Button>
            </div>
          ) : (
            <Button className="w-full" type="button" onClick={() => onAdd(product)}>Adicionar ao carrinho</Button>
          )
        ) : (
          <Button className="w-full">Adicionar ao carrinho</Button>
        )}
      </div>
    </Card>
  )
})
