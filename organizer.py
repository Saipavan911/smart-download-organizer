from pathlib import Path
import os
import shutil

# ✅ Auto-detect Downloads
source_dir = str(Path.home() / "Downloads")
destination_base_dir = 'C:/Users/Saipa/OneDrive/Desktop/Test_download'

f = os.listdir(source_dir)

file_types = {
    ".pdf": "PDF_files",
    ".jpeg": "Images",
    ".jpg": "Images",
    ".png": "Images",
    ".docx": "Documents",
    ".doc": "Documents"
}

# 🔒 Ask once
skip_input = input("Enter file name keywords to skip (comma separated): ")
skip_keywords = [k.strip().lower() for k in skip_input.split(",") if k.strip()]

# 🛡️ Dry run choice
dry_run_input = input("Enable DRY RUN? (yes/no): ").strip().lower()
dry_run = dry_run_input == "yes"

if dry_run:
    print("\n🟡 DRY RUN MODE ENABLED — No files will be moved\n")
else:
    print("\n🔴 LIVE MODE — Files WILL be moved\n")

summary = {}

for file in f:
    file_lower = file.lower()

    # 🔒 Skip protection
    skip_this = False
    for keyword in skip_keywords:
        if keyword in file_lower:
            print(f"⚠️ Skipping protected file: {file}")
            skip_this = True
            break

    if skip_this:
        continue

    item_full_path = os.path.join(source_dir, file)
    if not os.path.isfile(item_full_path):
        continue

    matched = False

    for ext in file_types:
        if file_lower.endswith(ext):
            matched = True
            folder_name = file_types[ext]

            source_path = os.path.join(source_dir, file)
            target_folder_path = os.path.join(destination_base_dir, folder_name)
            destination_file_path = os.path.join(target_folder_path, file)

            if not os.path.exists(target_folder_path):
                if not dry_run:
                    os.mkdir(target_folder_path)
                print(f"📁 Would create folder: {target_folder_path}")

            if os.path.exists(destination_file_path):
                name, extension = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_file_path):
                    newfile_name = name + "_" + str(counter) + extension
                    destination_file_path = os.path.join(target_folder_path, newfile_name)
                    counter += 1

            # 🛡️ DRY RUN GUARD
            if not dry_run:
                shutil.move(source_path, destination_file_path)
                summary[folder_name] = summary.get(folder_name, 0) + 1

            print(f"➡️ {'Would move' if dry_run else 'Moved'} '{file}' → '{destination_file_path}'")
            break

    if not matched:
        folder_name = "Others"
        source_path = os.path.join(source_dir, file)
        target_folder_path = os.path.join(destination_base_dir, folder_name)
        destination_file_path = os.path.join(target_folder_path, file)

        if not os.path.exists(target_folder_path):
            if not dry_run:
                os.mkdir(target_folder_path)
            print(f"📁 Would create folder: {target_folder_path}")

        if os.path.exists(destination_file_path):
            name, extension = os.path.splitext(file)
            counter = 1
            while os.path.exists(destination_file_path):
                newfile_name = name + "_" + str(counter) + extension
                destination_file_path = os.path.join(target_folder_path, newfile_name)
                counter += 1

        if not dry_run:
            shutil.move(source_path, destination_file_path)
            summary[folder_name] = summary.get(folder_name, 0) + 1

        print(f"➡️ {'Would move' if dry_run else 'Moved'} '{file}' → '{destination_file_path}'")

# ✅ Summary only for live mode
if not dry_run:
    print("\n***************************************** SUMMARY *****************************************")
    for key, value in summary.items():
        print(f"{key} : {value}")
