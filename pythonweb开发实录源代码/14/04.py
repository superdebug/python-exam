import wx
class App(wx.App):   
    def OnInit(self):   
        dlg = wx.MessageDialog(None, '�㵥���ˡ��˳�ϵͳ����ť����ȷ��Ҫ�˳����������ȷ���������ǡ������򵥻����񡿡�',   
                          '�����˳���ʾ', wx.YES_NO | wx.ICON_QUESTION)   
        result = dlg.ShowModal()    
        if result == wx.ID_YES:   
            print '�㵥����ȷ����ť'  
        dlg.Destroy()   
        return True    
if __name__ == '__main__':   
    app = App(False)   
    app.MainLoop()
