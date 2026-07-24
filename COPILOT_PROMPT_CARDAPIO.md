# 🚀 Script Copilot - Integrar Cardápio Completo MGourmet

## 📋 Contexto
Projeto full-stack: Backend FastAPI + Frontend React + PostgreSQL + Alembic
Repo: arthurraymundi/MGourmet
Objetivo: Integrar cardápio completo (38 produtos) mantendo padrões existentes

---

## ⚠️ RESTRIÇÕES CRÍTICAS

### Código
- ✅ Não altere a estrutura existente sem análise prévia
- ✅ Não crie migrations sem validar dados dependentes
- ✅ Todos os endpoints mantêm padrão `/api/v1/...`
- ✅ TypeScript: tipos fortemente tipados sempre
- ✅ Migrations: sempre usar Alembic, nunca SQL raw
- ✅ Não utilize drop table, alter column destrutivos

### Git
- ✅ Não alterar configurações Git
- ✅ Não remover arquivos .git
- ✅ Não criar submodules
- ✅ Não mover pastas do projeto
- ✅ **NÃO executar `git commit` automaticamente**
- ✅ **Apenas sugerir mensagens de commit após confirmar**

### Banco de dados
- ✅ Antes de qualquer migration: analisar tabelas existentes
- ✅ Verificar dados atuais e constraints
- ✅ Validar que seeds existentes não quebram
- ✅ Usar Alembic upgrade head para aplicar mudanças

### Implementação
- ✅ **Não criar arquivos inexistentes sem justificar primeiro**
- ✅ **Não assumir bibliotecas não instaladas** (verificar package.json / requirements.txt)
- ✅ **Não instalar dependências novas sem confirmação**
- ✅ Usar apenas libs já presentes no projeto
- ✅ Se precisar lib nova: sugerir e pedir aprovação ANTES

---

## 📊 Cardápio para integrar (38 produtos novos)

### PRATOS FITNESS (~300g) - 10 pratos
Preço: R$ 28,00 individual / R$ 250,00 kit 10
1. Panqueca de carne
2. Picadinho de carne com legumes e arroz
3. Bife acebolado, quibebe de mandioca e arroz com ervilha
4. Bolo de carne assado com tomate e queijo, purê de batata e cenoura
5. Feijoada magra, arroz e couve
6. Frango empanado, creme de milho e arroz
7. Frango xadrez e arroz de brócolis
8. Galinhada Fit (sobrecoxa, cenoura e milho)
9. Frango desfiado e purê de grão-de-bico
10. Moqueca de peixe, arroz e banana da terra

### MINI PRATOS FITNESS (~200g) - 10 pratos
Preço: R$ 20,00 individual / R$ 180,00 kit 10
(Mesmos 10 pratos acima, versão reduzida)

### PRATOS KIDS (~300g) - 5 pratos
Preço: R$ 28,00 individual / R$ 260,00 kit 10
1. Strogonoff de frango, arroz branco e purê de batata
2. Picadinho de carne, arroz branco, feijão e cenoura
3. Frango desfiado com purê de mandioquinha e brócolis
4. Carne moída, arroz branco, feijão e legumes
5. Espaguete com mini almôndegas

### SOPAS (~300ml) - 5 pratos
Preço: R$ 21,00 individual / R$ 200,00 kit 10
1. Abóbora, inhame e carne
2. Feijão com calabresa
3. Mandioquinha com frango
4. Caldo verde (chuchu, abobrinha, batata) com carne e couve
5. Puchero (grão de bico, calabresa e legumes)

### PROTEÍNAS (~500g) - 4 pratos
Preço: R$ 60,00 individual
1. Carne na cerveja preta
2. Estrogonofe de carne com champignon
3. Sobrecoxa assada ao molho pesto
4. Carne louca

### LINHA PREMIUM (~350g) - 4 pratos
Preço: R$ 35,00 individual
1. Iscas de carne ao creme de gorgonzola, arroz e batata saute
2. Carne ao vinho com Champignon e purê de mandioquinha com cenoura
3. Estrogonofe de carne com champignon e arroz integral a grega
4. Risoto 4 queijos com filé de tilápia

