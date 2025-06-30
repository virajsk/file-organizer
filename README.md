# File Organizer Script

This Python script helps you organize files in a directory by automatically sorting them into categorized folders based on their file extensions.

## Features

- Automatically creates folders for common file types:
  - Images, Videos, Audio, Documents, Archives, Executables, Code, Fonts, Design files, Ebooks, Spreadsheets
- Moves files into the appropriate folder based on their extension
- Renames files if they already exist in the target folder to avoid overwrite
- Ignores directories and only organizes files

## Supported Categories and Extensions

| Category      | Extensions                                                                 |
|---------------|----------------------------------------------------------------------------|
| Images        | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`                   |
| Videos        | `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.webm`                            |
| Audio         | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`                            |
| Documents     | `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`, `.rtf`, `.odt` |
| Archives      | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`                        |
| Executables   | `.exe`, `.msi`, `.bat`, `.sh`, `.apk`, `.dmg`, `.pkg`, `.deb`              |
| Code          | `.py`, `.js`, `.java`, `.c`, `.cpp`, `.cs`, `.html`, `.css`, `.php`, `.rb`, `.go`, `.ts` |
| Fonts         | `.ttf`, `.otf`, `.woff`, `.woff2`                                          |
| Design        | `.psd`, `.ai`, `.xd`, `.fig`, `.sketch`, `.indd`                           |
| Ebooks        | `.epub`, `.mobi`, `.azw`, `.azw3`, `.cbz`, `.cbr`                          |
| Spreadsheets  | `.csv`, `.xls`, `.xlsx`, `.ods`                                            |
| Others        | Any file types not matched above                                           |

## Usage

1. Place the `organizer.py` script in the directory you want to organize.
2. Run the script:

