import { Container } from '@/components/common/container'

export function Footer() {
  return (
    <footer className="border-t border-[var(--color-border)] py-8">
      <Container className="flex flex-col items-center justify-between gap-2 text-center text-sm text-[var(--color-text-secondary)] md:flex-row md:text-left">
        <p>© {new Date().getFullYear()} M Gourmet. Todos os direitos reservados.</p>
        <p>Marmitas fitness premium para rotina saudável.</p>
      </Container>
    </footer>
  )
}
