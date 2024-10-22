import struct
import sys

def convert_endianness(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            # Reading 4 bytes (32-bit integer)
            bytes_data = infile.read(4)
            if not bytes_data: 
                break
            
            # Ensure we have exactly 4 bytes before unpacking
            if len(bytes_data) == 4:

                # Unpacking  the little-endian integer and pack it back as big-endian

                little_endian_value = struct.unpack('<I', bytes_data)[0]
                big_endian_bytes = struct.pack('>I', little_endian_value)

                # Writing the big-endian bytes to the output file

                outfile.write(big_endian_bytes)
            elif len(bytes_data) < 4:

                # Pad the remaining bytes with zeros
                bytes_data += b'\x00' * (4 - len(bytes_data))  
                little_endian_value = struct.unpack('<I', bytes_data)[0]
                big_endian_bytes = struct.pack('>I', little_endian_value)
                outfile.write(big_endian_bytes)
                print(f"Warning: Incomplete data read, expected 4 bytes but got {len(bytes_data)}. Padding with zeros.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_endianness.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_endianness(input_file, output_file)
    print(f"Converted '{input_file}' from little-endian to big-endian and saved as '{output_file}'.")
