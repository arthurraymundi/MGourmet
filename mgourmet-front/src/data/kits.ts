import type { KitOffer } from '@/types/domain'

export const KITS_MOCK: KitOffer[] = [
  { id: 'kit-5', name: 'Kit 5', meals: 5, originalPrice: 134.5, discountedPrice: 119.9 },
  {
    id: 'kit-10',
    name: 'Kit 10',
    meals: 10,
    originalPrice: 269,
    discountedPrice: 224.9,
  },
  {
    id: 'kit-20',
    name: 'Kit 20',
    meals: 20,
    originalPrice: 538,
    discountedPrice: 409.9,
  },
]
