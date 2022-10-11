from flask import Flask, render_template
import folium

app = Flask(__name__)
start_coords = (40.428285284058816, -3.7070024693800345)

@app.route('/')
def index():
    folium_map = folium.Map(location=start_coords, zoom_start=10)
    folium_map.save('templates/map.html')
    return render_template('index.html')


@app.route('/templates/map')
def reload_map():
    # TODO: Reload map with the selected options
    folium_map = folium.Map(location=start_coords, zoom_start=10)
    folium_map.save('templates/map.html')
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)