import pytest
from dotenv import load_dotenv
import os
from fsedc.crawlers import CSDGM

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

def test_init():
    assert DATABASE_URL is not None and DATABASE_URL is not ""

def test_csdgm():
    crawler = CSDGM()
    assert crawler is not None

    # Test valid url
    url = f"https://data.fs.usda.gov/geodata/edw/edw_resources/meta/S_USA.Activity_SilvTSI.xml"
    soup = crawler.read_xml_url(url)
    assert soup is not None

    # Test invalid url
    url = f"https://data.fs.usda.gov/geodata/edw/edw_resources/meta/S_USA.Activity_SilvTSI.xyz"
    soup = crawler.read_xml_url(url)
    assert soup is None
