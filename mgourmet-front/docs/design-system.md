# Design System - M Gourmet

## Objetivo
Definir a base visual e de interacao para manter consistencia, escalabilidade e qualidade de UX em todas as telas.

## Fundamentos visuais

### Identidade
- Premium, minimalista, elegante e moderna.
- Foco em confianca, saude, praticidade e profissionalismo.
- Mobile first, com bastante espaco em branco.

### Grid e espacamento
- Unidade base: `8px`.
- Escala recomendada: `4, 8, 12, 16, 24, 32, 40, 48, 64, 80`.
- Largura de container:
  - Mobile: `100%` com padding horizontal `16px`.
  - Tablet: max `768px`.
  - Desktop: max `1200px`.

### Tipografia
- Headings: **Poppins**
- Texto e UI: **Inter**
- Escala:
  - H1: 48/56 semibold
  - H2: 36/44 semibold
  - H3: 28/36 semibold
  - H4: 22/30 medium
  - Body-lg: 18/28 regular
  - Body: 16/24 regular
  - Body-sm: 14/20 regular
  - Caption: 12/16 medium

## Tokens de cor (semanticos)

> Os nomes abaixo devem ser usados como referencia semantica no projeto.

- `color-primary-500`: laranja principal de acao
- `color-primary-600`: laranja para hover de CTA
- `color-primary-700`: laranja para pressed/ativo
- `color-bg-base`: branco principal
- `color-bg-subtle`: cinza muito claro para secoes
- `color-surface`: branco para cards
- `color-text-primary`: cinza escuro (alta legibilidade)
- `color-text-secondary`: cinza medio
- `color-border`: cinza claro
- `color-success`: verde para feedback positivo
- `color-warning`: amarelo para alertas
- `color-danger`: vermelho para erros
- `color-dark-900`: fundo escuro para secoes de contraste

## Radius e sombras

- Border radius:
  - `radius-sm`: 8px
  - `radius-md`: 12px
  - `radius-lg`: 16px
  - `radius-xl`: 24px
  - `radius-pill`: 9999px
- Sombras:
  - `shadow-sm`: cards discretos
  - `shadow-md`: cards destacados
  - `shadow-lg`: modais e elevacao forte

## Componentes base (regras)

### Button
- Variantes: `primary`, `secondary`, `outline`, `ghost`.
- Tamanhos: `sm`, `md`, `lg`.
- Estados: default, hover, focus-visible, disabled, loading.
- CTA principal sempre com `primary`.

### Input
- Label visivel por padrao.
- Estado de erro com mensagem curta e objetiva.
- `focus-visible` com alto contraste.

### Card
- Estrutura padrao: titulo, descricao, conteudo e area de acao opcional.
- Uso de espacamento interno consistente (`16px` ou `24px`).

### Badge
- Variantes para categorias do cardapio: hiperproteica, low carb, emagrecimento, ganho de massa, vegetariana.

### Iconografia
- Biblioteca: **Lucide React**.
- Tamanho base: 18px/20px.
- Usar icones como reforco de leitura, nao como unico meio de comunicacao.

## Interacao e animacao
- Animacoes suaves e discretas com Framer Motion.
- Duracoes recomendadas:
  - Microinteracoes: `0.15s` a `0.2s`
  - Entradas de secao: `0.25s` a `0.4s`
- Easing suave, evitando efeitos chamativos.
- Respeitar `prefers-reduced-motion`.

## Acessibilidade
- Contraste minimo AA.
- Ordem semantica de headings.
- Navegacao por teclado em todos os componentes interativos.
- Focus ring visivel e consistente.
- Texto alternativo em imagens de produto.

## SEO visual e conteudo
- Hierarquia tipografica clara para leitura de crawler e usuarios.
- CTA principal acima da dobra na Home.
- Blocos com titulos descritivos por secao.

## Preparacao para implementacao
- Implementar tokens via Tailwind config e variaveis CSS.
- Criar componentes UI base reutilizaveis antes das paginas complexas.
- Garantir que features consumam apenas componentes e tokens padronizados.
