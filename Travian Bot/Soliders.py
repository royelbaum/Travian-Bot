class Solider(object):
    def __init__(self, name, units, unitsname,trainingbuildingurl, TextLocation=None):
        self.Text_Location = TextLocation
        self.Name = name
        self.Units_Name = unitsname
        self.Units = units
        self.Training_Building_Url = trainingbuildingurl
        self.Units_To_Build = 0
        self.Build_Each_Time = 0

    def SetUnit(self, units):
        self.Units = units

    def BuildSoliders(self, amountofsoliders):
        self.Driver.get(self.Training_Building.Url_Game)
        Textlist = self.Driver.find_elements_by_class_name("text")
        Textlist[self.TextLocation].send_keys(amountofsoliders)
        element = self.Driver.find_elements_by_id("build")[0].find_elements_by_css_selector('button')
        for i in element:
            if (i.text == "אמן"):
                i.click()


class SolidersList(object):

    def __init__(self, driver, game_url, nekudatmifgash=None, tribe=None,megureyhaialim=None,urvaa=None):
        self.Tribe = tribe
        self.Driver = driver
        self.Url_Game = game_url + "/dorf1.php"
        self.Soliders_Building_Url = nekudatmifgash
        self.Soliders_List = []
        try:
            if (tribe == "Romans"):
                self.Soliders_List.append(Solider("Legionnaire", 0, "Legionnaires",megureyhaialim,0))
                self.Soliders_List.append(Solider("Praetorian", 0,"Praetorians",megureyhaialim,1))
                self.Soliders_List.append(Solider("Imperian", 0, "Imperians",megureyhaialim,2))
                self.Soliders_List.append(Solider("Equites Legati", 0, "Equites Legatis",urvaa,0))
                self.Soliders_List.append(Solider("Equites Imperatoris", 0, "Equites Imperatoris",urvaa,1))
                self.Soliders_List.append(Solider("Equites Caesaris", 0, "Equites Caesaris",urvaa,2))
            elif (tribe == "Teutons"):
                self.Soliders_List.append(Solider("Clubswinger", 0, "Clubswingers,",megureyhaialim,0))
                self.Soliders_List.append(Solider("Spearman", 0, "Spearmans"))
                self.Soliders_List.append(Solider("Axeman", 0, "Axemans"))
                self.Soliders_List.append(Solider("Scout", 0, "Scouts"))
                self.Soliders_List.append(Solider("Paladin", 0,"Paladins" , urvaa,0))
                self.Soliders_List.append(Solider("Teutonic Knight", 0, "Teutonic Knights", urvaa, 1))
            elif (tribe == "Gauls"):
                self.Soliders_List.append(Solider("Phalanx", 0,"Phalanxs",megureyhaialim.Url_Game,0))
                self.Soliders_List.append(Solider("Swordsman", 0,"Swordsmans",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("Pathfinder", 0,"Pathfinders",urvaa,0))
                self.Soliders_List.append(Solider("Theutates Thunder", 0,"Theutates Thunders",urvaa,0))
                self.Soliders_List.append(Solider("Druidrider", 0,"Druidriders",urvaa,0))
                self.Soliders_List.append(Solider("Haeduan", 0,"Haeduans",urvaa,0))

            elif(tribe == "הונים"):
                self.Soliders_List.append(Solider("שכיר חרב", 0,"שכירי חרב",megureyhaialim.Url_Game,0))
                self.Soliders_List.append(Solider("קשת", 0,"קשתים",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("צופה", 0,"צופים",megureyhaialim.Url_Game))
                self.Soliders_List.append(Solider("רוכב הערבה", 0,"רוכב הערבה",megureyhaialim.Url_Game,1 ))
                self.Soliders_List.append(Solider("צלף", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("שודד", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("אייל ניגוח", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("מקלעת", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("לוגדס", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("מתיישב", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
                self.Soliders_List.append(Solider("גיבור", 0,"רוכב הערבה",megureyhaialim.Url_Game,1))
        except:
            print("coundt make solider list")

    def GetSoliderList(self):
        return self.Soliders_List


    def Runsoliders(self, soliderList): ## working need to see if can cancel
        self.Driver.get(self.Soliders_Building_Url)
        textloc = self.Driver.find_elements_by_class_name("text")
        for i in soliderList:
            textloc[i.Text_Location].send_keys(str(i.Units))
        textloc[11].send_keys("The Killer2")
        button = self.Driver.find_elements_by_id("build")[0].find_elements_by_css_selector('button')[0]
        button.click()
        acceptbutton = self.Driver.find_element_by_id("waveForm").find_elements_by_css_selector('button')
        for i in acceptbutton:
            if(i.text == "אשר"):
                i.click()
        print("secsecc")

    def FindSolider(self,solidername):
        for i in self.Soliders_List:
            if(i.Name == solidername):
                return i

