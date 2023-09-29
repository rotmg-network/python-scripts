import re
#This script is for extracting the objects aswell as tiles from resource.assets, it puts them into two files objects.xml and tiles.xml, which are used the grab all game data,
#made to be easy to update all game data, if update just put resource.assets in the resources folder and run this script to update data
#only error that can happen is that in objects.xml there can be a weirdly formatted line, just delete it and should be fine


# Define the input file path and output file path
input_file_path = 'resources.assets'
object_output_file_path = 'objects.xml'
tile_output_file_path = 'tiles.xml'

# Read the entire content of the input file
with open(input_file_path, 'r', encoding='ISO-8859-1') as input_file:
    input_content = input_file.read()

objects_pattern = re.compile(r'<Objects>.*?</Objects>', re.DOTALL)
object_matches = objects_pattern.findall(input_content)

tiles_pattern = re.compile(r'<GroundTypes>.*?</GroundTypes>', re.DOTALL)
tile_matches = tiles_pattern.findall(input_content)

# Write the extracted XML content to the output file
with open(object_output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    output_file.write(object_matches[0][:-11])
    for match in object_matches[1:-1]:
        if match != object_matches[0] or object_matches[-1]:
            output_file.write(match[10:-11] + '\n')
            pass
    output_file.write(object_matches[-1][10:])

with open(tile_output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
    output_file.write(tile_matches[0][:-15])
    for match in tile_matches[1:-1]:
        if match != tile_matches[0] or tile_matches[-1]:
            output_file.write(match[14:-15] + '\n')
            pass
    output_file.write(tile_matches[-1][14:])