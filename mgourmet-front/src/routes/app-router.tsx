import { Suspense, lazy } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'
import { SiteLayout } from '@/components/layout/site-layout'

const HomePage = lazy(() => import('@/features/home/pages/home-page'))
const AboutPage = lazy(() => import('@/features/about/pages/about-page'))
const MenuPage = lazy(() => import('@/features/menu/pages/menu-page'))
const KitsPage = lazy(() => import('@/features/kits/pages/kits-page'))
const ContactPage = lazy(() => import('@/features/contact/pages/contact-page'))

export function AppRouter() {
  return (
    <Suspense fallback={<div className="p-8 text-center text-sm">Carregando...</div>}>
      <Routes>
        <Route element={<SiteLayout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/sobre" element={<AboutPage />} />
          <Route path="/cardapio" element={<MenuPage />} />
          <Route path="/kits" element={<KitsPage />} />
          <Route path="/contato" element={<ContactPage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </Suspense>
  )
}
