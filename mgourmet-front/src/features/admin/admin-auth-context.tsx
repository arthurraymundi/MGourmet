import { useCallback, useEffect, useMemo, useState, type PropsWithChildren } from 'react'
import type { AdminUser } from '@/types/domain'
import { ADMIN_TOKEN_STORAGE_KEY, getCurrentAdmin, loginAdmin } from './services/admin-auth-service'
import { AdminAuthContext } from './admin-auth-store'

export function AdminAuthProvider({ children }: PropsWithChildren) {
  const [admin, setAdmin] = useState<AdminUser | null>(null)
  const [token, setToken] = useState<string | null>(() => window.localStorage.getItem(ADMIN_TOKEN_STORAGE_KEY))
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    if (!token) {
      setIsLoading(false)
      return
    }
    void getCurrentAdmin(token)
      .then(setAdmin)
      .catch(() => {
        window.localStorage.removeItem(ADMIN_TOKEN_STORAGE_KEY)
        setToken(null)
      })
      .finally(() => setIsLoading(false))
  }, [token])

  const login = useCallback(async (email: string, password: string) => {
    const response = await loginAdmin(email, password)
    window.localStorage.setItem(ADMIN_TOKEN_STORAGE_KEY, response.accessToken)
    setToken(response.accessToken)
    setAdmin(await getCurrentAdmin(response.accessToken))
  }, [])

  const logout = useCallback(() => {
    window.localStorage.removeItem(ADMIN_TOKEN_STORAGE_KEY)
    setAdmin(null)
    setToken(null)
  }, [])

  const value = useMemo(() => ({ admin, token, isLoading, login, logout }), [admin, isLoading, login, logout, token])
  return <AdminAuthContext.Provider value={value}>{children}</AdminAuthContext.Provider>
}
