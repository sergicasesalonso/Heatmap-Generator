from pywinauto import Application
import time

def automate_google_earth(search_term, output_kml_path):
    # Start Google Earth Pro using the provided path
    app = Application(backend="uia").start("C:\Users\sergi\OneDrive\Escriptori\Google Earth Pro.lnk")
    time.sleep(10)  # Wait for Google Earth Pro to load completely

    # Connect to the main Google Earth Pro window
    earth_window = app.window(title_re=".*Google Earth.*")

    # Find the search bar and enter the search term
    search_box = earth_window.child_window(auto_id="search-text-box", control_type="Edit")
    search_box.set_text(search_term)
    search_box.type_keys("{ENTER}")  # Simulate pressing Enter to start the search
    time.sleep(10)  # Wait for search results to load

    # Open the File menu to save the results as a KML file
    file_menu = earth_window.child_window(title="File", control_type="MenuItem")
    file_menu.click_input()
    save_place_as = earth_window.child_window(title="Save Place As...", control_type="MenuItem")
    save_place_as.click_input()

    # Set the output file path in the Save As dialog
    save_dialog = app.window(title_re="Save As")
    save_dialog.child_window(auto_id="1001", control_type="Edit").set_text(output_kml_path)
    save_dialog.child_window(title="Save", control_type="Button").click_input()

    print(f"KML file successfully saved to: {output_kml_path}")

# Example usage
search_term = "gyms in Barcelona"
output_kml_path = r"C:\Users\sergi\Documents\gyms_in_barcelona.kml"
automate_google_earth(search_term, output_kml_path)