---

## 🔍 FASE 1: ANÁLISE COMPLETA (SEM IMPLEMENTAR)

⚠️ **EXECUTE APENAS ESTA FASE PRIMEIRO**
⚠️ **NÃO ALTERE NENHUM ARQUIVO**
⚠️ **APENAS ANALISE E RETORNE RELATÓRIO**

### 1.1 Backend - Product Model

Arquivo: `mgourmet-back/app/product/models.py`

Verificar:
- [ ] Como `ProductCategory` está implementada? (Enum? String?)
- [ ] Qual a estrutura exata da classe Product?
- [ ] Quais são os campos obrigatórios?
- [ ] Quais são os campos opcionais?
- [ ] Existe alguma constraint customizada?
- [ ] Há relacionamentos com outras tabelas?
- [ ] Como `image_url`, `ingredients`, `nutrition` são armazenados?

Output esperado:
```
ProductCategory: Enum com valores [...]
Product fields: id (pk), name, description, ...
Constraints: price >= 0, calories >= 0, ...
```

### 1.2 Backend - Product Schemas

Arquivo: `mgourmet-back/app/product/schemas.py`

Verificar:
- [ ] Como `ProductResponse` é serializado?
- [ ] Como `NutritionInfo` é estruturada?
- [ ] Qual o padrão de validação (Pydantic)?
- [ ] Como o frontend recebe os dados?

Output esperado:
```
ProductResponse fields: id, name, price, imageUrl, ...
Serializers: price como float, ...
```

### 1.3 Backend - Product Router/Endpoints

Arquivo: `mgourmet-back/app/product/router.py`

Verificar:
- [ ] Quais endpoints existem? (GET /products, GET /products/{id}, etc)
- [ ] Qual é o prefixo EXATO do endpoint? (/api/v1/products ou /api/v1/menu/products?)
- [ ] Como filtros funcionam? (category, search, pagination)
- [ ] Qual o padrão de paginação?
- [ ] Como ordenação funciona?

Output esperado:
```
Endpoint EXATO: /api/v1/products
GET /api/v1/products - retorna lista com paginação
Filtros: category, search, sort
Response: { items: [...], meta: { ... } }
```

### 1.4 Backend - Database/Alembic

Diretório: `mgourmet-back/alembic/versions/`

Verificar:
- [ ] Quais migrations já existem?
- [ ] Schema atual da tabela `products`
- [ ] **Quantos registros já existem na tabela products?**
- [ ] Há enums customizados no banco?
- [ ] Quais categorias já estão cadastradas?

Command para você executar (não o Copilot):
```sql
\d products  -- listar schema
SELECT COUNT(*) FROM products;  -- contar registros ATUAIS
SELECT DISTINCT category FROM products;  -- listar categorias ATUAIS
```

Output esperado:
```
Migrations: [lista de migrations]
Tabela products: [schema atual]
Registros ATUAIS: [quantidade]
Categorias ATUAIS: [lista]
```

### 1.5 Backend - Seed Atual

Arquivo: `mgourmet-back/scripts/seed.py`

Verificar:
- [ ] Como o seed atual funciona?
- [ ] Qual o padrão de IDs dos produtos?
- [ ] **Quantos produtos já existem no PRODUCTS tuple?**
- [ ] Quais categorias estão sendo seeded?
- [ ] Como a função `add_if_absent()` funciona?
- [ ] Há dados de testimonials, FAQs, content que não podem quebrar?

Output esperado:
```
Seed pattern: [estrutura atual]
ID pattern: [como IDs são formados]
Produtos no seed ATUAL: [quantidade]
Categorias no seed ATUAL: [lista]
Dados relacionados: testimonials, FAQs, content (proteger estes)
```

### 1.6 Frontend - Como Produtos são Consumidos

Arquivo: `mgourmet-front/src/features/menu/pages/menu-page.tsx`

