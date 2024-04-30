import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("./data/ne_10m_airports.shp")

print(gdf.head())  # View the first few rows of the dataframe
print(gdf.columns)  # Print the column names



# Assuming 'gdf' is your GeoDataFrame
fig, ax = plt.subplots(figsize=(15, 10))  # Adjust size as needed
gdf.plot(ax=ax, marker='o', color='blue', markersize=5, label='Airport Locations')
ax.set_title('Airport Locations Worldwide')
plt.legend()
plt.show()
