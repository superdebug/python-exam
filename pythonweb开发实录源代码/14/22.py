import wx
class OpenResource(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 400))
        panel = wx.Panel(self, -1)
        sizer = wx.GridBagSizer(4, 4)              #����Grid Bag���ֹ�����
        text1 = wx.StaticText(panel, -1, 'Select a resource to open')   #������̬�ı���
        sizer.Add(text1, (0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)   #����̬�ı�����ӵ����ֹ�������
        tc = wx.TextCtrl(panel, -1)                #����һ�������ı���
        sizer.Add(tc, (1, 0), (1, 3), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)   #�������ı�����ӵ����ֹ�������
        text2 = wx.StaticText(panel, -1, 'Matching resources')
        sizer.Add(text2, (2, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        list1 = wx.ListBox(panel, -1, style=wx.LB_ALWAYS_SB)    #����һ���յ��б��
        sizer.Add(list1, (3, 0), (5, 3), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)  #�����б����ӵ����ֹ�������
        text3 = wx.StaticText(panel, -1, 'In Folders')
        sizer.Add(text3, (8, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        list2 = wx.ListBox(panel, -1, style=wx.LB_ALWAYS_SB)
        sizer.Add(list2, (9, 0), (3, 3), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        cb = wx.CheckBox(panel, -1, 'Show derived resources')       #����һ����ѡ��
        sizer.Add(cb, (12, 0), flag=wx.LEFT | wx.RIGHT, border=5)   #����ѡ����ӵ����ֹ�������
        buttonOk = wx.Button(panel, -1, 'OK', size=(90, 28))        #����һ����ť
        buttonCancel = wx.Button(panel, -1, 'Cancel', size=(90, 28))
        sizer.Add(buttonOk, (14, 1))                                #�����洴����������ť�ؼ���ӵ����ֹ�������
        sizer.Add(buttonCancel, (14, 2), flag=wx.RIGHT | wx.BOTTOM, border=5)
        #����һ��λͼ��ť
        help = wx.BitmapButton(panel, -1, wx.Bitmap('ico/15b53eda7255d444d1164e2e.png'), style=wx.NO_BORDER) 
        sizer.Add(help, (14, 0), flag=wx.LEFT, border=5)       #��λͼ��ť�ؼ���ӵ����ֹ�������
        panel.SetSizer(sizer)            #�����ֹ�������ӵ�panel��
        self.Centre()
        self.Show(True)
app = wx.App()
OpenResource(None, -1, 'Open Resource')
app.MainLoop()


