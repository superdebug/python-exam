db={}   #����һ���յ��ֵ�
# ��������û�������Ҫע��
def newuser ():
    prompt='������ע���˺ţ�'
    while True:
        name=raw_input(prompt)
        # ����ֵ����Ƿ��Ѿ����ڼ�Ϊ�û�ע���˺ŵ�Ԫ��
        if db.has_key(name):
            prompt='��ע����˺��Ѿ����ڣ���ʹ�������˺�ע�᣺'
            continue
        else:
            password=raw_input('������ע�����룺')
            # ���û�ע����˺ź�������Ϊ�ֵ�ļ�����ֵ��
            db[name]=password
            break
# ����Ѿ�ע���������Ҫ��¼
def olduser ():
    name=raw_input('�������¼�˺�:')
    password=raw_input('�������¼����:')
    # ��ȡע���˺�����Ӧ������
    userpwd=db.get(name)
    # �ж��û�����ĵ�¼�����Ƿ���ע��������ͬ
    if userpwd == password:
        print '��ӭ����¼��',name
    else:
        print '�����û�����������������µ�¼��'
# ��ʾϵͳ����
def showmenu ():
    prompt="�������û�״̬��n��ע�� e����¼����"
    con = False
    while not con:
        chosen = False
        while not chosen:
            try:
                # ���û��������ĸСд��ʽ��
                choice=raw_input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice='q'
            print '�������ˡ�%s����'% choice
            if choice not in 'neq':
                print '����������ݲ��Ϸ������������룺'
            else:
                chosen = True
                con = True
        if choice == 'n':
            newuser()
        elif choice == 'e':
            olduser()
        else:
            showmenu()
        showmenu()

showmenu()            
        
            

           
            
    
    
    
        
        
        
    
