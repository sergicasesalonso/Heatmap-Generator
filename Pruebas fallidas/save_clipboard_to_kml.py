import pyperclip

# Get clipboard content
clipboard_content = pyperclip.paste()

# Define the output file path
output_path = r"C:\Users\sergi\OneDrive\Escriptori\HeatMaps\KML\output.kml"

# Write the content to the file
with open(output_path, "w", encoding="utf-8") as file:
    file.write(clipboard_content)

print(f"Clipboard content saved to {output_path}")
