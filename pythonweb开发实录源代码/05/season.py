sprints = ('�㽶','����','����֦','��ݮ','����')
summers=('â��','�ƹ�','������','����','����')
autumns=('����','ľ��','����','������','���Ĺ�')
winters=('��ʯ��','����','����','ƻ��')
seasons_fruits=(sprints,summers,autumns,winters)
seasons=('����','�ļ�','�＾','����')
select_season = raw_input('��ѡ�����μ��ڣ����죺1�����죺2�����죺3�����죺4����')
for sea in range(len(seasons)):
    if select_season == str(sea+1):
        print '��ѡ����ǣ�',seasons[sea]
        print seasons[sea]+'��ˮ���У�'
for season in range(len(seasons_fruits)) :    
    if select_season == str(season+1):
        for fruit in range(len(seasons_fruits[season])) :
            print seasons_fruits[season][fruit]
            
    

    

