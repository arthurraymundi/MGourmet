from app.content.schemas import FaqResponse, TestimonialResponse as TimonialSchema


def test_testimonial_response_matches_frontend_contract() -> None:
    response = TimonialSchema.model_validate(
        {"id": "1", "name": "Camila Rocha", "role": "Atleta", "quote": "Muito prático."}
    )

    assert response.model_dump(by_alias=True) == {
        "id": "1",
        "name": "Camila Rocha",
        "role": "Atleta",
        "quote": "Muito prático.",
    }


def test_faq_response_matches_frontend_contract() -> None:
    response = FaqResponse.model_validate(
        {"id": "1", "question": "Como entrega?", "answer": "Refrigerada."}
    )

    assert response.model_dump(by_alias=True) == {
        "id": "1",
        "question": "Como entrega?",
        "answer": "Refrigerada.",
    }
