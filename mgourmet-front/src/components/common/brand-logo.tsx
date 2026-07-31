import logo from '@/assets/logo.png'
import { COMPANY } from '@/data/company'
import { cn } from '@/utils/cn'

interface BrandLogoProps {
  className?: string
}

export function BrandLogo({ className }: BrandLogoProps) {
  return <img src={logo} alt={COMPANY.name} className={cn('h-10 w-auto object-contain', className)} />
}
