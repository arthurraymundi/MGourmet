import { ShoppingBag, Trash2, X } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { useCart } from '@/features/cart/use-cart'
import type { CustomerDetails } from '@/types/domain'
import { formatCurrency } from '@/utils/currency'
import { createOrderMessage, createWhatsAppUrl } from '@/utils/whatsapp'
import { CheckoutForm } from './checkout-form'
import { QuantityControl } from './quantity-control'

interface CartSummaryProps {
  mobile?: boolean
  onClose?: () => void
}

export function CartSummary({ mobile = false, onClose }: CartSummaryProps) {
  const { items, itemCount, total, incrementItem, decrementItem, removeItem, clearCart } = useCart()

  function handleCheckout(customer: CustomerDetails) {
    if (items.length === 0) return
    window.open(createWhatsAppUrl(createOrderMessage(items, total, customer)), '_blank', 'noopener,noreferrer')
    if (window.confirm('Deseja limpar o carrinho?')) {
      clearCart()
      onClose?.()
    }
  }

  const header = (
    <div className="flex shrink-0 items-center justify-between gap-3">
      <div className="flex items-center gap-2"><ShoppingBag className="h-5 w-5 text-orange-600" /><h2 className="text-lg font-semibold">Seu pedido {itemCount > 0 ? `(${itemCount})` : ''}</h2></div>
      {mobile ? <Button variant="ghost" size="sm" type="button" onClick={onClose} aria-label="Fechar carrinho"><X className="h-5 w-5" /></Button> : null}
    </div>
  )

  const content = (
    <>
      {items.length === 0 ? (
        <div className="py-8 text-center text-sm text-[var(--color-text-secondary)]"><ShoppingBag className="mx-auto mb-3 h-8 w-8" />Seu carrinho está vazio. Adicione seus pratos favoritos.</div>
      ) : (
        <>
          <ul className="space-y-4 border-y border-[var(--color-border)] py-4">
            {items.map((item) => (
              <li className="flex gap-3" key={item.product.id}>
                <img src={item.product.imageUrl} alt="" className="h-16 w-16 rounded-lg object-cover" />
                <div className="min-w-0 flex-1">
                  <div className="flex items-start justify-between gap-2"><p className="text-sm font-medium">{item.product.name}</p><Button variant="ghost" size="sm" type="button" onClick={() => removeItem(item.product.id)} aria-label={`Remover ${item.product.name}`}><Trash2 className="h-4 w-4 text-red-600" /></Button></div>
                  <p className="text-xs text-[var(--color-text-secondary)]">{formatCurrency(item.product.price)} cada</p>
                  <div className="mt-2 flex items-center justify-between gap-2"><QuantityControl quantity={item.quantity} label={item.product.name} onIncrement={() => incrementItem(item.product.id)} onDecrement={() => decrementItem(item.product.id)} /><span className="text-sm font-semibold">{formatCurrency(item.product.price * item.quantity)}</span></div>
                </div>
              </li>
            ))}
          </ul>
          <div className="flex items-center justify-between py-4"><span className="font-semibold">Total</span><span className="text-xl font-semibold text-orange-600">{formatCurrency(total)}</span></div>
          <Button variant="ghost" size="sm" type="button" onClick={clearCart} className="w-full">Limpar carrinho</Button>
        </>
      )}
      <CheckoutForm disabled={items.length === 0} onSubmit={handleCheckout} />
    </>
  )

  if (mobile) return <div className="flex h-full flex-col bg-white p-5">{header}<div className="min-h-0 flex-1 overflow-y-auto overscroll-contain pt-4 scroll-smooth">{content}</div></div>
  return <Card className="flex max-h-[calc(100vh-6rem)] flex-col overflow-hidden"><div className="pb-4">{header}</div><div className="min-h-0 flex-1 overflow-y-auto overscroll-contain pr-1 scroll-smooth">{content}</div></Card>
}
