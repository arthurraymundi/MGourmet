export type ProductCategory =
  | 'Hiperproteica'
  | 'Low Carb'
  | 'Emagrecimento'
  | 'Ganho de Massa'
  | 'Vegetariana'
  | 'Prato Fitness'
  | 'Mini Prato Fitness'
  | 'Prato Kids'
  | 'Sopa'
  | 'Proteína'
  | 'Premium'

export interface NutritionInfo {
  calories: number
  protein: number
  carbs: number
  fat: number
}

export interface Product {
  id: string
  name: string
  description: string
  imageUrl: string
  price: number
  category: ProductCategory
  ingredients: string[]
  nutrition: NutritionInfo
  featured?: boolean
}

export interface CartItem {
  product: Product
  quantity: number
}

export type DeliveryMethod = 'pickup' | 'delivery'

export interface CustomerDetails {
  name: string
  phone: string
  deliveryMethod: DeliveryMethod
  street: string
  number: string
  neighborhood: string
  complement: string
  notes: string
}

export interface KitOffer {
  id: string
  name: string
  meals: number
  originalPrice: number
  discountedPrice: number
}

export interface Testimonial {
  id: string
  name: string
  role: string
  quote: string
}

export interface FaqItem {
  id: string
  question: string
  answer: string
}

export interface ContactInfo {
  whatsapp: string
  instagram: string
  address: string
  businessHours: string
}

export interface SeoMeta {
  title: string
  description: string
  path: string
  image?: string
}
