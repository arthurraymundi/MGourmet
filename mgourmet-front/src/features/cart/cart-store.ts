import { createContext } from 'react'
import type { CartItem, Product } from '@/types/domain'

export interface CartContextValue {
  items: CartItem[]
  itemCount: number
  subtotal: number
  total: number
  addItem: (product: Product) => void
  incrementItem: (productId: string) => void
  decrementItem: (productId: string) => void
  removeItem: (productId: string) => void
  clearCart: () => void
}

export const CartContext = createContext<CartContextValue | null>(null)
