import { useMemo, useState } from 'react'
import type { Product, ProductCategory } from '@/types/domain'

export type MenuSort = 'relevance' | 'price-asc' | 'price-desc' | 'protein-desc'

export function useMenuFilters(products: Product[]) {
  const [query, setQuery] = useState('')
  const [category, setCategory] = useState<ProductCategory | 'all'>('all')
  const [sort, setSort] = useState<MenuSort>('relevance')

  const filteredProducts = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase()
    const filtered = products.filter((product) => {
      const byCategory = category === 'all' || product.category === category
      const searchableContent = `${product.name} ${product.description}`.toLowerCase()
      const byQuery = normalizedQuery.length === 0 || searchableContent.includes(normalizedQuery)
      return byCategory && byQuery
    })

    const sorted = [...filtered]
    if (sort === 'price-asc') sorted.sort((a, b) => a.price - b.price)
    if (sort === 'price-desc') sorted.sort((a, b) => b.price - a.price)
    if (sort === 'protein-desc') {
      sorted.sort((a, b) => b.nutrition.protein - a.nutrition.protein)
    }

    return sorted
  }, [products, query, category, sort])

  return {
    query,
    category,
    sort,
    setQuery,
    setCategory,
    setSort,
    filteredProducts,
  }
}
