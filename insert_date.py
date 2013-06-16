# https://github.com/facelessuser/sublime-settings/blob/ST3/insert_date.py

import sublime_plugin
from datetime import datetime


class InsertDateCommand(sublime_plugin.TextCommand):
    def run(self, edit, format="%Y-%m-%d"):
        date_time = datetime.now().strftime(format)
        for sel in self.view.sel():
            if sel.size() == 0:
                self.view.insert(edit, sel.begin(), date_time)
