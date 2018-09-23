#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os,hashlib,re,time

'''
# 测试了基本文本的格式，元数据有五行，第一行为书名，第三行为笔记
for lines in text_org:
    if lines.isspace() or lines[0] =='-':
        print("NO NEED:",lines)
        pass
    else:
        print("Valuable:",lines)
'''
def forbidDoubleeplicationR(files):
    hm = hashlib.md5()
    hm.update(files.read().encode('utf-8'))
    hashkey =hm.hexdigest()
    print('F')
    if not os.path.exists(os.path.join(path,'Hashkey.txt')):
        file = open(os.path.join(path,'Hashkey.txt'),'w')
        print('F1')
    hashkey_file = open(os.path.join(path,'Hashkey.txt'),'r+')
    print('F2')
    hashkey_org = hashkey_file.readline()
    print('F3')
    if hashkey != hashkey_org or hashkey_org == '':
        print('\'My Clippings.txt\' Id :%s'%hashkey)
        print('\'My Clippings.txt\' old Id :%s'%hashkey_org)
        hashkey_file.seek(0)
        hashkey_file.write(hashkey)
        hashkey_file.close()
        print('F4')
        return True
    else:
        print('F5')
        hashkey_file.close()
        return False

def pathConfirmation(file_org):
    text_org = file_org.readlines()
    length = len(text_org)
    if os.path.isdir(os.path.join(path,'Kindle Notes')) == False:
        os.mkdir(os.path.join(path,'Kindle Notes'))
    getKeyInformation(length, text_org)

def noteCombine(titleName,Notes):
    file = open(os.path.join(path,'Kindle Notes/%s.txt'%titleName),'a+')
    file.writelines(Notes + '\n')
    file.close()

def getKeyInformation(length,text_org):
    for i in range(length):
        print("进度:{0}%".format(round((i + 1) * 100 / length)), end="\r")
        if i%5 == 0:
######################## '\ufeff'解决方案.encode('utf-8').decode('utf-8-sig')#######################
            titleName = text_org[i][:-1].encode('utf-8').decode('utf-8-sig')
        if i%5 == 3:
            Notes = text_org[i]
            noteCombine(titleName, Notes)

if __name__ == '__main__':
    global path
####pyinstall打包后路径就变成主目录路径，无法获得相对路径，改 path = os.getcwd()为下面
    path = os.path.dirname(os.path.realpath(sys.executable))
#os.path.dirname(os.path.realpath(sys.argv[0]))也可以

    try:
        print(os.path.join(path,'My Clippings.txt'))
        file_org = open(os.path.join(path,'My Clippings.txt'))
        print('2')
        if forbidDoubleeplicationR(file_org):
            print('3')
            cache = open(os.path.join(path,'My Clippings.txt'))
            print('4')
            pathConfirmation(cache)
            print('5')
            print('Notes migration has been completed！')
            cache.close()
        else:
            print('There is no change for the file of \'My Clippings.txt\' ')
        file_org.close()
    except IOError:
        print('Please copy the file of \'My Clippings.txt\' to this folder')
    time.sleep(2)

