import scrapy

class PrensaSpider(scrapy.Spider):
    name = 'prensa'
    start_urls = ['http://www.atlantico.net']

    def parse(self, response):
        try:
            # Intenta decodificar el contenido utilizando utf-8 y ignora los caracteres no válidos
            content = response.body.decode('utf-8', 'ignore')
        except UnicodeDecodeError:
            # Si hay un error de decodificación, imprime un mensaje y regresa
            self.log('Error de decodificación Unicode en la página.')
            return

        # Contar el número de veces que aparece la palabra 'amnistía'
        count_amnistia = content.lower().count('Vigo')

        # Imprimir el resultado
        print(f'====== La palabra "amnistía" aparece {count_amnistia} veces en la página.======')

