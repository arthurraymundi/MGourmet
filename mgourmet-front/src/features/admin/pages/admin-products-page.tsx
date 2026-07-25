import { useCallback, useEffect, useState } from 'react'
import { Pencil, Plus, Trash2 } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { formatCurrency } from '@/utils/currency'
import type { Product } from '@/types/domain'
import { ProductForm } from '../components/product-form'
import { useAdminAuth } from '../hooks/use-admin-auth'
import { createAdminProduct, deleteAdminProduct, getAdminProducts, type ProductPayload, updateAdminProduct } from '../services/admin-product-service'

export default function AdminProductsPage() {
  const { token } = useAdminAuth()
  const [products, setProducts] = useState<Product[]>([])
  const [editingProduct, setEditingProduct] = useState<Product | null | undefined>(undefined)
  const [isSaving, setIsSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const loadProducts = useCallback(async () => { if (!token) return; try { setLoading(true); setError(null); setProducts(await getAdminProducts(token)) } catch (loadError) { setError(loadError instanceof Error ? loadError.message : 'Não foi possível carregar os produtos.') } finally { setLoading(false) } }, [token])
  useEffect(() => { void loadProducts() }, [loadProducts])
  async function saveProduct(payload: ProductPayload) { if (!token) return; setIsSaving(true); try { if (editingProduct) await updateAdminProduct(token, editingProduct.id, payload); else await createAdminProduct(token, payload); setEditingProduct(undefined); await loadProducts() } finally { setIsSaving(false) } }
  async function removeProduct(product: Product) { if (!token || !window.confirm(`Excluir ${product.name}?`)) return; try { await deleteAdminProduct(token, product.id); await loadProducts() } catch (deleteError) { setError(deleteError instanceof Error ? deleteError.message : 'Não foi possível excluir o produto.') } }
  const formOpen = editingProduct !== undefined
  return <div className="space-y-6"><div className="flex flex-wrap items-start justify-between gap-4"><div><p className="text-sm font-medium text-orange-600">Cardápio</p><h1 className="text-3xl font-semibold">Produtos</h1><p className="mt-1 text-sm text-[var(--color-text-secondary)]">Crie, edite e controle a disponibilidade do cardápio.</p></div><Button type="button" onClick={() => setEditingProduct(null)}><Plus className="h-4 w-4" /> Novo produto</Button></div>{error ? <p className="text-sm text-red-600" role="alert">{error}</p> : null}{formOpen ? <Card><h2 className="mb-5 text-lg font-semibold">{editingProduct ? 'Editar produto' : 'Novo produto'}</h2><ProductForm key={editingProduct?.id ?? 'new'} product={editingProduct} isSaving={isSaving} onCancel={() => setEditingProduct(undefined)} onSubmit={saveProduct} /></Card> : null}<Card className="overflow-x-auto p-0"><table className="w-full min-w-[760px] text-left text-sm"><thead className="border-b border-[var(--color-border)] bg-[var(--color-bg-subtle)] text-[var(--color-text-secondary)]"><tr><th className="p-4">Produto</th><th className="p-4">Categoria</th><th className="p-4">Preço</th><th className="p-4">Disponibilidade</th><th className="p-4 text-right">Ações</th></tr></thead><tbody>{loading ? <tr><td className="p-4" colSpan={5}>Carregando produtos...</td></tr> : products.map((product) => <tr className="border-b border-[var(--color-border)] last:border-0" key={product.id}><td className="p-4"><div className="flex items-center gap-3"><img src={product.imageUrl} alt="" className="h-10 w-10 rounded-lg object-cover" /><div><p className="font-medium">{product.name}</p><p className="max-w-60 truncate text-xs text-[var(--color-text-secondary)]">{product.description}</p></div></div></td><td className="p-4"><Badge>{product.category}</Badge></td><td className="p-4">{formatCurrency(product.price)}</td><td className="p-4"><span className={product.isAvailable ? 'text-emerald-600' : 'text-red-600'}>{product.isAvailable ? 'Disponível' : 'Indisponível'}</span></td><td className="p-4"><div className="flex justify-end gap-1"><Button variant="ghost" size="sm" type="button" onClick={() => setEditingProduct(product)} aria-label={`Editar ${product.name}`}><Pencil className="h-4 w-4" /></Button><Button variant="ghost" size="sm" type="button" onClick={() => void removeProduct(product)} aria-label={`Excluir ${product.name}`}><Trash2 className="h-4 w-4 text-red-600" /></Button></div></td></tr>)}</tbody></table></Card></div>
}
