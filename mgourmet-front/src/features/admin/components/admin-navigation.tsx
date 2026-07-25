import { LayoutDashboard, LogOut, Package, ReceiptText } from 'lucide-react'
import { NavLink } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { cn } from '@/utils/cn'
import { useAdminAuth } from '../hooks/use-admin-auth'

const links = [
  { to: '/admin', label: 'Visão geral', icon: LayoutDashboard, end: true },
  { to: '/admin/produtos', label: 'Produtos', icon: Package },
  { to: '/admin/pedidos', label: 'Pedidos', icon: ReceiptText },
]

export function AdminNavigation() {
  const { admin, logout } = useAdminAuth()
  return <aside className="border-b border-[var(--color-border)] bg-white lg:min-h-screen lg:w-64 lg:border-b-0 lg:border-r">
    <div className="flex h-full flex-col p-4">
      <div className="mb-6 px-2"><p className="text-lg font-semibold">M Gourmet</p><p className="text-sm text-orange-600">Administração</p></div>
      <nav className="flex gap-2 overflow-x-auto lg:flex-col">
        {links.map(({ to, label, icon: Icon, end }) => <NavLink key={to} to={to} end={end} className={({ isActive }) => cn('flex shrink-0 items-center gap-3 rounded-xl px-3 py-2 text-sm font-medium text-[var(--color-text-secondary)] hover:bg-orange-50 hover:text-orange-700', isActive && 'bg-orange-100 text-orange-700')}><Icon className="h-4 w-4" />{label}</NavLink>)}
      </nav>
      <div className="mt-4 flex items-center justify-between border-t border-[var(--color-border)] pt-4 lg:mt-auto"><p className="truncate text-sm text-[var(--color-text-secondary)]">{admin?.name}</p><Button variant="ghost" size="sm" type="button" onClick={logout} aria-label="Sair"><LogOut className="h-4 w-4" /></Button></div>
    </div>
  </aside>
}
