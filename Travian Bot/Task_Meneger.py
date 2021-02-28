from Building import BuildingsList
from Resources import*
from Hero import Hero
import json





class TaskMeneger(object,):
    Wood = Wood(None,None)
    Clay = Clay(None, None)
    Iron = Iron(None, None)
    Wheet = Wheet(None, None)
    Buildings = BuildingsList(None, None)
    Hero = Hero(None, None, None)

    def __init__(self,driver,villageurl):
        self.Driver = driver
        self.Village_Url = villageurl
        self.Resource_Task_List = []
        self.Building_Task_List = []
        self.Other_Tasks_List = []
        self.Buildings_To_Build = []
        self.Solider_To_Build = []
        self.Making_Soliders = False
        self.Farm_List = []
        self.Time_To_Robe = 0
        timer = time.localtime()
        self.Time = timer.tm_hour*3600 + timer.tm_min*60 + timer.tm_sec
        self.Solider_To_Build_When_Full = ""
        self.Amount_To_Build_When_Full = 0
        self.Nekudat_Mifgash = ""
        self.Url_Game = ""
        self.What_To_Upgrade_Recourse_Or_Building = False
        self.CelebrateSmall = True
        self.Tribe = ""

    def InitiateTaskMeneger(self,wood,clay,iron,wheet,buildings,hero,wherehousesize,burnsize,soliderlist,nekudatmifgash, urlgame,celebratesmall,tribe):
        self.Wood =wood
        self.Clay = clay
        self.Iron = iron
        self.Wheet = wheet
        self.Buildings = buildings
        self.Hero = hero
        self.WhereHouse_Size = wherehousesize
        self.Burn_Size = burnsize
        self.Solider_List = soliderlist
        self.Nekudat_Mifgash = nekudatmifgash
        self.Url_Game = urlgame
        self.CelebrateSmall = celebratesmall
        self.Tribe = tribe

    def AddTask(self, task):
        if(isinstance(task)==ReacourceTask):
            self.Resource_Task_List.append(task)
        elif(isinstance(task)== BuildingTask):
            self.Building_Task_List.append(task)
        else:
            print("Error Not a Task")



    def UprgafeOneFromEachResource(self,resourceslist):
        ResourceList = []
        BuildingList = []
        for i in resourceslist:
            if(i=="wood"):
              ResourceList.append(self.Wood)
            elif (i == "clay"):
                ResourceList.append(self.Clay)
            elif (i == "iron"):
                ResourceList.append(self.Iron)
            elif (i == "wheet"):
                ResourceList.append(self.Wheet)
            else:
                for k in self.Buildings:
                    if(i == k.Name):
                        BuildingList.append(k)
        while True:
            try:
                self.Hero.GoForAMission()
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("coudnt go for a Misson")
                Decomantation_File.close()
                print("coudnt go for a Misson")
            if (ResourceList.__len__() > 0):
                Resource = ResourceList.pop(0)
            try:
                    FindMinimunLevel(Resource).Upgrade()
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("couldnt uprage Resource")
                Decomantation_File.close()
                Timetosleep =0
                Timetosleep = checkifbiulding(self.Driver)
                time.sleep(Timetosleep)
            Timetosleep = checkifbiulding(self.Driver)
            ResourceList.append(Resource)
            time.sleep(Timetosleep)



    def UpgradeByPrefrence(self):
        while True:
            try:
                self.Hero.GoForAMission()
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("coudnt go for a Misson")
                Decomantation_File.close()
            chooseonetoupgrade = self.WhichResourceToUpgrade()
            Timetosleep = checkifbiulding(self.Driver)
            if(Timetosleep == 0):
                FindMinimunLevel(chooseonetoupgrade).Upgrade()
            elif(Timetosleep>600):
                time.sleep(600)
            else:
                time.sleep(Timetosleep)
                FindMinimunLevel(chooseonetoupgrade).Upgrade()

    def UpgradeByPrefrence2(self):

      #  self.Driver.get(self.Village_Url)
        try:
                heromission = HeroTask(self.Driver,self.Hero)
                self.Other_Tasks_List.append(heromission)
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coudnt go for a Misson")
            Decomantation_File.close()
        if self.Making_Soliders == False:
            if (self.Tribe== "Romans" or self.What_To_Upgrade_Recourse_Or_Building):
                chooseonetoupgrade = self.WhichResourceToUpgrade()
                self.Resource_Task_List.append(chooseonetoupgrade)


    # def BuildingToBuild(self):
    #     self.Driver.get(self.Village_Url)
    #     s = input("enter building name:")
    #     while s != "":
    #         self.Buildings_To_Build.append(s)
    #         buildingname = s.split(":")[0]
    #         Count = s.split(":")[1]
    #         building = self.Buildings.FindBuilding(buildingname)
    #         building.Amount_Needed_To_Upgrade = int(Count)
    #         s = input("enter Building name:")


    def UpgradeBuilding(self):
        for i in self.Buildings_To_Build:
            buildingname = i
            try:
                if self.Making_Soliders == False:
                    building = self.Buildings.FindBuilding(buildingname)
                    if(building.Upgrade_To_Level > building.Level):
                        if (self.Tribe== "Romans" or self.What_To_Upgrade_Recourse_Or_Building == False):
                            buildingTask = BuildingTask(self.Driver, building)
                            self.Building_Task_List.append(buildingTask)
                    else:
                        self.Buildings_To_Build.remove(i)

            except:
                print("coudnt iniate building to upgrade")




    def DoResourceTask(self):
        try:
           # self.Driver.get(self.Village_Url)
            self.Resource_Task_List.pop(0).DoTask()
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("There wasnt recourse task" + "\n")
            Decomantation_File.close()
            print("There wasnt recourse task")

    def DoBuildingTask(self):
        check = (len(self.Building_Task_List)==0)
        try:
          #  self.Driver.get(self.Village_Url)
            if(self.Building_Task_List.__len__()>self.Buildings_To_Build.__len__()+2):
                self.Building_Task_List.clear()
            while self.Building_Task_List.__len__()>0:
               buildingtask = self.Building_Task_List.pop(0)
               check = buildingtask.DoTask()
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("There wasnt building task" + "\n")
            Decomantation_File.close()
            print("There wasnt building task")
        finally:
            return check

    def DoOtherTask(self):
        while (self.Other_Tasks_List.__len__() > 0):
            try:
           #    self.Driver.get(self.Village_Url)
                    self.Other_Tasks_List.pop(0).DoTask()
            except:
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("There wasnt other tasks"+str(len(self.Other_Tasks_List))+ "\n")
                Decomantation_File.close()
                print("There wasnt other tasks", len(self.Other_Tasks_List))


    def CheckWhenWherehouseOrBurnWillBeFull(self):
        ResourceList = [self.Wood, self.Clay, self.Iron, self.Wheet]
        self.Wood.Production, self.Clay.Production, self.Iron.Production, self.Wheet.Production = FindOutHowMuchMakingPerSecond(self.Driver)
        self.Wood.Holding, self.Clay.Holding, self.Iron.Holding, self.Wheet.Holding = ChecHowMuchReasourceIHave(self.Driver)
        mintimetofillwherehouse = self.WhereHouse_Size / min(self.Wood.Production, self.Iron.Production, self.Clay.Production,  self.Wheet.Production)
        for i in range(3):
           spaceleftwherehouse = self.WhereHouse_Size-ResourceList[i].Holding
           timetofill = spaceleftwherehouse/ResourceList[i].Production
           if (timetofill < mintimetofillwherehouse):
               mintimetofillwherehouse = timetofill
        mintimetofillwherehouse = mintimetofillwherehouse*3600
        timelefttofillburn = self.Burn_Size-ResourceList[3].Holding/ResourceList[3].Production*3600
        return min(mintimetofillwherehouse,timelefttofillburn)

    def WhichResourceToUpgrade(self):
        try:
            ResourceList = [self.Wood,self.Clay,self.Iron,self.Wheet]
            for i in ResourceList:
                minlevel = FindMinimunLevel(i)
                if (minlevel==10):
                    ResourceList.remove(i)
            self.Wood.Production, self.Clay.Production, self.Iron.Production, self.Wheet.Production = FindOutHowMuchMakingPerSecond(self.Driver)
            self.Wood.Holding, self.Clay.Holding, self.Iron.Holding, self.Wheet.Holding = ChecHowMuchReasourceIHave(self.Driver)
            minimunholding = min(self.Wood.Holding, self.Clay.Holding, self.Iron.Holding)
            minmunproduction = min(self.Wood.Production, self.Clay.Production, self.Iron.Production)
            if (self.Wheet.Holding < 0.6 * minimunholding):
                if(minimunholding < self.Burn_Size):
                    minimunholding = self.Wheet.Holding
            ListOfMinimun = []
            for i in ResourceList:
                if (i.Holding < minimunholding + minmunproduction / 4):
                    ListOfMinimun.append(i)
            if(len(ListOfMinimun) == 0):
                for i in ResourceList:
                    ListOfMinimun.append(i)
            chooseonetoupgrade = ListOfMinimun.pop(0)
            for i in ListOfMinimun:
                if (chooseonetoupgrade.Precrence > i.Precrence):
                    chooseonetoupgrade = i
                if (chooseonetoupgrade.Precrence == i.Precrence):
                    if (chooseonetoupgrade.Production > i.Production):
                            chooseonetoupgrade = i
            chooseonetoupgrade = ReacourceTask(self.Driver,chooseonetoupgrade)
            return chooseonetoupgrade
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coudnt find which resource to upgrade")
            Decomantation_File.close()


