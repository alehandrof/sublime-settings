# http://www.sublimetext.com/forum/viewtopic.php?f=2&t=12439#p48727

import sublime
import sublime_plugin
import os

class FindInCurrentFolderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        current_dir = os.path.dirname(view.file_name())
        window.run_command("find_in_folder", {"dirs": [current_dir]})