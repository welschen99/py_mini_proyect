# Web Scraping linkedin jobs
import requests
from bs4 import BeautifulSoup

def buscar_trabajos_ciberseguridad():
    buscar = 'Ciberseguridad%20Jr'
    url = "https://www.linkedin.com/jobs/search?keywords=" + buscar + "&location=Argentina"
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    trabajos = soup.find_all("div", class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")

    if trabajos:
        print("Trabajos de ciberseguridad que requieren poca experiencia:")
        for i, trabajo in enumerate(trabajos, 1):
            titulo = trabajo.find("a", class_="base-card__full-link")
            # descripcion = trabajo.find("show-more-less-html__markup relative overflow-hidden", class_="job-result-card__title")
            lugar = trabajo.find("span", class_="job-search-card__location")
            if titulo and lugar:
                print(f"{i}. {titulo.get_text(strip=True)}")
                print(f"   Lugar: {lugar.get_text(strip=True)}")
                print(f"   Link: {titulo['href']}")
                print("------")
    else:
        print("No se encontraron trabajos de ciberseguridad.")

if __name__ == "__main__":
    print("Cargando...")
    buscar_trabajos_ciberseguridad()

