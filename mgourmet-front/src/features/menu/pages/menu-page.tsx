import { useEffect, useState } from 'react'
import { ProductCard } from '@/components/common/product-card'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { Input } from '@/components/ui/input'
import { PAGE_META } from '@/data/seo'
import { useMenuFilters, type MenuSort } from '@/hooks/use-menu-filters'
import { getProducts } from '@/services/product-service'
import type { Product, ProductCategory } from '@/types/domain'

const categories: Array<ProductCategory | 'all'> = [
  'all',
  'Hiperproteica',
  'Low Carb',
  'Emagrecimento',
  'Ganho de Massa',
  'Vegetariana',
]

const sortLabels: Record<MenuSort, string> = {
  relevance: 'Relevância',
  'price-asc': 'Preço: menor para maior',
  'price-desc': 'Preço: maior para menor',
  'protein-desc': 'Mais proteína',
}

export default function MenuPage() {
  const [products, setProducts] = useState<Product[]>([])
  const { query, category, sort, setQuery, setCategory, setSort, filteredProducts } = useMenuFilters(products)

  useEffect(() => {
    void getProducts().then(setProducts)
  }, [])

  return (
    <>
      <Seo meta={PAGE_META.menu} />
      <Section>
        <SectionTitle
          eyebrow="Cardápio"
          title="Escolha por objetivo nutricional"
          description="Filtre por categoria, busque pratos e ordene conforme sua prioridade."
        />

        <div className="mb-6 grid gap-3 md:grid-cols-3">
          <Input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Buscar por nome ou descrição"
            aria-label="Buscar pratos no cardápio"
          />
          <select
            className="h-11 rounded-xl border border-[var(--color-border)] px-3 text-sm"
            value={category}
            onChange={(event) => setCategory(event.target.value as ProductCategory | 'all')}
            aria-label="Filtrar cardápio por categoria"
          >
            {categories.map((item) => (
              <option key={item} value={item}>
                {item === 'all' ? 'Todas as categorias' : item}
              </option>
            ))}
          </select>
          <select
            className="h-11 rounded-xl border border-[var(--color-border)] px-3 text-sm"
            value={sort}
            onChange={(event) => setSort(event.target.value as MenuSort)}
            aria-label="Ordenação do cardápio"
          >
            {Object.entries(sortLabels).map(([value, label]) => (
              <option key={value} value={value}>
                {label}
              </option>
            ))}
          </select>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {filteredProducts.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </Section>
    </>
  )
}
