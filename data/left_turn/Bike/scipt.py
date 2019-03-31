import os,sys
# from shutil import copyfile
import shutil
path1="/home/azjargal/Documents/MTP/Bike0909/AtoB/"
dirs=os.listdir(path1)
count=0
for file in dirs:
    if os.path.isdir(file):

        shutil.copy2("/home/azjargal/Documents/MTP/Bike0909/AtoB/GraphPlot.py","/home/azjargal/Documents/MTP/Bike0909/AtoB/"+file+"/GraphPlot.py")
        dir=os.listdir(path1+file)
        print("------------------------------------------------------------------")
        if len(dir)==10:
            print(file)
            os.chdir(path1+file)
            exec(open(path1+file+"/GraphPlot.py").read())

            os.chdir(path1)
            count=count+1

# print(count)
        # for f in dir:
        #     if f =="Accelerometer.csv":
     # if os.path.exists(path+file+"/Graph"):
            # os.makedirs("/home/azjargal/Documents/MTP/Bike0909/AtoB/"+file+"/Graph")
            # shutil.copy2("/home/azjargal/Documents/MTP/Bike0909/AtoB/GraphPlot.py","/home/azjargal/Documents/MTP/Bike0909/AtoB/"+file+"/")
                # print(f)

            # exec(open("/home/azjargal/Documents/MTP/Bike0909/AtoB/"+file+"/GraphPlot.py").read())

        # print(file)
        # dir=os.listdir("/home/azjargal/Documents/MTP/Bike0909/AtoB/"+file)
        # for f in dir:
            # print(f)
