# Obtendo a geometria de um Lote Fiscal

Muitas vezes precisamos trabalhar com a feição de um ou alguns lotes para diversas finalidades. Recentemente estamos trabalhando para recortar atravéz da feição do lote a nuvem de pontos LiDAR da cidade de São Paulo e analisa-lo individualmente.

Para isso criamos esse repositório para estudar maneiras de se obter a feição do lote pela sua localização geográfica e criamos um (Jupyter Notebook)[https://github.com/geoinfo-smdu/lotes-m3dc/blob/master/Geometria%20do%20lote%20por%20servi%C3%A7o%20WMS%20do%20GeoSampa.ipynb] para tanto.

## Metodologia

Utilizamos o serviço WMS do GeoSampa e a partir da camada de lotes, selecionamos no mapa o lote desejado e obtemos a sua feição. 

## Objetivo

Apesar de simples, esse processo envolve algumas bibliotecas e padrões específicos que podem gerar aprendizado e derivar para o desenvolvimento de outras aplicações.

Sobretudo, pretendemos encapsular esse processo em uma biblioteca python e reutiliza-la em outros projetos e estudos

