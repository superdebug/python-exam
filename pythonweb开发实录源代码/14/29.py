import wx
class MyFrame(wx.Frame):
    def __init__ (self):
        wx.Frame.__init__(self,None,-1,'�༶�˵�',size=(300,100))
        panel=wx.Panel(self)
        menu=wx.Menu()
        sMenu=wx.Menu()
        sMenu.Append(-1,'�˵�һ')
        sMenu.Append(-1,'�˵���')
        menu.AppendMenu(-1,'�Ӳ˵�',sMenu)
        menuBar=wx.MenuBar()
        menuBar.Append(menu,'�˵�')
        self.SetMenuBar(menuBar)
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()

        
    