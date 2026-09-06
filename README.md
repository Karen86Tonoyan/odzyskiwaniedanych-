# Odzyskiwanie Danych

> **Educational Python signature-carving utility for selected embedded file formats**

This repository contains a small command-line script that scans a file or a
directory recursively for selected byte signatures and writes extracted byte
ranges to an output directory. It is a simple file-carving experiment, not a
replacement for forensic recovery software such as PhotoRec or TestDisk.

## Supported signatures

`recovery.py` currently recognises:

- JPEG (`jpg`);
- PNG (`png`);
- PDF (`pdf`);
- ZIP (`zip`);
- GIF (`gif`).

For formats with a footer, the script writes data from the header through the
first matching footer. ZIP output is written from its header to the end of the
scanned file.

## Use

The script uses the Python standard library:

```bash
python recovery.py --scan . --type jpg --output ./recovered_files
```

General form:

```text
python recovery.py --scan PATH [--output DIRECTORY] [--type jpg|png|pdf|zip|gif]
```

`example.py` supplies an additional example. Always write output to a different
location than the scanned source.

## Important limitations

The program reads files into memory and does not parse filesystems, deleted
file tables, partitions or fragmented files. It can produce incomplete,
duplicate or false-positive extracts. Never write to a drive or image that is
being recovered; make a verified copy and use specialist tools for important
data or forensic work.

## Contribution and licence

See `CONTRIBUTING.md` for contribution guidance. `LICENSE` is MIT.
