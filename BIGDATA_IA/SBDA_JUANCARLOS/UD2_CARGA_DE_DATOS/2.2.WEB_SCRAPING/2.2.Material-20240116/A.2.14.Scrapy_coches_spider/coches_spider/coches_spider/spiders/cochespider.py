import scrapy
import json
import pandas as pd
import os
'''

Se ejecuta con el comando: scrapy crawl cochespider
En el fichero dom.html está el DOM de la página web 
que estamos raspando para que seea más fácil de entender
Los coches son articles
y dentro de cada article hay un div con la clase car-card
y dentro de ese div hay un h2 con la clase maker
y dentro de ese h2 hay un strong con el nombre del coche
y dentro de ese div hay un span con la clase price
y dentro de ese span hay un texto con el precio
y dentro de ese div hay un span con la clase info
y dentro de ese span hay un texto con la información del coche

'''


class CocheSpiderSpider(scrapy.Spider):
    name = "cochespider"
    allowed_domains = ["www.clicars.com"]
    start_urls = ["https://www.clicars.com/coches-segunda-mano-ocasion/4x4-suv"]

    def parse(self, response):
        # Extraer datos de la página inicial
        scraped_data = self.extract_data(response)

        # Guardar datos en el archivo JSON
        with open('resultados.json', 'a', encoding='utf-8') as file:
            json.dump(scraped_data, file, indent=4, ensure_ascii=False)
            file.write('\n')  # Agregar una nueva línea para separar los datos de diferentes páginas

        # Crear un DataFrame de pandas
        df = pd.DataFrame(scraped_data)

        # Verificar si el archivo CSV ya existe
        df_exists = os.path.isfile('resultados.csv')

        # Guardar datos en el archivo CSV
        df.to_csv('resultados.csv', index=False, mode='a', header=not df_exists)

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
            title = vehicle.css('div.car-card h2.maker strong::text').get()
            price = vehicle.css('div.car-card span.price::text').get()
            info = vehicle.css('div.car-card span.info::text').get()

            # Limpiar caracteres no deseados en el título y el precio
            if title:
                title = title.strip()
            if price:
                price = price.replace('â‚¬', '').strip()
            if info:
                valores = info.split('|')
                valores = [valor.strip() for valor in valores]

                
            data = {
                'title': title,
                'price': price,
                'year': valores[0],
                'kms': valores[1],
                'power': valores[2],
                'cambio': valores[3],
            }
            scraped_data.append(data)

        return scraped_data

