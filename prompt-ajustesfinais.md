# Objetivo

Este documento define as regras obrigatórias para a implementação das melhorias finais do projeto MGourmet.

Antes de escrever qualquer código, o agente deve compreender completamente a arquitetura existente. A prioridade é preservar a estabilidade do sistema, reutilizar componentes existentes e evitar qualquer alteração desnecessária.

Este documento deve ser seguido durante toda a implementação.

# MGourmet — Análise Completa e Implementação das Melhorias Finais

Você está assumindo o desenvolvimento de um projeto já existente chamado **MGourmet**.

Este projeto já está funcional e **NÃO deve ser refatorado desnecessariamente**.

Seu objetivo é compreender completamente a arquitetura existente e implementar apenas as melhorias solicitadas, preservando todo o restante do sistema.

---

# REGRAS IMPORTANTES

Antes de qualquer alteração:

* Leia completamente o projeto.
* Entenda toda a arquitetura.
* Entenda o fluxo da aplicação.
* Reutilize componentes existentes.
* Respeite os padrões de código já utilizados.
* Não crie uma nova arquitetura.
* Não mova arquivos sem necessidade.
* Não renomeie arquivos apenas por preferência.
* Não altere endpoints existentes sem necessidade.
* Não modifique regras de negócio já funcionando.
* Não faça otimizações prematuras.
* Não remova funcionalidades existentes.
* Não faça commits.
* Não gere código antes da análise.

O objetivo é realizar mudanças pequenas, limpas e consistentes.

---

# ETAPA 1 — RECONHECIMENTO DO PROJETO

Analise completamente:

## Estrutura

* organização das pastas
* front-end
* back-end
* banco
* docker
* autenticação
* painel administrativo

---

## Front-end

Identifique:

* componentes reutilizados
* layout
* navbar
* footer
* dashboard
* páginas
* gerenciamento de estado
* serviços
* rotas

---

## Back-end

Analise:

* estrutura FastAPI
* routers
* models
* schemas
* services
* repositories
* autenticação
* middleware
* validações

---

## Banco

Liste:

* todas as tabelas
* relacionamentos
* enums
* migrations

---

## Dashboard Administrativo

Explique:

* como funciona
* como os pedidos são carregados
* como os produtos são gerenciados
* como ocorre a autenticação
* como o dashboard é organizado

---

## API

Liste todos os endpoints existentes.

---

## Fluxo da aplicação

Explique completamente:

Home

↓

Cardápio

↓

Carrinho

↓

Checkout

↓

Banco

↓

WhatsApp

↓

Dashboard

---

## Após a análise

Gere um relatório contendo:

* arquitetura
* pontos fortes
* possíveis melhorias
* arquivos que serão modificados
* justificativa de cada alteração

NÃO ESCREVA CÓDIGO AINDA.

---

# ETAPA 2 — IMPLEMENTAÇÃO

Após concluir a análise, implemente as melhorias abaixo.

---

## 1. Logo da M Gourmet

Adicionar suporte completo para a logo.

A logo deve aparecer em:

* Navbar
* Rodapé
* Login Administrativo
* Dashboard
* Favicon (caso exista suporte)

Caso exista uma pasta de assets, reutilize-a.

Não criar duplicação de imagens.

---

## 2. Centralização das informações da empresa

Criar um único local responsável pelas informações institucionais.

Centralizar:

* nome da empresa
* WhatsApp
* telefone
* Instagram
* TikTok
* Facebook (caso exista)
* email
* endereço (caso exista)

Todo o projeto deve consumir essas informações desse único local.

Nunca deixar números ou links espalhados pelo código.

---

## 3. Atualização das redes sociais

Trocar todos os links antigos.

Todos os botões da aplicação devem utilizar os novos dados centralizados.

---

## 4. Exclusão de pedidos

Adicionar um botão:

Excluir Pedido

No Dashboard Administrativo.

Antes da exclusão:

abrir confirmação.

Exemplo:

Deseja realmente excluir este pedido?

Cancelar

Excluir

Após excluir:

* atualizar lista
* remover do banco
* exibir mensagem de sucesso

---

## 5. Cadastro manual de pedidos

Adicionar:

Novo Pedido

no Dashboard.

Esse formulário deverá permitir cadastrar pedidos feitos por:

* telefone
* WhatsApp
* atendimento presencial

Campos:

Nome

Telefone

Produtos

Quantidade

Observações

Forma de pagamento

Status

Valor total

O pedido deverá utilizar exatamente a mesma estrutura utilizada pelos pedidos normais.

Não criar uma segunda lógica.

---

## 6. Melhorias do Dashboard

Adicionar indicadores.

Exemplo:

Pedidos Hoje

Pedidos Pendentes

Pedidos Finalizados

Faturamento do Dia

Total de Pedidos

Caso já exista estrutura semelhante, reutilize-a.

---

## 7. Filtros

## 7. Pesquisa e Filtros

Melhorar a gestão dos pedidos implementando:

- Pesquisa por nome do cliente.
- Pesquisa por telefone.
- Filtro por status:
  - Recebido
  - Preparando
  - Saiu para entrega
  - Finalizado
  - Cancelado

Os filtros devem ser rápidos, intuitivos e integrados à listagem existente, sem criar uma nova tela ou duplicar funcionalidades.

---

## 8. UX

Melhorar pequenas experiências do painel.

Exemplos:

Loading

Mensagens de sucesso

Mensagens de erro

Confirmações

Botões desabilitados durante requisições

Feedback visual

Sem alterar o design original.

---

## 9. Código

Todo código novo deve:

seguir o padrão existente

ser tipado

ser reutilizável

ter nomes claros

evitar duplicação

respeitar SOLID quando fizer sentido

não gerar código morto

não criar arquivos desnecessários

---

## 10. Compatibilidade

Garantir que:

Docker continue funcionando.

Banco continue funcionando.

API continue funcionando.

Front continue funcionando.

Dashboard continue funcionando.

Login continue funcionando.

Carrinho continue funcionando.

Checkout continue funcionando.

WhatsApp continue funcionando.

---

# ETAPA 3 — VALIDAÇÃO

Ao finalizar:

Revise todas as alterações.

Procure possíveis bugs.

Procure imports não utilizados.

Procure código duplicado.

Procure componentes repetidos.

Procure rotas quebradas.

Procure erros de tipagem.

Procure problemas de responsividade.

Verifique consistência visual.

Confirme que nenhuma funcionalidade existente foi quebrada.

---

# ENTREGA

Ao finalizar, apresente um relatório contendo:

* arquivos modificados
* motivo de cada alteração
* funcionalidades implementadas
* possíveis melhorias futuras
* testes recomendados

Somente considere a tarefa concluída quando todas as funcionalidades existentes permanecerem funcionando e todas as novas funcionalidades estiverem implementadas seguindo a arquitetura atual do projeto.
