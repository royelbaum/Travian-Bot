from selenium import webdriver
from Hero import Hero
from Resources import*
from Building import BuildingsList
from Useful_Function import loginTravian
from Task_Meneger import TaskMeneger, BuildingTask, ReacourceTask
from Soliders import SolidersList,Solider


class Village(object):
    def __init__(self,driver,Hitpotion_not_to_send_hero_for_a_quest,url_game,villageid):
        self.Url_Game = url_game
        self.Driver = driver
        self.Wood = Wood(driver,url_game)
        self.Clay = Clay(driver,url_game)
        self.Iron = Iron(driver,url_game)
        self.Wheet = Wheet(driver,url_game)
        self.WhereHouse_Size = 0
        self.Burn_Size = 0
        self.Hero = Hero(driver,url_game,Hitpotion_not_to_send_hero_for_a_quest)
        self.Buildings = BuildingsList(driver,url_game)
        self.Village_ID = villageid
        self.Village_Url = url_game + "/dorf1.php?newdid="+str(self.Village_ID) + "&"
        self.Task_Meneger = TaskMeneger(driver,self.Village_Url)
        self.Tasks = []
        self.Soliders_List =None
        self.Tribe = None
        self.Farm_List = []
        self.Celebrate = False
        self.CelebrateSmall = True


    def GetSoliderList(self):
        return self.Soliders_List

    def GetTaskMeneger(self) -> TaskMeneger:
        return self.Task_Meneger

    def InitiateVillage2(self,tribe):
        self.Tribe =tribe
        InitiateResource2(self.Driver,self.Url_Game,self.Wood,self.Clay,self.Iron,self.Wheet)
        self.Buildings.InitiateBuildingList()
        MegureiHaialim = None
        Urvaa = None
        NekudatMifgash =None
        try:
            NekudatMifgash = self.Buildings.FindBuilding("Rally Point")
            self.WhereHouse_Size , self.Burn_Size = FindWherehouseAndBurnSize(self.Driver)
            MegureiHaialim = self.Buildings.FindBuilding("Barracks")
            Urvaa = self.Buildings.FindBuilding("Stable")
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coundt find stable, barracks, meeting point")
            Decomantation_File.close()
            print("coundt find stable, barracks, meeting point")

        self.Soliders_List = SolidersList(self.Driver, self.Url_Game, NekudatMifgash.Url_Game, self.Tribe,MegureiHaialim,Urvaa)
        self.Task_Meneger.InitiateTaskMeneger(self.Wood,self.Clay,self.Iron,self.Wheet,self.Buildings,self.Hero,self.WhereHouse_Size,self.Burn_Size,self.Soliders_List,NekudatMifgash,self.Url_Game,self.CelebrateSmall,self.Tribe)







