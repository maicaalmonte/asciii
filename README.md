#me just being artsy. lmao. im losing my mind. made an edit to this hundred times haha

Installation and Execution Guide for the Image-to-ASCII Script
Ensure Python is Installed: Make sure Python 3 is installed on your machine. If not, download and install it from python.org.

Run the Following Command: Open your command prompt or terminal, navigate to your project folder, and run the following single line to:

Create a virtual environment
Activate the virtual environment
Install the required dependencies
Run the script

```bash
python -m venv venv && .\venv\Scripts\activate && pip install Pillow && python -c "from PIL import Image; def grayscale_image(image_path): img = Image.open(image_path); img = img.convert('L'); return img; def pixel_to_ascii(pixel_value): ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']; return ascii_chars[pixel_value // 25]; def image_to_ascii(image_path, new_width=80): img = grayscale_image(image_path); width, height = img.size; aspect_ratio = height / width; new_height = int(aspect_ratio * new_width); img = img.resize((new_width, new_height)); ascii_str = ''; for y in range(new_height): for x in range(new_width): pixel_value = img.getpixel((x, y)); ascii_str += pixel_to_ascii(pixel_value); ascii_str += '\n'; return ascii_str; def save_ascii_art(ascii_art, filename='ascii_art.txt'): with open(filename, 'w') as f: f.write(ascii_art); def main(image_path): ascii_art = image_to_ascii(image_path); save_ascii_art(ascii_art); print('ASCII art generated and saved to ascii_art.txt'); if __name__ == '__main__': image_path = r'C:\\Users\\jamai\\Downloads\\audrey14.jpg'; main(image_path)"

