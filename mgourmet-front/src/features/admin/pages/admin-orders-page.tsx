import { useCallback, useEffect, useState } from 'react'
import { Card } from '@/components/ui/card'
import { formatCurrency } from '@/utils/currency'
import type { AdminOrder, OrderStatus } from '@/types/domain'
import { useAdminAuth } from '../hooks/use-admin-auth'
import { getAdminOrders, updateOrderStatus } from '../services/admin-order-service'

const statuses: OrderStatus[] = ['Recebido', 'Preparando', 'Saiu para entrega', 'Finalizado', 'Cancelado']

export default function AdminOrdersPage() {
  const { token } = useAdminAuth()
  const [orders, setOrders] = useState<AdminOrder[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [updatingId, setUpdatingId] = useState<number | null>(null)
  const loadOrders = useCallback(async () => { if (!token) return; try { setLoading(true); setError(null); setOrders(await getAdminOrders(token)) } catch (loadError) { setError(loadError instanceof Error ? loadError.message : 'Não foi possível carregar os pedidos.') } finally { setLoading(false) } }, [token])
  useEffect(() => { void loadOrders() }, [loadOrders])
  async function changeStatus(order: AdminOrder, status: OrderStatus) { if (!token || order.status === status) return; try { setUpdatingId(order.id); const updated = await updateOrderStatus(token, order.id, status); setOrders((current) => current.map((item) => item.id === order.id ? updated : item)) } catch (updateError) { setError(updateError instanceof Error ? updateError.message : 'Não foi possível atualizar o pedido.') } finally { setUpdatingId(null) } }
  return <div className="space-y-6"><div><p className="text-sm font-medium text-orange-600">Operação</p><h1 className="text-3xl font-semibold">Pedidos</h1><p className="mt-1 text-sm text-[var(--color-text-secondary)]">Acompanhe os pedidos enviados pelo cardápio.</p></div>{error ? <p className="text-sm text-red-600" role="alert">{error}</p> : null}{loading ? <p className="text-sm text-[var(--color-text-secondary)]">Carregando pedidos...</p> : orders.length === 0 ? <Card><p className="text-sm text-[var(--color-text-secondary)]">Ainda não há pedidos registrados.</p></Card> : <div className="space-y-4">{orders.map((order) => <Card key={order.id}><div className="flex flex-wrap items-start justify-between gap-4"><div><p className="text-lg font-semibold">Pedido #{order.id}</p><p className="text-sm text-[var(--color-text-secondary)]">{new Date(order.createdAt).toLocaleString('pt-BR')}</p></div><div className="text-right"><p className="text-lg font-semibold text-orange-600">{formatCurrency(order.total)}</p><select className="mt-2 h-9 rounded-lg border border-[var(--color-border)] px-2 text-sm" value={order.status} disabled={updatingId === order.id} onChange={(event) => void changeStatus(order, event.target.value as OrderStatus)}>{statuses.map((status) => <option key={status}>{status}</option>)}</select></div></div><div className="mt-4 grid gap-4 border-y border-[var(--color-border)] py-4 md:grid-cols-2"><div><p className="text-sm font-medium">{order.customerName}</p><p className="text-sm text-[var(--color-text-secondary)]">{order.customerPhone} · {order.deliveryMethod === 'delivery' ? 'Entrega' : 'Retirada'}</p>{order.deliveryMethod === 'delivery' ? <p className="mt-1 text-sm text-[var(--color-text-secondary)]">{order.street}, {order.number} · {order.neighborhood}{order.complement ? ` · ${order.complement}` : ''}</p> : null}</div>{order.notes ? <p className="text-sm text-[var(--color-text-secondary)]"><span className="font-medium text-[var(--color-text-primary)]">Observações:</span> {order.notes}</p> : null}</div><ul className="mt-4 space-y-2">{order.items.map((item) => <li className="flex justify-between gap-3 text-sm" key={item.id}><span>{item.quantity}x {item.productName}</span><span className="font-medium">{formatCurrency(item.unitPrice * item.quantity)}</span></li>)}</ul></Card>)}</div>}</div>
}
