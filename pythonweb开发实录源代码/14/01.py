import wx
class MyFirstFrame(wx.Frame):
    def __init__ (self,parent):
        wx.Frame.__init__(self,parent,-1,'Hello World',size=(300,300))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        txt=wx.StaticText(panel,-1,'Hello World')
        sizer.Add(txt,0,wx.TOP| wx.LEFT,100)
        self.Centre()
app=wx.App()
frame=MyFirstFrame(None)
frame.Show(True)
app.MainLoop()
        
    
