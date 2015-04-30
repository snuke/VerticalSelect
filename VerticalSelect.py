import sublime, sublime_plugin

class VerticalSelectCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sels = self.view.sel()
    for sel in sels:
      r,c = self.view.rowcol(sel.a)
      pos = self.view.text_point(r+1,c)
      if self.view.rowcol(pos)[0] == r+1:
        self.view.sel().add(sublime.Region(pos))

class MultiNumberInsertCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    num = 1
    for region in self.view.sel():
      self.view.replace(edit, region, "%02d" % num)
      num += 1