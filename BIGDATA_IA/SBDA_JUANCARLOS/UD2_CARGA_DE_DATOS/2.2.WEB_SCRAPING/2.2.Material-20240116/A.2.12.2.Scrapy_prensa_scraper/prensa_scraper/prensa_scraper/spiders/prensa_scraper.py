import scrapy

class PrensaSpider(scrapy.Spider):
    # Simular que scrapy es un navegador para evitar robots.txt, no siempre funciona pero ahí queda
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    name = 'prensa'
    start_urls = ['http://www.lavoz.es']

    # Lista de palabras clave a buscar
    palabras_clave = ['Pedro', 'política', 'gobierno']

    def parse(self, response):
        try:
            content = response.xpath('//p[@class="a-min-text"]/text()').get()
            #content = response.css('div.clase-selector ::text').getall()
            content = ' '.join(content)
            print(content)  # Verifica contenido
        except Exception as e:
            # Maneja cualquier error de extracción
            self.log(f'Error en la extracción de contenido: {str(e)}')
            return

        # Realizar búsqueda de cada palabra clave y contar ocurrencias
        for palabra in self.palabras_clave:
            count_palabra = content.lower().count(palabra.lower())

            # Almacena los resultados en un archivo con codificación UTF-8
            with open('resultados.txt', 'a', encoding='utf-8') as file:
                file.write(f'====== La palabra "{palabra}" aparece {count_palabra} veces en la página.======\n')

            # Imprime un mensaje en la consola
            self.log(f'====== La palabra "{palabra}" aparece {count_palabra} veces en la página.======')
