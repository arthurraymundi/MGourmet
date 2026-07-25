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
    ProductSeed(
        id="prato-fitness-panqueca-carne",
        name="Panqueca de Carne",
        description="Panqueca integral recheada com carne bovina magra e molho de tomate caseiro.",
        image_url="https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Carne bovina", "Massa integral", "Tomate", "Cebola", "Salsinha"],
        calories=390, protein=31, carbs=38, fat=13,
    ),
    ProductSeed(
        id="prato-fitness-picadinho-carne-legumes-arroz",
        name="Picadinho de Carne com Legumes e Arroz",
        description="Picadinho de patinho com legumes frescos e arroz integral.",
        image_url="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Patinho", "Arroz integral", "Cenoura", "Abobrinha", "Vagem"],
        calories=430, protein=34, carbs=45, fat=12,
    ),
    ProductSeed(
        id="prato-fitness-bife-acebolado-quibebe-arroz-ervilha",
        name="Bife Acebolado, Quibebe de Mandioca e Arroz com Ervilha",
        description="Bife acebolado com quibebe cremoso de mandioca e arroz com ervilhas.",
        image_url="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Bife bovino", "Cebola", "Mandioca", "Arroz", "Ervilha"],
        calories=460, protein=33, carbs=52, fat=14,
    ),
    ProductSeed(
        id="prato-fitness-bolo-carne-pure-batata-cenoura",
        name="Bolo de Carne Assado com Purê de Batata e Cenoura",
        description="Bolo de carne assado com tomate e queijo, purê de batata e cenoura.",
        image_url="https://images.unsplash.com/photo-1574484284002-952d92456975?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Carne moída", "Tomate", "Queijo", "Batata", "Cenoura"],
        calories=440, protein=32, carbs=41, fat=17,
    ),
    ProductSeed(
        id="prato-fitness-feijoada-magra-arroz-couve",
        name="Feijoada Magra, Arroz e Couve",
        description="Feijoada preparada com cortes magros, arroz e couve refogada.",
        image_url="https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Feijão preto", "Carne magra", "Arroz", "Couve", "Alho"],
        calories=480, protein=29, carbs=55, fat=16,
    ),
    ProductSeed(
        id="prato-fitness-frango-empanado-creme-milho-arroz",
        name="Frango Empanado, Creme de Milho e Arroz",
        description="Frango assado empanado com creme de milho e arroz integral.",
        image_url="https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Frango", "Farinha integral", "Milho", "Leite", "Arroz integral"],
        calories=450, protein=36, carbs=49, fat=12,
    ),
    ProductSeed(
        id="prato-fitness-frango-xadrez-arroz-brocolis",
        name="Frango Xadrez e Arroz de Brócolis",
        description="Frango xadrez com pimentões, legumes e arroz de brócolis.",
        image_url="https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Frango", "Pimentão", "Brócolis", "Arroz", "Cebola"],
        calories=410, protein=35, carbs=43, fat=11,
    ),
    ProductSeed(
        id="prato-fitness-galinhada-fit",
        name="Galinhada Fit",
        description="Sobrecoxa de frango com arroz, cenoura e milho.",
        image_url="https://images.unsplash.com/photo-1598514982901-ae6273a2f8e8?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Sobrecoxa de frango", "Arroz", "Cenoura", "Milho", "Açafrão"],
        calories=470, protein=32, carbs=50, fat=15,
    ),
    ProductSeed(
        id="prato-fitness-frango-desfiado-pure-grao-de-bico",
        name="Frango Desfiado e Purê de Grão-de-Bico",
        description="Frango desfiado temperado com purê cremoso de grão-de-bico.",
        image_url="https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Frango", "Grão-de-bico", "Alho", "Limão", "Salsinha"],
        calories=400, protein=38, carbs=32, fat=12,
    ),
    ProductSeed(
        id="prato-fitness-moqueca-peixe-arroz-banana-terra",
        name="Moqueca de Peixe, Arroz e Banana-da-Terra",
        description="Moqueca leve de peixe com arroz e banana-da-terra assada.",
        image_url="https://images.unsplash.com/photo-1544943910-4c1dc44aab44?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_FITNESS,
        ingredients=["Peixe", "Leite de coco", "Pimentão", "Arroz", "Banana-da-terra"],
        calories=460, protein=30, carbs=48, fat=16,
    ),
    ProductSeed(
        id="mini-prato-fitness-panqueca-carne",
        name="Mini Panqueca de Carne",
        description="Porção reduzida de panqueca integral recheada com carne magra.",
        image_url="https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Carne bovina", "Massa integral", "Tomate", "Cebola"],
        calories=260, protein=21, carbs=25, fat=9,
    ),
    ProductSeed(
        id="mini-prato-fitness-picadinho-carne-legumes-arroz",
        name="Mini Picadinho de Carne com Legumes e Arroz",
        description="Porção reduzida de picadinho de patinho com legumes e arroz integral.",
        image_url="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Patinho", "Arroz integral", "Cenoura", "Abobrinha"],
        calories=285, protein=23, carbs=30, fat=8,
    ),
    ProductSeed(
        id="mini-prato-fitness-bife-acebolado-quibebe-arroz-ervilha",
        name="Mini Bife Acebolado, Quibebe e Arroz com Ervilha",
        description="Porção reduzida de bife acebolado com quibebe e arroz.",
        image_url="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Bife bovino", "Cebola", "Mandioca", "Arroz", "Ervilha"],
        calories=300, protein=22, carbs=34, fat=9,
    ),
    ProductSeed(
        id="mini-prato-fitness-bolo-carne-pure-batata-cenoura",
        name="Mini Bolo de Carne com Purê de Batata e Cenoura",
        description="Porção reduzida de bolo de carne assado com purê e cenoura.",
        image_url="https://images.unsplash.com/photo-1574484284002-952d92456975?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Carne moída", "Tomate", "Queijo", "Batata", "Cenoura"],
        calories=290, protein=21, carbs=27, fat=11,
    ),
    ProductSeed(
        id="mini-prato-fitness-feijoada-magra-arroz-couve",
        name="Mini Feijoada Magra, Arroz e Couve",
        description="Porção reduzida de feijoada com carnes magras, arroz e couve.",
        image_url="https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Feijão preto", "Carne magra", "Arroz", "Couve"],
        calories=310, protein=19, carbs=36, fat=10,
    ),
    ProductSeed(
        id="mini-prato-fitness-frango-empanado-creme-milho-arroz",
        name="Mini Frango Empanado, Creme de Milho e Arroz",
        description="Porção reduzida de frango empanado assado com creme de milho.",
        image_url="https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Frango", "Farinha integral", "Milho", "Arroz integral"],
        calories=295, protein=24, carbs=32, fat=8,
    ),
    ProductSeed(
        id="mini-prato-fitness-frango-xadrez-arroz-brocolis",
        name="Mini Frango Xadrez e Arroz de Brócolis",
        description="Porção reduzida de frango xadrez com arroz de brócolis.",
        image_url="https://images.unsplash.com/photo-1603133872878-684f208fb84b?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Frango", "Pimentão", "Brócolis", "Arroz"],
        calories=270, protein=23, carbs=28, fat=7,
    ),
    ProductSeed(
        id="mini-prato-fitness-galinhada-fit",
        name="Mini Galinhada Fit",
        description="Porção reduzida de galinhada com cenoura e milho.",
        image_url="https://images.unsplash.com/photo-1598514982901-ae6273a2f8e8?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Sobrecoxa de frango", "Arroz", "Cenoura", "Milho"],
        calories=315, protein=21, carbs=34, fat=10,
    ),
    ProductSeed(
        id="mini-prato-fitness-frango-desfiado-pure-grao-de-bico",
        name="Mini Frango Desfiado e Purê de Grão-de-Bico",
        description="Porção reduzida de frango desfiado com purê de grão-de-bico.",
        image_url="https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Frango", "Grão-de-bico", "Alho", "Salsinha"],
        calories=265, protein=25, carbs=21, fat=8,
    ),
    ProductSeed(
        id="mini-prato-fitness-moqueca-peixe-arroz-banana-terra",
        name="Mini Moqueca de Peixe, Arroz e Banana-da-Terra",
        description="Porção reduzida de moqueca leve de peixe com arroz e banana-da-terra.",
        image_url="https://images.unsplash.com/photo-1544943910-4c1dc44aab44?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("20.00"), category=ProductCategory.MINI_PRATO_FITNESS,
        ingredients=["Peixe", "Leite de coco", "Arroz", "Banana-da-terra"],
        calories=305, protein=20, carbs=33, fat=10,
    ),
    ProductSeed(
        id="prato-kids-strogonoff-frango-arroz-pure-batata",
        name="Strogonoff de Frango, Arroz Branco e Purê de Batata",
        description="Strogonoff suave de frango com arroz branco e purê de batata.",
        image_url="https://images.unsplash.com/photo-1604908176997-43101d4b1d7e?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_KIDS,
        ingredients=["Frango", "Creme de leite", "Arroz branco", "Batata", "Cenoura"],
        calories=480, protein=28, carbs=57, fat=15,
    ),
    ProductSeed(
        id="prato-kids-picadinho-carne-arroz-feijao-cenoura",
        name="Picadinho de Carne, Arroz, Feijão e Cenoura",
        description="Picadinho de carne com arroz branco, feijão e cenoura macia.",
        image_url="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_KIDS,
        ingredients=["Carne bovina", "Arroz branco", "Feijão", "Cenoura", "Cebola"],
        calories=450, protein=27, carbs=54, fat=13,
    ),
    ProductSeed(
        id="prato-kids-frango-desfiado-pure-mandioquinha-brocolis",
        name="Frango Desfiado com Purê de Mandioquinha e Brócolis",
        description="Frango desfiado com purê de mandioquinha e brócolis ao vapor.",
        image_url="https://images.unsplash.com/photo-1543352634-a1c51d9f1fa7?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_KIDS,
        ingredients=["Frango", "Mandioquinha", "Brócolis", "Leite", "Azeite"],
        calories=410, protein=30, carbs=42, fat=12,
    ),
    ProductSeed(
        id="prato-kids-carne-moida-arroz-feijao-legumes",
        name="Carne Moída, Arroz Branco, Feijão e Legumes",
        description="Carne moída caseira com arroz, feijão e legumes coloridos.",
        image_url="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_KIDS,
        ingredients=["Carne moída", "Arroz branco", "Feijão", "Abobrinha", "Cenoura"],
        calories=455, protein=27, carbs=55, fat=13,
    ),
    ProductSeed(
        id="prato-kids-espaguete-mini-almondegas",
        name="Espaguete com Mini Almôndegas",
        description="Espaguete ao molho de tomate com mini almôndegas assadas.",
        image_url="https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("28.00"), category=ProductCategory.PRATO_KIDS,
        ingredients=["Espaguete", "Carne bovina", "Tomate", "Queijo", "Manjericão"],
        calories=470, protein=25, carbs=60, fat=14,
    ),
    ProductSeed(
        id="sopa-abobora-inhame-carne",
        name="Sopa de Abóbora, Inhame e Carne",
        description="Sopa cremosa de abóbora e inhame com cubos de carne bovina.",
        image_url="https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("21.00"), category=ProductCategory.SOPA,
        ingredients=["Abóbora", "Inhame", "Carne bovina", "Cebola", "Salsinha"],
        calories=290, protein=22, carbs=32, fat=8,
    ),
    ProductSeed(
        id="sopa-feijao-calabresa",
        name="Sopa de Feijão com Calabresa",
        description="Caldo encorpado de feijão com calabresa e legumes.",
        image_url="https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("21.00"), category=ProductCategory.SOPA,
        ingredients=["Feijão", "Calabresa", "Cenoura", "Cebola", "Alho"],
        calories=330, protein=18, carbs=38, fat=12,
    ),
    ProductSeed(
        id="sopa-mandioquinha-frango",
        name="Sopa de Mandioquinha com Frango",
        description="Creme de mandioquinha com frango desfiado e ervas frescas.",
        image_url="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("21.00"), category=ProductCategory.SOPA,
        ingredients=["Mandioquinha", "Frango", "Alho", "Cebola", "Salsinha"],
        calories=280, protein=24, carbs=30, fat=7,
    ),
    ProductSeed(
        id="sopa-caldo-verde-carne-couve",
        name="Caldo Verde com Carne e Couve",
        description="Caldo verde de chuchu, abobrinha e batata com carne e couve.",
        image_url="https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("21.00"), category=ProductCategory.SOPA,
        ingredients=["Chuchu", "Abobrinha", "Batata", "Carne bovina", "Couve"],
        calories=310, protein=21, carbs=34, fat=10,
    ),
    ProductSeed(
        id="sopa-puchero-grao-de-bico-calabresa-legumes",
        name="Puchero de Grão-de-Bico, Calabresa e Legumes",
        description="Sopa de grão-de-bico com calabresa e legumes variados.",
        image_url="https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("21.00"), category=ProductCategory.SOPA,
        ingredients=["Grão-de-bico", "Calabresa", "Cenoura", "Abobrinha", "Tomate"],
        calories=350, protein=17, carbs=43, fat=12,
    ),
    ProductSeed(
        id="proteina-carne-cerveja-preta",
        name="Carne na Cerveja Preta",
        description="Carne bovina cozida lentamente em molho de cerveja preta.",
        image_url="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("60.00"), category=ProductCategory.PROTEINA,
        ingredients=["Carne bovina", "Cerveja preta", "Cebola", "Cenoura", "Ervas"],
        calories=760, protein=72, carbs=18, fat=42,
    ),
    ProductSeed(
        id="proteina-estrogonofe-carne-champignon",
        name="Estrogonofe de Carne com Champignon",
        description="Estrogonofe de carne bovina com champignon e molho cremoso.",
        image_url="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("60.00"), category=ProductCategory.PROTEINA,
        ingredients=["Carne bovina", "Champignon", "Creme de leite", "Mostarda", "Cebola"],
        calories=720, protein=68, carbs=14, fat=43,
    ),
    ProductSeed(
        id="proteina-sobrecoxa-assada-molho-pesto",
        name="Sobrecoxa Assada ao Molho Pesto",
        description="Sobrecoxas assadas com molho pesto de manjericão e castanhas.",
        image_url="https://images.unsplash.com/photo-1598514982901-ae6273a2f8e8?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("60.00"), category=ProductCategory.PROTEINA,
        ingredients=["Sobrecoxa de frango", "Manjericão", "Castanhas", "Parmesão", "Azeite"],
        calories=690, protein=70, carbs=8, fat=42,
    ),
    ProductSeed(
        id="proteina-carne-louca",
        name="Carne Louca",
        description="Carne bovina desfiada e cozida com pimentões e tomate.",
        image_url="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("60.00"), category=ProductCategory.PROTEINA,
        ingredients=["Carne bovina", "Pimentão", "Tomate", "Cebola", "Azeitona"],
        calories=650, protein=74, carbs=12, fat=35,
    ),
    ProductSeed(
        id="premium-iscas-carne-creme-gorgonzola-arroz-batata",
        name="Iscas de Carne ao Creme de Gorgonzola, Arroz e Batata Sauté",
        description="Iscas de carne ao creme de gorgonzola com arroz e batata sauté.",
        image_url="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("35.00"), category=ProductCategory.PREMIUM,
        ingredients=["Carne bovina", "Gorgonzola", "Arroz", "Batata", "Creme de leite"],
        calories=610, protein=38, carbs=52, fat=29,
    ),
    ProductSeed(
        id="premium-carne-vinho-champignon-pure-mandioquinha-cenoura",
        name="Carne ao Vinho com Champignon e Purê de Mandioquinha",
        description="Carne ao vinho com champignon, purê de mandioquinha e cenoura.",
        image_url="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("35.00"), category=ProductCategory.PREMIUM,
        ingredients=["Carne bovina", "Vinho tinto", "Champignon", "Mandioquinha", "Cenoura"],
        calories=570, protein=39, carbs=43, fat=24,
    ),
    ProductSeed(
        id="premium-estrogonofe-carne-champignon-arroz-integral-grega",
        name="Estrogonofe de Carne com Champignon e Arroz Integral à Grega",
        description="Estrogonofe de carne com champignon e arroz integral à grega.",
        image_url="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("35.00"), category=ProductCategory.PREMIUM,
        ingredients=["Carne bovina", "Champignon", "Arroz integral", "Cenoura", "Ervilha"],
        calories=590, protein=37, carbs=50, fat=26,
    ),
    ProductSeed(
        id="premium-risoto-quatro-queijos-file-tilapia",
        name="Risoto 4 Queijos com Filé de Tilápia",
        description="Risoto cremoso de quatro queijos acompanhado de filé de tilápia.",
        image_url="https://images.unsplash.com/photo-1544943910-4c1dc44aab44?auto=format&fit=crop&w=1200&q=80",
        price=Decimal("35.00"), category=ProductCategory.PREMIUM,
        ingredients=["Tilápia", "Arroz arbóreo", "Parmesão", "Muçarela", "Gorgonzola"],
        calories=620, protein=36, carbs=58, fat=28,
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
