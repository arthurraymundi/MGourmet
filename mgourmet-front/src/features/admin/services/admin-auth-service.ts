import { postToApi, requestFromApi } from '@/services/api-client'
import type { AdminUser } from '@/types/domain'

export const ADMIN_TOKEN_STORAGE_KEY = 'mgourmet-admin-token'

interface LoginResponse {
  accessToken: string
}

export async function loginAdmin(email: string, password: string) {
  return postToApi<LoginResponse>('/auth/login', { email, password })
}

export function getCurrentAdmin(token: string) {
  return requestFromApi<AdminUser>('/auth/me', { headers: { Authorization: `Bearer ${token}` } })
}