Verificar:
- [ ] Existe página de menu? (se sim, qual o conteúdo?)
- [ ] Como dados são carregados? (fetch, axios, SWR?)
- [ ] Existe context/provider para produtos?
- [ ] Qual o padrão de hooks utilizados?
- [ ] Como filtros são implementados?

Output esperado:
```
Menu page: [existe/não existe]
Data fetching: [padrão utilizado]
State management: [context/hooks/redux]
Filtros: [como funcionam]
```

### 1.7 Frontend - Tipos TypeScript

Arquivo: `mgourmet-front/src/types/` (se existir)

Verificar:
- [ ] Já existe type/interface de Product?
- [ ] Como NutritionInfo é tipada?
- [ ] Qual o padrão de tipagem do projeto?

Output esperado:
```
Tipos encontrados: [lista ou "não encontrados"]
Padrão TypeScript: [strict mode? camelCase?]
```

### 1.8 Frontend - Componentes Existentes

Diretório: `mgourmet-front/src/components/`

Verificar:
- [ ] Quais componentes base existem?
- [ ] Como cards são implementados?
- [ ] Como filtros/buttons são estilizados?
- [ ] Qual o padrão de componentes (Radix UI + Tailwind)?

Output esperado:
```
Componentes base: [lista]
Padrão de estilo: Radix UI + Tailwind
UI Kit: [quais componentes disponíveis]
```

### 1.9 Frontend - Dependências

Arquivo: `mgourmet-front/package.json`

Verificar:
- [ ] Quais dependências já estão instaladas?
- [ ] Qual versão de React, React Router, Tailwind?
- [ ] Há bibliotecas de state management (Redux, Zustand, Context)?
- [ ] Há biblioteca de HTTP client (axios, fetch, SWR)?

Output esperado:
```
Dependencies ATUAIS: [lista com versões]
HTTP client: [qual é usado]
State management: [qual é usado ou "apenas Context"]
```

### 1.10 Backend - Dependências

Arquivo: `mgourmet-back/pyproject.toml`

Verificar:
- [ ] Quais dependências backend estão instaladas?
- [ ] Há alguma lib para image handling?
- [ ] FastAPI versão?

Output esperado:
```
Dependencies ATUAIS: [lista com versões]
```

---

## 📋 PLANO DE ALTERAÇÃO (baseado na análise)

Depois de completar 1.1-1.10, o Copilot deve retornar:

### Backend Changes
```
[ ] ProductCategory: adicionar X novas categorias (não remover antigas)
[ ] Migration Alembic: sim/não (se sim, qual operation?)
[ ] Seed: adicionar 38 novos produtos (total final: X)
[ ] Nenhum arquivo será removido
[ ] Nenhuma dependência nova será instalada
```

### Frontend Changes
```
[ ] Criar: src/types/product.ts (se não existir)
[ ] Criar: src/services/products-service.ts (se não existir)
[ ] Criar: src/features/menu/components/menu-filter.tsx (se não existir)
[ ] Criar: src/features/menu/components/menu-card.tsx (se não existir)
[ ] Atualizar: src/features/menu/pages/menu-page.tsx (se existir)
[ ] Nenhuma dependência nova será instalada
```

### Commits Sugeridos
```
1. feat: update product categories
2. feat: add alembic migration (se necessário)
3. feat: add mgourmet menu seed (38 new products)
4. feat: create menu types and api service
5. feat: create menu page components
```

---

## ✅ FASE 2: IMPLEMENTAÇÃO (após aprovação de análise)

⚠️ **INICIE ESTA FASE SOMENTE APÓS FASE 1 SER APROVADA**
⚠️ **SIGA O PLANO DE ALTERAÇÃO EXATAMENTE**

### 2.1 Backend - ProductCategory Update

Arquivo: `mgourmet-back/app/product/models.py`

Tarefas:
- ✅ Analisar estrutura atual do ProductCategory
- ✅ Adicionar 6 categorias novas seguindo padrão existente
- ✅ Manter todas as categorias antigas
- ✅ Não remover ou renomear valores existentes
- ✅ Se necessário migration: criar automaticamente

