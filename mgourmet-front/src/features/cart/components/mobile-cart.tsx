import { useState } from 'react'
import { ShoppingBag } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { useCart } from '@/features/cart/use-cart'
import { CartSummary } from './cart-summary'

export function MobileCart() {
  const [isOpen, setIsOpen] = useState(false)
  const { itemCount } = useCart()

  return (
    <div className="lg:hidden">
      <Button className="fixed bottom-20 right-4 z-40 h-12 rounded-full px-4 shadow-lg" type="button" onClick={() => setIsOpen(true)} aria-label="Abrir carrinho">
        <ShoppingBag className="h-5 w-5" /><span>Carrinho</span>{itemCount > 0 ? <span className="rounded-full bg-white px-2 py-0.5 text-xs font-semibold text-orange-600">{itemCount}</span> : null}
      </Button>
      {isOpen ? <div className="fixed inset-0 z-50 bg-black/40" role="dialog" aria-modal="true" aria-label="Resumo do pedido" onMouseDown={() => setIsOpen(false)}><aside className="ml-auto h-full w-[min(92vw,430px)]" onMouseDown={(event) => event.stopPropagation()}><CartSummary mobile onClose={() => setIsOpen(false)} /></aside></div> : null}
    </div>
  )
}
