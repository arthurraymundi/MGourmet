import { AtSign, Camera, MapPin, MessageCircle, Phone, Music2 } from 'lucide-react'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { Card } from '@/components/ui/card'
import { PAGE_META } from '@/data/seo'
import { COMPANY, COMPANY_WHATSAPP_URL } from '@/data/company'

export default function ContactPage() {
  return (
    <>
      <Seo meta={PAGE_META.contact} />
      <Section>
        <SectionTitle
          eyebrow="Contato"
          title={`Fale com a ${COMPANY.name}`}
          description={`Atendimento rápido por WhatsApp, telefone e redes sociais. Entregas em ${COMPANY.serviceArea}.`}
        />
        <div className="grid gap-4 md:grid-cols-2">
          <Card className="space-y-3">
            <p className="flex items-center gap-2 text-sm">
              <MessageCircle className="h-4 w-4 text-orange-600" />
              <a className="hover:text-orange-600" href={COMPANY_WHATSAPP_URL} target="_blank" rel="noreferrer">{COMPANY.whatsapp}</a>
            </p>
            <p className="flex items-center gap-2 text-sm">
              <Phone className="h-4 w-4 text-orange-600" />
              <a className="hover:text-orange-600" href={`tel:${COMPANY.whatsappPhone}`}>{COMPANY.phone}</a>
            </p>
            <p className="flex items-center gap-2 text-sm">
              <AtSign className="h-4 w-4 text-orange-600" />
              <a className="hover:text-orange-600" href={`mailto:${COMPANY.email}`}>{COMPANY.email}</a>
            </p>
            <p className="flex items-center gap-2 text-sm">
              <Camera className="h-4 w-4 text-orange-600" />
              <a className="hover:text-orange-600" href={COMPANY.instagramUrl} target="_blank" rel="noreferrer">Instagram</a>
            </p>
            <p className="flex items-center gap-2 text-sm">
              <Music2 className="h-4 w-4 text-orange-600" />
              <a className="hover:text-orange-600" href={COMPANY.tiktokUrl} target="_blank" rel="noreferrer">TikTok</a>
            </p>
            <p className="flex items-center gap-2 text-sm">
              <MapPin className="h-4 w-4 text-orange-600" />
              Entregas em {COMPANY.serviceArea}
            </p>
          </Card>
          <Card>
            <h3 className="mb-3 text-lg font-semibold">Mapa ilustrativo</h3>
            <div className="h-60 rounded-xl bg-[var(--color-bg-subtle)] p-4 text-sm text-[var(--color-text-secondary)]">
              Região de atendimento destacada em {COMPANY.serviceArea}.
            </div>
          </Card>
        </div>
      </Section>
    </>
  )
}
