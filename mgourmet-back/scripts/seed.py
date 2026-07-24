import asyncio
import logging
from dataclasses import dataclass
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.content.models import ContactInfo, ContentItem, ContentSection, Faq, Testimonial
from app.core.database import get_session_factory
from app.core.logging import configure_logging
from app.kit.models import Kit
from app.product.models import Product, ProductCategory

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ProductSeed:
    id: str
    name: str
    description: str
    image_url: str
    price: Decimal
    category: ProductCategory
    ingredients: list[str]
    calories: int
    protein: int
    carbs: int
    fat: int
    featured: bool = False


PRODUCTS = (
    ProductSeed(
        id="frango-grelhado-fit",
        name="Frango Grelhado com Arroz Integral",
        description="Peito de frango grelhado, arroz integral e legumes no vapor.",
        image_url="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("24.90"),
        category=ProductCategory.HIGH_PROTEIN,
        ingredients=["Frango", "Arroz integral", "Brócolis", "Cenoura", "Azeite"],
        calories=420,
        protein=38,
        carbs=39,
        fat=11,
        featured=True,
    ),
    ProductSeed(
        id="tilapia-low-carb",
        name="Tilápia Low Carb com Abobrinha",
        description="Tilápia assada com purê de couve-flor e abobrinha salteada.",
        image_url="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("27.90"),
        category=ProductCategory.LOW_CARB,
        ingredients=["Tilápia", "Couve-flor", "Abobrinha", "Alho", "Salsinha"],
        calories=360,
        protein=36,
        carbs=18,
        fat=15,
        featured=True,
    ),
    ProductSeed(
        id="patinho-emagrecimento",
        name="Patinho Magro com Mix de Vegetais",
        description="Patinho refogado com temperos naturais e vegetais coloridos.",
        image_url="https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("25.50"),
        category=ProductCategory.WEIGHT_LOSS,
        ingredients=["Patinho", "Abóbora", "Vagem", "Pimentão", "Cebola roxa"],
        calories=390,
        protein=35,
        carbs=27,
        fat=14,
    ),
    ProductSeed(
        id="massa-ganho",
        name="Frango com Batata-Doce Power",
        description="Prato energético para rotina intensa de treino.",
        image_url="https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("26.90"),
        category=ProductCategory.MUSCLE_GAIN,
        ingredients=["Frango desfiado", "Batata-doce", "Feijão", "Couve", "Azeite"],
        calories=520,
        protein=41,
        carbs=54,
        fat=13,
    ),
    ProductSeed(
        id="vegetariana-proteica",
        name="Bowl Vegetariano de Grão-de-Bico",
        description="Grão-de-bico, quinoa e legumes para alta saciedade.",
        image_url="https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("23.90"),
        category=ProductCategory.VEGETARIAN,
        ingredients=["Grão-de-bico", "Quinoa", "Abóbora", "Espinafre", "Tomate"],
        calories=410,
        protein=20,
        carbs=48,
        fat=14,
    ),
)

KITS = (
    Kit(id="kit-5", name="Kit 5", meals=5, original_price=Decimal("134.50"), discounted_price=Decimal("119.90")),
    Kit(id="kit-10", name="Kit 10", meals=10, original_price=Decimal("269.00"), discounted_price=Decimal("224.90")),
    Kit(id="kit-20", name="Kit 20", meals=20, original_price=Decimal("538.00"), discounted_price=Decimal("409.90")),
)

TESTIMONIALS = (
    Testimonial(
        id="1",
        name="Camila Rocha",
        role="Atleta amadora",
        quote="Economizei tempo e melhorei meu desempenho com refeições práticas e saborosas.",
    ),
    Testimonial(
        id="2",
        name="Diego Matos",
        role="Analista de TI",
        quote="A qualidade é excelente e me ajuda a manter a dieta na rotina corrida.",
    ),
)

FAQS = (
    Faq(
        id="1",
        question="As refeições chegam congeladas ou refrigeradas?",
        answer="As marmitas são entregues refrigeradas e prontas para armazenamento seguro.",
    ),
    Faq(
        id="2",
        question="Posso combinar categorias no mesmo pedido?",
        answer="Sim. Você pode misturar pratos de qualquer categoria e montar seu plano ideal.",
    ),
    Faq(
        id="3",
        question="Vocês atendem empresas?",
        answer="Sim. Temos planos corporativos para equipes com personalização de cardápio.",
    ),
)

CONTENT_ITEMS = (
    ContentItem(id="benefit-1", section=ContentSection.BENEFITS, text="Pratos balanceados por nutricionistas", position=0),
    ContentItem(id="benefit-2", section=ContentSection.BENEFITS, text="Entrega programada e pontual", position=1),
    ContentItem(id="benefit-3", section=ContentSection.BENEFITS, text="Ingredientes frescos e seleção premium", position=2),
    ContentItem(id="benefit-4", section=ContentSection.BENEFITS, text="Cardápio variado para objetivos diferentes", position=3),
    ContentItem(id="how-it-works-1", section=ContentSection.HOW_IT_WORKS, text="Escolha seus pratos ou kits", position=0),
    ContentItem(id="how-it-works-2", section=ContentSection.HOW_IT_WORKS, text="Monte seu pedido por objetivo", position=1),
    ContentItem(id="how-it-works-3", section=ContentSection.HOW_IT_WORKS, text="Receba em casa pronto para consumir", position=2),
)

CONTACT_INFO = ContactInfo(
    id="default",
    whatsapp="+55 (11) 98888-0000",
    instagram="@mgourmetfit",
    address="Rua Exemplo, 250 - São Paulo/SP",
    business_hours="Segunda a sábado, 08h às 19h",
)


async def add_if_absent(session: AsyncSession, entity: object, entity_id: str) -> bool:
    if await session.get(type(entity), entity_id) is not None:
        return False
    session.add(entity)
    return True


async def seed() -> int:
    """Insere o conteúdo inicial sem substituir alterações administrativas existentes."""
    created = 0
    async with get_session_factory()() as session:
        for seed_product in PRODUCTS:
            product = Product(**seed_product.__dict__)
            created += await add_if_absent(session, product, product.id)
        for kit in KITS:
            created += await add_if_absent(session, kit, kit.id)
        for testimonial in TESTIMONIALS:
            created += await add_if_absent(session, testimonial, testimonial.id)
        for faq in FAQS:
            created += await add_if_absent(session, faq, faq.id)
        for content_item in CONTENT_ITEMS:
            created += await add_if_absent(session, content_item, content_item.id)
        created += await add_if_absent(session, CONTACT_INFO, CONTACT_INFO.id)
        await session.commit()
    logger.info("Seed concluído", extra={"created_records": created})
    return created


def main() -> None:
    configure_logging()
    asyncio.run(seed())


if __name__ == "__main__":
    main()
