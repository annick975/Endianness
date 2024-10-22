# Endianness Converter

A Python tool that converts 32-bit binary files from **little-endian** to **big-endian** format. Endianness refers to the order of bytes in binary data, and this tool helps to swap the byte order for 32-bit values in a file.

## Features
- Converts 32-bit binary data from little-endian to big-endian.
- Automatically pads incomplete 32-bit values with zeros.
- Supports processing any binary file.

## Requirements
- Python 3.x

## Installation
Clone the repository:
```bash
git clone https://github.com/annick975/Endianness_converter.git
cd Endianness_converter
 ```
## Usage
Run the script from the command line as follows:
```bash
python convert_endianness.py <input_file> <output_file>
```
- **<input_file>**: Path to the binary file that you want to convert from little-endian to big-endian.
- **<output_file>**: Path where the converted big-endian file will be saved.

Feel free to contribute by opening issues or submitting pull requests!
