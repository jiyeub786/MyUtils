import geopandas as gpd
from requests import Request
from owslib.wfs import WebFeatureService
from owslib.wms import WebMapService
#########################
##서비스목록 추출         requset = DescribeFeatureType
##https://geo.safemap.go.kr/geoserver/safemap/wms?service=wfs&version=1.3.0&request=DescribeFeatureType
##wms = DescribeLayer
##https://geo.safemap.go.kr/geoserver/safemap/wms?service=wms&request=DescribeLayer&version=1.3.0
url = 'https://geo.safemap.go.kr/geoserver/safemap/wms'
wfs = WebFeatureService(url=url)

params = dict(service='wfs', version='1.3.0', typeName='A2SM_FLUDMARKS',
              request='GetFeature', outputFormat='application/json')


q = Request('GET', url, params=params).prepare().url
data = gpd.read_file(q)


data.to_file('A2SM_FLUDMARKS.shp', driver='ESRI Shapefile', encoding='utf-8' )
#########################



