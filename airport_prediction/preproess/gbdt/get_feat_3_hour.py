
#-*-coding:utf-8-*-
import csv
import pandas as pd
import os
import cPickle
###################################### 连续两个小时求和平均 ####################################
passengers_count_dict={}
time_count_dict = {}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0][-1]#取出1、2、3
            time = row[1].split(" ")[1].split(":")[0]#取出小时
            newtime="0"
            if int(time)-6<=2 and int(time)-6>=0:
                newtime="6"
            if int(time)-9<=2 and int(time)-9>=0:
                newtime="9"
            if int(time)-12<=2 and int(time)-12>=0:
                newtime="12"
            key = wifi_name_dict[int(file_name.split(".")[0])]+":"+date+"-"+newtime
            data = float(row[0])
            if newtime=="6" or newtime=="9" or newtime=="12":
                if key in passengers_count_dict:
                    passengers_count_dict[key] += data
                    time_count_dict[key] += 1
                else:
                    passengers_count_dict[key] = data
                    time_count_dict[key] = 1
                print time_count_dict[key]
    print "writting..."

#
# time_stamp_dict=[]
# # time_stamp_sublist = []
# for key in passengers_count_dict:
#     time_stamp_sublist=[float(passengers_count_dict[key])/time_count_dict[key],key.split(":")[0],key.split(":")[1]]
#     time_stamp_dict.append(time_stamp_sublist)
#     # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
# f = open("../gbdt_feat/3_hour_sum.csv", "wb")
# write = csv.writer(f)
# write.writerow(["passengerCount", "wifiap","time"])
# write.writerows(time_stamp_dict)
# f.close()

time_stamp_dict={}
for key in passengers_count_dict:
    time_stamp_sublist=float(passengers_count_dict[key])/time_count_dict[key]
    time_stamp_dict[key]=time_stamp_sublist
    # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
f = open("../3_hour_sum.pkl",'wb')
cPickle.dump(time_stamp_dict,f,-1)
f.close()