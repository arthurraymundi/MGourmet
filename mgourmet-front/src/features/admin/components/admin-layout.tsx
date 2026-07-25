import { Outlet } from 'react-router-dom'
import { AdminNavigation } from './admin-navigation'

export function AdminLayout() {
  return <div className="min-h-screen bg-[var(--color-bg-subtle)] lg:flex"><AdminNavigation /><main className="min-w-0 flex-1 p-4 md:p-8"><Outlet /></main></div>
}
