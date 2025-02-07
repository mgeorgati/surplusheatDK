import geopandas as gpd
import pandas as pd
def select_intersection_points(polygon_geojson_path, points_geojson_path):
    """
    Selects points that intersect with polygons from GeoJSON files and returns them as a GeoDataFrame.
    
    Args:
    polygon_geojson_path (str): Path to the GeoJSON file containing the polygon(s).
    points_geojson_path (str): Path to the GeoJSON file containing the points.
    
    Returns:
    GeoDataFrame: GeoDataFrame containing the intersecting points with their attributes.
    """
    
    # Load GeoJSON files
    polygons_gdf = gpd.read_file(polygon_geojson_path)
    points_gdf = gpd.read_file(points_geojson_path)
    
    # Ensure the coordinate reference systems (CRS) match
    if polygons_gdf.crs != points_gdf.crs:
        points_gdf = points_gdf.to_crs(polygons_gdf.crs)
    
    # Create a list to store the filtered points
    intersecting_points_list = []

    # Iterate over polygons and check intersections with points
    for poly in polygons_gdf.geometry:

        # Filter points that are within the current polygon
        filtered_points_gdf = points_gdf[points_gdf.geometry.apply(poly.contains)]
        
        # Append the filtered points to the list
        intersecting_points_list.append(filtered_points_gdf)
    
    # Concatenate all the filtered GeoDataFrames into one GeoDataFrame
    intersecting_points_gdf = pd.concat(intersecting_points_list, ignore_index=True)
    intersecting_points_gdf = gpd.GeoDataFrame(intersecting_points_gdf, geometry='geometry', crs=points_gdf.crs)
    
    return intersecting_points_gdf

