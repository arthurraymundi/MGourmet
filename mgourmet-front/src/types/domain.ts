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
  isAvailable?: boolean
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

export interface AdminUser {
  id: number
  name: string
  email: string
  createdAt: string
}

export type OrderStatus = 'Recebido' | 'Preparando' | 'Saiu para entrega' | 'Finalizado' | 'Cancelado'
export type OrderSource = 'site' | 'telefone' | 'whatsapp' | 'presencial'

export interface AdminOrderItem {
  id: number
  productId: string
  productName: string
  unitPrice: number
  quantity: number
}

export interface AdminOrder {
  id: number
  customerName: string
  customerPhone: string
  deliveryMethod: DeliveryMethod
  street: string | null
  number: string | null
  neighborhood: string | null
  complement: string | null
  notes: string | null
  status: OrderStatus
  source: OrderSource
  paymentMethod: string | null
  total: number
  createdAt: string
  items: AdminOrderItem[]
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
