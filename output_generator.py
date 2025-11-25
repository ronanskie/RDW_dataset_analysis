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
            highlight=True
        ).add_to(map)

        folium.GeoJson(
            geojson,
            tooltip=tooltip,
            style_function=lambda x: {"fillOpacity": 0, "weight": 0}
        ).add_to(map)

        # Remove default legend
        for key in list(map._children):
            if key.startswith('color_map_'):
                del map._children[key]

        # Custom HTML for legend
        legend = """
            <div style="
                position: fixed; 
                bottom: 50px; 
                left: 50px; 
                width: 150px; 
                background-color: white;
                border: 2px solid #444;
                padding: 10px;
                z-index: 9999;
                font-size: 12px;
                display: flex;
                flex-direction: column;
            ">
                <div style="margin-bottom:8px; font-weight:bold; text-align:center; width:100%;">
                    <b>Vehicles per Country</b><br>
                </div>

                <div style="display:flex; flex-direction: column; width:100%;">

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#f7fcf5;width:20px;height:20px;margin-right:8px;"></div>
                        <span>0 - 25k</span>
                    </div>

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#e5f5e0;width:20px;height:20px;margin-right:8px;"></div>
                        <span>25k - 200k</span>
                    </div>

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#c7e9c0;width:20px;height:20px;margin-right:8px;"></div>
                        <span>200k - 400k</span>
                    </div>

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#a1d99b;width:20px;height:20px;margin-right:8px;"></div>
                        <span>400k - 800k</span>
                    </div>

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#74c476;width:20px;height:20px;margin-right:8px;"></div>
                        <span>800k - 1.6M</span>
                    </div>

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#31a354;width:20px;height:20px;margin-right:8px;"></div>
                        <span>1.6M - 2.4M</span>
                    </div>

                    <div style="display:flex; align-items:center; margin-bottom:0px;">
                        <div style="background:#006d2c;width:20px;height:20px;margin-right:8px;"></div>
                        <span>2.4M - Max</span>
                    </div>
                </div>
            </div>
        """

        map.get_root().html.add_child(folium.Element(legend))

        # Save the map to an HTML file
        map.save("output_map.html")