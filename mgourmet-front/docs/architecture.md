# Arquitetura Front-End - M Gourmet

## Objetivo
Definir uma arquitetura escalavel, desacoplada de dados mockados e pronta para evoluir para API REST sem retrabalho estrutural.

## Principios arquiteturais
- Feature-first: organizacao por dominio de negocio.
- UI desacoplada de dados: componentes recebem props tipadas, sem importar mocks diretamente.
- Separacao de responsabilidades: view, logica de apresentacao, servicos e tipos em camadas claras.
- Reutilizacao: componentes comuns em `components/common` e base visual em `components/ui`.
- Evolucao segura: contratos de dados centralizados em `types` para facilitar migracao para backend real.

## Camadas
1. **Routes**: define navegacao, code splitting e boundaries por pagina.
2. **Features**: implementa casos de uso por dominio (`home`, `about`, `menu`, `kits`, `contact`).
3. **Components**: biblioteca de blocos reutilizaveis e layout.
4. **Services**: adaptadores de dados (mock hoje, API amanha).
5. **Data**: fonte mock centralizada e versionavel.
6. **Types**: contratos de dominio e de UI compartilhados.
7. **Utils/Hooks**: funcoes puras e hooks reutilizaveis.

## Fluxo de dados
`data/*` -> `services/*` -> `features/*` -> `components/*`

Regras:
- Nenhum componente visual importa dados de `data/*` diretamente.
- `services/*` expoe funcoes assicronas para manter interface compativel com API futura.
- `features/*` coordena transformacoes de dados para apresentacao.

## Roteamento e carregamento
- React Router com rotas por pagina: Home, Sobre, Cardapio, Kits e Contato.
- Lazy loading por rota para reduzir bundle inicial.
- Layout compartilhado (Navbar + Footer) aplicado via rota raiz.
- Fallback de carregamento padrao para telas lazy.

## Estado e interacoes
- Estado local por feature com hooks do React.
- Sem gerenciador global neste MVP; manter simplicidade e baixo acoplamento.
- Filtros, busca e ordenacao do Cardapio encapsulados em hooks da feature.

## Contratos de dominio (base)
- `Product`
- `ProductCategory`
- `NutritionInfo`
- `KitOffer`
- `Testimonial`
- `FaqItem`
- `ContactInfo`

Todos os contratos ficam em `src/types` e sao consumidos por `services` e `features`.

## Preparacao para futuras funcionalidades
- Espaco reservado para modulos futuros (`auth`, `cart`, `checkout`, `customer`, `admin`) sem afetar features atuais.
- Servicos pensados como adaptadores para trocar facilmente mock por API.
- Estrutura de rotas preparada para areas privadas no futuro.

## Qualidade transversal
- TypeScript strict e proibicao de `any`.
- Acessibilidade desde os componentes base (foco, aria, contraste, semantica).
- SEO tecnico por rota (metadados, Open Graph, Twitter Cards e dados estruturados).
- Performance com code splitting e otimizacao de assets.
