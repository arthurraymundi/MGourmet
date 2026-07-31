import type { SeoMeta } from '@/types/domain'
import { COMPANY } from './company'

const BASE_URL = 'https://mgourmet.com.br'

export const DEFAULT_META: SeoMeta = {
  title: `${COMPANY.name} | Marmitas Fitness Premium`,
  description:
    `${COMPANY.name} oferece marmitas fitness premium para dieta, treino e rotina com praticidade em ${COMPANY.serviceArea}.`,
  path: '/',
  image: `${BASE_URL}/og-image.jpg`,
}

export const PAGE_META: Record<string, SeoMeta> = {
  home: DEFAULT_META,
  about: {
    title: `Sobre | ${COMPANY.name}`,
    description: `Conheça a história, missão e valores da ${COMPANY.name}.`,
    path: '/sobre',
    image: `${BASE_URL}/og-image.jpg`,
  },
  menu: {
    title: `Cardápio | ${COMPANY.name}`,
    description: `Explore opções hiperproteicas, low carb e vegetarianas no cardápio ${COMPANY.name}.`,
    path: '/cardapio',
    image: `${BASE_URL}/og-image.jpg`,
  },
  kits: {
    title: `Kits Promocionais | ${COMPANY.name}`,
    description: 'Kits 5, 10 e 20 refeições com economia para sua rotina saudável.',
    path: '/kits',
    image: `${BASE_URL}/og-image.jpg`,
  },
  contact: {
    title: `Contato | ${COMPANY.name}`,
    description: `Fale com a ${COMPANY.name} pelo WhatsApp, telefone, Instagram ou TikTok.`,
    path: '/contato',
    image: `${BASE_URL}/og-image.jpg`,
  },
}

export const SITE_URL = BASE_URL
