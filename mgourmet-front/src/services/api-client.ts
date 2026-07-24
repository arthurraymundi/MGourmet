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
  const response = await fetch(`${API_BASE_URL}${path}`)

  if (!response.ok) {
    throw new Error(`Falha ao carregar dados da API: ${response.status}`)
  }

  return response.json() as Promise<T>
}
