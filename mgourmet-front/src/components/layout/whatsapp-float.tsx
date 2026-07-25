import { MessageCircle } from 'lucide-react'
import { WHATSAPP_PHONE_NUMBER } from '@/utils/whatsapp'

export function WhatsappFloat() {
  return (
    <a
      href={`https://wa.me/${WHATSAPP_PHONE_NUMBER}`}
      target="_blank"
      rel="noreferrer"
      aria-label="Conversar no WhatsApp"
      className="fixed right-4 bottom-4 z-40 inline-flex h-12 w-12 items-center justify-center rounded-full bg-green-500 text-white shadow-lg transition hover:brightness-110"
    >
      <MessageCircle className="h-6 w-6" />
    </a>
  )
}
