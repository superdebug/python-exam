import wx
class App(wx.App):
    def OnInit(self):
       dlg=wx.TextEntryDialog(None,"��ô����ϲ����һ�ֱ��������ʲô��","һ������","Python")
       if dlg.ShowModal()==wx.ID_OK:
           print dlg.GetValue()
       return True
if __name__ == '__main__':
    app = App(False)   
    app.MainLoop()



