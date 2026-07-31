import { NavLink } from 'react-router-dom'
import { Container } from '@/components/common/container'
import { BrandLogo } from '@/components/common/brand-logo'
import { Button } from '@/components/ui/button'
import { cn } from '@/utils/cn'
import { COMPANY_WHATSAPP_URL } from '@/data/company'

const links = [
  { to: '/', label: 'Home' },
  { to: '/sobre', label: 'Sobre' },
  { to: '/cardapio', label: 'Cardápio' },
  { to: '/kits', label: 'Kits' },
  { to: '/contato', label: 'Contato' },
]

export function Navbar() {
  return (
    <header className="sticky top-0 z-40 border-b border-[var(--color-border)] bg-white/90 backdrop-blur">
      <Container className="flex h-16 items-center justify-between py-3">
        <NavLink to="/" aria-label="Página inicial da MGourmet"><BrandLogo className="h-10" /></NavLink>
        <nav className="hidden items-center gap-6 md:flex">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              className={({ isActive }) =>
                cn(
                  'text-sm font-medium text-[var(--color-text-secondary)] transition-colors hover:text-[var(--color-text-primary)]',
                  isActive && 'text-[var(--color-text-primary)]',
                )
              }
            >
              {link.label}
            </NavLink>
          ))}
        </nav>
        <Button asChild size="sm">
          <a href={COMPANY_WHATSAPP_URL} target="_blank" rel="noreferrer">
            Negociar pedido
          </a>
        </Button>
      </Container>
    </header>
  )
}
