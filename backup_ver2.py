'''
TODO
1 Сохранять в архив все в целевых папках
2 Выводить отчет об удавшейся/неудавшейся операции
3 Брать список папок и места назначения из txt файла
4 Сделать проверку на существование целевых папок
5 Интерактивный режим? Ключи с целевыми директориями?
'''

import os
import time
import zipfile

source_list = ['/mnt/FORALL/PYTHON/', '/home/awe/git']	#list of target directories

tatget_dir = '/mnt/FORALL/BACKUP/'	#directory for backup files

today = tatget_dir + os.sep + time.strftime('%Y%m%d')	#string with today date for making directory
now = time.strftime('%H%M%S')	#string with time for naming backup file 

if not os.path.exists(today):	#if directory yet exist - make it
	os.makedirs(today)
	print('Каталог успешно создан', today)

target = today + os.sep + now + '.zip'	#full path and name for backup file

with zipfile.ZipFile(target, 'w') as backup_zip:	#open file for writing
	for source in source_list:	#watching all path list
		source_up = str(os.path.split(source)[:-1])
		print(source_up, "My Print!")
		for folder, subfolders, files in os.walk(source):	#collecting all directories and files
			for file in files:	#all directories and files we add to backup file 
				backup_zip.write(os.path.join(folder, file), \
					os.path.relpath(os.path.join(folder,file), source_up),\
					compress_type = zipfile.ZIP_DEFLATED)

# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ!')
