const API_BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api/v1'

export interface ListResponse<T> {
  items: T[]
  meta: {
    page: number
    pageSize: number
    total: number
    totalPages: number
  }
}

export async function getFromApi<T>(path: string): Promise<T> {
  return requestFromApi<T>(path)
}

export async function postToApi<T>(path: string, body: unknown): Promise<T> {
  return requestFromApi<T>(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
}

export async function requestFromApi<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, options)

  if (!response.ok) {
    const error: unknown = await response.json().catch(() => null)
    const detail = typeof error === 'object' && error !== null && 'detail' in error && typeof error.detail === 'string'
      ? error.detail
      : `Falha ao comunicar com a API: ${response.status}`
    throw new Error(detail)
  }

  if (response.status === 204) return undefined as T

  return response.json() as Promise<T>
}
