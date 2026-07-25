import { useCallback, useEffect, useMemo, useState } from 'react'
import { ProductCard } from '@/components/common/product-card'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { Input } from '@/components/ui/input'
import { PAGE_META } from '@/data/seo'
import { CartSummary } from '@/features/cart/components/cart-summary'
import { MobileCart } from '@/features/cart/components/mobile-cart'
import { useCart } from '@/features/cart/use-cart'
import { useMenuFilters, type MenuSort } from '@/hooks/use-menu-filters'
import { getProducts } from '@/services/product-service'
import type { Product, ProductCategory } from '@/types/domain'

const categories: Array<ProductCategory | 'all'> = ['all', 'Hiperproteica', 'Low Carb', 'Emagrecimento', 'Ganho de Massa', 'Vegetariana', 'Prato Fitness', 'Mini Prato Fitness', 'Prato Kids', 'Sopa', 'Proteína', 'Premium']

const sortLabels: Record<MenuSort, string> = {
  relevance: 'Relevância',
  'price-asc': 'Preço: menor para maior',
  'price-desc': 'Preço: maior para menor',
  'protein-desc': 'Mais proteína',
}

export default function MenuPage() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const { query, category, sort, setQuery, setCategory, setSort, filteredProducts } = useMenuFilters(products)
  const { items, addItem, incrementItem, decrementItem } = useCart()
  const quantities = useMemo(() => new Map(items.map((item) => [item.product.id, item.quantity])), [items])
  const handleAdd = useCallback((product: Product) => addItem(product), [addItem])

  useEffect(() => {
    let active = true
    async function loadProducts() {
      try {
        setLoading(true)
        setError(null)
        const loadedProducts = await getProducts()
        if (active) setProducts(loadedProducts)
      } catch {
        if (active) setError('Não foi possível carregar o cardápio. Tente novamente em instantes.')
      } finally {
        if (active) setLoading(false)
      }
    }
    void loadProducts()
    return () => { active = false }
  }, [])

  return (
    <>
      <Seo meta={PAGE_META.menu} />
      <Section containerClassName="lg:grid lg:grid-cols-[minmax(0,1fr)_360px] lg:gap-8">
        <div>
          <SectionTitle eyebrow="Cardápio" title="Escolha por objetivo nutricional" description="Filtre por categoria, busque pratos e ordene conforme sua prioridade." />
          <div className="mb-6 grid gap-3 md:grid-cols-3">
            <Input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Buscar por nome ou descrição" aria-label="Buscar pratos no cardápio" />
            <select className="h-11 rounded-xl border border-[var(--color-border)] px-3 text-sm" value={category} onChange={(event) => setCategory(event.target.value as ProductCategory | 'all')} aria-label="Filtrar cardápio por categoria">
              {categories.map((item) => <option key={item} value={item}>{item === 'all' ? 'Todas as categorias' : item}</option>)}
            </select>
            <select className="h-11 rounded-xl border border-[var(--color-border)] px-3 text-sm" value={sort} onChange={(event) => setSort(event.target.value as MenuSort)} aria-label="Ordenação do cardápio">
              {Object.entries(sortLabels).map(([value, label]) => <option key={value} value={value}>{label}</option>)}
            </select>
          </div>
          {loading ? <p className="text-sm text-[var(--color-text-secondary)]">Carregando cardápio...</p> : null}
          {error ? <p className="text-sm text-red-600" role="alert">{error}</p> : null}
          {!loading && !error ? <>
            <p className="mb-4 text-sm text-[var(--color-text-secondary)]">Exibindo {filteredProducts.length} {filteredProducts.length === 1 ? 'produto' : 'produtos'}</p>
            {filteredProducts.length > 0 ? <div className="grid gap-6 md:grid-cols-2">
              {filteredProducts.map((product) => <ProductCard key={product.id} product={product} quantity={quantities.get(product.id) ?? 0} onAdd={handleAdd} onIncrement={incrementItem} onDecrement={decrementItem} />)}
            </div> : <p className="text-sm text-[var(--color-text-secondary)]">Nenhum produto foi encontrado com os filtros selecionados.</p>}
          </> : null}
        </div>
        <aside className="sticky top-20 hidden self-start lg:block"><CartSummary /></aside>
      </Section>
      <MobileCart />
    </>
  )
}
