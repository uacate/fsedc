import requests
from bs4 import BeautifulSoup
import re
import arrow
from dotenv import load_dotenv
import os


def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    stripped_text = stripped_text.replace("\n", " ")
    return stripped_text

def fsgeodata():
    base_url = "https://data.fs.usda.gov/geodata/edw/datasets.php"
    metadata_urls = []
    assets = []

    # Read the page that has the matedata links and cache locally
    resp = requests.get(base_url)
    soup = BeautifulSoup(resp.content, "html.parser")

    anchors = soup.find_all("a")
    for anchor in anchors:
        if anchor and anchor.get_text() == "metadata":
            metadata_urls.append(anchor["href"])

    # Download the metadata files
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    for u in metadata_urls:
        url = f"https://data.fs.usda.gov/geodata/edw/{u}"
        outfile_name = f"tmp/{u.split('/')[-1]}"

        if not os.path.exists(outfile_name):
            resp = requests.get(url)
            with open(outfile_name, "wb") as f:
                f.write(resp.content)

    # Parse the metadata files
    xml_files = [f for f in os.listdir("tmp") if f.endswith(".xml")]
    for xml_file in xml_files:
        with open(f"tmp/{xml_file}", "r") as f:
            soup = BeautifulSoup(f, "xml")
            title = strip_html_tags(soup.find("title").get_text())
            desc_block = soup.find("descript")
            abstract = strip_html_tags(desc_block.find("abstract").get_text())
            themekeys = soup.find_all("themekey")
            keywords = [tk.get_text() for tk in themekeys]
            idinfo_citation_citeinfo_pubdate = soup.find("pubdate")
            if idinfo_citation_citeinfo_pubdate:
                modified = arrow.get(idinfo_citation_citeinfo_pubdate.get_text())
            else:
                modified = ""

            asset = {
                "title": title,
                "description": abstract,
                "modified": modified,
                "metadata_source_url": url,
                "keywords": keywords,
            }

            assets.append(asset)

    return assets


def main():
    assets = fsgeodata()


if __name__ == "__main__":
    main()
