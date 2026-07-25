import { getFromApi, type ListResponse } from '@/services/api-client'
import type { Product } from '@/types/domain'

export async function getProducts(): Promise<Product[]> {
  const pageSize = 100
  const firstPage = await getFromApi<ListResponse<Product>>(`/products?page=1&page_size=${pageSize}`)

  if (firstPage.meta.totalPages <= 1) {
    return firstPage.items
  }

  const remainingPages = await Promise.all(
    Array.from({ length: firstPage.meta.totalPages - 1 }, (_, index) =>
      getFromApi<ListResponse<Product>>(`/products?page=${index + 2}&page_size=${pageSize}`),
    ),
  )

  return firstPage.items.concat(...remainingPages.map((page) => page.items))
}

export async function getFeaturedProducts(): Promise<Product[]> {
  const response = await getFromApi<ListResponse<Product>>('/products/featured')
  return response.items
}
