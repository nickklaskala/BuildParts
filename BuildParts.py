import sublime, sublime_plugin, os

f=open("C:/Program Files/Sublime Text 3/plain_selection.txt", 'w')#
class BuildPartsCommand(sublime_plugin.WindowCommand):
	def run(self):
		# Get the current view in this window
		view = self.window.active_view()

		# Get the first selection and write it to a file
		f=open("C:/Program Files/Sublime Text 3/plain_selection.txt", 'w')# create a
		b=open("C:/Program Files/Sublime Text 3/plain_selection.bat", 'w')# create a

		#test for blank/no selection
		i=''
		for sel in view.sel():
			i=i+view.substr(sel)
		i=i.strip()

		if i=='':
			view.run_command("select_all")
		else:
			view.run_command("expand_selection", {"to": "line"})

		i=''
		for sel in view.sel():
			i=i+view.substr(sel)
		i=i.strip()

		for sel in view.sel():
			f.write(view.substr(sel)+'\n')
			b.write(view.substr(sel)+'\n')
		f.close()
		b.close()

		file_name=view.file_name() if view.file_name() != None else ''

		
			

		# Run the build now		
		if i=='' and '.bat' in file_name:
			self.window.run_command("build", {"variant": "Batch"})
			print('build1')
		elif '.bat' in file_name:
			self.window.run_command("build", {"variant": "BatchSelection"})
			print('build2')
		elif i=='':
			self.window.run_command("build", {"variant": "Py"})
			print('build3')
		else:
			self.window.run_command("build", {"variant": "PySelection"})
			print('build4')