#---------------------new the check -----------------
    def MakeCelebration(self):
        try:
            cityhall = self.Buildings.FindBuilding("בניין העירייה")
            celebrationtask = CelebrationTask(self.Driver,cityhall,self.CelebrateSmall)
            self.Other_Tasks_List.append(celebrationtask)
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("cant make a celebration  task")
            Decomantation_File.close()
            print("cant make a celebration  task")


    def UpgradeWhereHouse(self):
        try:
           g = open("Text_Files\Game_Info", "r")
           data = g.read()
           data = json.loads(data)
           g.close()
           try:
                WareHouse_Time = int(data["warehouseholdstime"])
           except:
                WareHouse_Time = 8
           try:
                Burn_Time = int(data["burnholdstime"])
           except:
                Burn_Time = 8
           if self.Making_Soliders == False:
               self.WhereHouse_Size , self.Burn_Size = FindWherehouseAndBurnSize(self.Driver)
               woodproduction,clayproduction,ironproduction,wheetproduction = FindOutHowMuchMakingPerSecond(self.Driver)
               maxwherehouseproduction = max(woodproduction,clayproduction,ironproduction)
               if(self.WhereHouse_Size<WareHouse_Time *maxwherehouseproduction):
                   if(self.Tribe == "Romans" or self.What_To_Upgrade_Recourse_Or_Building==False):
                       wherehouse = self.Buildings.FindBuilding("Warehouse")
                       wherehouse.Upgrade_To_Level = wherehouse.Level +1
                       wherehouseTask = BuildingTask(self.Driver,wherehouse)
                       self.Building_Task_List.append(wherehouseTask)
                       #self.Buildings_To_Build.append(wherehouse.Name)
               if (self.Burn_Size < Burn_Time * wheetproduction):
                   if (self.Tribe == "Romans" or self.What_To_Upgrade_Recourse_Or_Building== False):
                        burn = self.Buildings.FindBuilding("Granary")
                        burn.Upgrade_To_Level = burn.Level + 1
                        burnTask = BuildingTask(self.Driver, burn)
                        self.Building_Task_List.append(burnTask)
                        #self.Buildings_To_Build.append(burn.Name)
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("count upgrade the wherehouse")
            Decomantation_File.close()
            print ("count upgrade the wherehouse")

    def BuildSolidersWhenWhereHouseIsFull(self):
        try:
            woodholding ,clayholding ,ironholding ,wheetholding = ChecHowMuchReasourceIHave(self.Driver)
            maxholding = max(woodholding,clayholding,ironholding)
            if(self.WhereHouse_Size*0.9 < maxholding): ## need to be Wherehouse*0.9
                solider = self.Solider_List.FindSolider(self.Solider_To_Build_When_Full)
                soliderTask = SoliderWhenFullTask(self.Driver,solider,self.Amount_To_Build_When_Full)
                self.Other_Tasks_List.append(soliderTask)
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coudnt make soliders when full")
            Decomantation_File.close()
            print ("coudnt make soliders when full")

    def MakeSoliderTask(self):
        count = 0
        for i in self.Solider_List.GetSoliderList():
            if i.Units_To_Build > 0:
                solidertask = SoliderTask(self.Driver,i)
                self.Other_Tasks_List.append(solidertask)
                count +=1
        if(count == 0 ):
            self.Making_Soliders = False

    def MakeAttackTask(self):
        nowtime1 = time.localtime()
        nowtime = nowtime1.tm_hour * 3600 + nowtime1.tm_min * 60 + nowtime1.tm_sec
        if nowtime- self.Time > self.Time_To_Robe:
            self.Time = nowtime
            for farm in self.Farm_List:
                try:
                    if(farm["tosend"]== "true"):
                        attaktask = AttackTask(self.Driver,farm["xcord"],farm["ycord"],farm["numofsolider"],farm["amount"],self.Url_Game)
                        self.Other_Tasks_List.append(attaktask)
                except:
                    print("cant make a farm list attck")






