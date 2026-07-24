from app.content.schemas import ContactInfoResponse, ContentItemResponse


def test_contact_info_response_matches_frontend_contract() -> None:
    response = ContactInfoResponse.model_validate(
        {
            "whatsapp": "+55 (11) 98888-0000",
            "instagram": "@mgourmetfit",
            "address": "Rua Exemplo, 250 - São Paulo/SP",
            "businessHours": "Segunda a sábado, 08h às 19h",
        }
    )

    assert response.model_dump(by_alias=True) == {
        "whatsapp": "+55 (11) 98888-0000",
        "instagram": "@mgourmetfit",
        "address": "Rua Exemplo, 250 - São Paulo/SP",
        "businessHours": "Segunda a sábado, 08h às 19h",
    }


def test_content_item_response_preserves_display_order() -> None:
    response = ContentItemResponse.model_validate(
        {"id": "benefit-1", "text": "Ingredientes frescos", "position": 0}
    )

    assert response.position == 0
