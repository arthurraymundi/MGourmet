import { useEffect, useState } from 'react'
import { AtSign, MapPin, MessageCircle, Clock3 } from 'lucide-react'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { Card } from '@/components/ui/card'
import { PAGE_META } from '@/data/seo'
import { getContactInfo } from '@/services/content-service'
import type { ContactInfo } from '@/types/domain'

export default function ContactPage() {
  const [contact, setContact] = useState<ContactInfo | null>(null)

  useEffect(() => {
    void getContactInfo().then(setContact)
  }, [])

  if (!contact) {
    return <Section>Carregando contato...</Section>
  }

  return (
    <>
      <Seo meta={PAGE_META.contact} />
      <Section>
        <SectionTitle
          eyebrow="Contato"
          title="Fale com a M Gourmet"
          description="Atendimento rápido por WhatsApp e Instagram."
        />
        <div className="grid gap-4 md:grid-cols-2">
          <Card className="space-y-3">
            <p className="flex items-center gap-2 text-sm">
              <MessageCircle className="h-4 w-4 text-orange-600" />
              {contact.whatsapp}
            </p>
            <p className="flex items-center gap-2 text-sm">
              <AtSign className="h-4 w-4 text-orange-600" />
              {contact.instagram}
            </p>
            <p className="flex items-center gap-2 text-sm">
              <MapPin className="h-4 w-4 text-orange-600" />
              {contact.address}
            </p>
            <p className="flex items-center gap-2 text-sm">
              <Clock3 className="h-4 w-4 text-orange-600" />
              {contact.businessHours}
            </p>
          </Card>
          <Card>
            <h3 className="mb-3 text-lg font-semibold">Mapa ilustrativo</h3>
            <div className="h-60 rounded-xl bg-[var(--color-bg-subtle)] p-4 text-sm text-[var(--color-text-secondary)]">
              Região de atendimento destacada em São Paulo/SP (mock visual).
            </div>
          </Card>
        </div>
      </Section>
    </>
  )
}
