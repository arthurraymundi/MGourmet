import type { ContactInfo, FaqItem, Testimonial } from '@/types/domain'

export const BENEFITS = [
  'Pratos balanceados por nutricionistas',
  'Entrega programada e pontual',
  'Ingredientes frescos e seleção premium',
  'Cardápio variado para objetivos diferentes',
]

export const HOW_IT_WORKS = [
  'Escolha seus pratos ou kits',
  'Monte seu pedido por objetivo',
  'Receba em casa pronto para consumir',
]

export const TESTIMONIALS_MOCK: Testimonial[] = [
  {
    id: '1',
    name: 'Camila Rocha',
    role: 'Atleta amadora',
    quote: 'Economizei tempo e melhorei meu desempenho com refeições práticas e saborosas.',
  },
  {
    id: '2',
    name: 'Diego Matos',
    role: 'Analista de TI',
    quote: 'A qualidade é excelente e me ajuda a manter a dieta na rotina corrida.',
  },
]

export const FAQ_MOCK: FaqItem[] = [
  {
    id: '1',
    question: 'As refeições chegam congeladas ou refrigeradas?',
    answer: 'As marmitas são entregues congelada e prontas para armazenamento seguro.',
  },
  {
    id: '2',
    question: 'Posso combinar categorias no mesmo pedido?',
    answer: 'Sim. Você pode misturar pratos de qualquer categoria e montar seu plano ideal.',
  },
  {
    id: '3',
    question: 'Vocês atendem empresas?',
    answer: 'Sim. Temos planos corporativos para equipes com personalização de cardápio.',
  },
]

export const CONTACT_MOCK: ContactInfo = {
  whatsapp: '+55 (11) 98888-0000',
  instagram: '@mgourmetfit',
  address: 'Rua Exemplo, 250 - São Paulo/SP',
  businessHours: 'Segunda a sábado, 08h às 19h',
}
