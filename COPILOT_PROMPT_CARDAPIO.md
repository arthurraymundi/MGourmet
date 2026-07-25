🚀 MGourmet — FASE 3
Sistema Completo de Pedidos via WhatsApp
CONTEXTO

O projeto MGourmet já possui uma arquitetura consolidada.

Backend:

FastAPI
SQLAlchemy
PostgreSQL
API de Produtos concluída

Frontend:

React
TypeScript
React Router
TailwindCSS
Cardápio integrado ao backend
ProductCard existente
Hook de filtros existente
Serviço de produtos existente
Build funcionando
Responsividade funcionando

Esta etapa NÃO altera o backend.

O objetivo é transformar o cardápio em um sistema completo de pedidos via WhatsApp.

O pedido será totalmente montado no frontend.

Nenhum pagamento será implementado nesta fase.

REGRAS OBRIGATÓRIAS

NÃO alterar arquitetura.

NÃO instalar dependências.

NÃO remover arquivos.

NÃO criar componentes duplicados.

NÃO modificar backend.

NÃO modificar migrations.

NÃO modificar seed.

NÃO modificar Docker.

NÃO modificar Git.

NÃO criar submodules.

NÃO alterar APIs existentes.

Reutilizar ao máximo:

ProductCard
Button
Card
Input
Layout existente

Caso seja necessário criar novos componentes, criar apenas quando realmente não existir equivalente reutilizável.

Todo código deve seguir o padrão atual do projeto.

FASE 1 — ANÁLISE (NÃO IMPLEMENTAR)

Antes de escrever qualquer código:

Analisar completamente o frontend.

Identificar:

quais arquivos serão alterados;
quais novos arquivos realmente precisam existir;
onde ficará o estado do carrinho;
como persistir o carrinho;
onde ficará o resumo do pedido;
como reutilizar o ProductCard;
como evitar renderizações desnecessárias;
como manter o código escalável.

Também explicar:

Por que cada decisão foi tomada.

Ao final apresentar um plano de implementação.

Não alterar nenhum arquivo.

Aguardar aprovação.

FASE 2 — IMPLEMENTAÇÃO
ETAPA 1 — Arquitetura do Carrinho

Criar um carrinho desacoplado da página.

Utilizar Context API do React.

O contexto deve encapsular toda a lógica do carrinho.

Responsabilidades:

adicionar produto
remover produto
incrementar quantidade
decrementar quantidade
limpar carrinho
calcular subtotal
calcular total
persistir automaticamente

Evitar lógica espalhada entre componentes.

ETAPA 2 — Persistência

Persistir automaticamente utilizando localStorage.

Ao abrir o site novamente:

o carrinho deve ser restaurado.

Caso o localStorage esteja inválido:

ignorar os dados corrompidos sem quebrar a aplicação.

ETAPA 3 — ProductCard

Reutilizar o ProductCard existente.

Adicionar controles:

[-] quantidade [+]

Enquanto quantidade = 0:

mostrar botão "Adicionar".

Após adicionar:

substituir pelo seletor de quantidade.

Atualizar instantaneamente o carrinho.

Não duplicar ProductCard.

ETAPA 4 — Resumo do Pedido

Desktop:

Painel lateral fixo.

Mobile:

Drawer responsivo.

Mostrar:

imagem

nome

preço unitário

quantidade

subtotal

valor total

Permitir:

incrementar

decrementar

remover

limpar carrinho

Caso vazio:

mostrar estado vazio amigável.

ETAPA 5 — Dados do Cliente

Antes do envio solicitar:

Nome

Telefone

Forma de entrega

Opções:

Retirada

Entrega

Caso Entrega:

Rua

Número

Bairro

Complemento (opcional)

Observações (opcional)

Validações:

Nome obrigatório.

Telefone obrigatório.

Se entrega:

Rua obrigatória.

Número obrigatório.

Bairro obrigatório.

ETAPA 6 — Geração do Pedido

Gerar automaticamente uma mensagem organizada.

Formato:

Olá!

Gostaria de fazer um pedido.

======================

Nome:
Arthur

Telefone:
(11) 99999-9999

Forma de entrega:
Entrega

Endereço:

Rua XX
Número 100
Bairro Centro

======================

Pedido

2x Marmita Fitness Frango .......... R$56,00

1x Sopa de Legumes ................. R$22,00

======================

TOTAL

R$78,00

======================

Observações

Sem cebola.

Os valores devem ser formatados utilizando Intl.NumberFormat("pt-BR").

ETAPA 7 — WhatsApp

Criar utilitário responsável por gerar a URL.

Utilizar:

encodeURIComponent()

Abrir:

https://wa.me/55XXXXXXXXXXX?text=...

Não utilizar APIs.

Não enviar mensagens automaticamente.

Apenas abrir a conversa.

O número do WhatsApp deve ficar centralizado em uma constante para facilitar futuras alterações.

Caso o carrinho esteja vazio:

não permitir envio.

ETAPA 8 — UX

Após abrir o WhatsApp:

Perguntar:

"Deseja limpar o carrinho?"

Se confirmar:

limpar carrinho.

Caso contrário:

manter tudo.

Mostrar feedback visual para:

produto adicionado

produto removido

pedido vazio

campos obrigatórios

ETAPA 9 — Responsividade

Desktop

Produtos à esquerda.

Resumo fixo à direita.

Mobile

Botão flutuante do carrinho.

Badge mostrando quantidade.

Drawer ocupando boa parte da tela.

Todos os componentes devem continuar totalmente responsivos.

ETAPA 10 — Performance

Evitar renderizações desnecessárias.

Utilizar useMemo, useCallback e React.memo quando fizer sentido.

Evitar cálculos repetitivos.

Não realizar múltiplas leituras do localStorage.

ETAPA 11 — Qualidade

Código limpo.

Funções pequenas.

Boa separação de responsabilidades.

Comentários apenas quando realmente necessários.

Não gerar código morto.

Não deixar TODOs.

Não deixar console.log.

NÃO IMPLEMENTAR

Não implementar:

Pix
Mercado Pago
Stripe
PagSeguro
Cartão
Login
Cadastro
Área do Cliente
Painel Administrativo
Histórico de Pedidos
Banco de Dados
Backend
APIs adicionais

O objetivo desta fase é exclusivamente um sistema de pedidos via WhatsApp.

VALIDAÇÃO

Ao finalizar validar:

adicionar produto
remover produto
alterar quantidade
persistência
restauração do carrinho
geração da mensagem
abertura do WhatsApp
cálculo do total
validação dos campos
layout desktop
layout mobile
npm run build

Não executar migrations.

Não executar seeds.

Não alterar backend.

RELATÓRIO FINAL

Ao terminar:

Mostrar:

arquivos alterados;
motivo de cada alteração;
arquitetura utilizada;
confirmação de que nenhum arquivo do backend foi alterado;
confirmação de que nenhuma migration foi criada;
confirmação de que nenhum seed foi alterado;
confirmação de que nenhuma dependência foi instalada;
confirmação de que o build passou sem erros.

Não criar commits.

Aguardar minha aprovação antes de qualquer commit.