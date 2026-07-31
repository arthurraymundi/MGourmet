import { requestFromApi, type ListResponse } from '@/services/api-client'
import type { AdminOrder, DeliveryMethod, OrderSource, OrderStatus } from '@/types/domain'

function authorizedOptions(token: string, options: RequestInit = {}): RequestInit {
  return {
    ...options,
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}`, ...options.headers },
  }
}

export interface AdminOrderPayload {
  customerName: string
  customerPhone: string
  deliveryMethod: DeliveryMethod
  street?: string
  number?: string
  neighborhood?: string
  complement?: string
  notes?: string
  items: Array<{ productId: string; quantity: number }>
  source: OrderSource
  paymentMethod: string
  status: OrderStatus
}

export async function getAdminOrders(token: string, filters: { search?: string; status?: OrderStatus } = {}) {
  const query = new URLSearchParams({ page_size: '100' })
  if (filters.search) query.set('search', filters.search)
  if (filters.status) query.set('status', filters.status)
  const response = await requestFromApi<ListResponse<AdminOrder>>(`/orders?${query}`, authorizedOptions(token))
  return response.items
}

export function updateOrderStatus(token: string, orderId: number, status: OrderStatus) {
  return requestFromApi<AdminOrder>(`/orders/${orderId}/status`, authorizedOptions(token, { method: 'PUT', body: JSON.stringify({ status }) }))
}

export function createAdminOrder(token: string, payload: AdminOrderPayload) {
  return requestFromApi<AdminOrder>('/orders/admin', authorizedOptions(token, {
    method: 'POST',
    body: JSON.stringify({
      customer_name: payload.customerName,
      customer_phone: payload.customerPhone,
      delivery_method: payload.deliveryMethod,
      street: payload.street || null,
      number: payload.number || null,
      neighborhood: payload.neighborhood || null,
      complement: payload.complement || null,
      notes: payload.notes || null,
      items: payload.items.map((item) => ({ product_id: item.productId, quantity: item.quantity })),
      source: payload.source,
      payment_method: payload.paymentMethod,
      status: payload.status,
    }),
  }))
}

export function deleteAdminOrder(token: string, orderId: number) {
  return requestFromApi<void>(`/orders/${orderId}`, authorizedOptions(token, { method: 'DELETE' }))
}
