from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.product.schemas import ProductCreate


def test_product_create_accepts_frontend_camel_case_contract() -> None:
    product = ProductCreate.model_validate(
        {
            "id": "frango-grelhado-fit",
            "name": "Frango Grelhado",
            "description": "Frango com acompanhamentos saudáveis.",
            "imageUrl": "https://example.com/frango.jpg",
            "price": 24.9,
            "category": "Hiperproteica",
            "ingredients": ["Frango"],
            "nutrition": {"calories": 420, "protein": 38, "carbs": 39, "fat": 11},
        }
    )

    assert str(product.image_url) == "https://example.com/frango.jpg"
    assert product.price == Decimal("24.9")


def test_product_create_rejects_invalid_product_id() -> None:
    with pytest.raises(ValidationError):
        ProductCreate.model_validate(
            {
                "id": "Produto inválido",
                "name": "Produto",
                "description": "Descrição válida.",
                "imageUrl": "https://example.com/product.jpg",
                "price": 20,
                "category": "Low Carb",
                "ingredients": ["Ingrediente"],
                "nutrition": {"calories": 1, "protein": 1, "carbs": 1, "fat": 1},
            }
        )
