import wx
class CheckBoxFrame(wx.Frame):
    def __init__ (self):
        wx.Frame.__init__(self,None,-1,'��ѡ��',size=(400,200))
        panel=wx.Panel(self,-1)
        wx.StaticText(panel,-1,'����ϲ���ĵ�Ӱ��Ա�ǣ�',pos=(10,10),size=(150,20))
        wx.CheckBox(panel,-1,'½��',pos=(10,30),size=(100,20))
        wx.CheckBox(panel,-1,'����',pos=(10,50),size=(100,20))
        wx.CheckBox(panel,-1,'����',pos=(10,70),size=(100,20))
        wx.CheckBox(panel,-1,'�����',pos=(10,90),size=(100,20))
        wx.CheckBox(panel,-1,'��ޱ',pos=(10,110),size=(100,20))
if __name__=='__main__':
    app=wx.PySimpleApp()
    checkBox=CheckBoxFrame()
    checkBox.Show()
    app.MainLoop()


        
    
