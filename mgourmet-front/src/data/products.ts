import type { Product } from '@/types/domain'

export const PRODUCTS_MOCK: Product[] = [
  {
    id: 'frango-grelhado-fit',
    name: 'Frango Grelhado com Arroz Integral',
    description: 'Peito de frango grelhado, arroz integral e legumes no vapor.',
    imageUrl:
      'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=1200&q=80',
    price: 24.9,
    category: 'Hiperproteica',
    ingredients: ['Frango', 'Arroz integral', 'Brócolis', 'Cenoura', 'Azeite'],
    nutrition: { calories: 420, protein: 38, carbs: 39, fat: 11 },
    featured: true,
  },
  {
    id: 'tilapia-low-carb',
    name: 'Tilápia Low Carb com Abobrinha',
    description: 'Tilápia assada com purê de couve-flor e abobrinha salteada.',
    imageUrl:
      'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=1200&q=80',
    price: 27.9,
    category: 'Low Carb',
    ingredients: ['Tilápia', 'Couve-flor', 'Abobrinha', 'Alho', 'Salsinha'],
    nutrition: { calories: 360, protein: 36, carbs: 18, fat: 15 },
    featured: true,
  },
  {
    id: 'patinho-emagrecimento',
    name: 'Patinho Magro com Mix de Vegetais',
    description: 'Patinho refogado com temperos naturais e vegetais coloridos.',
    imageUrl:
      'https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=1200&q=80',
    price: 25.5,
    category: 'Emagrecimento',
    ingredients: ['Patinho', 'Abóbora', 'Vagem', 'Pimentão', 'Cebola roxa'],
    nutrition: { calories: 390, protein: 35, carbs: 27, fat: 14 },
  },
  {
    id: 'massa-ganho',
    name: 'Frango com Batata-Doce Power',
    description: 'Prato energético para rotina intensa de treino.',
    imageUrl:
      'https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=1200&q=80',
    price: 26.9,
    category: 'Ganho de Massa',
    ingredients: ['Frango desfiado', 'Batata-doce', 'Feijão', 'Couve', 'Azeite'],
    nutrition: { calories: 520, protein: 41, carbs: 54, fat: 13 },
  },
  {
    id: 'vegetariana-proteica',
    name: 'Bowl Vegetariano de Grão-de-Bico',
    description: 'Grão-de-bico, quinoa e legumes para alta saciedade.',
    imageUrl:
      'https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=1200&q=80',
    price: 23.9,
    category: 'Vegetariana',
    ingredients: ['Grão-de-bico', 'Quinoa', 'Abóbora', 'Espinafre', 'Tomate'],
    nutrition: { calories: 410, protein: 20, carbs: 48, fat: 14 },
  },
]
