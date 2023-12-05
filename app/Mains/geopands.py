import geopandas as gpd
from requests import Request
from owslib.wfs import WebFeatureService

url = 'https://geo.safemap.go.kr/geoserver/safemap/wms'
wfs = WebFeatureService(url=url)

params = dict(service='wfs', version='1.1.1', typeName='A2SM_FLOODDAMAGE',
              request='GetFeature', outputFormat='application/json')
q = Request('GET', url, params=params).prepare().url
data = gpd.read_file(q)

data.to_file('FloodMap.shp', driver='ESRI Shapefile')