import { getFromApi, type ListResponse } from '@/services/api-client'
import type { Product } from '@/types/domain'

export async function getProducts(): Promise<Product[]> {
  const response = await getFromApi<ListResponse<Product>>('/products')
  return response.items
}

export async function getFeaturedProducts(): Promise<Product[]> {
  const response = await getFromApi<ListResponse<Product>>('/products/featured')
  return response.items
}
