#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os,hashlib,re

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
    if not os.path.exists('Hashkey.txt') :
        file = open('Hashkey.txt','w')
    hashkey_file = open('Hashkey.txt','r+')
    hashkey_org = hashkey_file.readline()
    if hashkey != hashkey_org or hashkey_org == '':
        print(hashkey)
        print(hashkey_org)
        hashkey_file.seek(0,0)
        hashkey_file.write(hashkey)
        hashkey_file.close()
        return True
    else:
        hashkey_file.close()
        return False

def pathConfirmation(file_org):
    text_org = file_org.readlines()
    length = len(text_org)
    if os.path.isdir('Kindle Notes') == False:
        save_folder = os.mkdir('Kindle Notes')
    getKeyInformation(length, text_org)

def noteCombine(titleName,Notes):
    file = open(r'./Kindle Notes/%s.txt'%titleName,'a+',encoding='utf-8')
    file.writelines(Notes + '\n')
    file.close()

def getKeyInformation(length,text_org):
    for i in range(length):
        print("进度:{0}%".format(round((i + 1) * 100 / length)), end="\r")
        if i%5 == 0:
            titleName = re.sub('[\/:*?"<>|]','',text_org[i][:-1])
        if i%5 == 3:
            Notes = text_org[i]
            noteCombine(titleName,Notes)

if __name__ == '__main__':
    try:
        file_org = open(r'./My Clippings.txt',encoding='utf-8')
        if forbidDoubleeplicationR(file_org):
            cache =open(r'./My Clippings.txt',encoding='utf-8')
            pathConfirmation(cache)
            print('Notes migration has been completed！')
            cache.close()
        else:
            print('There is no change for the file of \'My Clippings.txt\' ')
        file_org.close()
    except IOError:
        print('Please copy the file of \'My Clippings.txt\' to this folder')

