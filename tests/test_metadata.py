import pytest
from pydantic import HttpUrl
from fsedc.metadata import DCAT


def test_dcat_init():
    conformsTo = "https://project-open-data.cio.gov/v1.1/schema"
    dataset = [{}]
    dcat = DCAT(conformsTo=conformsTo, dataset=dataset)
    assert dcat is not None
    assert dcat.conformsTo == HttpUrl(conformsTo)
