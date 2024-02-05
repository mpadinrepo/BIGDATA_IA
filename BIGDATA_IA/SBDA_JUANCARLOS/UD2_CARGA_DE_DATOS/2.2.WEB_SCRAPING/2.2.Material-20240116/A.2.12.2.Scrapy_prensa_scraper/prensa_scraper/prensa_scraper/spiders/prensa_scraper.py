import scrapy

class PrensaSpider(scrapy.Spider):
    #simular que scrapy es un navegador para evitar robots.txt,no siempre funciona pero ahí queda
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    name = 'prensa'
    start_urls = ['http://www.lavoz.es']

    def parse(self, response):
        try:
            content = response.xpath('//p[@class="a-min-text"]/text()').get()
            #content = response.css('div.clase-selector ::text').getall()
            content = ' '.join(content)
            print(content)  # verifica contenido
        except Exception as e:
            # Maneja cualquier error de extracción
            self.log(f'Error en la extracción de contenido: {str(e)}')
            return

        # Contar el número de veces que aparece la palabra 'amnistía'
        count_amnistia = content.lower().count('presidente')

        # Almacena los resultados en un archivo
        with open('resultados.txt', 'a') as file:
            file.write(f'====== La palabra "amnistía" aparece {count_amnistia} veces en la página.======\n')

        # Imprime un mensaje en la consola
        self.log(f'====== La palabra "amnistía" aparece {count_amnistia} veces en la página.======')
