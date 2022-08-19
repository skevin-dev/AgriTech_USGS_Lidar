import pandas as pd 
import json 
import numpy as np 
import pdal 
import warnings 
warnings.filterwarnings('ignore')
from pyproj import Proj, transform
from shapely.geometry import Polygon, Point, mapping
import geopandas as gpd


class DataFetching():

    def json_load(filepath):
        """
    - function to load json file 
        """
        try:
            with open(filepath) as file:
                json_file = json.load(file)
            return json_file
        except FileNotFoundError:
            print('this is file is not found')

    def convert_EPSG(fromT, lon, lat):
        """
        -- function to change to the needed CRS format for better visualization
        parameters:
        
        1. fromT: original EPSG format
        2. lon: longitude
        3. lat: latitude
        
        WGS84 is the most common global CRS in latitude and longitude and it have
        "init=epsg4326" that will be used in this function 
        
        """
    
        P3857 = Proj(init='epsg:3857')
        P4326 = Proj(init='epsg:4326')
        if(fromT == 4326):
            input1 = P4326
            input2 = P3857
            
        else:
            input1 = p3857
            input2 = p4326
            
        x, y = transform(input1,input2,lon,lat)
        return [x, y]

    def loop_EPSG_converter(List):
        """
        -- function to change format of a list of cordinates to a list of points 
        """
        converted_list = []
        for i in List:
            converted_list.append(convert_EPSG(4326, i[0], i[1]))
            
        return converted_list 

    def generate_polygon(coor, epsg):
        """
        --Generate a polygon given a co-ordinate and CRS format

        """
        polygon_g = Polygon(coor)
        crs = {'init': 'epsg:'+str(epsg)}
        polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_g])       
        return polygon
    def json_modification(json_filepath, url, region,espg_in, espg_out):
        """
        -- function to modify json pipeline file to fetch data 
        """
        d = json_load(json_filepath)
        d['pipeline'][0]['polygon'] = str(polygon.iloc[:,0][0])
        d['pipeline'][0]['filename'] = f"{url}/{region}/ept.json"
        d['pipeline'][2]['in_srs'] = f"EPSG:{espg_in}"
        d['pipeline'][2]['out_srs'] = f"EPSG:{espg_out}"
        return d
    def geo_df(pipe,epsg):
        elevations = []
        geometry_ = []
        counts = pipe.execute()
        arrays = pipe.arrays[0]
        
        for i in arrays:
            lists = list(i)[-3:]
            elevations.append(lists[2])
            geometry_.append(Point(lists[0],lists[1]))
            
        df = gpd.GeoDataFrame(columns=["elevation_m", "Geometry"])
        df['elevation_m'] = elevations
        df['Geometry'] = geometry_
        df = df.set_geometry('Geometry')
        df.set_crs(epsg = epsg, inplace=True)
        
        return df 