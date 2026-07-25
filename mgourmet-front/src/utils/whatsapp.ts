import type { CartItem, CustomerDetails } from '@/types/domain'
import { formatCurrencyForMessage } from './currency'

export const WHATSAPP_PHONE_NUMBER = '5511988880000'

export function createOrderMessage(items: CartItem[], total: number, customer: CustomerDetails) {
  const deliveryDetails =
    customer.deliveryMethod === 'delivery'
      ? `\n\nEndereço:\n\n${customer.street}\nNúmero ${customer.number}\nBairro ${customer.neighborhood}${customer.complement ? `\nComplemento ${customer.complement}` : ''}`
      : ''
  const orderItems = items
    .map((item) => `${item.quantity}x ${item.product.name} — ${formatCurrencyForMessage(item.product.price * item.quantity)}`)
    .join('\n')
  const notes = customer.notes ? `\n\n======================\n\nObservações\n\n${customer.notes}` : ''

  return `Olá!\n\nGostaria de fazer um pedido.\n\n======================\n\nNome:\n${customer.name}\n\nTelefone:\n${customer.phone}\n\nForma de entrega:\n${customer.deliveryMethod === 'delivery' ? 'Entrega' : 'Retirada'}${deliveryDetails}\n\n======================\n\nPedido\n\n${orderItems}\n\n======================\n\nTOTAL\n\n${formatCurrencyForMessage(total)}${notes}`
}

export function createWhatsAppUrl(message: string) {
  return `https://wa.me/${WHATSAPP_PHONE_NUMBER}?text=${encodeURIComponent(message)}`
}
