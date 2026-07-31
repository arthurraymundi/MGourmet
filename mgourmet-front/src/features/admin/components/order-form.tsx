import { useMemo, useState, type FormEvent } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import type { DeliveryMethod, OrderSource, OrderStatus, Product } from '@/types/domain'
import { formatCurrency } from '@/utils/currency'
import type { AdminOrderPayload } from '../services/admin-order-service'

const statuses: OrderStatus[] = ['Recebido', 'Preparando', 'Saiu para entrega', 'Finalizado', 'Cancelado']
const sources: Array<{ value: OrderSource; label: string }> = [
  { value: 'telefone', label: 'Telefone' }, { value: 'whatsapp', label: 'WhatsApp' }, { value: 'presencial', label: 'Atendimento presencial' },
]

export function OrderForm({ products, isSaving, onCancel, onSubmit }: { products: Product[]; isSaving: boolean; onCancel: () => void; onSubmit: (payload: AdminOrderPayload) => Promise<void> }) {
  const [customerName, setCustomerName] = useState('')
  const [customerPhone, setCustomerPhone] = useState('')
  const [deliveryMethod, setDeliveryMethod] = useState<DeliveryMethod>('pickup')
  const [street, setStreet] = useState('')
  const [number, setNumber] = useState('')
  const [neighborhood, setNeighborhood] = useState('')
  const [complement, setComplement] = useState('')
  const [notes, setNotes] = useState('')
  const [source, setSource] = useState<OrderSource>('whatsapp')
  const [paymentMethod, setPaymentMethod] = useState('Pix')
  const [status, setStatus] = useState<OrderStatus>('Recebido')
  const [quantities, setQuantities] = useState<Record<string, number>>({})
  const selectedItems = useMemo(() => products.filter((product) => quantities[product.id]).map((product) => ({ product, quantity: quantities[product.id] })), [products, quantities])
  const total = useMemo(() => selectedItems.reduce((sum, item) => sum + item.product.price * item.quantity, 0), [selectedItems])
  const isDeliveryInvalid = deliveryMethod === 'delivery' && (!street.trim() || !number.trim() || !neighborhood.trim())

  function setQuantity(productId: string, value: number) { setQuantities((current) => ({ ...current, [productId]: Math.max(0, value) })) }
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (selectedItems.length === 0 || isDeliveryInvalid) return
    await onSubmit({ customerName, customerPhone, deliveryMethod, street, number, neighborhood, complement, notes, source, paymentMethod, status, items: selectedItems.map((item) => ({ productId: item.product.id, quantity: item.quantity })) })
  }

  return <form className="space-y-5" onSubmit={(event) => void submit(event)}><div className="grid gap-4 md:grid-cols-2"><label className="space-y-1"><span className="text-sm font-medium">Nome</span><Input required value={customerName} onChange={(event) => setCustomerName(event.target.value)} /></label><label className="space-y-1"><span className="text-sm font-medium">Telefone</span><Input required type="tel" value={customerPhone} onChange={(event) => setCustomerPhone(event.target.value)} /></label><label className="space-y-1"><span className="text-sm font-medium">Origem</span><select className="h-11 w-full rounded-xl border border-[var(--color-border)] bg-white px-3 text-sm" value={source} onChange={(event) => setSource(event.target.value as OrderSource)}>{sources.map((item) => <option key={item.value} value={item.value}>{item.label}</option>)}</select></label><label className="space-y-1"><span className="text-sm font-medium">Forma de pagamento</span><select className="h-11 w-full rounded-xl border border-[var(--color-border)] bg-white px-3 text-sm" value={paymentMethod} onChange={(event) => setPaymentMethod(event.target.value)}><option>Pix</option><option>Cartão</option><option>Dinheiro</option><option>A combinar</option></select></label><label className="space-y-1"><span className="text-sm font-medium">Status</span><select className="h-11 w-full rounded-xl border border-[var(--color-border)] bg-white px-3 text-sm" value={status} onChange={(event) => setStatus(event.target.value as OrderStatus)}>{statuses.map((item) => <option key={item}>{item}</option>)}</select></label><fieldset className="space-y-1"><legend className="text-sm font-medium">Forma de entrega</legend><div className="flex h-11 items-center gap-4 text-sm"><label><input type="radio" checked={deliveryMethod === 'pickup'} onChange={() => setDeliveryMethod('pickup')} /> Retirada</label><label><input type="radio" checked={deliveryMethod === 'delivery'} onChange={() => setDeliveryMethod('delivery')} /> Entrega</label></div></fieldset></div>{deliveryMethod === 'delivery' ? <div className="grid gap-4 md:grid-cols-3"><label className="space-y-1 md:col-span-2"><span className="text-sm font-medium">Rua</span><Input required value={street} onChange={(event) => setStreet(event.target.value)} /></label><label className="space-y-1"><span className="text-sm font-medium">Número</span><Input required value={number} onChange={(event) => setNumber(event.target.value)} /></label><label className="space-y-1 md:col-span-2"><span className="text-sm font-medium">Bairro</span><Input required value={neighborhood} onChange={(event) => setNeighborhood(event.target.value)} /></label><label className="space-y-1"><span className="text-sm font-medium">Complemento</span><Input value={complement} onChange={(event) => setComplement(event.target.value)} /></label></div> : null}<label className="block space-y-1"><span className="text-sm font-medium">Observações</span><textarea className="min-h-20 w-full rounded-xl border border-[var(--color-border)] px-3 py-2 text-sm" value={notes} onChange={(event) => setNotes(event.target.value)} /></label><div><p className="mb-2 text-sm font-medium">Produtos</p><div className="max-h-64 space-y-2 overflow-y-auto rounded-xl border border-[var(--color-border)] p-3">{products.map((product) => <div className="flex items-center justify-between gap-3" key={product.id}><label className="min-w-0 flex-1 text-sm"><input className="mr-2" type="checkbox" checked={Boolean(quantities[product.id])} onChange={(event) => setQuantity(product.id, event.target.checked ? 1 : 0)} />{product.name} <span className="text-[var(--color-text-secondary)]">({formatCurrency(product.price)})</span></label>{quantities[product.id] ? <Input className="w-20" type="number" min="1" max="100" value={quantities[product.id]} onChange={(event) => setQuantity(product.id, Number(event.target.value))} aria-label={`Quantidade de ${product.name}`} /> : null}</div>)}</div>{selectedItems.length === 0 ? <p className="mt-2 text-sm text-red-600">Selecione ao menos um produto.</p> : null}</div><div className="flex flex-wrap items-center justify-between gap-3 border-t border-[var(--color-border)] pt-4"><p className="text-lg font-semibold">Total calculado: <span className="text-orange-600">{formatCurrency(total)}</span></p><div className="flex gap-2"><Button type="button" variant="outline" onClick={onCancel} disabled={isSaving}>Cancelar</Button><Button type="submit" disabled={isSaving || selectedItems.length === 0 || isDeliveryInvalid}>{isSaving ? 'Salvando...' : 'Salvar pedido'}</Button></div></div></form>
}
