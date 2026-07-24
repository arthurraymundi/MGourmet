from scripts.seed import CONTENT_ITEMS, FAQS, KITS, PRODUCTS, TESTIMONIALS


def test_seed_data_covers_all_frontend_collections() -> None:
    assert len(PRODUCTS) == 5
    assert len(KITS) == 3
    assert len(TESTIMONIALS) == 2
    assert len(FAQS) == 3
    assert len(CONTENT_ITEMS) == 7
