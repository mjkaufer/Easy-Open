import sublime
import sublime_plugin
import webbrowser

class OpenBrowserCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        file_name = self.view.file_name()
        extension = file_name[file_name.rfind("."):]
        
        if extension == ".html":
        	webbrowser.open("file:///" + file_name)
