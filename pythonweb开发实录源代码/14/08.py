import wx
class StatusbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '״̬��',
                size=(500, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusbar = self.CreateStatusBar()     # ����״̬��
        statusbar.SetStatusText("״̬����Ϣ") # ��״̬�������ʾ��Ϣ
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = StatusbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
