#coding=utf-8
print '你好'


print_num = input('which loop do you want to be print out?')

count = 0 
while count < 10000:
    if count == print_num:
        print 'there you got the num :',count
        choice = raw_input('Do you want to continue the loop?(y/n)')
        if choice == 'n':
          break
        else:
          while print_num <= count:
            print_num = input('which loop do you want it print?')
          print '已经过了'  
    else:
        print 'Loop: ',count
    count +=1 
else:
     print 'Loop: ',count
