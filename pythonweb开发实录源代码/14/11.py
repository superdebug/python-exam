import wx

class MultiTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"�û�ע�����",
                          size=(500,400))
        panel=wx.Panel(self,-1)
        #����һ����̬�ı������
        labName=wx.StaticText(panel,-1,'�û���',pos=(50,10))
        #����һ����ͨ�ı������
        self.inputText=wx.TextCtrl(panel,-1,'',pos=(120,10),size=(150,-1),style=wx.TE_LEFT|wx.TE_PROCESS_TAB)
        self.inputText.SetInsertionPoint(0)
        labPwd=wx.StaticText(panel,-1,'����',pos=(50,50))
        #����һ�������ı�����򣬵�������������а��»س����󴥷��¼�
        self.pwdText=wx.TextCtrl(panel,-1,'',pos=(120,50),size=(150,-1),style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        #���¼�
        self.Bind(wx.EVT_TEXT_ENTER,self.OnLostFocus,self.pwdText)
        #��ͨ�����ı������
        multiLabel=wx.StaticText(panel,-1,"�������Э��:",pos=(40,90))
        multiText=wx.TextCtrl(panel,-1,"��Э����������ǿƼ����޹�˾��ͬ�޽ᣬ��Э����к�ͬЧ����\n��Э����Э��˫���ϳ�Э�鷽�����ǿƼ��������޹�˾��Э�������Ϊ'����'��\n��Ӧ����ʹ�û��ǿƼ����Ͻ�ѧ֮ǰ�����Ķ�ȫ��Э�����ݣ�����Э�����ԼӴ�������ʾ�����ݣ���Ӧ�ص��Ķ���������Э�����κ����ʵģ�Ӧ����ǿƼ���ѯ������������ʵ���Ƿ���ʹ�û��ǿƼ�����֮ǰ�����Ķ��˱�Э�����ݣ�ֻҪ��ʹ�û��ǿƼ����Ͻ�ѧ������Э�鼴��������Լ������ʱ����Ӧ��δ�Ķ���Э������ݻ���δ��û��ǿƼ�������ѯ�Ľ������ɣ����ű�Э����Ч����Ҫ������Э�顣",
                              pos=(120,90),
                              size=(300,100),
                              style=wx.TE_MULTILINE)
        
        #�ḻ��ʽ�Ķ����ı������
        richLabel=wx.StaticText(panel,-1,"�������Э��:",pos=(40,210))
        richText=wx.TextCtrl(panel,-1,
                             "��Э����������ǿƼ����޹�˾��ͬ�޽ᣬ��Э����к�ͬЧ����\n��Э����Э��˫���ϳ�Э�鷽�����ǿƼ��������޹�˾��Э�������Ϊ'����'��\n��Ӧ����ʹ�û��ǿƼ����Ͻ�ѧ֮ǰ�����Ķ�ȫ��Э�����ݣ�����Э�����ԼӴ�������ʾ�����ݣ���Ӧ�ص��Ķ���������Э�����κ����ʵģ�Ӧ����ǿƼ���ѯ������������ʵ���Ƿ���ʹ�û��ǿƼ�����֮ǰ�����Ķ��˱�Э�����ݣ�ֻҪ��ʹ�û��ǿƼ����Ͻ�ѧ������Э�鼴��������Լ������ʱ����Ӧ��δ�Ķ���Э������ݻ���δ��û��ǿƼ�������ѯ�Ľ������ɣ����ű�Э����Ч����Ҫ������Э�顣",
                             pos=(120,210),
                             size=(300,100),
                             #�����ḻ�ı��ؼ�
                             style=wx.TE_MULTILINE|wx.TE_RICH2)
        #����richText�ؼ����ı���ʽ
        richText.SetStyle(2,6,wx.TextAttr("white","black"))
        points=richText.GetFont().GetPointSize()
        #����һ��������ʽ
        f=wx.Font(points+3,wx.ROMAN,wx.ITALIC,wx.BOLD,True)
        #�ô�����������ʽ�����ı���ʽ
        richText.SetStyle(8,14,wx.TextAttr("blue",wx.NullColor,f))
    def OnLostFocus (self,event):
        wx.MessageBox('username:%s,password:%s'%(self.inputText.GetValue(),self.pwdText.GetValue()),'admin')      
def main():
    app=wx.PySimpleApp()
    frame=MultiTextFrame()
    frame.Show(True)
    app.MainLoop()

if __name__=="__main__":
    main()
