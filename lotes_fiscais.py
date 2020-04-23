from owslib.wms import WebMapService
import json
from shapely.geometry import Polygon, Point, box
from pyproj import Proj, transform, Transformer
from ipyleaflet import Map, WMSLayer, basemaps, Marker, WidgetControl, Polygon as LeafLetPolygon
from ipywidgets import Label

url_wms = 'http://wms.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wms'
wms = WebMapService(url_wms, version='1.3.0')
coords_wgs84 = [-23.545567989349365, -46.6351979970932]
center = coords_wgs84

mapa_base = WMSLayer(
    url = url_wms,
    layers = 'MapaBase_Politico',
    format = 'image/png',
    transparent = True,
    attribution = 'GeoSampa'
)

lotes = WMSLayer(
    url = 'http://wms.geosampa.prefeitura.sp.gov.br/geoserver/geoportal/wms',
    layers = 'lote_cidadao',
    format = 'image/png',
    transparent = True,
    attribution = 'GeoSampa'
)

transformer = Transformer.from_crs(31983, 4326)

marker = Marker(location=center, draggable=True)

shape = ''

def geo2utm(coord_geo):
    in_proj  = Proj("EPSG:4326")
    out_proj = Proj("EPSG:31983")
    y1, x1 = coord_geo
    return transform(in_proj, out_proj, y1, x1)

def get_bb_from_point(p):
    bb = Point(p[0], p[1]).buffer(0.000001).bounds
    # return list(box(bb[0], bb[1], bb[2], bb[3]).exterior.coords)
    return bb

def get_polygon_coord(coordinate):
    c = coordinate
    s = 0.25
    lote = wms.getfeatureinfo(layers = ['lote_cidadao'],
                          format = 'image/png',
                          info_format = 'application/json',
                          srs = 'EPSG:31983',
                          bbox = (c[0] - s, c[1] - s, c[0] + s, c[1] + s),
                          size = (2, 2), 
                          xy = (1, 1))
    lote_json = json.load(lote)
    # print(lote_json)
    return lote_json['features'][0]['geometry']['coordinates'][0]

def handle_click(*args, **kwargs):
    lote_xy = geo2utm(marker.location)
    poligono_coord = get_polygon_coord(lote_xy)
#     print(list(transformer.itransform(poligono_coord)))
#     print(poligono_coord)
    poligono = LeafLetPolygon(locations=list(transformer.itransform(poligono_coord)), 
                              color="green", 
                              fill_color="green")
    m.add_layer(poligono)
    display(Polygon(poligono_coord))


def _map():
    m = Map(center=center, 
            zoom=17,
        scroll_wheel_zoom = True)

    m.add_layer(mapa_base)
    m.add_layer(lotes)

    m.add_layer(marker)

    marker.on_click(handle_click)

    return m

m = _map()

def show_map():
    return m