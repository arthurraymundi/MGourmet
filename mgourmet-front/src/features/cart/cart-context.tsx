import { useCallback, useEffect, useMemo, useState, type PropsWithChildren } from 'react'
import type { CartItem, Product } from '@/types/domain'
import { CartContext } from './cart-store'

const CART_STORAGE_KEY = 'mgourmet-cart'
let cachedCart: CartItem[] | undefined

function loadCart(): CartItem[] {
  if (cachedCart) return cachedCart

  try {
    const storedCart = window.localStorage.getItem(CART_STORAGE_KEY)
    if (!storedCart) return (cachedCart = [])

    const parsedCart: unknown = JSON.parse(storedCart)
    if (!Array.isArray(parsedCart)) return (cachedCart = [])

    return (cachedCart = parsedCart.filter(
      (item): item is CartItem =>
        typeof item === 'object' &&
        item !== null &&
        'product' in item &&
        'quantity' in item &&
        typeof item.product === 'object' &&
        item.product !== null &&
        'id' in item.product &&
        'name' in item.product &&
        'price' in item.product &&
        typeof item.product.id === 'string' &&
        typeof item.product.name === 'string' &&
        typeof item.product.price === 'number' &&
        typeof item.quantity === 'number' &&
        item.quantity > 0,
    ))
  } catch {
    return (cachedCart = [])
  }
}

export function CartProvider({ children }: PropsWithChildren) {
  const [items, setItems] = useState<CartItem[]>(loadCart)

  useEffect(() => {
    window.localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(items))
  }, [items])

  const addItem = useCallback((product: Product) => {
    setItems((currentItems) => {
      const existingItem = currentItems.find((item) => item.product.id === product.id)
      if (existingItem) {
        return currentItems.map((item) =>
          item.product.id === product.id ? { ...item, quantity: item.quantity + 1 } : item,
        )
      }
      return [...currentItems, { product, quantity: 1 }]
    })
  }, [])

  const incrementItem = useCallback((productId: string) => {
    setItems((currentItems) =>
      currentItems.map((item) =>
        item.product.id === productId ? { ...item, quantity: item.quantity + 1 } : item,
      ),
    )
  }, [])

  const decrementItem = useCallback((productId: string) => {
    setItems((currentItems) =>
      currentItems.flatMap((item) => {
        if (item.product.id !== productId) return item
        return item.quantity > 1 ? { ...item, quantity: item.quantity - 1 } : []
      }),
    )
  }, [])

  const removeItem = useCallback((productId: string) => {
    setItems((currentItems) => currentItems.filter((item) => item.product.id !== productId))
  }, [])

  const clearCart = useCallback(() => setItems([]), [])

  const value = useMemo(() => {
    const itemCount = items.reduce((count, item) => count + item.quantity, 0)
    const subtotal = items.reduce((sum, item) => sum + item.product.price * item.quantity, 0)

    return { items, itemCount, subtotal, total: subtotal, addItem, incrementItem, decrementItem, removeItem, clearCart }
  }, [addItem, clearCart, decrementItem, incrementItem, items, removeItem])

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>
}
