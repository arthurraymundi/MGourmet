import { MessageCircle } from 'lucide-react'
import { COMPANY_WHATSAPP_URL } from '@/data/company'

export function WhatsappFloat() {
  return (
    <a
      href={COMPANY_WHATSAPP_URL}
      target="_blank"
      rel="noreferrer"
      aria-label="Negociar pedido pelo WhatsApp"
      className="fixed right-4 bottom-4 z-40 inline-flex h-12 w-12 items-center justify-center rounded-full bg-green-500 text-white shadow-lg transition hover:brightness-110"
    >
      <MessageCircle className="h-6 w-6" />
    </a>
  )
}
