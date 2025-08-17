import numpy as np
import matplotlib.pyplot as plt


def load_image(image_path):
    """Load an image into a numpy array."""
    image = plt.imread(image_path)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()
    return image


def rotate_image(image, angle):
    """Rotate the image by a given angle without scaling."""
    angle_rad = np.deg2rad(angle)
    cos_angle, sin_angle = np.cos(angle_rad), np.sin(angle_rad)

    height, width = image.shape[:2]
    center_x, center_y = width / 2, height / 2

    new_image = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            # Translate to origin
            xt, yt = x - center_x, y - center_y
            # Rotate
            xr = int(xt * cos_angle + yt * sin_angle + center_x)
            yr = int(-xt * sin_angle + yt * cos_angle + center_y)
            # Translate back and assign if within bounds
            if 0 <= xr < width and 0 <= yr < height:
                new_image[yr, xr] = image[y, x]

    plt.imshow(new_image)
    plt.title("Rotated Image")
    plt.axis("off")
    plt.show()
    return new_image


def scale_image(image, sx, sy):
    """Scale the image by sx and sy factors."""
    height, width = image.shape[:2]
    new_height, new_width = int(height * sy), int(width * sx)
    new_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            source_x = int(x / sx)
            source_y = int(y / sy)
            if source_x < width and source_y < height:
                new_image[y, x] = image[source_y, source_x]

    plt.imshow(new_image)
    plt.title("Scaled Image")
    plt.axis("off")
    plt.show()
    return new_image


image = load_image("holbein.png")
rotated_image = rotate_image(image, 60)
stretched_image = scale_image(
    rotated_image, 3.0, 0.5
)  # Scale by a factor of 1.5 for both dimensions


zoomed_image = stretched_image[250:500, 2400:2650]
plt.imshow(zoomed_image)
plt.show()
