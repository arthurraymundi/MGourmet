import { useState, type FormEvent, type ReactNode } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import type { CustomerDetails } from '@/types/domain'

const initialCustomer: CustomerDetails = {
  name: '', phone: '', deliveryMethod: 'pickup', street: '', number: '', neighborhood: '', complement: '', notes: '',
}

interface CheckoutFormProps {
  disabled: boolean
  isSubmitting: boolean
  onSubmit: (customer: CustomerDetails) => Promise<void>
}

export function CheckoutForm({ disabled, isSubmitting, onSubmit }: CheckoutFormProps) {
  const [customer, setCustomer] = useState<CustomerDetails>(initialCustomer)
  const [errors, setErrors] = useState<Partial<Record<keyof CustomerDetails, string>>>({})

  function updateField<Field extends keyof CustomerDetails>(field: Field, value: CustomerDetails[Field]) {
    setCustomer((current) => ({ ...current, [field]: value }))
    setErrors((current) => ({ ...current, [field]: undefined }))
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const nextErrors: Partial<Record<keyof CustomerDetails, string>> = {}
    if (!customer.name.trim()) nextErrors.name = 'Informe seu nome.'
    if (!customer.phone.trim()) nextErrors.phone = 'Informe seu telefone.'
    if (customer.deliveryMethod === 'delivery') {
      if (!customer.street.trim()) nextErrors.street = 'Informe sua rua.'
      if (!customer.number.trim()) nextErrors.number = 'Informe o número.'
      if (!customer.neighborhood.trim()) nextErrors.neighborhood = 'Informe o bairro.'
    }
    setErrors(nextErrors)
    if (Object.keys(nextErrors).length === 0) await onSubmit(customer)
  }

  return (
    <form className="space-y-4 border-t border-[var(--color-border)] pt-5" onSubmit={handleSubmit} noValidate>
      <h3 className="font-semibold">Seus dados</h3>
      <FormField label="Nome" error={errors.name}>
        <Input value={customer.name} onChange={(event) => updateField('name', event.target.value)} aria-invalid={Boolean(errors.name)} />
      </FormField>
      <FormField label="Telefone" error={errors.phone}>
        <Input type="tel" value={customer.phone} onChange={(event) => updateField('phone', event.target.value)} aria-invalid={Boolean(errors.phone)} />
      </FormField>
      <fieldset className="space-y-2">
        <legend className="text-sm font-medium">Forma de entrega</legend>
        <div className="flex gap-4 text-sm">
          <label className="flex items-center gap-2"><input type="radio" checked={customer.deliveryMethod === 'pickup'} onChange={() => updateField('deliveryMethod', 'pickup')} /> Retirada</label>
          <label className="flex items-center gap-2"><input type="radio" checked={customer.deliveryMethod === 'delivery'} onChange={() => updateField('deliveryMethod', 'delivery')} /> Entrega</label>
        </div>
      </fieldset>
      {customer.deliveryMethod === 'delivery' ? (
        <div className="grid gap-4 sm:grid-cols-2">
          <FormField label="Rua" error={errors.street} className="sm:col-span-2"><Input value={customer.street} onChange={(event) => updateField('street', event.target.value)} aria-invalid={Boolean(errors.street)} /></FormField>
          <FormField label="Número" error={errors.number}><Input value={customer.number} onChange={(event) => updateField('number', event.target.value)} aria-invalid={Boolean(errors.number)} /></FormField>
          <FormField label="Bairro" error={errors.neighborhood}><Input value={customer.neighborhood} onChange={(event) => updateField('neighborhood', event.target.value)} aria-invalid={Boolean(errors.neighborhood)} /></FormField>
          <FormField label="Complemento (opcional)" className="sm:col-span-2"><Input value={customer.complement} onChange={(event) => updateField('complement', event.target.value)} /></FormField>
        </div>
      ) : null}
      <FormField label="Observações (opcional)">
        <textarea className="min-h-20 w-full rounded-xl border border-[var(--color-border)] bg-white px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-primary-500)]" value={customer.notes} onChange={(event) => updateField('notes', event.target.value)} />
      </FormField>
      <Button className="w-full" type="submit" disabled={disabled || isSubmitting}>{isSubmitting ? 'Salvando pedido...' : 'Finalizar pedido pelo WhatsApp'}</Button>
      {disabled ? <p className="text-center text-sm text-[var(--color-text-secondary)]" role="status">Adicione produtos ao carrinho para continuar.</p> : null}
    </form>
  )
}

function FormField({ label, error, className, children }: { label: string; error?: string; className?: string; children: ReactNode }) {
  return <label className={`block space-y-1 ${className ?? ''}`}><span className="text-sm font-medium">{label}</span>{children}{error ? <span className="block text-xs text-red-600" role="alert">{error}</span> : null}</label>
}
