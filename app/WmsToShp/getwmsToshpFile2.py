import geopandas as gpd
from requests import Request
from owslib.wfs import WebFeatureService
#########################
url = 'https://geo.safemap.go.kr/geoserver/safemap/wms'
wfs = WebFeatureService(url=url)




params = dict(service='wfs', version='1.3.0', typeName='A2SM_DrowsyShelter_area',
              request='GetFeature', outputFormat='application/json')


q = Request('GET', url, params=params).prepare().url
print(q)

data = gpd.read_file(q)


data.to_file('A2SM_DrowsyShelter_area.shp', driver='ESRI Shapefile', encoding='utf-8' )
#########################



