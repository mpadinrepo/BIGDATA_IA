import scrapy

class PrensaSpider(scrapy.Spider):
    name = 'prensa'
    start_urls = ['http://www.elmundo.es']

    def parse(self, response):
        try:
            # Utiliza un selector CSS específico para apuntar a la sección que contiene el texto
            content = response.css('div.clase-selector ::text').getall()
            content = ' '.join(content)
        except Exception as e:
            # Maneja cualquier error de extracción
            self.log(f'Error en la extracción de contenido: {str(e)}')
            return

        # Contar el número de veces que aparece la palabra 'amnistía'
        count_amnistia = content.lower().count('Israel')

        # Almacena los resultados en un archivo
        with open('resultados.txt', 'a') as file:
            file.write(f'====== La palabra "amnistía" aparece {count_amnistia} veces en la página.======\n')

        # Imprime un mensaje en la consola
        self.log(f'====== La palabra "amnistía" aparece {count_amnistia} veces en la página.======')