Novas categorias a adicionar:
```python
PRATO_FITNESS = "Prato Fitness"
MINI_PRATO_FITNESS = "Mini Prato Fitness"
PRATO_KIDS = "Prato Kids"
SOPA = "Sopa"
PROTEINA = "Proteína"
PREMIUM = "Premium"
```

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.1 completa. Categorias atualizadas. Pronto para próxima etapa?"

### 2.2 Backend - Alembic Migration (SE NECESSÁRIO)

Arquivo: `mgourmet-back/alembic/versions/[timestamp]_add_new_product_categories.py`

Tarefas:
- ✅ Verificar se migration é necessária (baseado em 1.4)
- ✅ Se sim: criar com `alembic revision --autogenerate -m "add new product categories"`
- ✅ Validar migration forward/downgrade
- ✅ **NÃO executar alembic upgrade head** (user fará depois)

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.2 completa. Migration criada [ou "não necessária"]. Pronto para próxima etapa?"

### 2.3 Backend - Seed com 38 Produtos Novos

Arquivo: `mgourmet-back/scripts/seed.py`

Tarefas:
- ✅ Adicionar EXATAMENTE 38 novos produtos (não alterar produtos existentes)
- ✅ IDs seguem padrão existente: `prato-fitness-panqueca-carne`, etc
- ✅ Imagens específicas por categoria (não aleatórias):
  - Fitness/Mini: proteína, frango, carne, peixe, feijoada
  - Kids: refeições simples e coloridas
  - Sopas: imagens de sopas/caldos
  - Premium: pratos gourmet elegantes
- ✅ Nutrition realista: calories, protein, carbs, fat (baseado em cada prato)
- ✅ Usar função `add_if_absent()` existente (idempotente)
- ✅ Manter testimonials, FAQs, content items existentes INTACTOS

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.3 completa. 38 produtos adicionados. Total esperado: X registros. Pronto para próxima etapa?"

### 2.4 Frontend - Types (USAR LIBS EXISTENTES)

Arquivo: `mgourmet-front/src/types/product.ts` (novo arquivo)

Tarefas:
- ✅ Criar types usando APENAS TypeScript built-in
- ✅ Não usar bibliotecas externas para tipos
- ✅ Seguir padrão do projeto (camelCase, interfaces)

```typescript
export enum ProductCategory {
  PratoFitness = 'Prato Fitness',
  MiniPratoFitness = 'Mini Prato Fitness',
  PratoKids = 'Prato Kids',
  Sopa = 'Sopa',
  Proteina = 'Proteína',
  Premium = 'Premium',
}

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
  featured: boolean
}

export interface ProductFilters {
  category?: ProductCategory
  search?: string
  priceMin?: number
  priceMax?: number
  sort?: 'name' | 'price'
}

export interface PaginatedResponse<T> {
  items: T[]
  meta: {
    total: number
    page: number
    limit: number
    hasMore: boolean
  }
}
```

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.4 completa. Tipos criados em src/types/product.ts. Pronto para próxima etapa?"

### 2.5 Frontend - API Service (USAR LIBS EXISTENTES)

Arquivo: `mgourmet-front/src/services/products-service.ts` (novo arquivo)

Tarefas:
- ✅ Usar apenas `fetch` built-in do browser (não instalar axios)
- ✅ Função `fetchProducts(filters?: ProductFilters)`
- ✅ Endpoint EXATO (baseado em 1.3): `/api/v1/products`
- ✅ Tipagem completa TypeScript
- ✅ Error handling com try/catch
- ✅ Retornar `PaginatedResponse<Product>`
- ✅ Base URL: usar variável de ambiente `VITE_API_URL`
- ✅ Não usar dependências não listadas em package.json

