
import os
import zipfile

fantasy_zip = zipfile.ZipFile('/mnt/FORALL/BACKUP/backup.zip', 'w')
for folder, subfolders, files in os.walk('/mnt/FORALL/PYTHON'):
    for file in files:
        fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), '/mnt/FORALL/PYTHON'), compress_type = zipfile.ZIP_DEFLATED)

fantasy_zip.close()