import requests
from bs4 import BeautifulSoup
import arrow
# from dotenv import load_dotenv

class CSDGM:
    
    def __init__(self):
        pass

    def read_xml_url(self, url):        
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, features="xml")
            return soup
        else:
            return None