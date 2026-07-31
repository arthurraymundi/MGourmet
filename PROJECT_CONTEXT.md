# PROJECT_CONTEXT.md

# MGourmet

## Visão Geral

MGourmet é um sistema web desenvolvido para uma empresa de marmitas congeladas fitness localizada em Jundiaí/SP.

O projeto encontra-se em fase final de desenvolvimento e será utilizado em produção por uma empresa real.

O objetivo desta etapa é finalizar o sistema preservando toda a arquitetura existente, implementando apenas melhorias incrementais de forma organizada, segura e consistente.

---

# Objetivos do Projeto

O sistema deve oferecer:

- Catálogo de produtos
- Carrinho de compras
- Checkout
- Integração com WhatsApp
- Painel Administrativo
- CRUD de Produtos
- Gestão de Pedidos
- Autenticação JWT
- Interface responsiva
- Boa experiência para clientes e administradores

---

# Stack Tecnológica

## Frontend

- React
- TypeScript

## Backend

- FastAPI
- SQLAlchemy

## Banco de Dados

- PostgreSQL

## Infraestrutura

- Docker Compose

---

# Arquitetura

Toda nova funcionalidade deve seguir obrigatoriamente a arquitetura já existente.

É proibido:

- alterar a estrutura do projeto sem necessidade;
- mover arquivos apenas por preferência;
- criar novas arquiteturas;
- duplicar componentes;
- duplicar serviços;
- criar lógica paralela para funcionalidades já existentes.

Sempre reutilize componentes, serviços, hooks, modelos e padrões já presentes no projeto.

---

# Dados Oficiais da Empresa

## Nome

MGourmet

---

## Logo Oficial

A logo oficial encontra-se dentro do projeto.

Ela representa a identidade visual oficial da empresa.

Utilize exatamente essa imagem.

Não gerar outra logo.

Não substituir por ícones.

Não modificar suas cores.

Caso seja necessário, apenas ajuste:

- tamanho;
- alinhamento;
- responsividade.

A logo deve aparecer em:

- Navbar
- Rodapé
- Login Administrativo
- Dashboard Administrativo
- Favicon (quando possível)

---

## Contato

Telefone:

+55 11 97670-2164

WhatsApp:

+55 11 97670-2164

Email:

marlania.raymundi2@gmail.com

---

## Redes Sociais

Instagram

https://www.instagram.com/mgourmet_comidafit.ofc/

TikTok

https://www.tiktok.com/@mgourmet1

---

## Área de Atendimento

Entregas em:

Jundiaí - SP

Sempre que houver informações institucionais, mencionar que a MGourmet realiza entregas em Jundiaí/SP.

---

# Centralização das Informações

Todas as informações institucionais devem ser centralizadas em um único local da aplicação.

Nenhum destes dados deve permanecer espalhado pelo código:

- nome da empresa;
- telefone;
- WhatsApp;
- email;
- Instagram;
- TikTok;
- endereço;
- área de atendimento.

Todo componente deve consumir essas informações a partir da configuração centralizada.

---

# Diretrizes de Desenvolvimento

Toda implementação deve priorizar:

- simplicidade;
- estabilidade;
- legibilidade;
- reutilização;
- escalabilidade;
- baixo acoplamento;
- alta coesão.

Evite:

- código morto;
- duplicação;
- componentes gigantes;
- lógica repetida;
- imports desnecessários;
- hardcodes;
- refatorações desnecessárias.

---

# Experiência do Usuário

Toda alteração deve manter uma experiência moderna e consistente.

Sempre considerar:

- carregamentos (loading);
- mensagens de sucesso;
- mensagens de erro;
- estados vazios;
- confirmação para ações destrutivas;
- feedback visual;
- responsividade.

---

# Compatibilidade

Após qualquer alteração, garantir que continuam funcionando:

- Frontend
- Backend
- API
- Banco de Dados
- Docker
- Login
- Painel Administrativo
- CRUD de Produtos
- Gestão de Pedidos
- Checkout
- Carrinho
- Integração com WhatsApp

Nenhuma funcionalidade existente pode ser quebrada.

---

# Qualidade do Código

Antes de finalizar qualquer implementação, revisar:

- erros de tipagem;
- imports não utilizados;
- componentes duplicados;
- código duplicado;
- rotas quebradas;
- problemas de responsividade;
- warnings;
- possíveis bugs.

---

# Critério de Conclusão

Uma tarefa somente poderá ser considerada concluída quando:

- todas as funcionalidades existentes continuarem funcionando;
- todas as novas funcionalidades estiverem implementadas;
- a arquitetura original tiver sido preservada;
- o projeto permanecer consistente visualmente;
- não existirem erros de compilação;
- não existirem erros de tipagem;
- todas as alterações seguirem os padrões já existentes no projeto.

A estabilidade da aplicação é prioridade máxima.