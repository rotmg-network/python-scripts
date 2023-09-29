import struct

def offset_count_pair(offset, count):
    print("Found Offset + Count: ", offset, count)
    correct_order.append(offset)
    correct_order.append(count)
    incorrect_order.remove(offset)
    incorrect_order.remove(count)

#function that find the offsets and counts        
def find_offset_count_pair(offset: int):
    for sizeI in incorrect_order:
        next_offset = offset + sizeI
        if next_offset in incorrect_order:
            if next_offset == offset:
                if len(incorrect_order) <= 6:
                    pass
                else:
                    continue
            offset_count_pair(offset, sizeI)
            if find_offset_count_pair(next_offset):
                return True
            
    closest_offset_value = 999999999
    closest_count = None
    closest_offset = None
    for countK in incorrect_order:
        next_offset = offset + countK
        for offsetK in incorrect_order:
            if offsetK == offset or offsetK < next_offset:
                continue
            value = offsetK - next_offset
            if value < closest_offset_value:
                closest_count = countK
                closest_offset = offsetK
                closest_offset_value = value

        if closest_offset_value <= 20:
            if len(incorrect_order) == 2:
                offset_count_pair(max(incorrect_order), min(incorrect_order))
                return True
            
            offset_count_pair(offset, closest_count)
            if find_offset_count_pair(closest_offset):
                return True
            
    return False


# Define the format for a single int32_t value (4 bytes)
with open('metadataheader.dat', 'rb') as file:
    binary_data = file.read(256)
incorrect_order = list(struct.unpack('i' * (len(binary_data) // struct.calcsize('i')), binary_data))

#checking for sanity and version
sanity = None
if -89056337 in incorrect_order:
    incorrect_order.remove(-89056337)
    sanity = -89056337
else:
    print("didnt find sanity")
    exit(1)

version = None
if 29 in incorrect_order:
    incorrect_order.remove(29)
    version = 29
else:
    print("didnt find version")
    exit(1)

string_offset = min([x for x in incorrect_order if x != 0])
correct_order = [sanity, version]

success = find_offset_count_pair(string_offset)
if not success:
    print("Failed to find correct order")
    exit(1)
else:
    print("Success!")

with open('fixed_metadataheader.dat', 'wb') as file:
    for value in correct_order:
        packed_value = struct.pack('i', value)
        file.write(packed_value)