```typescript
import { Product, ProductFilters, PaginatedResponse } from '@/types/product'

const API_BASE = import.meta.env.VITE_API_URL

export async function fetchProducts(
  filters?: ProductFilters
): Promise<PaginatedResponse<Product>> {
  const params = new URLSearchParams()

  if (filters?.category) {
    params.append('category', filters.category)
  }
  if (filters?.search) {
    params.append('search', filters.search)
  }
  if (filters?.priceMin) {
    params.append('price_min', filters.priceMin.toString())
  }
  if (filters?.priceMax) {
    params.append('price_max', filters.priceMax.toString())
  }
  if (filters?.sort) {
    params.append('sort', filters.sort)
  }

  const url = `${API_BASE}/products?${params.toString()}`

  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error('Error fetching products:', error)
    throw error
  }
}
```

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.5 completa. API service criado. Pronto para próxima etapa?"

### 2.6 Frontend - Menu Filter Component

Arquivo: `mgourmet-front/src/features/menu/components/menu-filter.tsx` (novo arquivo)

Tarefas:
- ✅ Usar APENAS bibliotecas já em package.json (React, Tailwind, Radix UI)
- ✅ Props: `filters: ProductFilters`, `onFilterChange: (filters) => void`
- ✅ Filtro categoria: tabs ou button group com todas as 6 categorias
- ✅ Campo busca: input text
- ✅ Filtro preço: range slider (R$ 0 a R$ 100)
- ✅ Botão reset: limpar todos filtros
- ✅ Estilo: Tailwind + Radix UI (padrão do projeto)
- ✅ Responsivo: mobile friendly

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.6 completa. MenuFilter componente criado. Pronto para próxima etapa?"

### 2.7 Frontend - Menu Card Component

Arquivo: `mgourmet-front/src/features/menu/components/menu-card.tsx` (novo arquivo)

Tarefas:
- ✅ Usar APENAS bibliotecas já em package.json
- ✅ Props: `product: Product`
- ✅ Exibir: imagem, nome, descrição (truncado ~80 chars)
- ✅ Preço em destaque (formato: "R$ 28,00")
- ✅ Badge categoria
- ✅ Lista de 3-5 ingredientes principais
- ✅ Botão "Adicionar ao carrinho" (visual apenas, callback preparado)
- ✅ Estilo: card com shadow, hover effect
- ✅ Responsivo: mobile, tablet, desktop

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.7 completa. MenuCard componente criado. Pronto para próxima etapa?"

### 2.8 Frontend - Menu Page

Arquivo: `mgourmet-front/src/features/menu/pages/menu-page.tsx` (novo ou atualizar)

Tarefas:
- ✅ Layout: filter (sidebar/top) + grid de cards
- ✅ Estado: `products`, `filters`, `loading`, `error`
- ✅ `useEffect`: carregar produtos ao montar
- ✅ `useEffect`: recarregar quando filters mudam
- ✅ Loading state: skeleton ou spinner
- ✅ Error state: mensagem amigável
- ✅ Grid responsivo: 1 col (mobile), 2 col (tablet), 3-4 col (desktop)
- ✅ Total na página: "Exibindo X produtos" (ou filtrados)
- ✅ Sem scroll infinito (por enquanto)

**Após implementar, não fazer commit ainda. Apenas reportar:**
"Seção 2.8 completa. MenuPage implementada. Pronto para próxima etapa?"

---

## 📝 COMMITS SUGERIDOS (NÃO FAZER AUTOMATICAMENTE)

Após cada seção implementada, o Copilot **SUGERE** (não executa):

### Após 2.1
```
Sugestão de commit:

feat: update product categories

- Add 6 new ProductCategory enum values
- Maintain backward compatibility
- No database data affected

Files: mgourmet-back/app/product/models.py

Quer confirmar e commitar? (responda: sim/não)
```

### Após 2.2 (se necessário)
```
Sugestão de commit:

feat: add alembic migration for product categories

- Auto-generated migration for enum update
- Tested with upgrade head
- No data loss

Files: mgourmet-back/alembic/versions/[...].py

Quer confirmar e commitar? (responda: sim/não)
```

