from selenium import webdriver
from Village import*
from Useful_Function import *
import time

Only_Buildings = False

class Player(object):
    def __init__(self,driver,username, password, urlgame,tribe):
        self.Driver = driver
        self.User_Name = username
        self.Password = password
        self.Url_Game = urlgame
        self.tribe = tribe
        self.Villages = []
        self.Task_Queue = []
        timer = time.localtime()
        self.Time = timer.tm_hour * 3600 + timer.tm_min * 60 + timer.tm_sec

    def GetVillage(self, index) -> Village :
        return self.Villages[index]


    def InitiatePlayer(self, onlybuilding = False):
        try:
            time.sleep(3)
            cookies = self.Driver.find_elements_by_class_name("CybotCookiebotDialogBodyButton")
            cookies[2].click()
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coudnt close Cookies\n")
            Decomantation_File.close()
        Only_Buildings = onlybuilding
        for i in self.Villages:
            self.Driver.get(i.Village_Url)
            time.sleep(1)
            i.InitiateVillage2(self.tribe)



# ---------  determan hero hp
    def AddVillage(self,villageid):
        village = Village(self.Driver,20,self.Url_Game,villageid)
        self.Villages.append(village)

    def PrintVilliges(self):
        for i in self.Villages:
            print("Village Numer 0 is"+ i.Village_ID)

# the task should look like:                 1:מחסן:2
    def MakeVilligesBuildingTask2(self,buildingstasks):
        for i in buildingstasks:
            s= i.split(":")
            villagenumber = int(s[0])-1
            buildingname = s[1]
            count = int(s[2])
            try:
                building = self.Villages[villagenumber].Buildings.FindBuilding(buildingname)
                building.Upgrade_To_Level = count
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("didnt find the building\n")
                Decomantation_File.close()
            self.Villages[villagenumber].GetTaskMeneger().Buildings_To_Build.append(buildingname)

    def MakeVilligesBuildingTask(self, buildingstasks):
        for i in buildingstasks["buildings"]:
            villagenumber = int(i["villnumber"]) - 1
            buildingname = i["name"]
            count = int(i["leveltoupgrade"])
            try:
                building = self.Villages[villagenumber].Buildings.FindBuilding(buildingname)
                building.Upgrade_To_Level = count
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("didnt find the building\n")
                Decomantation_File.close()
            self.Villages[villagenumber].GetTaskMeneger().Buildings_To_Build.append(buildingname)

    def MakeCelebrationTask(self,celebrationvillages):
        for i in celebrationvillages:
            arr = i.split(":")
            arr[0] = int(i[0])
            self.Villages[arr[0]-1].Celebrate = True
            if(arr[1]!="small"):
                self.Villages[arr[0]].CelebrateSmall = False

    def MakeSolidersBuildingTask2(self,soliderslist, onlysoliders):
        try:
            for i in soliderslist:
                s = i.split(":")
                villagenumber = int(s[0]) - 1
                solidername = s[1]
                count = int(s[2])
                buildingeachtime= int(s[3])
                village = self.GetVillage(villagenumber)
                soliderlist = village.GetSoliderList()
                village.GetTaskMeneger().Making_Soliders = onlysoliders
                for i in soliderlist.GetSoliderList():
                    if i.Name == solidername:
                        i.Units_To_Build = int(count)
                        i.Build_Each_Time = buildingeachtime
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("There is no soliders for solider task\n")
            Decomantation_File.close()

    def MakeSolidersBuildingTask(self,soliderslist, onlysoliders):
        try:
            for i in soliderslist["soliders"]:
                villagenumber = int(i["villnumber"]) - 1
                solidername = i["name"]
                count = int(i["generalamount"])
                buildingeachtime= int(i["amounteachtime"])
                village = self.GetVillage(villagenumber)
                soliderlist = village.GetSoliderList()
                village.GetTaskMeneger().Making_Soliders = onlysoliders
                for i in soliderlist.GetSoliderList():
                    if i.Name == solidername:
                        i.Units_To_Build = int(count)
                        i.Build_Each_Time = buildingeachtime
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("There is no soliders for solider task\n")
            Decomantation_File.close()


    def  MakeRobFarmTask(self,time,farmlist,village):
        self.Villages[village-1].GetTaskMeneger().Farm_List = farmlist["farms"]
        self.Villages[village - 1].GetTaskMeneger().Time_To_Robe = time

    def IniateBuildWhenFull(self,soliderlist):
        try:
            for i in soliderlist["soliders"]:
                s=i.split(":")
                village = int(s[0])-1
                solidername = s[1]
                amount = s[2]
                self.Villages[village].GetTaskMeneger().Solider_To_Build_When_Full = solidername
                self.Villages[village].GetTaskMeneger().Amount_To_Build_When_Full= amount
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("Coudnt iniate Soliders Build When Full\n")
            Decomantation_File.close()


    def DotasksForAllVileges(self,timetoattack = None,timetosleepifnothingisbuiled = 2000):
        #self.Villages[0].GetTaskMeneger().UpgradeBuilding()
        url = self.Url_Game + "/dorf1.php"
        self.Driver.get(url)
        while True:
            for i in self.Villages:
                i.Driver.get(i.Village_Url)
                i.GetTaskMeneger().UpgradeByPrefrence2()
                i.GetTaskMeneger().MakeAttackTask()
                i.GetTaskMeneger().MakeSoliderTask()
                i.GetTaskMeneger().UpgradeBuilding()
                i.GetTaskMeneger().UpgradeWhereHouse()
                i.GetTaskMeneger().BuildSolidersWhenWhereHouseIsFull()
                if i.Celebrate == True:
                    i.GetTaskMeneger().MakeCelebration()

            for i in self.Villages:
                    i.Driver.get(i.Village_Url)
                    time.sleep(TimeToSleep)
                    if(self.tribe!="Romans" ):
                        if(i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building == True):
                             i.GetTaskMeneger().DoResourceTask()
                        if (i.GetTaskMeneger().Buildings_To_Build.__len__()>0):
                                i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building = not i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building
                                i.GetTaskMeneger().DoBuildingTask()
                        i.GetTaskMeneger().DoOtherTask()
                    elif(i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building == True):
                        i.GetTaskMeneger().DoResourceTask()
                        i.GetTaskMeneger().DoBuildingTask()
                        i.GetTaskMeneger().DoOtherTask()
                        i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building = not i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building
                    else:
                        i.GetTaskMeneger().DoBuildingTask()
                        i.GetTaskMeneger().DoResourceTask()
                        i.GetTaskMeneger().DoOtherTask()
                        i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building = not i.GetTaskMeneger().What_To_Upgrade_Recourse_Or_Building

            try:
                mintimetosleep = float('inf')
                for i in self.Villages:
                    i.Driver.get(i.Village_Url)
                    try:
                         timetosleep = CheckHowMuchTimeToSleep(self.Driver, timetoattack)
                         if (timetosleep < mintimetosleep):
                             mintimetosleep = timetosleep
                    except:
                        mintimetosleep = timetosleepifnothingisbuiled
                        Decomantation_File = open("Text_Files\Decomantation", "a")
                        Decomantation_File.write("coudnt find how much time to sleep\n")
                        Decomantation_File.close()
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("going to sleep for:" + str(mintimetosleep)+"\n")
                Decomantation_File.close()
                print("going to sleep for:" + str(mintimetosleep))
                time.sleep(mintimetosleep)
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("coudnt go to sleep\n")
                Decomantation_File.close()
                print(("coudnt go to sleep"))





