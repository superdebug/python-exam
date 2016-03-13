#coding=utf-8
items=['老大','老二','老三','老四']

key='老三'

for item in items:
    if item==key:
        print key,"as found"
        break
else :
    print key ,"not found"

