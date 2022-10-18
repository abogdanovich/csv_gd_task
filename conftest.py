import pytest

from .parser import CSVParser


@pytest.fixture
def csv_parser():
    csv_parser = CSVParser()
    yield csv_parser
