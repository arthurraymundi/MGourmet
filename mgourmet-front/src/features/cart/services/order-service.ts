import type { CartItem, CustomerDetails } from '@/types/domain'
import { postToApi } from '@/services/api-client'

interface CreatedOrder {
  id: number
  total: number
}

export function createOrder(items: CartItem[], customer: CustomerDetails) {
  return postToApi<CreatedOrder>('/orders', {
    customer_name: customer.name,
    customer_phone: customer.phone,
    delivery_method: customer.deliveryMethod,
    street: customer.street || null,
    number: customer.number || null,
    neighborhood: customer.neighborhood || null,
    complement: customer.complement || null,
    notes: customer.notes || null,
    items: items.map((item) => ({ product_id: item.product.id, quantity: item.quantity })),
  })
}
