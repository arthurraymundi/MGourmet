import { Suspense, lazy } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'
import { SiteLayout } from '@/components/layout/site-layout'
import { AdminLayout } from '@/features/admin/components/admin-layout'
import { RequireAdmin } from '@/features/admin/components/require-admin'

const HomePage = lazy(() => import('@/features/home/pages/home-page'))
const AboutPage = lazy(() => import('@/features/about/pages/about-page'))
const MenuPage = lazy(() => import('@/features/menu/pages/menu-page'))
const KitsPage = lazy(() => import('@/features/kits/pages/kits-page'))
const ContactPage = lazy(() => import('@/features/contact/pages/contact-page'))
const AdminLoginPage = lazy(() => import('@/features/admin/pages/admin-login-page'))
const AdminDashboardPage = lazy(() => import('@/features/admin/pages/admin-dashboard-page'))
const AdminProductsPage = lazy(() => import('@/features/admin/pages/admin-products-page'))
const AdminOrdersPage = lazy(() => import('@/features/admin/pages/admin-orders-page'))

export function AppRouter() {
  return <Suspense fallback={<div className="p-8 text-center text-sm">Carregando...</div>}><Routes>
    <Route element={<SiteLayout />}><Route path="/" element={<HomePage />} /><Route path="/sobre" element={<AboutPage />} /><Route path="/cardapio" element={<MenuPage />} /><Route path="/kits" element={<KitsPage />} /><Route path="/contato" element={<ContactPage />} /></Route>
    <Route path="/admin/login" element={<AdminLoginPage />} />
    <Route element={<RequireAdmin />}><Route path="/admin" element={<AdminLayout />}><Route index element={<AdminDashboardPage />} /><Route path="produtos" element={<AdminProductsPage />} /><Route path="pedidos" element={<AdminOrdersPage />} /></Route></Route>
    <Route path="*" element={<Navigate to="/" replace />} />
  </Routes></Suspense>
}
