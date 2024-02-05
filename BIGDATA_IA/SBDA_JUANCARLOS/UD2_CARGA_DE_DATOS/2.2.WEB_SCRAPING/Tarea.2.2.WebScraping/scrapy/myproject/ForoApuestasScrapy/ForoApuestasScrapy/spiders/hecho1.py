import logging
from scrapy import Spider, Request
from scrapy.http import HtmlResponse
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader

class Pregunta(Item):
    pregunta = Field()
    id = Field()

class ForoApuestasScrapySpider(Spider):
    name = 'foroapuestasscrapy'
    allowed_domains = ['foroapuestas.forobet.com']
    start_urls = ['http://foroapuestas.forobet.com/ludopatia-adiccion-y-problemas-con-el-juego/']

    def parse(self, response: HtmlResponse):
        sel = response.xpath('//body')

        preguntas = sel.xpath('.//h3[@class="threadtitle"]/a/text()')

        for i, pregunta_text in enumerate(preguntas.getall()):
            item = ItemLoader(Pregunta(), response)
            item.add_value('pregunta', pregunta_text)
            item.add_value('id', i)
            pregunta_item = item.load_item()

            # Agregar mensajes de registro
            logging.info(f"Pregunta {i + 1}: {pregunta_item.get('pregunta')}")

            yield pregunta_item

        logging.info("Extracción de datos completada con éxito")
