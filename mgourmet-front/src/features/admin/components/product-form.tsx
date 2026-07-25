import { useState, type FormEvent, type ReactNode } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import type { Product, ProductCategory } from '@/types/domain'
import type { ProductPayload } from '../services/admin-product-service'

const categories: ProductCategory[] = ['Hiperproteica', 'Low Carb', 'Emagrecimento', 'Ganho de Massa', 'Vegetariana', 'Prato Fitness', 'Mini Prato Fitness', 'Prato Kids', 'Sopa', 'Proteína', 'Premium']

interface ProductFormProps {
  product?: Product | null
  isSaving: boolean
  onCancel: () => void
  onSubmit: (payload: ProductPayload) => Promise<void>
}

function createInitialValues(product?: Product | null): ProductPayload {
  return {
    name: product?.name ?? '', description: product?.description ?? '', imageUrl: product?.imageUrl ?? '', price: product?.price ?? 0,
    category: product?.category ?? 'Prato Fitness', ingredients: product?.ingredients ?? [], nutrition: product?.nutrition ?? { calories: 0, protein: 0, carbs: 0, fat: 0 }, featured: product?.featured ?? false, isAvailable: product?.isAvailable ?? true,
  }
}

export function ProductForm({ product, isSaving, onCancel, onSubmit }: ProductFormProps) {
  const [values, setValues] = useState(() => createInitialValues(product))
  const [error, setError] = useState<string | null>(null)

  function update<Field extends keyof ProductPayload>(field: Field, value: ProductPayload[Field]) { setValues((current) => ({ ...current, [field]: value })) }
  function updateNutrition(field: keyof ProductPayload['nutrition'], value: number) { setValues((current) => ({ ...current, nutrition: { ...current.nutrition, [field]: value } })) }
  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (values.ingredients.length === 0) { setError('Informe ao menos um ingrediente.'); return }
    setError(null)
    try { await onSubmit(values) } catch (submissionError) { setError(submissionError instanceof Error ? submissionError.message : 'Não foi possível salvar o produto.') }
  }

  return <form className="space-y-4" onSubmit={submit}>
    <div className="grid gap-4 md:grid-cols-2">
      <Field label="Nome"><Input value={values.name} required onChange={(event) => update('name', event.target.value)} /></Field>
      <Field label="Categoria"><select className="h-11 w-full rounded-xl border border-[var(--color-border)] px-3 text-sm" value={values.category} onChange={(event) => update('category', event.target.value as ProductCategory)}>{categories.map((category) => <option key={category}>{category}</option>)}</select></Field>
      <Field label="Preço"><Input type="number" min="0" step="0.01" value={values.price} required onChange={(event) => update('price', Number(event.target.value))} /></Field>
      <Field label="URL da imagem"><Input type="url" value={values.imageUrl} required onChange={(event) => update('imageUrl', event.target.value)} /></Field>
      <Field label="Ingredientes (separados por vírgula)" className="md:col-span-2"><Input value={values.ingredients.join(', ')} required onChange={(event) => update('ingredients', event.target.value.split(',').map((item) => item.trim()).filter(Boolean))} /></Field>
      <Field label="Descrição" className="md:col-span-2"><textarea className="min-h-24 w-full rounded-xl border border-[var(--color-border)] px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--color-primary-500)]" value={values.description} required onChange={(event) => update('description', event.target.value)} /></Field>
      {(['calories', 'protein', 'carbs', 'fat'] as const).map((field) => <Field key={field} label={{ calories: 'Calorias', protein: 'Proteínas', carbs: 'Carboidratos', fat: 'Gorduras' }[field]}><Input type="number" min="0" value={values.nutrition[field]} required onChange={(event) => updateNutrition(field, Number(event.target.value))} /></Field>)}
    </div>
    <div className="flex flex-wrap gap-5 text-sm"><label className="flex items-center gap-2"><input type="checkbox" checked={values.isAvailable} onChange={(event) => update('isAvailable', event.target.checked)} /> Disponível no cardápio</label><label className="flex items-center gap-2"><input type="checkbox" checked={values.featured} onChange={(event) => update('featured', event.target.checked)} /> Produto em destaque</label></div>
    {error ? <p className="text-sm text-red-600" role="alert">{error}</p> : null}
    <div className="flex justify-end gap-3"><Button type="button" variant="outline" onClick={onCancel}>Cancelar</Button><Button type="submit" disabled={isSaving}>{isSaving ? 'Salvando...' : 'Salvar produto'}</Button></div>
  </form>
}

function Field({ label, className, children }: { label: string; className?: string; children: ReactNode }) {
  return <label className={`block space-y-1 ${className ?? ''}`}><span className="text-sm font-medium">{label}</span>{children}</label>
}
