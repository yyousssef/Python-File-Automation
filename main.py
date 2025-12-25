import os
import shutil

SOURCE_FOLDER = "downloads"
FILE_TYPES = {
    "PDFs": ['.pdf'],
    "IMAGES": ['.jpg', '.png', '.jpeg'],
    "Text": ['.txt', '.csv']
}
for folder in FILE_TYPES:
  folder_path = os.path.join(SOURCE_FOLDER, folder)
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for file in os.listdir(SOURCE_FOLDER):
  file_path = os.path.join(SOURCE_FOLDER, file)
  if os.path.isfile(file_path):
    file_ext = os.path.splitext(file)[1].lower()
    for floder, extensions in FILE_TYPES.items():
      if file_ext in extensions:
        destination = os.path.join(SOURCE_FOLDER, floder, file)
        shutil.move(file_path, destination)
        print(f"moved {file} to {folder}")
