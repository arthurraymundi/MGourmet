import { requestFromApi, type ListResponse } from '@/services/api-client'
import type { Product, ProductCategory } from '@/types/domain'

export interface ProductPayload {
  name: string
  description: string
  imageUrl: string
  price: number
  category: ProductCategory
  ingredients: string[]
  nutrition: Product['nutrition']
  featured: boolean
  isAvailable: boolean
}

function authorizedOptions(token: string, options: RequestInit = {}): RequestInit {
  return {
    ...options,
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}`, ...options.headers },
  }
}

export async function getAdminProducts(token: string) {
  const response = await requestFromApi<ListResponse<Product>>('/products/admin', authorizedOptions(token))
  return response.items
}

export function createAdminProduct(token: string, payload: ProductPayload) {
  return requestFromApi<Product>('/products', authorizedOptions(token, { method: 'POST', body: JSON.stringify(payload) }))
}

export function updateAdminProduct(token: string, productId: string, payload: Partial<ProductPayload>) {
  return requestFromApi<Product>(`/products/${productId}`, authorizedOptions(token, { method: 'PUT', body: JSON.stringify(payload) }))
}

export function deleteAdminProduct(token: string, productId: string) {
  return requestFromApi<void>(`/products/${productId}`, authorizedOptions(token, { method: 'DELETE' }))
}
