import { getFromApi, type ListResponse } from '@/services/api-client'
import type { KitOffer } from '@/types/domain'

export async function getKits(): Promise<KitOffer[]> {
  const response = await getFromApi<ListResponse<KitOffer>>('/kits')
  return response.items
}
