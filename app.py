from flask import Flask, request, jsonify, render_template, send_from_directory
from places_script import fetch_places, extract_place_details, save_to_csv, create_heatmap
import os
import pdfkit


app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_heatmap', methods=['POST'])
def generate_heatmap():
    data = request.json
    query = data.get('query')
    location = data.get('location')
    max_results = int(data.get('maxResults', 100))

    try:
        # File paths
        csv_filename = "static/places.csv"
        heatmap_filename = "static/heatmap.html"

        # Generate data and heatmap
        results = fetch_places(query, location, 'AIzaSyDn4CeVnXilEiMx_aVxAr_achPUwvioDkk', max_results)
        places = extract_place_details(results)
        save_to_csv(places, csv_filename)
        create_heatmap(csv_filename, heatmap_filename)

        return jsonify(success=True, heatmap_url=f"/{heatmap_filename}")
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


if __name__ == "__main__":
    app.run(debug=True)
