import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { BenefitCard } from '@/components/common/benefit-card'
import { FAQItem } from '@/components/common/faq-item'
import { Hero } from '@/components/common/hero'
import { ProductCard } from '@/components/common/product-card'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { TestimonialCard } from '@/components/common/testimonial-card'
import { Button } from '@/components/ui/button'
import { PAGE_META } from '@/data/seo'
import type { FaqItem, Product, Testimonial } from '@/types/domain'
import { getBenefits, getFaqItems, getHowItWorks, getTestimonials } from '@/services/content-service'
import { getFeaturedProducts } from '@/services/product-service'
import { getKits } from '@/services/kit-service'
import type { KitOffer } from '@/types/domain'
import { Card } from '@/components/ui/card'
import { formatCurrency } from '@/utils/currency'

const localBusinessSchema = {
  '@context': 'https://schema.org',
  '@type': 'LocalBusiness',
  name: 'M Gourmet',
  image: 'https://mgourmet.com.br/og-image.jpg',
  telephone: '+55 11 98888-0000',
  address: {
    '@type': 'PostalAddress',
    streetAddress: 'Rua Exemplo, 250',
    addressLocality: 'São Paulo',
    addressRegion: 'SP',
    addressCountry: 'BR',
  },
  openingHours: 'Mo-Sa 08:00-19:00',
  url: 'https://mgourmet.com.br',
}

export default function HomePage() {
  const [benefits, setBenefits] = useState<string[]>([])
  const [howItWorks, setHowItWorks] = useState<string[]>([])
  const [featuredProducts, setFeaturedProducts] = useState<Product[]>([])
  const [testimonials, setTestimonials] = useState<Testimonial[]>([])
  const [faqItems, setFaqItems] = useState<FaqItem[]>([])
  const [kits, setKits] = useState<KitOffer[]>([])

  useEffect(() => {
    void Promise.all([
      getBenefits(),
      getHowItWorks(),
      getFeaturedProducts(),
      getTestimonials(),
      getFaqItems(),
      getKits(),
    ]).then(([nextBenefits, nextHowItWorks, nextProducts, nextTestimonials, nextFaq, nextKits]) => {
      setBenefits(nextBenefits)
      setHowItWorks(nextHowItWorks)
      setFeaturedProducts(nextProducts)
      setTestimonials(nextTestimonials)
      setFaqItems(nextFaq)
      setKits(nextKits)
    })
  }, [])

  return (
    <>
      <Seo meta={PAGE_META.home} schema={localBusinessSchema} />
      <Hero />

      <Section>
        <SectionTitle
          eyebrow="Diferenciais"
          title="Comida de verdade para resultados consistentes"
          description="Receitas equilibradas para diferentes objetivos sem abrir mão de sabor e praticidade."
        />
        <div className="grid gap-4 md:grid-cols-2">
          {benefits.map((benefit) => (
            <BenefitCard key={benefit} text={benefit} />
          ))}
        </div>
      </Section>

      <Section className="bg-[var(--color-bg-subtle)]">
        <SectionTitle eyebrow="Como funciona" title="Seu plano em 3 passos" />
        <div className="grid gap-4 md:grid-cols-3">
          {howItWorks.map((step, index) => (
            <Card key={step} className="space-y-2">
              <p className="text-sm font-semibold text-orange-600">Passo {index + 1}</p>
              <p className="text-sm text-[var(--color-text-secondary)]">{step}</p>
            </Card>
          ))}
        </div>
      </Section>

      <Section>
        <SectionTitle eyebrow="Destaques" title="Produtos em destaque" />
        <div className="grid gap-6 md:grid-cols-2">
          {featuredProducts.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </Section>

      <Section>
        <SectionTitle eyebrow="Kits promocionais" title="Mais economia para o seu mês" />
        <div className="grid gap-4 md:grid-cols-3">
          {kits.map((kit) => (
            <Card key={kit.id} className="space-y-3">
              <h3 className="text-xl font-semibold">{kit.name}</h3>
              <p className="text-sm text-[var(--color-text-secondary)]">{kit.meals} refeições</p>
              <p className="text-sm text-[var(--color-text-secondary)] line-through">
                {formatCurrency(kit.originalPrice)}
              </p>
              <p className="text-2xl font-semibold text-orange-600">{formatCurrency(kit.discountedPrice)}</p>
              <Button className="w-full">Comprar kit</Button>
            </Card>
          ))}
        </div>
      </Section>

      <Section className="bg-[var(--color-bg-subtle)]">
        <SectionTitle eyebrow="Depoimentos" title="Quem já transformou a rotina com a M Gourmet" />
        <div className="grid gap-4 md:grid-cols-2">
          {testimonials.map((testimonial) => (
            <TestimonialCard key={testimonial.id} testimonial={testimonial} />
          ))}
        </div>
      </Section>

      <Section>
        <SectionTitle eyebrow="FAQ" title="Dúvidas frequentes" />
        <div className="mx-auto max-w-3xl space-y-3">
          {faqItems.map((item) => (
            <FAQItem key={item.id} item={item} />
          ))}
        </div>
      </Section>

      <Section className="bg-[var(--color-dark-900)] text-white">
        <SectionTitle
          title="Pronto para simplificar sua alimentação?"
          description="Escolha seu objetivo e comece hoje mesmo com refeições premium."
        />
        <div className="flex justify-center">
          <Button asChild size="lg">
            <Link to="/cardapio">Começar pedido</Link>
          </Button>
        </div>
      </Section>
    </>
  )
}
