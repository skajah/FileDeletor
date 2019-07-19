from tkinter import *
from tkinter import messagebox
from delete_files import delete_files_r
import os


about_lines = '\n'.join([

		"Tool Name: File Deletion Tool\n",

		"This tool was created to automate the task", 
		"of deleting unwanted files in a directory.", 
		"The necessary things needed are the directory name and the format of the files to be deleted.\n",
		"See <Usage> under <Help> for more information"
		])

usage_lines = '\n'.join([

	"1) Enter the full path to a directory",
	"2) Enter the file name format as a regular expression\n",
	"Two optional commands are available. They are off by default\n",

	"The first option will make sure all subdirectories are visited, and the files matching the regular expression in those subdirectories are deleted as well.\n",


	"The second option will delete all empty directories and subdirectories after the files are deleted."
	])


def about_info():
	messagebox.showinfo("Tool Info", 
		about_lines)


def usage_info():
	messagebox.showinfo("Tool Usage", 
		usage_lines)

def run_deletion(event):
	root_dir = dir_text_box.get().strip()

	if not os.path.exists(root_dir):
		messagebox.showerror("Error", "Directory [%s] not found" % root_dir)
		return
		# raise Exception("Directory [%s] not found" % root_dir)

	if not os.path.isdir(root_dir):
		messagebox.showerror("Error", "[%s] is not a directory" % root_dir)
		return
		#raise Exception("[%s] is not a directory" % root_dir)

	regex_text = regex_text_box.get().strip()

	if not regex_text:
		result = messagebox.askyesno("Warning", "An empty regex expression will delete all files. Continue anyway?")
		if not result:
			return
	
	regex_object = re.compile(regex_text)

	delete_in_subdir = True if subdir_var.get() == 1 else False
	delete_in_empty_dir = True if empty_dir_var.get() == 1 else False

	delete_files_r(root_dir, regex_object, delete_in_subdir, delete_in_empty_dir)

if __name__ == '__main__':

	main_window = Tk()

	main_window.title('File Deletion Tool')
	main_window.geometry('600x350+400+300')
	main_window.resizable(width=False, height=False)


	top_frame = Frame(main_window)
	bottom_frame = Frame(main_window)

	top_frame.pack()
	bottom_frame.pack(side=BOTTOM)

	Label(top_frame, text="Root Directory").grid(row=0, column=0, sticky=E)
	Label(top_frame, text="File Name Regex").grid(row=1, column=0, sticky=E)

	dir_text_box = Entry(top_frame, width=50)
	dir_text_box.grid(row=0, column=1)

	regex_text_box = Entry(top_frame, width=50)
	regex_text_box.grid(row=1, column=1)


	subdir_var = IntVar()
	empty_dir_var = IntVar()

	subdir_button = Checkbutton(top_frame, text="Delete Files in Subdirectories", variable=subdir_var)
	subdir_button.grid(row=2, column=1, sticky=W, pady=10)

	empty_dir_button = Checkbutton(top_frame, text="Delete Empty Directories", variable=empty_dir_var)
	empty_dir_button.grid(row=3, column=1, sticky=W, pady=6)


	delete_icon = PhotoImage(file="trash_icon.gif").subsample(6, 6)


	run_button = Button(bottom_frame, text="Delete\nFiles", compound=LEFT)
	run_button.config(image=delete_icon)
	run_button.bind("<Button-1>", run_deletion)
	run_button.grid(row=4, column=2, sticky=W, pady=25)

	main_menu = Menu(main_window) #the main row
	help_menu = Menu(main_menu, tearoff=0) #add a column header

	#add column items
	help_menu.add_command(label="About", command=about_info)
	help_menu.add_command(label="Usage", command=usage_info)
	help_menu.add_separator()

	#add the column to the main row
	main_menu.add_cascade(label="Help", menu=help_menu)

	#add the main menu row to main window
	main_window.config(menu=main_menu)



	main_window.mainloop()