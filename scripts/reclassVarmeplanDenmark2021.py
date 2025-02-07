# Read shp, reclassify column GRP127HOVE to 5classes and save as geojson
### Fix paths o local folder
### Check if there are entries in column GRP127HOVE that have not been assigned in any of the new classes --> Unknown

import geopandas as gpd

# Load the shapefile (replace 'path_to_your_shapefile.shp' with your file path)
gdf = gpd.read_file('./data/Varmeplan Danmark 2021/industrial_excess_heat.shp')
print(gdf.head(4))
# Define the classification dictionary
classification = {
    "Manufacturing & Industry": [
        "Mobelindustri", "Fremst. af skibe og andre transportmidler", "Fremst. af metal",
        "Fremst. af computere og kommunikationsudstyr mv.", "Fremst. af maling og saebe mv.",
        "Papirindustri", "Fremst. af andre maskiner", "Drikkevareindustri",
        "Laeder- og fodtojsindustri", "Fremst. af motorer, vindmoller og pumper",
        "Fremst. af motorkoretojer og dele hertil", "Metalvareindustri",
        "Fremst. af andet elektronisk udstyr", "Fremst. af elektriske motorer mv.",
        "Glasindustri og keramisk industri", "Betonindustri og teglvaerker",
        "Plast- og gummiindustri", "Tekstilindustri", "Fremst. af husholdningsapparater, lamper mv.",
        "Legetoj og anden fremstillingsvirksomhed", "Tobaksindustri",
        "Fremst. af basiskemikalier", "Fremst. af ledninger og kabler", "Beklaedningsindustri",
        'Traeindustri', 'Medicinalindustri', 'Fremstilling af medicinske og dentale instrumenter samt udstyr hertil'
    ],
    "Agriculture, Forestry & Fishing": [
        "Landbrug og gartneri", "Skovbrug", "Fiskeri"
    ],
    "Food & Beverage": [
        "Slagterier", "Mejerier", "Fiskeindustri", "Anden fodevareindustri",
        "Bagerier, brodfabrikker mv.", "Drikkevareindustri"
    ],
    "Retail & Trade": [
        "Bilhandel", "Detailhandel undtagen med motorkoretojer og motorcykler",
        "Engroshandel undtagen med motorkoretojer og motorcykler", "Hoteller mv.",
        "Restauranter",'Bilvaerksteder mv.'
    ],
    "Energy, Mining & Services": [
        "Olieraffinaderier mv.", "Indvinding af grus og sten", "Service til rastofindvinding",
        "Reparation og installation af maskiner og udstyr", "Trykkerier mv.",'Olieraffinaderier mv. - Olieraffinaderier mv.'
    ]
}

# Reverse the classification dictionary for easy lookup
category_to_class = {category: cls for cls, categories in classification.items() for category in categories}

# Add the 'SectorClass' column to the GeoDataFrame
gdf['FiveClasses'] = gdf['GRP127HOVE'].apply(lambda x: category_to_class.get(x, "Unknown"))  # Replace 'CategoryField' with the actual column name containing the categories

print(gdf.loc[gdf['FiveClasses'] == "Unknown", 'GRP127HOVE'].unique())
# Save the modified shapefile
gdf.to_file('./data/Varmeplan Danmark 2021/industrial_excess_heat_new_classes.geojson')

print("New classificatio column added and shapefile saved in geojson format!")
