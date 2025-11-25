# output_generator.py
# Generate output like plots from dataframes

# Import libraries
import folium
import pandas as pd
import requests

class Output_Generator:

    '''
    generate_plot(data): generate a plot from a 2D array
    data: the 2D array of which a plot will be generated
    '''
    def generate_plot(self, data):
        df = pd.DataFrame(data, columns=["name", "count"])
        df = df[df['name'] != 'Unknown']
        df["count"] = df["count"].astype(int)

        url = "https://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
        geojson = requests.get(url).json()

        df_dict = df.set_index("name")["count"].to_dict()

        for feature in geojson["features"]:
            cname = feature["properties"]["name"]
            feature["properties"]["count"] = df_dict.get(cname, 0)

        max_count = df["count"].max()

        map = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron no labels")

        tooltip = folium.GeoJsonTooltip(
            fields=["name", "count"],
            aliases=["Country:", "Amount:"],
            localize=True,
            labels=True,
            sticky=False,
            style=("""
                   background-color: white; 
                   color: black; 
                   font-family: "Courier New", Courier, monospace; 
                   font-size: 10pt; 
                   padding: 5px;
                """
            )
        )

        folium.Choropleth(
            geo_data=geojson,
            data=df,
            columns=['name', 'count'],
            key_on="feature.properties.name",
            fill_color="YlGn",
            fill_opacity=0.8,
            line_opacity=0.2,
            nan_fill_color="white",
            bins=[0, 25000, 200000, 400000, 800000, 1600000, 2400000, max_count],
            legend_name="Number of Vehicles per Country",
            highlight=True
        ).add_to(map)

        folium.GeoJson(
            geojson,
            tooltip=tooltip,
            style_function=lambda x: {"fillOpacity": 0, "weight": 0}
        ).add_to(map)

        map.save("output_map.html")