class ReacourceTask(object):
    def __init__(self,driver, resource):
        self.Driver = driver
        self.Resource = resource
    def DoTask(self):
        resource = FindMinimunLevel(self.Resource)
        return resource.Upgrade2()


class BuildingTask(object):
    def __init__(self, driver, building):
        self.Driver = driver
        self.Building = building
    def DoTask(self):
        self.Building.UpgradeBuilding2()

class SoliderTask(object):
    def __init__(self,driver,solider):
        self.Solider = solider
        self.Driver = driver

    def DoTask(self):
        self.Driver.get(self.Solider.Training_Building_Url.Url_Game)
        time.sleep(TimeToSleep)
        textloc = self.Solider.Text_Location
        textloclocation1 = self.Driver.find_elements_by_name("t"+str(textloc+1))
        webelement = textloclocation1[0]
        amount = str(self.Solider.Build_Each_Time)
        webelement.send_keys(amount)
        element = self.Driver.find_element_by_name("s1")
        try:
             element.click()
             self.Solider.Units_To_Build -= self.Solider.Build_Each_Time
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coudnlt build the solider")
            Decomantation_File.close()
            print("coudnlt build the solider")

class RunSoliderTask(object):
    def __init__(self,driver):
        self.Driver = driver


    def DoTask(self,soliderList):
        self.Driver.get(self.Soliders_Building_Url)
        textloc = self.Driver.find_elements_by_class_name("text")
        for i in soliderList:
            textloc[i.Text_Location].send_keys(str(i.Units))
        textloc[11].send_keys("The Killer2")
        button = self.Driver.find_elements_by_id("build")[0].find_elements_by_css_selector('button')[0]
        button.click()
        acceptbutton = self.Driver.find_element_by_id("waveForm").find_elements_by_css_selector('button')
        for i in acceptbutton:
            if (i.text == "אשר"):
                i.click()
        print("secsecc")
        time.sleep(20)


