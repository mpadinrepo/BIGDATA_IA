import logging
from scrapy import Spider, Request
from scrapy.http import HtmlResponse
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader

class ForoApuestasItems(Item):
    Publicacion = Field()
    Fecha = Field()
    Hora = Field()

class ForoApuestasScrapySpider(Spider):
    name = 'foroapuestasscrapy'
    allowed_domains = ['foroapuestas.forobet.com']
    start_urls = ['http://foroapuestas.forobet.com/ludopatia-adiccion-y-problemas-con-el-juego/']

    def parse(self, response: HtmlResponse):
        # Extraer la información de cada post en el listado
        posts = response.xpath('//*[@id="postlist"]/li[contains(@class, "postbitlegacy")]')

        for post in posts:
            # Extraer la fecha y la hora
            fecha = post.xpath('.//span[@class="postdate old"]/span[@class="date"]/text()').get()
            hora = post.xpath('.//span[@class="postdate old"]/span[@class="time"]/text()').get()

            # Extraer el contenido del post
            contenido = post.xpath('.//div[@class="content"]/div/blockquote[@class="postcontent restore "]/text()').get()

            # Agregar información al item final
            foro_item = ItemLoader(ForoApuestasItems(), post)
            foro_item.add_value('Publicacion', contenido)
            foro_item.add_value('Fecha', fecha)
            foro_item.add_value('Hora', hora)

            yield foro_item.load_item()

        # Paginación: seguir al siguiente enlace si existe
        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page:
            yield Request(url=next_page, callback=self.parse)
