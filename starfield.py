# Standard imports for timestamping, math, plotting, noise, and color handling
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2                # Perlin noise for nebula
import colorsys                          # HSV-RGB conversion for softer color control

# ------ Generate star colors with soft (less saturated) hues using HSV model ------
def softer_star_colors(num_stars):
    colors = []
    for _ in range(num_stars):
        h = np.random.uniform(0, 1)          # Random hue (rainbow spectrum)
        s = np.random.uniform(0.2, 0.5)      # Lower saturation - less intense color
        v = np.random.uniform(0.85, 1.0)     # High value (brightness) for visible stars
        rgb = colorsys.hsv_to_rgb(h, s, v)   # Convert HSV to RGB color
        colors.append(rgb)
    return np.array(colors)                  # Returns array of RGB star colors

# ------ Create the RGB starfield with randomly placed, softly colored stars ------
def generate_starfield_rgb(w, h):
    img = np.zeros((h, w, 3))                # Create black image (height x width x RGB channels)
    star_density = np.random.uniform(0.001, 0.003)    # How many stars per pixel (random for variety)
    num_stars = int(w * h * star_density)             # Total number of stars
    xs = np.random.randint(0, w, num_stars)           # X coordinates for stars
    ys = np.random.randint(0, h, num_stars)           # Y coordinates for stars
    colors = softer_star_colors(num_stars)            # Get colors for each star
    for i in range(num_stars):
        img[ys[i], xs[i]] = colors[i]                 # Set each star pixel to its color
    return img                                        # Final starfield image (RGB)

# ------ Generate a random, softly-colored mix for the nebula tint ------
def random_color_mix_soft():
    colors = []
    for _ in range(3):
        h = np.random.uniform(0, 1)                   # Random hue
        s = np.random.uniform(0.25, 0.5)              # Lower saturation than stars
        v = np.random.uniform(0.5, 1.0)               # Variable brightness
        rgb = colorsys.hsv_to_rgb(h, s, v)
        colors.append(rgb)
    weights = np.random.dirichlet(np.ones(3), size=1)[0]  # Random weights that sum to 1
    mixed = sum(weight * np.array(color) for weight, color in zip(weights, colors))  # Weighted mix
    return mixed                                       # Single RGB tint for nebula

# ------ Create a nebula image using Perlin noise, then tint it with a random mix ------
def generate_nebula_rgb(w, h):
    # Randomize Perlin noise parameters each run for unique nebula shapes
    scale = np.random.uniform(75, 200)                # Controls size/detail of perlin patterns
    octaves = np.random.randint(4, 8)                 # More octaves = more 'turbulence'
    ox, oy = np.random.uniform(0, 1000), np.random.uniform(0, 1000)  # Noise offset so the nebula moves every run
    nebula = np.zeros((h, w))                         # One-channel (grayscale) brightness array

    # Fill nebula brightness using Perlin noise, pixel by pixel
    for y in range(h):
        for x in range(w):
            nx = (x / scale) + ox                     # Noise-space coordinate (with scaling and offset)
            ny = (y / scale) + oy
            n = pnoise2(nx, ny, octaves)              # Get perlin noise value
            nebula[y, x] = n

    nebula = nebula - nebula.min()                    # Normalize: shift so min=0
    nebula = nebula / nebula.max()                    # Now max=1
    nebula = nebula ** 1.1                            # Slight contrast enhancement for more visible clouds
    nebula *= np.random.uniform(1.05, 1.25)           # Random boost to nebula brightness
    nebula = np.clip(nebula, 0, 1)                    # Clamp to valid image intensity

    nebula_color = random_color_mix_soft()             # Get soft RGB tint for this nebula
    nebula_rgb = np.zeros((h, w, 3))                  # Prepare empty RGB nebula image
    for i in range(3):                                # For each channel (R,G,B),
        nebula_rgb[:,:,i] = nebula * nebula_color[i]  # Tint nebula map with that channel's value

    return nebula_rgb                                 # Final nebula (RGB)

# ------ Main function: generate starfield and nebula, blend, show & save image ------
def main():
    W, H = 800, 600                                   # Image size

    # Get unique timestamp for the filename
    now = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create a dark colored background (not pure black, slight cosmic tint)
    background = np.ones((H, W, 3)) * np.random.uniform(0.04, 0.09, 3)  # e.g., (0.07, 0.08, 0.05) RGB

    stars = generate_starfield_rgb(W, H)              # Star layer
    nebula = generate_nebula_rgb(W, H)                # Nebula layer

    # Blend layers using multipliers for softer look (do NOT simply add!)
    combined = background + stars * 0.65 + nebula * 0.55
    combined = np.clip(combined, 0, 1)               # Clamp values to image range

    plt.imshow(combined)                             # Show the combined cosmic image (RGB)
    plt.axis('off')                                  # No axis ticks/labels, just art!
    filename = f"starfield_{now}.png"                # Unique per run
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)  # Save to disk with tight borders
    plt.show()                                       # Open the image window for viewing

# ------ Ensure this runs only if script is executed directly ------
if __name__ == "__main__":
    main()