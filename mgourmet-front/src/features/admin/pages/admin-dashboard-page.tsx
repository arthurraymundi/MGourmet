import { useEffect, useMemo, useState } from 'react'
import { CheckCircle2, Clock3, Package, ReceiptText, TrendingUp } from 'lucide-react'
import { BrandLogo } from '@/components/common/brand-logo'
import { Card } from '@/components/ui/card'
import { formatCurrency } from '@/utils/currency'
import type { AdminOrder, Product } from '@/types/domain'
import { getAdminOrders } from '../services/admin-order-service'
import { getAdminProducts } from '../services/admin-product-service'
import { useAdminAuth } from '../hooks/use-admin-auth'

export default function AdminDashboardPage() {
  const { token } = useAdminAuth()
  const [products, setProducts] = useState<Product[]>([])
  const [orders, setOrders] = useState<AdminOrder[]>([])
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  useEffect(() => { if (!token) return; void Promise.all([getAdminProducts(token), getAdminOrders(token)]).then(([nextProducts, nextOrders]) => { setProducts(nextProducts); setOrders(nextOrders) }).catch((loadError: unknown) => setError(loadError instanceof Error ? loadError.message : 'Não foi possível carregar os dados.')).finally(() => setLoading(false)) }, [token])
  const todayOrders = useMemo(() => orders.filter((order) => new Date(order.createdAt).toDateString() === new Date().toDateString()), [orders])
  const pendingOrders = useMemo(() => orders.filter((order) => ['Recebido', 'Preparando', 'Saiu para entrega'].includes(order.status)), [orders])
  const completedOrders = useMemo(() => orders.filter((order) => order.status === 'Finalizado'), [orders])
  const dailySales = useMemo(() => todayOrders.filter((order) => order.status !== 'Cancelado').reduce((sum, order) => sum + order.total, 0), [todayOrders])
  const availableCount = useMemo(() => products.filter((product) => product.isAvailable).length, [products])
  return <div className="space-y-6"><div className="flex items-start justify-between gap-4"><div><p className="text-sm font-medium text-orange-600">Administração</p><h1 className="text-3xl font-semibold">Visão geral</h1><p className="mt-1 text-sm text-[var(--color-text-secondary)]">Acompanhe o cardápio e os pedidos da MGourmet.</p></div><BrandLogo className="h-12" /></div>{error ? <p className="text-sm text-red-600" role="alert">{error}</p> : null}{loading ? <p className="text-sm text-[var(--color-text-secondary)]" role="status">Carregando dados...</p> : <><div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3"><Metric label="Pedidos hoje" value={todayOrders.length} icon={ReceiptText} /><Metric label="Pedidos pendentes" value={pendingOrders.length} icon={Clock3} /><Metric label="Pedidos finalizados" value={completedOrders.length} icon={CheckCircle2} /><Metric label="Faturamento do dia" value={formatCurrency(dailySales)} icon={TrendingUp} /><Metric label="Total de pedidos" value={orders.length} icon={ReceiptText} /><Metric label="Produtos disponíveis" value={`${availableCount}/${products.length}`} icon={Package} /></div><Card><h2 className="mb-4 text-lg font-semibold">Pedidos recentes</h2>{orders.length === 0 ? <p className="text-sm text-[var(--color-text-secondary)]">Ainda não há pedidos registrados.</p> : <ul className="divide-y divide-[var(--color-border)]">{orders.slice(0, 5).map((order) => <li className="flex items-center justify-between gap-4 py-3" key={order.id}><div><p className="font-medium">#{order.id} · {order.customerName}</p><p className="text-sm text-[var(--color-text-secondary)]">{new Date(order.createdAt).toLocaleString('pt-BR')}</p></div><div className="text-right"><p className="font-medium">{formatCurrency(order.total)}</p><p className="text-sm text-orange-600">{order.status}</p></div></li>)}</ul>}</Card></>}</div>
}

function Metric({ label, value, icon: Icon }: { label: string; value: string | number; icon: typeof Package }) { return <Card className="flex items-center justify-between"><div><p className="text-sm text-[var(--color-text-secondary)]">{label}</p><p className="mt-1 text-2xl font-semibold">{value}</p></div><Icon className="h-6 w-6 text-orange-600" /></Card> }
