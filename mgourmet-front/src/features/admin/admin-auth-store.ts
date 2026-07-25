import { createContext } from 'react'
import type { AdminUser } from '@/types/domain'

export interface AdminAuthContextValue {
  admin: AdminUser | null
  token: string | null
  isLoading: boolean
  login: (email: string, password: string) => Promise<void>
  logout: () => void
}

export const AdminAuthContext = createContext<AdminAuthContextValue | null>(null)
