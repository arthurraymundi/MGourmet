import type { SeoMeta } from '@/types/domain'

const BASE_URL = 'https://mgourmet.com.br'

export const DEFAULT_META: SeoMeta = {
  title: 'M Gourmet | Marmitas Fitness Premium',
  description:
    'M Gourmet oferece marmitas fitness premium para dieta, treino e rotina com praticidade.',
  path: '/',
  image: `${BASE_URL}/og-image.jpg`,
}

export const PAGE_META: Record<string, SeoMeta> = {
  home: DEFAULT_META,
  about: {
    title: 'Sobre | M Gourmet',
    description: 'Conheça a história, missão e valores da M Gourmet.',
    path: '/sobre',
    image: `${BASE_URL}/og-image.jpg`,
  },
  menu: {
    title: 'Cardápio | M Gourmet',
    description: 'Explore opções hiperproteicas, low carb e vegetarianas no cardápio M Gourmet.',
    path: '/cardapio',
    image: `${BASE_URL}/og-image.jpg`,
  },
  kits: {
    title: 'Kits Promocionais | M Gourmet',
    description: 'Kits 5, 10 e 20 refeições com economia para sua rotina saudável.',
    path: '/kits',
    image: `${BASE_URL}/og-image.jpg`,
  },
  contact: {
    title: 'Contato | M Gourmet',
    description: 'Fale com a M Gourmet pelo WhatsApp, Instagram ou endereço.',
    path: '/contato',
    image: `${BASE_URL}/og-image.jpg`,
  },
}

export const SITE_URL = BASE_URL
