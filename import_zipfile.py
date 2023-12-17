import zipfile
import os
import shutil

def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Berkas diekstrak ke: {extract_to}")

def create_zip(zip_name, files_to_zip):
    with zipfile.ZipFile(zip_name, 'w') as zip_ref:
        for file in files_to_zip:
            zip_ref.write(file, os.path.basename(file))
    print(f"Berkas ZIP dibuat: {zip_name}")

def add_to_zip(zip_name, files_to_add):
    with zipfile.ZipFile(zip_name, 'a') as zip_ref:
        for file in files_to_add:
            zip_ref.write(file, os.path.basename(file))
    print(f"Berkas ditambahkan ke {zip_name}")

def remove_from_zip(zip_name, files_to_remove):
    temp_zip = "temp.zip"
    with zipfile.ZipFile(zip_name, 'r') as zip_read, zipfile.ZipFile(temp_zip, 'w') as zip_write:
        for item in zip_read.infolist():
            if item.filename not in files_to_remove:
                data = zip_read.read(item.filename)
                zip_write.writestr(item, data)
    os.remove(zip_name)
    os.rename(temp_zip, zip_name)
    print(f"Berkas dihapus dari {zip_name}")

def compress_file(file_path, compressed_path):
    with zipfile.ZipFile(compressed_path + ".zip", 'w', zipfile.ZIP_DEFLATED) as zip_ref:
        zip_ref.write(file_path, os.path.basename(file_path))
    print(f"Berkas dikompresi dan ditambahkan ke {compressed_path}.zip")

def add_to_zip_with_compression(zip_name, files_to_add, compression_extensions=['txt']):
    with zipfile.ZipFile(zip_name, 'a') as zip_ref:
        for file in files_to_add:
            file_extension = os.path.splitext(file)[1][1:]
            if file_extension in compression_extensions:
                compressed_path = f"{os.path.splitext(file)[0]}_compressed"
                compress_file(file, compressed_path)
                zip_ref.write(compressed_path + ".zip", os.path.basename(compressed_path + ".zip"))
                os.remove(compressed_path + ".zip")
            else:
                zip_ref.write(file, os.path.basename(file))
    print(f"Berkas ditambahkan (dengan kompresi) ke {zip_name}")
    
def add_folder_to_zip(zip_name, folder_name, files_to_add):
    with zipfile.ZipFile(zip_name, 'a') as zip_ref:
        for file in files_to_add:
            file_path_in_zip = os.path.join(folder_name, os.path.basename(file))
            zip_ref.write(file, arcname=file_path_in_zip)
    print(f"Folder '{folder_name}' dan file-filenya ditambahkan ke {zip_name}")
  
# Contoh penggunaan:
# extract_zip('example.zip', 'extracted_files')
# create_zip('new_archive.zip', ['file1.txt', 'file2.txt'])
# add_to_zip('existing_archive.zip', ['file3.txt', 'file4.txt'])
# remove_from_zip('archive_to_modify.zip', ['file_to_remove.txt'])
# compress_file('file_to_compress.txt', 'compressed_file')
# add_to_zip_with_compression('existing_archive.zip', ['file3.txt', 'file4.txt'])
# add_folder_to_zip('existing_archive.zip', 'new_folder', ['file5.txt', 'file6.txt'])