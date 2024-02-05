import scrapy
import json

class CocheSpiderSpider(scrapy.Spider):
    name = "cochespider"
    allowed_domains = ["www.clicars.com"]
    start_urls = ["https://www.clicars.com/coches-segunda-mano-ocasion/4x4-suv"]

    def parse(self, response):
        # Extraer datos de la página inicial
        scraped_data = self.extract_data(response)

        # Guardar datos en el archivo JSON
        with open('resultados.json', 'a') as file:
            json.dump(scraped_data, file, indent=4)
            file.write('\n')  # Agregar una nueva línea para separar los datos de diferentes páginas

        # Extraer el número total de páginas
        total_pages = response.css('div.pagination-scroll::attr(data-pages)').get()

        # Si hay más páginas, realizar solicitudes adicionales
        if total_pages and int(total_pages) > 1:
            for page in range(2, int(total_pages) + 1):
                next_page_url = f"{response.url}?page={page}"
                yield scrapy.Request(url=next_page_url, callback=self.parse)

    def extract_data(self, response):
        # Método para extraer datos de la página actual
        scraped_data = []

        for vehicle in response.css('article.sale-list__item'):
            data = {
                'title': vehicle.css('div.car-card h2.maker strong::text').get(),
                'price': vehicle.css('div.car-card span.price::text').get(),
            }
            scraped_data.append(data)

        return scraped_data
