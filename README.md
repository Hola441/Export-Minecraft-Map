# Minecraft Map Exporter

A Python script to convert a Minecraft `.dat` map file into an image file (`.png`, `.jpg`, etc.). This can be useful for extracting in-game maps for use in projects, sharing, or archival purposes.

## Features
- Reads Minecraft `map_#.dat` files (NBT format).
- Uses Minecraft's **official map color palette** for accurate rendering.
- Optionally displays the generated image in a viewer.
- Saves the image to a file if specified.

---

## Requirements

This script uses the following Python packages:
- [nbtlib](https://pypi.org/project/nbtlib/) — for reading Minecraft NBT data.
- [Pillow](https://pypi.org/project/Pillow/) — for creating and saving images.

Install dependencies:
```bash
pip install nbtlib pillow
```

---

## Usage

### Command
```bash
python export_minecraft_map.py <input_map_file> [options]
```

### Arguments
| Argument | Description |
|----------|----------|
| input_map_file | Path to the Minecraft .dat map file (e.g. Input/File/map_0.dat). |
| -d, --display | Whether to open the image after creating it. Accepted values to display the image: true, yes, y, 1 |
| -o, --output | Path to save the output image (e.g. Output/File/minecraft_map.png). If omitted, the image will not be saved. |

### Examples

#### Export and Save Only
```bash
python export_map.py saves/MyWorld/data/map_0.dat -o output_map.png
```

#### Export and Display
```bash
python export_map.py saves/MyWorld/data/map_0.dat -d true
```

#### Export, Display, and Save
```bash
python export_map.py saves/MyWorld/data/map_0.dat -d yes -o output_map.png
```

## Script Details
 - **Map Size:** Always renders as 128 × 128 pixels (Minecraft's default map resolution).
 - **Color Palette:** Matches the official Minecraft map colors, including shading multipliers for different brightness levels.
 - **Missing Colors:** If a color ID is missing from the palette, it is shown as magenta (255, 0, 255).

## Notes
The script works for both vanilla and most modded Minecraft worlds, provided the .dat format matches the official structure.

Works with both singleplayer and multiplayer map files (you just need to locate them in the world folder).

Map color information was retrieved from the [Minecraft Wiki](https://minecraft.wiki/w/Map_item_format#Color_table)

## License
This script is released under the MIT License — feel free to use and modify it for personal or commercial projects.
