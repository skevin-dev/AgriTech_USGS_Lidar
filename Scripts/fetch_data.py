import pdal
import json
import sys
from shapely.geometry import Point
import geopandas as gpd


def get_json_data(path):
    """
    --function to return json data
    """
    with open(path, 'r') as json_file:
        json_obj = json.load(json_file)
    return json_obj


pipe = pdal.Pipeline(json.dumps(get_json_data('../pipeline_json.json')))
counts = pipe.execute()
arrays = pipe.arrays[0]

elevations=[]
geometry_ =[]
for i in arrays:
    lists = list(i)[-3:]
    elevations.append(lists[2])
    geometry_.append(Point(lists[0],lists[1]))
    
geo_df = gpd.GeoDataFrame(columns=["elevation_m", "Geometry"])
geo_df['elevation_m'] = elevations
geo_df['Geometry'] = geometry_

print(geo_df)

    