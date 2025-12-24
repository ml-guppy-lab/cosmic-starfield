# cosmic-starfield

# Cosmic Starfield Generator

Generate beautiful, natural-looking cosmic starfields with randomized nebulae and stars — no datasets or machine learning required!  
Every run produces a unique image inspired by astrophotography.

---

## Features

- Realistic nebula clouds using Perlin noise
- Soft, natural star and nebula colors
- Unique, non-repeating images saved with timestamps
- Easy Python setup; pure numpy and matplotlib
- Modular functions (easy to extend for animation or effects)
- Animated cosmos

---

## Installation 

1. **Clone this repository**

    ```bash
    git clone https://github.com/yourusername/cosmic_starfield.git
    cd cosmic_starfield
    ```

2. **(Recommended) Create and activate a Python virtual environment**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

- **Generate a cosmic image**

    ```bash
    python starfield.py
    ```

    Each run creates a new PNG file in the folder, uniquely named by date/time.

- **Animate starfields (optional)**

    ```bash
    python animate_starfield.py
    ```

    This displays an animated moving nebula over a static starfield.  
    Set `save_gif=True` in `animate_starfield.py` to save it as a GIF.

---

## Customization

- Tweak nebula brightness, colors, size, or star density directly in the code
- Use your own resolution (change `W, H`)
- Combine with other scripts for batch generation or gallery creation

---

## Example Output

see attached png images

---

## License

MIT License — Free for personal and commercial use.

---

## Credits

- Perlin noise using Ken Perlin’s original `noise` library.
- Inspiration: astrophotography and Python creative coding community.

---

## Contact

Questions or ideas? Open an issue or contact [themlguppie@gmail.com].
