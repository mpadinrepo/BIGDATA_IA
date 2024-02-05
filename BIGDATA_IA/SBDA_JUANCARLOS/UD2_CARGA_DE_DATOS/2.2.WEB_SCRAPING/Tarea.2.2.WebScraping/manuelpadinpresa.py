{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "33a76a33-18d7-4e20-8270-f9b464f64db5",
   "metadata": {},
   "source": [
    "# Parseamos URL para hacer Scrapping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "443a2901-d3e9-423c-ac1f-76396ea05e9d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "from scrapy.item import Item, Field\n",
    "from scrapy.spiders import CrawlSpider\n",
    "from scrapy.spiders import Rule\n",
    "from scrapy.linkextractors import LinkExtractor\n",
    "from scrapy.loader.processors import Join\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "url = \"https://www.latiendadelasconservas.es/conservas-de-carne\"\n",
    "peticion = requests.get(url)\n",
    "pagina = BeautifulSoup(peticion.content, \"html.parser\")\n",
    "libros = pagina.find_all('article')  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5eafe2a4-b33f-4f01-97ae-fa068d45ae0f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "incomplete input (168932718.py, line 14)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[9], line 14\u001b[1;36m\u001b[0m\n\u001b[1;33m    \u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m incomplete input\n"
     ]
    }
   ],
   "source": [
    "class TiendadeConservasItem(Item):\n",
    "    titulo = Field()\n",
    "    precio = Field()\n",
    "    enlace = Field()\n",
    "\n",
    "class TiendadeConservasCrawler(CrawlSpider):\n",
    "    name = 'tiendadeconservascrawler'\n",
    "    allowed_domains = ['latiendadelasconservas.es']\n",
    "    start_url = ['https://www.latiendadelasconservas.es/conservas-de-carne']\n",
    "    \n",
    "    rules = (\n",
    "        Rule(LinkExtractor(allow=r'https://www.latiendadelasconservas.es/conservas-de-carne/')\n",
    "            )\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "474603a2-48c0-492e-bcaf-e29b2a2a407c",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from scrapy.loader import ItemLoader\n",
    "from scrapy.loader.processors import TakeFirst\n",
    "\n",
    "# ... (código anterior)\n",
    "\n",
    "class TiendadeConservasCrawler(CrawlSpider):\n",
    "    name = 'tiendadeconservascrawler'\n",
    "    allowed_domains = ['latiendadelasconservas.es']\n",
    "    start_urls = ['https://www.latiendadelasconservas.es/conservas-de-carne']\n",
    "\n",
    "    rules = (\n",
    "        Rule(LinkExtractor(allow=r'https://www.latiendadelasconservas.es/conservas-de-carne/'), callback='parse_item'),\n",
    "    )\n",
    "\n",
    "    def parse_item(self, response):\n",
    "        item_loader = ItemLoader(item=TiendadeConservasItem(), response=response)\n",
    "        item_loader.default_output_processor = TakeFirst()\n",
    "\n",
    "        # Extracción de datos usando XPath\n",
    "        item_loader.add_value('enlace', response.url)\n",
    "        item_loader.add_xpath('titulo', '/html/body/div/strong/main/div/div[2]/div/div[2]/div[3]/div/div[3]/h1')\n",
    "        item_loader.add_xpath('precio', '/html/body/div/strong/main/div/div[2]/div/div[2]/div[3]/div/div[5]/div/p/span/bdi')\n",
    "\n",
    "        return item_loader.load_item()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f7f8be37-6d49-45f2-8c93-134371205516",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "class TiendadeConservasCrawler(CrawlSpider):\n",
    "    # ... (código anterior)\n",
    "\n",
    "    def parse_item(self, response):\n",
    "        item_loader = ItemLoader(item=TiendadeConservasItem(), response=response)\n",
    "        item_loader.default_output_processor = TakeFirst()\n",
    "\n",
    "        # Extracción de datos usando XPath\n",
    "        item_loader.add_value('enlace', response.url)\n",
    "        item_loader.add_xpath('titulo', '/html/body/div/strong/main/div/div[2]/div/div[2]/div[3]/div/div[3]/h1')\n",
    "        item_loader.add_xpath('precio', '/html/body/div/strong/main/div/div[2]/div/div[2]/div[3]/div/div[5]/div/p/span/bdi')\n",
    "\n",
    "        item = item_loader.load_item()\n",
    "\n",
    "        # Imprimir los resultados en la consola\n",
    "        self.logger.info(f\"Enlace: {item['enlace']}\")\n",
    "        self.logger.info(f\"Título: {item['titulo']}\")\n",
    "        self.logger.info(f\"Precio: {item['precio']}\")\n",
    "\n",
    "        yield item\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "68e3b0d8-1fcc-45fd-a3d1-eacb2994b654",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from scrapy.loader import ItemLoader\n",
    "from scrapy.loader.processors import TakeFirst\n",
    "\n",
    "class TiendadeConservasCrawler(CrawlSpider):\n",
    "    name = 'tiendadeconservascrawler'\n",
    "    allowed_domains = ['latiendadelasconservas.es']\n",
    "    start_urls = ['https://www.latiendadelasconservas.es/conservas-de-carne']\n",
    "\n",
    "    rules = (\n",
    "        Rule(LinkExtractor(allow=r'https://www.latiendadelasconservas.es/conservas-de-carne/'), callback='parse_item'),\n",
    "    )\n",
    "\n",
    "    def parse_item(self, response):\n",
    "        item_loader = ItemLoader(item=TiendadeConservasItem(), response=response)\n",
    "        item_loader.default_output_processor = TakeFirst()\n",
    "\n",
    "        # Extracción de datos usando XPath\n",
    "        item_loader.add_value('enlace', response.url)\n",
    "        item_loader.add_xpath('titulo', '/html/body/div/strong/main/div/div[2]/div/div[2]/div[3]/div/div[3]/h1')\n",
    "        item_loader.add_xpath('precio', '/html/body/div/strong/main/div/div[2]/div/div[2]/div[3]/div/div[5]/div/p/span/bdi')\n",
    "\n",
    "        item = item_loader.load_item()\n",
    "\n",
    "        # Obtener el texto del título y el precio\n",
    "        titulo_texto = item_loader.get_output_value('titulo').extract_first()\n",
    "        precio_texto = item_loader.get_output_value('precio').extract_first()\n",
    "\n",
    "        # Imprimir los resultados en la consola\n",
    "        print(f\"Enlace: {item['enlace']}\")\n",
    "        print(f\"Título: {titulo_texto}\")\n",
    "        print(f\"Precio: {precio_texto}\")\n",
    "\n",
    "        yield item\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad16f66a-d94b-48ef-b102-4a111c74736a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
