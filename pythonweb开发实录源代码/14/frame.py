import wx
class MyFrame(wx.Frame):
    def __init__ (self):
        wx.Frame.__init__(self,None,-1,'�Զ��崰��',size=(400,200))
        self.Show()
app=wx.PySimpleApp()
myFrame=MyFrame()
app.MainLoop()
        
    