### Após 2.3
```
Sugestão de commit:

feat: add mgourmet menu seed (38 new products)

- Add 10 Prato Fitness items
- Add 10 Mini Prato Fitness items
- Add 5 Prato Kids items
- Add 5 Sopa items
- Add 4 Proteína items
- Add 4 Premium items
- Idempotent seed function (add_if_absent)
- Real nutrition data
- High-quality images per category

Files: mgourmet-back/scripts/seed.py

Quer confirmar e commitar? (responda: sim/não)
```

### Após 2.4
```
Sugestão de commit:

feat: create menu types and api service

- Add ProductCategory enum with 6 values
- Add Product, NutritionInfo interfaces
- Add ProductFilters, PaginatedResponse types
- Add products-service.ts with fetchProducts
- Full TypeScript typing
- No new dependencies required

Files:
- mgourmet-front/src/types/product.ts
- mgourmet-front/src/services/products-service.ts

Quer confirmar e commitar? (responda: sim/não)
```

### Após 2.5-2.8
```
Sugestão de commit:

feat: create menu page components

- Add MenuFilter component (category, search, price range)
- Add MenuCard component (product display)
- Add MenuPage with layout and state management
- Responsive design (mobile, tablet, desktop)
- Loading and error states
- No new dependencies required

Files:
- mgourmet-front/src/features/menu/components/menu-filter.tsx
- mgourmet-front/src/features/menu/components/menu-card.tsx
- mgourmet-front/src/features/menu/pages/menu-page.tsx

Quer confirmar e commitar? (responda: sim/não)
```

---

## 🧪 FASE 3: VALIDAÇÃO & TESTES

⚠️ **EXECUTE APÓS IMPLEMENTAÇÃO COMPLETA**

### Backend Validation

```bash
# 1. Criar novo ambiente (se needed)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou: venv\Scripts\activate  # Windows

# 2. Instalar dependências
pip install -e ".[dev]"

# 3. Iniciar banco
docker compose -f mgourmet-back/docker-compose.yml up -d db redis

# 4. Aplicar migrations (incluindo a nova, se houver)
cd mgourmet-back
alembic upgrade head

# 5. Executar seed
python -m scripts.seed

# 6. Validar dados
psql -U mgourmet -d mgourmet_db -c "SELECT COUNT(*) FROM products;"
psql -U mgourmet -d mgourmet_db -c "SELECT DISTINCT category FROM products;"

# 7. Testar endpoint EXATO (verificar em 1.3)
curl http://localhost:8000/api/v1/products
curl "http://localhost:8000/api/v1/products?category=Prato%20Fitness"

# 8. Swagger docs
# Abrir: http://localhost:8000/docs
```

Checklist:
- [ ] Alembic upgrade head sem erros
- [ ] Seed executado (check: X created records)
- [ ] 38 novos produtos adicionados (não quebrou existentes)
- [ ] Total de produtos: [mostrar quantidade]
- [ ] 6 categorias novas aparecem no SELECT DISTINCT
- [ ] GET /api/v1/products retorna status 200
- [ ] Filtro por categoria funciona
- [ ] Dados antigos (testimonials, FAQs) não foram quebrados

### Frontend Validation

```bash
# 1. Copiar .env.example
cp mgourmet-front/.env.example mgourmet-front/.env

# 2. Configurar VITE_API_URL (verificar em 1.3 qual endpoint exato)
# .env: VITE_API_URL=http://localhost:8000/api/v1

# 3. Instalar dependências (VERIFICAR se já estão em package.json)
cd mgourmet-front
npm install

# 4. Build type check
npm run build  # deve passar TypeScript strict

# 5. Dev server
npm run dev

# 6. Testar manualmente
# Abrir: http://localhost:5173
# Ir para: /cardapio
# Verificar:
```

Checklist:
- [ ] npm run build sem erros TypeScript
- [ ] Frontend compilado com sucesso
- [ ] Página /cardapio carrega
- [ ] 38 produtos aparecem no grid (ou total correto)
- [ ] Sem erros no console
- [ ] Imagens carregam corretamente
- [ ] Filtro por categoria funciona
- [ ] Busca funciona
- [ ] Filtro preço funciona
- [ ] Cards exibem: imagem, nome, preço, categoria, ingredientes
- [ ] Responsividade: mobile, tablet, desktop OK
- [ ] Botão "Adicionar ao carrinho" visível (sem lógica)

