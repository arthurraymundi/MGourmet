import { Container } from '@/components/common/container'
import { BrandLogo } from '@/components/common/brand-logo'
import { COMPANY } from '@/data/company'

export function Footer() {
  return (
    <footer className="border-t border-[var(--color-border)] py-8">
      <Container className="flex flex-col items-center justify-between gap-4 text-center text-sm text-[var(--color-text-secondary)] md:flex-row md:text-left">
        <div className="flex flex-col items-center gap-2 md:items-start"><BrandLogo className="h-10" /><p>© {new Date().getFullYear()} {COMPANY.name}. Todos os direitos reservados.</p></div>
        <div><p>Marmitas fitness premium com entregas em {COMPANY.serviceArea}.</p><div className="mt-2 flex justify-center gap-3 md:justify-end"><a className="hover:text-orange-600" href={COMPANY.instagramUrl} target="_blank" rel="noreferrer">Instagram</a><a className="hover:text-orange-600" href={COMPANY.tiktokUrl} target="_blank" rel="noreferrer">TikTok</a><a className="hover:text-orange-600" href={`mailto:${COMPANY.email}`}>E-mail</a></div></div>
      </Container>
    </footer>
  )
}
