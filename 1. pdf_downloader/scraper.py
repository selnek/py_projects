import sys
import requests
import pathlib
from bs4 import BeautifulSoup


def scraper(url, folder):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
    except Exception:
        return "Invalid URL"

    i = 0

    for link in links:
        if '.pdf' in link.get('href', []):
            i += 1
            try:
                response = requests.get(link.get('href'))
                path = pathlib.Path(f"{folder}", f"{i}.pdf")
                pdf = open(path, 'wb')
                pdf.write(response.content)
                pdf.close()
            except Exception:
                print("Unexpected error:", sys.exc_info()[0])
                return "Some error occurred"
    return f"Number of downloaded pdf files: {i}"

