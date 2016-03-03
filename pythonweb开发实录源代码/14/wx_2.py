import wx
class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '��̨����ϵͳ',
                size=(500, 300))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        toolbar = self.CreateToolBar()     #����������
        toolbar.AddSimpleTool(wx.NewId(),wx.Image( 'ico/xin.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(),
                "New")#������������һ������
        toolbar.AddSimpleTool(wx.NewId(),wx.Image( 'ico/save.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(),
                "Save")#������������һ������
        toolbar.AddSimpleTool(wx.ID_DELETE,wx.Image( 'ico/abc.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(),
                "Delete")#������������һ������
        toolbar.AddSimpleTool(wx.ID_EXIT, wx.Image( 'ico/exit.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(),
                "Exit")
        toolbar.SetToolBitmapSize(wx.Size (10, 10)) 
        toolbar.Realize() # ׼����ʾ������

        statusbar = self.CreateStatusBar()     # ����״̬��
        statusbar.SetStatusText("��Ȩ���У�����ʡ֣���л��ǿƼ����޹�˾ ����֧�֣����ǿƼ�ȫ��Ա��") # ��״̬�������ʾ��Ϣ
        
        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_TOOL,self.OnDelete,id=wx.ID_DELETE)
    def OnExit(self,event):
        dlg = wx.MessageDialog(None, 'ȷ��Ҫ�˳�������',   
                          '�����˳���ʾ', wx.YES_NO | wx.ICON_QUESTION)   
        result = dlg.ShowModal()   
        # �����������ȷ����ť   
        if result == wx.ID_YES:   
            self.Close(True) 
        dlg.Destroy()
    def OnDelete(self,event):
        dlg = wx.MessageDialog(None, 'ȷ��Ҫɾ������������',   
                          'ɾ��������ʾ', wx.YES_NO | wx.ICON_QUESTION)   
        result = dlg.ShowModal()   
        # �����������ȷ����ť   
        if result == wx.ID_YES:
            mydialog=MyDialog(parent=None,id=-1,title='ɾ��')
        dlg.Destroy()
    
class MyDialog(wx.Dialog):
    def __init__(self,parent,id,title):
        wx.Dialog.__init__(self,parent,id,title,size=(200,200))
        self.panel=wx.Panel(self)
        self.OkBtn=wx.Button(self,10,'ȷ��',pos=(50,100),size=(80,30))
        self.Bind(wx.EVT_BUTTON,self.CloseDlg,self.OkBtn)
        self.Show()
    def CloseDlg(self,event):
        self.Close()

        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
