import requests
import sys
import datetime
from datetime import *
from time import * 


#introduction 
Author = "XEFT"
Copyright = "Xeft software 2022 ©"
Name = "Metaload_lite.py"
Time = time()


print("How To use: simply paste the web address of the document to download it")
print("You can download any documents online so far as you are with the download link")
print("Your current time is "+ ctime(Time))

Active = True
while Active:
    br = input("Please Provide your download Link here: ")
    type = input("File Type: ")
    Time = time()
    start = perf_counter()
    Url = requests.get(br)
    br0, br1 = br.split(".com/") #default website extension
    """Please write your website extension. Extensions: br.split(".ng/"), br.split(".ng/"), br.split(".org/"), br.split(".uk/"), br.split(".co/"), etc"""
    format = "wb"
    if Url.status_code == 200:
                print("Your file started downloading by", ctime(Time))
                print("File Downloading....")
                print("Successful")
                Rename = br1
                Rename = input("Set file name: ")+type
                with open(Rename, format)as f:
                    f.write(Url.content)
                    end = perf_counter()
                    Total = (end - start)
                    Time = time()
                    print("Your file Stopped downloading by", ctime(Time))
                    print("It Took", Total,"sec to download")
                    print("Your files has been downloaded Please Kindly search", Rename, "in the folder you saved this script")
                  
    elif Url.status_code == 500:
                print("Failed")
                print("Sorry we couldn't find your download link")
                
                
    con = input("Do you want to quit: YES/NO: ")
    if con == "NO":
       Active =True
       
    else:
        Active = False
        sys.exit("Goodbye Thanks for using Metaload lite.py")
        break 
      
