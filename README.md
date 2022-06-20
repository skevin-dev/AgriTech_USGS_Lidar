# AgriTech_USGS_Lidar


# <h1>Table of Contents</h1>
<ol type='1'>
<li><h2><a href="#overview">Project Overview</a></h2></li>
<li><h2><a href="#data">Data</a></h2></li>
<li><h2><a href="#install">installation</a></h2></li>
<li><h2><a href="#requirements">Requirements</a></h2></li>
<ol type='a'>

  
<h1><a name="overview">Project Overview</a></h1>
  
 AgriTech is fascinated by how water flows through a maize farm field. This information will aid our research on new agricultural products being tested on farms.
  
Understanding water flow in a field requires measuring the elevation of the field at multiple points. In a public dataset on Amazon, the USGS recently released high resolution elevation data as a lidar point cloud called USGS 3DEP. This dataset is critical for developing water flow models and forecasting plant health and maize harvest.
  
As part of the data engineering team, you are tasked to produce an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data

  
<h2><a name="data">Data</a></h2>

The 3D Elevation Program (3DEP) of the USGS (United States Geological Survey) provides access to the 3DEP repository's lidar point cloud data. Users can interact with massive amounts of lidar point cloud data without having to download it to their local computers.
  
  
<h1><a name="install">Installation</a></h1>
  
```
git clone
```
  
```
pip freeze > requirements.txt 
```


<h1><a name="requirements">Requirements</a></h1>
Geopandas
  
PDAL
  
Laspy
