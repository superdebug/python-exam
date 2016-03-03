import wx  
import os
class MainFrame ( wx.Frame ):          
    def __init__( self, parent ):  
        wx.Frame.__init__(self,parent,-1,'EditPlus',size=(500,300))
        panel=wx.Panel(self)
        menuBar=wx.MenuBar()
        fileMenu=wx.Menu()
        sFileMenu=wx.Menu()
        sFileMenu.Append(11,'��׼�ı�')
        sFileMenu.Append(12,'HTML��ҳ')
        fileMenu.AppendMenu(-1,'�½�(N)',sFileMenu)#��˵�����Ӳ˵���
        fileMenu.Append(2,'&o ��(O)')
        wx.EVT_MENU(self, 2, self.OnOpen) 
        fileMenu.Append(3,'�ر�(C)')        
        menuBar.Append(fileMenu, "�ļ�");
        fileMenu.AppendSeparator()
        editMenu=wx.Menu()
        editMenu.Append(4,'&Ctrl+Z ����')
        editMenu.Append(5,'&Ctrl+Y ����')
        editMenu.Append(6,'����')
        editMenu.Append(7,'����')
        menuBar.Append(editMenu,'�༭')
        editMenu.AppendSeparator()
        viewMenu=wx.Menu()
        menuBar.Append(viewMenu,'��ͼ')
        self.exitMenu=wx.Menu()
        self.exitMenu.Append(1000,'�˳�')
        menuBar.Append(self.exitMenu,'ϵͳ�˵�')
        sysMenu=wx.Menu()
        subSetMenu=sysMenu.Append(1001,'��/���β˵�')
        self.Bind(wx.EVT_MENU,self.OnExit,id=1000)
        self.Bind(wx.EVT_MENU_HIGHLIGHT,self.OnItemSelected,id=1000)
        self.Bind(wx.EVT_MENU,self.OnEnable,subSetMenu)
        menuBar.Append(sysMenu,'����')
        self.SetMenuBar(menuBar)          #�����˵���ӵ�������
        self.Show()
    def OnOpen (self,event):
        filterFile='Python Source(*.py)|*.py|All files(*.*)|*.*'
        dialog=wx.FileDialog(None,'ѡ���ļ�',os.getcwd(),'',filterFile,wx.OPEN)
        dialog.ShowModal()
        dialog.Destroy()
    def OnEnable (self,event):
        menuBar=self.GetMenuBar()
        enabled=menuBar.IsEnabled(1000)
        self.exitMenu.Enable(1000,not enabled)
    def OnExit (self,event):
        self.Close()
    def OnItemSelected (self,event):
        item=self.GetMenuBar().FindItemById(event.GetId())
        wx.MessageBox('Menu:'+item.GetText())
app=wx.PySimpleApp()
MainFrame(None).Show()
app.MainLoop()
