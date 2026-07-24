from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.kit.schemas import KitCreate, KitResponse


def test_kit_create_accepts_frontend_camel_case_contract() -> None:
    kit = KitCreate.model_validate(
        {
            "id": "kit-5",
            "name": "Kit 5",
            "meals": 5,
            "originalPrice": 134.5,
            "discountedPrice": 119.9,
        }
    )

    assert kit.original_price == Decimal("134.5")
    response = KitResponse.model_validate(kit.model_dump())
    assert response.model_dump(by_alias=True, mode="json")["discountedPrice"] == 119.9


def test_kit_create_rejects_a_discount_greater_than_original_price() -> None:
    with pytest.raises(ValidationError):
        KitCreate.model_validate(
            {
                "id": "kit-5",
                "name": "Kit 5",
                "meals": 5,
                "originalPrice": 100,
                "discountedPrice": 101,
            }
        )
