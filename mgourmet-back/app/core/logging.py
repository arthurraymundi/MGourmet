import logging


def configure_logging() -> None:
    """Configura logging estruturado básico, extensível por um coletor externo."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
