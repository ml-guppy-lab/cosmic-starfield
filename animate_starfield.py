# Import nebula and starfield-generating functions from your starfield.py module
from starfield import generate_starfield_rgb, generate_nebula_rgb
import matplotlib.pyplot as plt                    # For plotting
from matplotlib.animation import FuncAnimation     # For animation
import numpy as np                                # For numerical manipulation (esp. np.roll)

# ----------- Function to animate the starfield and nebula movement -----------

def animate_starfield(w=800, h=600, frames=120, save_gif=False):
    """
    Generate an animated space scene by shifting the nebula horizontally
    over a static starfield. Optionally save as GIF.
    """
    # Generate one random RGB starfield (static background)
    starfield = generate_starfield_rgb(w, h)

    # Generate one random RGB nebula (Perlin noise colored cloud)
    nebula = generate_nebula_rgb(w, h)

    # OPTIONAL: Exaggerate the nebula's contrast for animation (more dramatic movement)
    # nebula = nebula ** 2       # This step is optional and might be omitted for more color

    # Set up the figure and axes for displaying the animation
    fig = plt.figure(figsize=(8,6))
    plt.axis('off')             # Hide axes for a clean cosmic look

    # Initial frame: combine starfield and nebula, clipped to [0, 1] range for image
    # Note: Since starfield and nebula are already RGB, don't use a cmap here!
    img = plt.imshow(np.clip(starfield + nebula*0.5, 0, 1))

    # ----------- Animation update function -----------

    def update(frame):
        """
        Animate nebula by shifting its pixels horizontally.
        The stars remain fixed; nebula appears to flow across.
        """
        shift = frame   # Each frame, shift nebula right by 'frame' pixels
        nebula_shifted = np.roll(nebula, shift, axis=1)  # Shift right along x (axis=1)
        im = np.clip(starfield + nebula_shifted*0.5, 0, 1)  # Blend shifted nebula over stars
        img.set_array(im)   # Update displayed image data
        return [img]        # Return updated image handle (required by FuncAnimation)

    # ----------- Create and run the animation -----------

    anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
    # - frames: Number of animation frames (e.g., 120 frames)
    # - interval: Delay between frames in ms (e.g., 50ms -> ~20fps)
    # - blit: Only update image data for efficiency

    if save_gif:
        # Save the animation as an animated GIF using Pillow
        anim.save("starfield_animated.gif", writer="pillow", dpi=80)
    else:
        # Show animation in a pop-up window
        plt.show()

# ----------- Main entry point: run animation, don't save to GIF by default -----------
if __name__ == "__main__":
    animate_starfield(save_gif=False)