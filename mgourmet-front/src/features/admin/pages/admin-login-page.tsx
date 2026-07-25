import { useState, type FormEvent } from 'react'
import { Navigate, useNavigate } from 'react-router-dom'
import { Card } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useAdminAuth } from '../hooks/use-admin-auth'

export default function AdminLoginPage() {
  const { admin, isLoading, login } = useAdminAuth()
  const navigate = useNavigate()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)
  if (!isLoading && admin) return <Navigate to="/admin" replace />
  async function submit(event: FormEvent<HTMLFormElement>) { event.preventDefault(); try { setIsSubmitting(true); setError(null); await login(email, password); navigate('/admin', { replace: true }) } catch (loginError) { setError(loginError instanceof Error ? loginError.message : 'Não foi possível entrar.') } finally { setIsSubmitting(false) } }
  return <main className="grid min-h-screen place-items-center bg-[var(--color-bg-subtle)] p-4"><Card className="w-full max-w-md"><div className="mb-6"><p className="text-xl font-semibold">M Gourmet</p><h1 className="mt-2 text-2xl font-semibold">Acessar administração</h1><p className="mt-2 text-sm text-[var(--color-text-secondary)]">Use suas credenciais de administrador.</p></div><form className="space-y-4" onSubmit={submit}><label className="block space-y-1"><span className="text-sm font-medium">E-mail</span><Input type="email" value={email} required onChange={(event) => setEmail(event.target.value)} /></label><label className="block space-y-1"><span className="text-sm font-medium">Senha</span><Input type="password" value={password} required onChange={(event) => setPassword(event.target.value)} /></label>{error ? <p className="text-sm text-red-600" role="alert">{error}</p> : null}<Button className="w-full" type="submit" disabled={isSubmitting || isLoading}>{isSubmitting ? 'Entrando...' : 'Entrar'}</Button></form></Card></main>
}
