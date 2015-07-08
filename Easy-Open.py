import sublime
import sublime_plugin
import webbrowser

class OpenBrowserCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        file_vars = sublime.active_window().extract_variables()
        
        if file_vars["file_extension"] == "html":
        	webbrowser.open("file:///" + file_vars["file"])
