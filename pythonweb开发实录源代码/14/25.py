import wx 
ID_ABOUT = 101 
ID_EXIT  = 102   
class MyFrame(wx.Frame): 
    def __init__(self, parent, ID, title): 
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(400, 150)) 
        self.CreateStatusBar() 
        self.SetStatusText("���ǿƼ����޹�˾����Ȩ") 
        menuBar = wx.MenuBar()             #�����˵���
        menu = wx.Menu()                    #�����˵�
        menuBar.Append(menu, "File");      #��File���˵���ӵ��˵�����
        menu.Append(ID_ABOUT, "About", "More information about this program")      #��˵�������Ӳ˵�
        menu.AppendSeparator()             #��ӷָ���
        menu.Append(ID_EXIT, "E&xit", "Terminate the program")       #��˵�������Ӳ˵�
        self.SetMenuBar(menuBar)          #�����˵���ӵ�������
        #���¼�
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout) 
        wx.EVT_MENU(self, ID_EXIT,  self.TimeToQuit) 
    #������About�˵�ʱ��������ʾ�Ի���
    def OnAbout(self, event): 
        dlg = wx.MessageDialog(self, "This sample program shows off\n" 
                              "frames, menus, statusbars, and this\n" 
                              "message dialog.", 
                              "About Me", wx.OK | wx.ICON_INFORMATION) 
        dlg.ShowModal()          #��ģʽ���ڴ�
        dlg.Destroy() 
    #����Exit�˵�ʱ���رճ���
    def TimeToQuit(self, event):     
        self.Close(True) 

class MyApp(wx.App): 
    def OnInit(self): 
        frame = MyFrame(None, -1, "Hello from wxPython") 
        frame.Show(True) 
        self.SetTopWindow(frame) 
        return True 
app = MyApp(0) 
app.MainLoop() 

