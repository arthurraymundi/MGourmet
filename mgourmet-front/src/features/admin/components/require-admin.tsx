import { Navigate, Outlet } from 'react-router-dom'
import { useAdminAuth } from '../hooks/use-admin-auth'

export function RequireAdmin() {
  const { admin, isLoading } = useAdminAuth()
  if (isLoading) return <div className="grid min-h-screen place-items-center text-sm text-[var(--color-text-secondary)]">Validando acesso...</div>
  return admin ? <Outlet /> : <Navigate to="/admin/login" replace />
}
