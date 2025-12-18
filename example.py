#!/usr/bin/env python3
"""
Example script demonstrating the data recovery tool usage.
This creates some test files and then shows how to recover them.
"""

import os
import shutil
from pathlib import Path

# Create a test directory
test_dir = Path('./test_recovery')
test_dir.mkdir(exist_ok=True)

print("Creating test files...")

# Create a simple text file with embedded image signature
# This simulates a scenario where file fragments might be found
test_file = test_dir / 'test_data.bin'

# JPG signature
jpg_data = b'\xFF\xD8\xFF\xE0\x00\x10JFIF\x00' + b'X' * 100 + b'\xFF\xD9'

# PDF signature  
pdf_data = b'%PDF-1.4\n' + b'Some PDF content here...' + b'\n%%EOF'

# PNG signature
png_data = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' + b'PNG data...' + b'\x49\x45\x4E\x44\xAE\x42\x60\x82'

# Write combined data to a file
with open(test_file, 'wb') as f:
    f.write(b'Some random data before...')
    f.write(jpg_data)
    f.write(b'Some data in between...')
    f.write(pdf_data)
    f.write(b'More random data...')
    f.write(png_data)
    f.write(b'Random data at the end...')

print(f"✓ Created test file: {test_file}")
print(f"  File size: {test_file.stat().st_size} bytes")
print()

print("Now run the recovery tool:")
print(f"  python recovery.py --scan {test_dir} --output ./recovered_test")
print()
print("Or to recover only JPG files:")
print(f"  python recovery.py --scan {test_dir} --type jpg --output ./recovered_test")
print()
print("After recovery, check the ./recovered_test directory for recovered files.")