### Integration Tests

```bash
# 1. Deletar um produto (para testar)
# Verificar: GET /api/v1/products retorna corretamente

# 2. Buscar categoria específica
# GET /api/v1/products?category=Prato%20Fitness
# Verificar: retorna exato 10 produtos

# 3. Buscar por preço
# GET /api/v1/products?price_min=20&price_max=30
# Verificar: retorna produtos corretos

# 4. Buscar por texto
# GET /api/v1/products?search=frango
# Verificar: retorna produtos com "frango"

# 5. Frontend + Backend
# Abrir /cardapio
# Clicar em filtro "Prato Fitness"
# Verificar: apenas 10 produtos mostram
# Buscar por "carne"
# Verificar: filtra corretamente
```

---

## 📋 CHECKLIST FINAL

Backend:
- [ ] ProductCategory tem 6 novas categorias (antigas mantidas)
- [ ] Migration Alembic criada (se necessária) e testada
- [ ] 38 novos produtos adicionados ao seed
- [ ] Total de produtos no banco: [quantidade]
- [ ] Seed é idempotente (add_if_absent)
- [ ] GET /api/v1/products retorna 200
- [ ] Filtros funcionam (category, search, price)
- [ ] Dados antigos não foram quebrados

Frontend:
- [ ] npm run build sem erros TypeScript
- [ ] Tipos criados: Product, ProductCategory, etc
- [ ] API service funcional: fetchProducts()
- [ ] MenuFilter componente renderiza
- [ ] MenuCard componente renderiza
- [ ] MenuPage exibe produtos corretos
- [ ] Filtros funcionam (category, search, price)
- [ ] Imagens carregam
- [ ] Layout responsivo
- [ ] Sem erros no console

Código:
- [ ] Nenhuma dependência nova foi instalada
- [ ] Nenhum arquivo .git foi alterado
- [ ] Nenhum submodule foi criado
- [ ] Commits sugeridos (não feitos automaticamente)
- [ ] Mensagens de commit descritivas

---

## 🚀 PRÓXIMOS PASSOS (NÃO IMPLEMENTAR AGORA)

- [ ] Sistema de carrinho (outro prompt)
- [ ] Checkout (outro prompt)
- [ ] Integração de pagamento (outro prompt)
- [ ] Admin dashboard para gerenciar produtos (outro prompt)

---

## 📞 COMO USAR ESTE PROMPT

### Passo 1: Execute FASE 1 (Análise)

```
Você é um senior developer full-stack.
Siga EXATAMENTE este documento.

[Cola o arquivo inteiro]

PRIMEIRA MENSAGEM:
Execute APENAS a FASE 1.
Não altere nenhum arquivo.
Faça análise completa das seções 1.1 até 1.10.
Retorne um relatório com todas as respostas.
Depois me mostre o PLANO DE ALTERAÇÃO esperado.
```

### Passo 2: Você revisa análise

Depois que Copilot responder, **você valida**:
- Faz sentido?
- Está completo?
- Endpoint está correto?
- Não vai quebrar nada?

### Passo 3: Execute FASE 2 (Implementação)

```
Com base na análise da FASE 1, execute a FASE 2.
Implemente as seções 2.1 até 2.8 exatamente como descrito.
Após cada seção completa, sugira a mensagem de commit.
NÃO execute git commit automaticamente.
NÃO instale dependências sem confirmação.
Mantenha todas as restrições críticas.
Não execute migrations ainda (user fará depois).
```

### Passo 4: Você aprova commits

Após cada seção, Copilot sugere commit. Você responde:
```
Aprovado, pode commitar.
OU
Não, refaz isso.
```

### Passo 5: Você testa (FASE 3)

Execute commands de validação e confirma tudo funciona.

### Passo 6: Deploy

Após FASE 3 passar, tudo pronto para deploy.

---

**Status: 10/10 ✅ Pronto para time profissional**
