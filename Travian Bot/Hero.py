import time
from selenium import webdriver
from Useful_Function import MaketimetoInt
MainUrl= "https://tx3.anglosphere.travian.com/dorf1.php"

class Hero(object):
    def __init__(self,driver=None,game_url=None,hitpoint_not_to_go_for_a_mission=None):
        if(driver!=None and game_url!=None and hitpoint_not_to_go_for_a_mission!=None):
            self.Url_Game =game_url +"/hero.php?flagAttributesBoxOpen"
            self.Main_Url = game_url + "/dorf1.php"
            self.Driver =driver
            self.Minmun_Hitpoints =hitpoint_not_to_go_for_a_mission
            self.Home_Village_Name = None;
        else:
            self.Url_Game = game_url
            self.Driver = driver
            self.Minmun_Hitpoints = hitpoint_not_to_go_for_a_mission


    def GoForAMission(self):
        self.Driver.get(self.Main_Url)
        time.sleep(0.5)
        if(self.CheckIfHeroInVillage()):
            herohp =self.getHeroLifePoints()
            if(herohp>self.Minmun_Hitpoints):
                maxtimeindex = None;
                maxtime = 0
                self.Driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[3]").click()
                time.sleep(0.5)
                element = self.Driver.find_element_by_id("adventureListForm")
                element2 = element.find_element_by_css_selector('tbody').find_elements_by_class_name("goTo")
                element3 = element.find_elements_by_class_name("moveTime")
                timeinsec = []
                for i in range(1, element3.__len__()):
                   timeinsec.append(MaketimetoInt(element3[i].text))
                for x in range(0, timeinsec.__len__()):
                    if (maxtime < timeinsec[x]):
                        maxtime = timeinsec[x]
                        maxtimeindex = x
                if(maxtimeindex != None):
                    element2.__getitem__(maxtimeindex).click()
                    time.sleep(0.5)
                    self.Driver.get(MainUrl)
                    time.sleep(0.5)
                else:
                    f = open("Text_Files\Decomantation", "a")
                    f.write("Coudnt go to a Mission because there wast any mission\n")
                    f.close()
                    self.Driver.get(self.Main_Url)
                    time.sleep(0.5)
            else:
                f = open("Text_Files\Decomantation", "a")
                f.write("Coudnt go to a Mission the hero didnt have enoght HP\n")
                f.close()
                self.Driver.get(self.Main_Url)
                time.sleep(0.5)
        else:
            print("Coudnt go to a Mission Hero Wasnt in the viilage\n")
            self.Driver.get(MainUrl)
            time.sleep(0.5)
            return False


    def getHeroLifePoints(self):
        self.Driver.get(self.Url_Game)
        time.sleep(0.5)
        list = self.Driver.find_elements_by_xpath("//*[@id='attributes']/div[1]/div[3]/table/tbody/tr[1]/td[3]/div")
        lifepoints = list[0].find_element_by_css_selector('div.bar')
        hppoints = int(str(lifepoints.get_attribute("style")).split(":")[1].split("%")[0])
        return hppoints

    def CheckIfHeroInVillage(self):  ## need to complete
        element = self.Driver.find_element_by_id("troops")
        element2 = element.find_elements_by_class_name("un")
        for i in element2:
            if (i.text == "Hero"):
                return True
        return False

    def SetHeroHomeVillage(self,village):
        self.Home_Village_Name = village.Name