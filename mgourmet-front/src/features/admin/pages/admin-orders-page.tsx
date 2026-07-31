import { useCallback, useEffect, useState } from 'react'
import { Plus, Trash2 } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { formatCurrency } from '@/utils/currency'
import type { AdminOrder, OrderStatus, Product } from '@/types/domain'
import { OrderForm } from '../components/order-form'
import { useAdminAuth } from '../hooks/use-admin-auth'
import { createAdminOrder, deleteAdminOrder, getAdminOrders, updateOrderStatus, type AdminOrderPayload } from '../services/admin-order-service'
import { getAdminProducts } from '../services/admin-product-service'

const statuses: OrderStatus[] = ['Recebido', 'Preparando', 'Saiu para entrega', 'Finalizado', 'Cancelado']

export default function AdminOrdersPage() {
  const { token } = useAdminAuth()
  const [orders, setOrders] = useState<AdminOrder[]>([])
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState<string | null>(null)
  const [updatingId, setUpdatingId] = useState<number | null>(null)
  const [isSaving, setIsSaving] = useState(false)
  const [isFormOpen, setIsFormOpen] = useState(false)
  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState<OrderStatus | ''>('')
  const loadOrders = useCallback(async () => {
    if (!token) return
    try { setLoading(true); setError(null); setOrders(await getAdminOrders(token, { search: search.trim() || undefined, status: statusFilter || undefined })) }
    catch (loadError) { setError(loadError instanceof Error ? loadError.message : 'Não foi possível carregar os pedidos.') }
    finally { setLoading(false) }
  }, [search, statusFilter, token])
  useEffect(() => { void loadOrders() }, [loadOrders])
  useEffect(() => { if (!token) return; void getAdminProducts(token).then((items) => setProducts(items.filter((product) => product.isAvailable))).catch(() => setError('Não foi possível carregar os produtos disponíveis.')) }, [token])
  async function changeStatus(order: AdminOrder, status: OrderStatus) { if (!token || order.status === status) return; try { setUpdatingId(order.id); setError(null); const updated = await updateOrderStatus(token, order.id, status); setOrders((current) => current.map((item) => item.id === order.id ? updated : item)); setSuccess(`Pedido #${order.id} atualizado.`) } catch (updateError) { setError(updateError instanceof Error ? updateError.message : 'Não foi possível atualizar o pedido.') } finally { setUpdatingId(null) } }
  async function saveOrder(payload: AdminOrderPayload) { if (!token) return; try { setIsSaving(true); setError(null); await createAdminOrder(token, payload); setIsFormOpen(false); setSuccess('Pedido criado com sucesso.'); await loadOrders() } catch (saveError) { setError(saveError instanceof Error ? saveError.message : 'Não foi possível criar o pedido.') } finally { setIsSaving(false) } }
  async function removeOrder(order: AdminOrder) { if (!token || !window.confirm(`Deseja realmente excluir o pedido #${order.id}? Esta ação não pode ser desfeita.`)) return; try { setUpdatingId(order.id); setError(null); await deleteAdminOrder(token, order.id); setOrders((current) => current.filter((item) => item.id !== order.id)); setSuccess(`Pedido #${order.id} excluído com sucesso.`) } catch (deleteError) { setError(deleteError instanceof Error ? deleteError.message : 'Não foi possível excluir o pedido.') } finally { setUpdatingId(null) } }
  return <div className="space-y-6"><div className="flex flex-wrap items-start justify-between gap-4"><div><p className="text-sm font-medium text-orange-600">Operação</p><h1 className="text-3xl font-semibold">Pedidos</h1><p className="mt-1 text-sm text-[var(--color-text-secondary)]">Acompanhe e registre pedidos de todos os canais.</p></div><Button type="button" onClick={() => { setIsFormOpen((current) => !current); setSuccess(null) }}><Plus className="h-4 w-4" /> Novo pedido</Button></div>{error ? <p className="rounded-xl bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">{error}</p> : null}{success ? <p className="rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-700" role="status">{success}</p> : null}{isFormOpen ? <Card><h2 className="mb-5 text-lg font-semibold">Novo pedido manual</h2>{products.length === 0 ? <p className="text-sm text-[var(--color-text-secondary)]">Não há produtos disponíveis para criar um pedido.</p> : <OrderForm products={products} isSaving={isSaving} onCancel={() => setIsFormOpen(false)} onSubmit={saveOrder} />}</Card> : null}<Card><div className="flex flex-col gap-3 md:flex-row"><Input placeholder="Buscar por nome ou telefone" value={search} onChange={(event) => setSearch(event.target.value)} /><select className="h-11 rounded-xl border border-[var(--color-border)] bg-white px-3 text-sm" value={statusFilter} onChange={(event) => setStatusFilter(event.target.value as OrderStatus | '')}><option value="">Todos os status</option>{statuses.map((status) => <option key={status}>{status}</option>)}</select></div></Card>{loading ? <p className="text-sm text-[var(--color-text-secondary)]" role="status">Carregando pedidos...</p> : orders.length === 0 ? <Card><p className="text-sm text-[var(--color-text-secondary)]">Nenhum pedido encontrado para os filtros selecionados.</p></Card> : <div className="space-y-4">{orders.map((order) => <Card key={order.id}><div className="flex flex-wrap items-start justify-between gap-4"><div><p className="text-lg font-semibold">Pedido #{order.id}</p><p className="text-sm text-[var(--color-text-secondary)]">{new Date(order.createdAt).toLocaleString('pt-BR')} · {order.source === 'site' ? 'Site' : order.source}</p></div><div className="flex items-start gap-2"><div className="text-right"><p className="text-lg font-semibold text-orange-600">{formatCurrency(order.total)}</p><select className="mt-2 h-9 rounded-lg border border-[var(--color-border)] px-2 text-sm" value={order.status} disabled={updatingId === order.id} onChange={(event) => void changeStatus(order, event.target.value as OrderStatus)}>{statuses.map((status) => <option key={status}>{status}</option>)}</select></div><Button variant="ghost" size="sm" type="button" disabled={updatingId === order.id} onClick={() => void removeOrder(order)} aria-label={`Excluir pedido ${order.id}`}><Trash2 className="h-4 w-4 text-red-600" /></Button></div></div><div className="mt-4 grid gap-4 border-y border-[var(--color-border)] py-4 md:grid-cols-2"><div><p className="text-sm font-medium">{order.customerName}</p><p className="text-sm text-[var(--color-text-secondary)]">{order.customerPhone} · {order.deliveryMethod === 'delivery' ? 'Entrega' : 'Retirada'}{order.paymentMethod ? ` · ${order.paymentMethod}` : ''}</p>{order.deliveryMethod === 'delivery' ? <p className="mt-1 text-sm text-[var(--color-text-secondary)]">{order.street}, {order.number} · {order.neighborhood}{order.complement ? ` · ${order.complement}` : ''}</p> : null}</div>{order.notes ? <p className="text-sm text-[var(--color-text-secondary)]"><span className="font-medium text-[var(--color-text-primary)]">Observações:</span> {order.notes}</p> : null}</div><ul className="mt-4 space-y-2">{order.items.map((item) => <li className="flex justify-between gap-3 text-sm" key={item.id}><span>{item.quantity}x {item.productName}</span><span className="font-medium">{formatCurrency(item.unitPrice * item.quantity)}</span></li>)}</ul></Card>)}</div>}</div>
}
