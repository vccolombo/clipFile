import argparse
import os
import sys

import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def main():
    parser = argparse.ArgumentParser(
        description="Copy file content to clipboard"
    )

    parser.add_argument('File',
        metavar='file',
        type=str,
        help="Path to file to be copied to clipboard"
    )

    args = parser.parse_args()
    file_path = args.File

    if os.path.isfile(file_path):
        file = open(file_path, "r")

        file_text = file.read()
        copy_to_clipboard(file_text)
    else:
        print(f'ERROR: {file_path} does not exists or is not a file')

