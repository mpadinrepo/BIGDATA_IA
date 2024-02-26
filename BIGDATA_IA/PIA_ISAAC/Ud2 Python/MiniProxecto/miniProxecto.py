""" Mini Proxecto
Trátase de detectar que nomes firmaron na folla de firmas ou non.

A folla está composta por ter partes interesantes:

- Na parte superior hai un QR que te da información sobre o día que corresponde á folla e mais o número de follas de que corresponde ao día.

- Na zona central están tanto os nomes coma as firmas. No lado esquerdo se encontran os nomes das persoas e no lado dereito debería estar a súa firma.

O primeiro debería ser detectar o QR. Iso se pode facer ou ben con open cv ou ben con algunha outra librería como zbar. Nas probas, funcionou moito mellor pyzbar que o propio de open CV.

Tes pyzbar aquí: https://pypi.org/project/pyzbar/

Se o instalas mediante pip tes que incluír no sistema a libreria zbar: zbar-tools (apt). Con conda xe mete o necesario.

O seguinte sería traballar sobre a zona central. Na parte esquerda deberás detectar cada unha das zonas onde aparece o nome, é dicir, o rectángulo branco e extraer o nome escrito. Para extraer o texto podes usa pytesseract, que é un wrapper da librería tesseract de google para facer OCR. Na páxina de pypy tedes información sobre como instalalo e usalo: https://pypi.org/project/pytesseract/



Por ultimo, no lado dereito acompañando ao nome, deberás buscar se existe algún contorno na zona interior. Non hai que recoñecer a firma nin nada polo estilo. Simplemente se trata de ver se hai algo escrito..

Tedes un par de ficheiros para probar.


 """