import { Outlet } from 'react-router-dom'
import { Footer } from './footer'
import { Navbar } from './navbar'
import { WhatsappFloat } from './whatsapp-float'

export function SiteLayout() {
  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <main className="flex-1">
        <Outlet />
      </main>
      <Footer />
      <WhatsappFloat />
    </div>
  )
}
