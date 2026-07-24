import { getFromApi, type ListResponse } from '@/services/api-client'
import type { ContactInfo, FaqItem, Testimonial } from '@/types/domain'

export async function getBenefits(): Promise<string[]> {
  const response = await getFromApi<ListResponse<string>>('/content/benefits')
  return response.items
}

export async function getHowItWorks(): Promise<string[]> {
  const response = await getFromApi<ListResponse<string>>('/content/how-it-works')
  return response.items
}

export async function getTestimonials(): Promise<Testimonial[]> {
  const response = await getFromApi<ListResponse<Testimonial>>('/testimonials')
  return response.items
}

export async function getFaqItems(): Promise<FaqItem[]> {
  const response = await getFromApi<ListResponse<FaqItem>>('/faqs')
  return response.items
}

export async function getContactInfo(): Promise<ContactInfo> {
  return getFromApi<ContactInfo>('/contact')
}
