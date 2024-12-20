import argparse
import logging

from social_etl import etl_factory  # type: ignore
# from transform import transformation_factory
from utils.db import db_factory

def main(source: str, transformation: str) -> None:
    """Function to call the ETL code

    Args:
        source (str, optional): Defines which ata to pull.
        Defaults to 'reddit'.
    """
    logging.info(f'Starting {source} ETL')
    logging.info(f'Getting {source} ETL object from factory')
    client, social_etl = etl_factory(source)
    db = db_factory()
    
