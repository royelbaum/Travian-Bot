#from Player import*
#from Resources import*
from selenium import webdriver
import time,sched,threading
Decomantation_File = open("Text_Files\Decomantation", "w")
Decomantation_File.close()
# when a user login in the first time need to get his info
#the game url is without login to the game //latesummer10x.travian.com
#need to inite every new village by hand or set them in the begining ... need to fix it
from Player import Player
from Useful_Function import loginTravian
import json


def Intredaction():
    username = input('please Enter UserName:')
    password = input('please Enter Password:')
    urlgame = input('please Enter Game_Url:')
    f = open("Game_info", "a")
    f.write("The UserName Is:" + username + '\n')
    f.write("The Password Is:" + password + '\n')
    f.write("The Game_Url Is:" + urlgame + '\n')
    s  = input('please Enter Village Id:')
    while s!="exit":
        f.write("The Village ID:" + str(s)+ "\n")
        s = input('please Enter Village Id:')



def InitiateBot2():
    f = open("Text_Files\Game_info", "r")
    g = open("Text_Files\Villages_ID", "r")
    if(f.read()==""):
        Intredaction()
    driver = webdriver.Chrome(r"C:\Users\royel\Pyton Project\drivers\chromedriver.exe")
    driver.maximize_window()
    f = open("Text_Files\Game_info", "r")
    username = f.readline()
    username = username.replace("\n","")
    urlgame = f.readline()
    urlgame = urlgame.replace("\n", "")
    tribe = f.readline()
    tribe = tribe.replace("\n", "")
    password = f.readline()
    password = password.replace("\n", "")
    player1 = Player(driver,username,password,urlgame,tribe)
    villageid = g.readline()
    while villageid!="\n" and villageid!= "":
        villageid = villageid.replace("\n", "")
        player1.AddVillage(int(villageid))
        villageid = g.readline()
    loginTravian(driver,username,password,urlgame)
    player1.InitiatePlayer()
    driver.get(player1.Villages[0].Village_Url)
    # driver.get(urlgame+"/dorf1.php")
    # village1 = player1.GetVillage(0)
    # driver.get(urlgame + "/dorf1.php")
    return player1

def InitiateBot(onlybuilding):
    f = open("Text_Files\Game_info", "r")
    g = open("Text_Files\Villages_ID", "r")
    if(f.read()==""):
        Intredaction()
    driver = webdriver.Chrome(r"C:\Users\royel\Pyton Project\drivers\chromedriver.exe")
    driver.maximize_window()
    f = open("Text_Files\Game_info", "r")
    data = f.read()
    data = json.loads(data)
    username = data["username"]
    urlgame = data["server"]
    tribe = data["tribe"]
    password = data["password"]
    player1 = Player(driver,username,password,urlgame,tribe)
    villageid = g.readline()
    while villageid!="\n" and villageid!= "":
        villageid = villageid.replace("\n", "")
        player1.AddVillage(int(villageid))
        villageid = g.readline()
    loginTravian(driver,username,password,urlgame)
    player1.InitiatePlayer(onlybuilding)
    driver.get(player1.Villages[0].Village_Url)
    # driver.get(urlgame+"/dorf1.php")
    # village1 = player1.GetVillage(0)
    # driver.get(urlgame + "/dorf1.php")
    return player1

def MainStart(farmlist = [],buildingtobuildlist = [],soliderlisttobuildwhenfulllist = [],soliderforbuildiglist = [],timetosleepbetweenattacksfromgui = 3600,timetosleepifnothingbuiledfromgui= 1800,onlybuilding = False):
    player1 = InitiateBot(onlybuilding)

    # need to be iniate by array like["123", "-7", "troops[0][t1]", "40","true"]
    #[x-location, y- location , the location on the solider in the solider list, number of soliders to send, if to send to this village or not]
    ## iniate farmlist
    ## params: time - in sec , the farmlist, the village number
    timetosleepbetweenattacks = timetosleepbetweenattacksfromgui
    player1.MakeRobFarmTask(timetosleepbetweenattacks,farmlist,1)


    # the solider that you want to build every
    soliderlisttobuildwhenfull = soliderlisttobuildwhenfulllist
    timetosleepifnothingbuiled = timetosleepifnothingbuiledfromgui
    player1.IniateBuildWhenFull(soliderlisttobuildwhenfull)


    #--------------------------------------------------------------------
    ## need to eneter all the building task that want to do in the schema:
    #1:מחסן:2
    #while the first number is the village and then the name of the builidng and then how many levels
    BuildingTaskforvilliges = buildingtobuildlist
    player1.MakeVilligesBuildingTask(BuildingTaskforvilliges)
    #---------------------------------------------------------------------

    #soliderforbuildig = []
    soliderforbuildig = soliderforbuildiglist

    onlysolider = []

    player1.MakeSolidersBuildingTask(soliderforbuildig,False)

    celebrations = []
    player1.MakeCelebrationTask(celebrations)



    player1.DotasksForAllVileges(timetosleepbetweenattacks,timetosleepifnothingbuiled)



