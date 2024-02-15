import os
from PIL import Image


def convert_jpg_to_png(source_dir, destination_dir, keep_originals=False):
    if not os.path.exists(source_dir):
        return f"Source directory '{source_dir}' does not exist."

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files_converted = 0
    for file in os.listdir(source_dir):
        if file.endswith('.jpg'):
            file_path = os.path.join(source_dir, file)
            img = Image.open(file_path)
            file_name, _ = os.path.splitext(file)
            new_file_path = os.path.join(destination_dir, f'{file_name}.png')
            img.save(new_file_path)
            files_converted += 1

            if not keep_originals:
                os.remove(file_path)

    return f"Converted {files_converted} files to PNG format in '{destination_dir}'."


def main():
    print("Welcome to the JPG to PNG Converter!")
    source_dir = input("Enter the path to the directory containing JPG files: ")
    destination_dir = input("Enter the path to the destination directory for PNG files: ")
    keep_originals = input("Do you want to keep the original JPG files? (yes/no): ").lower() == 'yes'

    result = convert_jpg_to_png(source_dir, destination_dir, keep_originals)
    print(result)


if __name__ == "__main__":
    main()
