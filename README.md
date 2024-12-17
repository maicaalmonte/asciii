To set up and run the ASCII art generation project using Python, follow these steps for installation and usage:

Installation Guide
1. Clone the repository (if it's hosted on GitHub or similar platform):

  ```bash
    git clone https://github.com/maicaalmonte/GRAPH-READING.git
    cd GRAPH-READING

 2. Create a virtual environment:
  To isolate your project dependencies, create a virtual environment with the following command:

  ```bash
   python -m venv .venv


3. Activate the virtual environment:
On Windows:

```bash
  .venv\Scripts\activate

On macOS/Linux:

```bash
  source .venv/bin/activate

4. Install the required dependencies:
Install the necessary packages listed in the requirements.txt file (you'll need to create this file if it doesn't exist, or manually install dependencies):

Create a requirements.txt file with the following content:
```bash
  Pillow

Then, install the dependencies by running:

```bash
  pip install -r requirements.txt

Alternatively, you can install the dependencies manually with:

```bash
  pip install Pillow


Project Usage
Once the virtual environment is activated and the dependencies are installed, you can run the script to convert images to ASCII art.

Create a Python file (e.g., ascii_art.py) and paste the code into it. You can use this script to generate ASCII art from any image.

Modify the image_path: Replace the image path in the image_path variable with the full path of the image you'd like to convert to ASCII art.

```python
  image_path = r"C:\Users\YourUsername\path\to\your\image.jpg"  # Update this path


Run the script:
```bash
  python ascii_art.py


Summary of Functions
grayscale_image(image_path): Converts the image to grayscale.
pixel_to_ascii(pixel_value): Maps pixel intensity to ASCII characters.
image_to_ascii(image_path, new_width=80): Converts the image into ASCII art, resizing it based on the provided width.
save_ascii_art(ascii_art, filename="ascii_art.txt"): Saves the generated ASCII art to a text file.
main(image_path): Main function to execute the process


Example Image Path
For Windows, the image_path might look like this:

```python
  image_path = r"C:\Users\YourUsername\Pictures\image.jpg"


For macOS/Linux, the path might look like:

```python
  image_path = "/Users/YourUsername/Pictures/image.jpg"









