import os
import re


def delete_files_r(root, regex_object, recursive=False, delete_empty_dirs=False):
	if not os.path.isdir(root):
		return
	
	for f in os.listdir(root):
		full_name = os.path.join(root,f)
		if os.path.isfile(full_name):
			if regex_object.search(f):
				os.remove(full_name)
		else: # must be a directory
			if recursive:
				delete_files_r(full_name, regex_object, recursive, delete_empty_dirs)

	if delete_empty_dirs and not os.listdir(root):
		os.rmdir(root)
				