class HeroTask(object):
    def __init__(self,driver,Hero):
        self.Driver = driver
        self.Hero = Hero

    def DoTask(self):
        self.Hero.GoForAMission()
class AttackTask(object):
    def __init__(self,driver,x,y,textloc,amout,gameurl):
        self.Driver = driver
        self.X_Cord = x
        self.Y_Cord = y
        self.Text_Loc = textloc
        self.Amount = amout
        self.Url_Game = gameurl


    def DoTask(self):
        url = self.Url_Game+"/build.php?tt=2&id=39"
        self.Driver.get(url)
        xcotd = self.Driver.find_elements_by_class_name("xCoord")[0].find_element_by_name("x")
        ycord = self.Driver.find_elements_by_class_name("yCoord")[0].find_element_by_name("y")
        xcotd.send_keys(self.X_Cord)
        ycord.send_keys(self.Y_Cord)
        troopstext = self.Driver.find_element_by_id("troops").find_elements_by_name("troops[0][t" +self.Text_Loc+"]")
        troopstext[0].send_keys(self.Amount)
        element1 = self.Driver.find_elements_by_class_name("radio")
        attack = element1[2]
        attack.click()
        button = self.Driver.find_element_by_name("s1")
        button.click()
        okbutton =  self.Driver.find_element_by_name("a")
        okbutton.click()

class SoliderWhenFullTask(object):
    def __init__(self,driver,solider,amount):
        self.Driver = driver
        self.Solider = solider
        self.Amount = amount
    def DoTask(self):
        self.Driver.get(self.Solider.Training_Building_Url)
        element1 = self.Driver.find_elements_by_class_name("cta")
        textloc = self.Solider.Text_Location
        textloclocation = element1[textloc].find_elements_by_class_name("text")
        webelement = textloclocation[0]
        amount = str(self.Amount)
        webelement.send_keys(amount)
        element = self.Driver.find_element_by_name("s1")
        element.click()
#------------------ new to checkp-----------------------
class CelebrationTask(object):
    def __init__(self,driver,cityhall,celebratesmall = True):
        self.Driver = driver
        self.City_Hall = cityhall
        self.Small = celebratesmall

    def DoTask(self):
        self.Driver.get(self.City_Hall.Url_Game)
        time.sleep(TimeToSleep)
        build = self.Driver.find_element_by_id("build")
        costs = build.find_element_by_class_name("research")
        costs = costs.text.split(":")
        button = costs[2].split("\n")[1]
        costs = costs[0].split("\n")
        wood = int(costs[1])
        clay = int(costs[2])
        iron = int(costs[3])
        wheet = int(costs[4])
        if (button != "ערוך"):
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("cant do celebration")
            Decomantation_File.close()
            print("cant do celebration")
        else:
            woodhold, clayhold, ironhold, wheethold = ChecHowMuchReasourceIHave(self.Driver)
            if (woodhold > wood and clayhold > clay and ironhold > iron and wheethold > wheet):
                reserch = self.Driver.find_elements_by_class_name("research")
                if(self.Small == True):
                    cta = reserch[0].find_element_by_class_name("cta")
                    button = cta.find_element_by_class_name("textButtonV1")
                    button.click()
                else:
                    cta = reserch[1].find_element_by_class_name("cta")
                    button = cta.find_element_by_class_name("textButtonV1")
                    button.click()







