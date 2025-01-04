Heatmap Generator
The Heatmap Generator is a web application that uses the Google Places API to fetch place data, extract coordinates, and generate a CSV file. This CSV file is then processed using Python to display the data in a Pandas DataFrame, and the results are presented as an interactive web page built with Flask, HTML, and CSS.

Features
Queries Google Places API for location data based on user input.
Extracts coordinates (latitude and longitude) and saves them as a CSV file.
Processes the CSV using Python and displays the data as a Pandas DataFrame.
Visualizes the processed data in a heatmap using HTML and CSS.
Fully functional web interface powered by Flask.
Project Structure
graphql
Copiar código
HeatMaps/
├── Static/
│   ├── heatmap.html         # Heatmap visualization
│   ├── styles.css           # Custom styles for the web app
│   ├── places.csv           # Generated CSV file with coordinates
├── Templates/
│   ├── index.html           # Main HTML page template
├── app.py                   # Main Flask application
├── places_script.py         # Script to fetch data from Google Places API
└── README.md                # Project documentation
Technologies Used
Backend:

Python 3.x
Flask (for the web framework)
Pandas (for CSV processing)
Frontend:

HTML
CSS
APIs:

Google Places API (to fetch place data)
Data:

CSV format (coordinates and place information)
Setup Instructions
1. Prerequisites
Python 3.8 or higher installed.
A Google Cloud project with the Places API enabled. Guide to Enable Places API.
2. Clone the Repository
bash
Copiar código
git clone https://github.com/sergicasesalonso/Heatmap-Generator.git
cd Heatmap-Generator
3. Install Dependencies
Use pip to install the required Python packages:

bash
Copiar código
pip install -r requirements.txt
4. Set Up Google Places API Key
Obtain your API key from Google Cloud Console.
Create a .env file in the project root and add your API key:
makefile
Copiar código
GOOGLE_API_KEY=your_google_places_api_key
5. Run the Application
Execute the script to fetch data from the Google Places API and generate the CSV:
bash
Copiar código
python places_script.py
Start the Flask web server:
bash
Copiar código
python app.py
Open your browser and go to http://127.0.0.1:5000.
How It Works
Fetch Places Data:

The app uses the Google Places API to fetch location data for specific queries (e.g., "restaurants in New York").
The places_script.py extracts coordinates (latitude and longitude) and saves the results as a CSV file.
Process Data:

The generated CSV file is read using Python's Pandas library to create a DataFrame.
The processed data is displayed on the web interface.
Display Results:

The Flask app serves the processed data as a heatmap or in tabular format.
The web interface is styled with HTML and CSS for a user-friendly experience.
Screenshots
Main Web Page
(Add a screenshot of the app's homepage or heatmap visualization.)

Pandas DataFrame Display
(Add a screenshot of the Pandas DataFrame shown on the web page.)

Future Enhancements
Add more visualization options, such as interactive maps.
Allow users to dynamically query the Google Places API from the web interface.
Optimize performance for large datasets.
Include error handling for API limits or invalid inputs.
Contributing
If you'd like to contribute to the project:

Fork the repository.
Create a feature branch:
bash
Copiar código
git checkout -b feature-name
Commit your changes and push to your forked repository.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Google Places API Documentation
Flask Documentation
Pandas Documentation
Let me know if you'd like any edits or additional sections!
