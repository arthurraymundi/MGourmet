import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Container } from './container'

export function Hero() {
  return (
    <section className="bg-[var(--color-bg-subtle)] py-16 md:py-24">
      <Container className="grid items-center gap-10 md:grid-cols-2">
        <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.35 }}>
          <p className="mb-3 text-sm font-semibold uppercase tracking-widest text-orange-600">M Gourmet</p>
          <h1 className="text-4xl leading-tight font-semibold md:text-5xl">
            Marmitas fitness premium para sua rotina render mais.
          </h1>
          <p className="mt-4 max-w-xl text-base text-[var(--color-text-secondary)]">
            Alimentação saudável, prática e com alto padrão nutricional para treino, dieta e performance.
          </p>
          <div className="mt-6 flex flex-wrap gap-3">
            <Button asChild size="lg">
              <Link to="/cardapio">Ver cardápio</Link>
            </Button>
            <Button asChild variant="outline" size="lg">
              <Link to="/kits">Conhecer kits</Link>
            </Button>
          </div>
        </motion.div>
        <motion.img
          initial={{ opacity: 0, scale: 0.98 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.35 }}
          src="https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=1400&q=80"
          alt="Refeição fitness com legumes e proteína"
          className="h-80 w-full rounded-3xl object-cover md:h-[420px]"
          loading="eager"
        />
      </Container>
    </section>
  )
}
