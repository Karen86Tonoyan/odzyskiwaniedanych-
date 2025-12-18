#!/usr/bin/env python3
"""
Data Recovery Tool - Odzyskiwanie Danych
A simple open-source tool for recovering deleted files.
"""

import os
import sys
import argparse
from pathlib import Path


# Common file signatures (magic bytes)
FILE_SIGNATURES = {
    'jpg': {
        'header': b'\xFF\xD8\xFF',
        'footer': b'\xFF\xD9',
        'ext': '.jpg'
    },
    'png': {
        'header': b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A',
        'footer': b'\x49\x45\x4E\x44\xAE\x42\x60\x82',
        'ext': '.png'
    },
    'pdf': {
        'header': b'%PDF-',
        'footer': b'%%EOF',
        'ext': '.pdf'
    },
    'zip': {
        'header': b'\x50\x4B\x03\x04',
        'footer': None,
        'ext': '.zip'
    },
    'gif': {
        'header': b'\x47\x49\x46\x38',
        'footer': b'\x00\x3B',
        'ext': '.gif'
    },
}


class DataRecovery:
    """Main class for data recovery operations."""
    
    def __init__(self, scan_path, output_path, file_type=None):
        """
        Initialize the data recovery tool.
        
        Args:
            scan_path: Path to scan for deleted files
            output_path: Path to save recovered files
            file_type: Specific file type to recover (None = all types)
        """
        self.scan_path = Path(scan_path)
        self.output_path = Path(output_path)
        self.file_type = file_type
        self.recovered_count = 0
        
        # Create output directory if it doesn't exist
        self.output_path.mkdir(parents=True, exist_ok=True)
    
    def scan_for_files(self):
        """
        Scan the specified path for recoverable files.
        """
        print(f"🔍 Scanning: {self.scan_path}")
        print(f"📁 Output directory: {self.output_path}")
        
        # Determine which file types to scan for
        if self.file_type:
            if self.file_type.lower() in FILE_SIGNATURES:
                signatures = {self.file_type.lower(): FILE_SIGNATURES[self.file_type.lower()]}
            else:
                print(f"❌ Unsupported file type: {self.file_type}")
                return
        else:
            signatures = FILE_SIGNATURES
        
        print(f"🔎 Looking for file types: {', '.join(signatures.keys())}")
        
        # Scan files in the directory
        if self.scan_path.is_file():
            self._scan_file(self.scan_path, signatures)
        elif self.scan_path.is_dir():
            for root, dirs, files in os.walk(self.scan_path):
                for file in files:
                    file_path = Path(root) / file
                    self._scan_file(file_path, signatures)
        else:
            print(f"❌ Invalid path: {self.scan_path}")
            return
        
        print(f"\n✅ Recovery complete! Recovered {self.recovered_count} file(s)")
    
    def _scan_file(self, file_path, signatures):
        """
        Scan a single file for recoverable data.
        
        Args:
            file_path: Path to the file to scan
            signatures: Dictionary of file signatures to look for
        """
        try:
            # Skip if file is in output directory
            if self.output_path in file_path.parents or file_path.parent == self.output_path:
                return
            
            with open(file_path, 'rb') as f:
                data = f.read()
            
            # Check for file signatures
            for file_type, sig_info in signatures.items():
                header = sig_info['header']
                footer = sig_info.get('footer')
                
                # Look for all occurrences of this file type
                search_offset = 0
                while True:
                    # Look for header in the file data
                    offset = data.find(header, search_offset)
                    if offset == -1:
                        break  # No more occurrences found
                    
                    if footer:
                        # Look for footer after header
                        footer_offset = data.find(footer, offset + len(header))
                        if footer_offset != -1:
                            # Extract the file content
                            file_data = data[offset:footer_offset + len(footer)]
                            self._save_recovered_file(file_data, file_type, sig_info['ext'])
                            search_offset = footer_offset + len(footer)
                        else:
                            # No footer found, skip this occurrence
                            search_offset = offset + len(header)
                    else:
                        # No footer specified, save from header to end
                        file_data = data[offset:]
                        self._save_recovered_file(file_data, file_type, sig_info['ext'])
                        break  # Only one occurrence possible without footer
        
        except (PermissionError, IOError) as e:
            # Skip files that can't be read due to permissions or I/O errors
            pass
        except Exception as e:
            # Log unexpected errors but continue
            print(f"⚠ Warning: Error scanning {file_path}: {e}")
    
    def _save_recovered_file(self, data, file_type, extension):
        """
        Save recovered file data to the output directory.
        
        Args:
            data: Binary data of the recovered file
            file_type: Type of the file
            extension: File extension
        """
        self.recovered_count += 1
        filename = f"recovered_{file_type}_{self.recovered_count:04d}{extension}"
        output_file = self.output_path / filename
        
        try:
            with open(output_file, 'wb') as f:
                f.write(data)
            print(f"✓ Recovered: {filename} ({len(data)} bytes)")
        except Exception as e:
            print(f"✗ Failed to save {filename}: {e}")


def main():
    """Main entry point for the data recovery tool."""
    parser = argparse.ArgumentParser(
        description='Data Recovery Tool - Recover deleted files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python recovery.py --scan /path/to/scan
  python recovery.py --scan . --type jpg --output ./my_recovered
  python recovery.py --scan /dev/sdb1 --output ./recovered_files
        """
    )
    
    parser.add_argument(
        '--scan',
        required=True,
        help='Path to scan for deleted files'
    )
    
    parser.add_argument(
        '--output',
        default='./recovered_files',
        help='Directory to save recovered files (default: ./recovered_files)'
    )
    
    parser.add_argument(
        '--type',
        help='Specific file type to recover (jpg, png, pdf, zip, gif)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("  Data Recovery Tool - Odzyskiwanie Danych")
    print("  Open Source File Recovery")
    print("=" * 60)
    print()
    
    # Create recovery instance and start scanning
    recovery = DataRecovery(args.scan, args.output, args.type)
    recovery.scan_for_files()


if __name__ == '__main__':
    main()
