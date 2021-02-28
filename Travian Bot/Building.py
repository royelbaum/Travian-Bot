from selenium import webdriver

from Useful_Function import*


class Building(object):
    def __init__(self,driver,name,id,url_game):
        self.Level = 1
        self.Name = name
        self.ID = id
        self.Main_Url = url_game +"/dorf1.php"
        self.Url_Game = url_game + "/build.php?id=" +str(id)
        self.Driver = driver
        self.Level = 0
        self.Village_Center = url_game + "/dorf2.php"
        self.Amount_Needed_To_Upgrade = 0
        self.Upgrade_To_Level = 0


    def InsertName(self,name):
        self.Name = name

    def UpgradeBuilding2(self):  ## need to see how to choose th building
        self.Driver.get(self.Village_Center)
        self.Driver.get(self.Url_Game)
        time.sleep(TimeToSleep)
        canbuild = CheckIfCanBuild(self.Driver,self.Url_Game)
        if(canbuild):
            if(self.Upgrade_To_Level > self.Level):
                canbuild = ClickHardButton(self.Driver)
                if(canbuild== False):
                    self.Driver.back()
                else:
                    self.Level+=1
        return canbuild

class BuildingsList(object):
    def __init__(self,driver = None,game_url = None):
        if (driver != None and game_url != None):
            self.Building_List=[]
            self.Driver = driver
            self.Url_Game = game_url
            self.Center_Village_Url = game_url+"/dorf2.php"
        else:
            self.Building_List = []
            self.Url_Game = game_url
            self.Driver = driver

    def InitiateBuildingList(self):
        self.Driver.get(self.Center_Village_Url)   ## Added
        for i in range(19,41):
            try:
                self.Building_List.append(Building(self.Driver , "Empty Slot" , i , self.Url_Game))
            except:
                print("Some Error")
        for k in self.Building_List:
            self.Driver.get(k.Url_Game)
            try:
                 time.sleep(TimeToSleep)
                 x = self.Driver.find_element_by_xpath("//*[@id='content']/h1")
                 if(x.text!= "Construct new building"):
                     array = str(x.text).split()
                     name = ""
                     for p in range(0,array.__len__()-2):
                        if(p<array.__len__()-2 and p>0):
                            name = name + " " + str(array[p])
                        else:
                            name = name + str(array[p])
                     k.Name= name
                     k.Level = int(array[array.__len__()-1])
                 else:
                     k.Name = "Empty Slot"
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("Coundt Iniate Building List Properly\n")
                Decomantation_File.close()
                print("Coundt Iniate Building List Properly")

    def FindBuilding(self,name):
        for i in self.Building_List:
            if(i.Name == name):
                return i
    def WriteAllBuildingsToFile(self):
        file = open("Buildings_To_Build","a")
        for i in self.Building_List:
            file.write(i.Name + ",")


#driver = webdriver.Chrome(r"C:\Users\royel\Pyton Project\drivers\chromedriver.exe")
#urlgame= "https://tx3.travian.co.il"
#building1= Building(driver,"EmptySlot",32,urlgame)
#loginTravian(driver,"roy12el3","1q3e5t7u9o",urlgame)
#buildinglist = BuildingsList(driver,urlgame)
#buildinglist.InitiateBuildingList()
#buildinglist.CheckIfInitiate()
#building1.UpgradeBuilding()



