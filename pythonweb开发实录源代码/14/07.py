import wx
import wx.py.images as images
class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '������',
                size=(500, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        toolbar = self.CreateToolBar()     #2 ����������
        toolbar.AddSimpleTool(wx.NewId(), images.getPyBitmap(),
                "New", "Long help for 'New'") #3 ������������һ������
        toolbar.Realize() # ׼����ʾ������
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
