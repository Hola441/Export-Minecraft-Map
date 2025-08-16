"""Script used to download a minecraft map as an image file."""

import argparse
import os
from nbtlib import load
from PIL import Image

MAP_COLORS = ['Transparent', (127, 178, 56), (247, 233, 163), (199, 199, 199), (255, 0, 0),
              (160, 160, 255), (167, 167, 167), (0, 124, 0), (255, 255, 255), (164, 168, 184),
              (151, 109, 77), (112, 112, 112), (64, 64, 255), (143, 119, 72), (255, 252, 245),
              (216, 127, 51), (178, 76, 216), (102, 153, 216), (229, 229, 51), (127, 204, 25),
              (242, 127, 165), (76, 76, 76), (153, 153, 153), (76, 127, 153), (127, 63, 178),
              (51, 76, 178), (102, 76, 51), (102, 127, 51), (153, 51, 51), (25, 25, 25),
              (250, 238, 77), (92, 219, 213), (74, 128, 255), (0, 217, 58), (129, 86, 49),
              (112, 2, 0), (209, 177, 161), (159, 82, 36), (149, 87, 108), (112, 108, 138),
              (186, 133, 36), (103, 117, 53), (160, 77, 78), (57, 41, 35), (135, 107, 98),
              (87, 92, 92), (122, 73, 88), (76, 62, 92), (76, 50, 35), (76, 82, 42), (142, 60, 46),
              (37, 22, 16), (189, 48, 49), (148, 63, 97), (92, 25, 29), (22, 126, 134),
              (58, 142, 140), (86, 44, 62), (20, 180, 133), (100, 100, 100), (216, 175, 147)]
MAP_MULTIPLIER = [0.71, 0.86, 1, 0.53]

def export_map(dat_file, display_image = False, output_file = None):
    """Export minecraft map to be saved as an image.
    
    Arguments:
        dat_file: File location of map data file.

        display_image: Define whether to pop up the map image or not.
            The default value is False.

        output_file: File location to save image.
            If left blank or set to None, the image is not saved.
    """

    if not os.path.exists(dat_file):
        print(f"Error: No map file exists at: {dat_file}")
        return

    # Load NBT data
    nbt_data = load(dat_file)

    colors = nbt_data['data']['colors']  # This is the byte array of color indexes

    img = Image.new('RGB', (128, 128))
    pixels = img.load()

    for y in range(128):
        for x in range(128):
            color_id = colors[y * 128 + x] & 0xFF
            block_id = color_id // 4
            multiplier_id = color_id % 4
            if block_id < len(MAP_COLORS):
                block_color = MAP_COLORS[block_id]
                color_shift = MAP_MULTIPLIER[multiplier_id]
                pixels[x, y] = tuple(round(b * color_shift) for b in block_color)
            else:
                pixels[x, y] = (255, 0, 255)  # magenta for missing color

    if output_file:
        try:
            img.save(output_file)
            print(f"Saved map image to {output_file}")
        except Exception as e:
            print(f"Error saving image: {e}")
    if display_image:
        try:
            img.show()
        except Exception as e:
            print(f"Error opening image: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Download a minecraft map as an image file")
    parser.add_argument("input", type = str, help = "Example: Input\\File\\map_#.dat")
    parser.add_argument("-d", "--display", help = "Open up the map image. Example: True")
    parser.add_argument("-o", "--output", help = "Example: Output\\File\\minecraft_map.png")

    argument = parser.parse_args()

    DISPLAY = str(argument.display).strip().lower() in ('true', 'yes', 'y', '1')
    export_map(argument.input, DISPLAY, argument.output)
