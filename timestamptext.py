import sublime, sublime_plugin, time

class TimestamptextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, str(int(time.time())))
