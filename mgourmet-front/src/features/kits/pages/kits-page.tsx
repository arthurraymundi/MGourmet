import { useEffect, useState } from 'react'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { PAGE_META } from '@/data/seo'
import { getKits } from '@/services/kit-service'
import type { KitOffer } from '@/types/domain'
import { formatCurrency } from '@/utils/currency'

function calculateSavings(kit: KitOffer) {
  return kit.originalPrice - kit.discountedPrice
}

export default function KitsPage() {
  const [kits, setKits] = useState<KitOffer[]>([])

  useEffect(() => {
    void getKits().then(setKits)
  }, [])

  return (
    <>
      <Seo meta={PAGE_META.kits} />
      <Section>
        <SectionTitle
          eyebrow="Kits"
          title="Planos promocionais para ganho de consistência"
          description="Economize no volume e mantenha a rotina saudável por mais tempo."
        />
        <div className="grid gap-4 md:grid-cols-3">
          {kits.map((kit) => (
            <Card key={kit.id} className="space-y-3">
              <h3 className="text-xl font-semibold">{kit.name}</h3>
              <p className="text-sm text-[var(--color-text-secondary)]">{kit.meals} refeições</p>
              <p className="text-sm line-through text-[var(--color-text-secondary)]">
                {formatCurrency(kit.originalPrice)}
              </p>
              <p className="text-2xl font-semibold text-orange-600">{formatCurrency(kit.discountedPrice)}</p>
              <p className="text-sm font-medium text-emerald-600">
                Economia de {formatCurrency(calculateSavings(kit))}
              </p>
              <Button className="w-full">Comprar</Button>
            </Card>
          ))}
        </div>
      </Section>
    </>
  )
}
