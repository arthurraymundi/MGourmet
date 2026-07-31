import { Card } from '@/components/ui/card'
import { Section } from '@/components/common/section'
import { SectionTitle } from '@/components/common/section-title'
import { Seo } from '@/components/common/seo'
import { COMPANY } from '@/data/company'
import { PAGE_META } from '@/data/seo'

export default function AboutPage() {
  return (
    <>
      <Seo meta={PAGE_META.about} />
      <Section>
        <SectionTitle
          eyebrow="Sobre"
          title="Nutrição inteligente com padrão premium"
          description="Conteúdo fictício para validação de identidade, narrativa e experiência da marca."
        />
        <div className="grid gap-4 md:grid-cols-2">
          <Card>
            <h3 className="text-xl font-semibold">História</h3>
            <p className="mt-2 text-sm text-[var(--color-text-secondary)]">
              A {COMPANY.name} nasceu para resolver a falta de praticidade de quem busca alimentação equilibrada.
            </p>
          </Card>
          <Card>
            <h3 className="text-xl font-semibold">Missão</h3>
            <p className="mt-2 text-sm text-[var(--color-text-secondary)]">
              Entregar refeições saudáveis com qualidade premium para simplificar a rotina.
            </p>
          </Card>
          <Card>
            <h3 className="text-xl font-semibold">Visão</h3>
            <p className="mt-2 text-sm text-[var(--color-text-secondary)]">
              Ser referência em alimentação fitness prática para pessoas e empresas.
            </p>
          </Card>
          <Card>
            <h3 className="text-xl font-semibold">Valores e Equipe</h3>
            <p className="mt-2 text-sm text-[var(--color-text-secondary)]">
              Cuidado, consistência, inovação e equipe multidisciplinar focada em experiência do cliente.
            </p>
          </Card>
        </div>
      </Section>
    </>
  )
}
