const BRL_FORMATTER = new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL',
})

export function formatCurrency(value: number) {
  return BRL_FORMATTER.format(value)
}

export function formatCurrencyForMessage(value: number) {
  return BRL_FORMATTER.format(value).replace(/\u00a0/g, ' ')
}
