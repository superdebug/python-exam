import wx
class RadioFrame(wx.Frame):
    def __init__ (self):
        wx.Frame.__init__(self,None,-1,'��ѡ��ť',size=(200,150))
        panel=wx.Panel(self,-1)
        radioMale=wx.RadioButton(panel,-1,'��',pos=(20,20))
        radioFemale=wx.RadioButton(panel,-1,'Ů',pos=(20,40))

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=RadioFrame()
    frame.Show()
    app.MainLoop()

        
    
