import { requestFromApi, type ListResponse } from '@/services/api-client'
import type { AdminOrder, OrderStatus } from '@/types/domain'

function authorizedOptions(token: string, options: RequestInit = {}): RequestInit {
  return {
    ...options,
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}`, ...options.headers },
  }
}

export async function getAdminOrders(token: string) {
  const response = await requestFromApi<ListResponse<AdminOrder>>('/orders?page_size=100', authorizedOptions(token))
  return response.items
}

export function updateOrderStatus(token: string, orderId: number, status: OrderStatus) {
  return requestFromApi<AdminOrder>(`/orders/${orderId}/status`, authorizedOptions(token, { method: 'PUT', body: JSON.stringify({ status }) }))
}
