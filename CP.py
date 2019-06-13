# -*- coding:utf-8 -*-
import re
import shutil
import os
import xlrd

#def read_excel():
#	ExcelFile = xlrd.open_workbook(r'/home/wang.fan/name_list.xlsx')
#	sheet = ExcelF.sheet_by_name('names_list')
#	list = []
#	rows = sheet.nrows
#	cols = sheet.ncols
#	for i in range(rows):
#		for n in range(cols):
#			test = sheet.cell(i, n)value.encode('utf-8')
#			if text not in list:
#				list.append(text)

def cp(OldName, NewName):
    shutil.copyfile(OldName, NewName)

if __name__ == '__main__':
    #获取txt内容，生成列表
    list = []
    file = open("/home/wang.fan/name_list.txt", "r")
    ff = file.readlines()
    for line in ff:
        line = line.rstrip("\n")
        list.append(line)
	#read_excel
    #print list

    #获取源文件列表
    file_path = '/home/wang.fan/2000_PCAP'
    file_path_new = '/home/wang.fan/2000_PCAP_part1'
    dirs = os.listdir(file_path)
    #print dirs

    #判断是否存在相应文件,存在则copy
    for abc in list:
        for dir in dirs:
            if abc in dir[:5]:
                print "Copying：%s" %dir
                cp(file_path+"/"+dir, file_path_new+"/"+dir)
                print "done~"