from selenium import webdriver
from Soliders import Solider,SolidersList
from Resources import Wood,Wheet,Iron,Clay
from Task_Meneger import SoliderTask
from Useful_Function import ClickHardButton,FindOutHowMuchMakingPerSecond,ChecHowMuchReasourceIHave,FindWherehouseAndBurnSize
from Useful_Function import*
import time
import json


def loginTravian(driver,username, password,urlgame):
    driver.get(urlgame + "/dorf1.php")
    driver.find_element_by_name("name").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("s1").click()

#
# driver = webdriver.Chrome(r"C:\Users\royel\Pyton Project\drivers\chromedriver.exe")
# urlgame= "https://tx3.anglosphere.travian.com"
# loginTravian(driver,"royelbu","Luka1309",urlgame)
# time.sleep(1)
# try:
#     element = driver.find_elements_by_class_name("capacity")
#     wherehousesizearray = Make_Str_to_int(element[0].text[1:len(element[0].text) - 1])
#     burnsizearray = Make_Str_to_int(element[1].text[1:len(element[1].text) - 1])
#     print("the warehouse size", wherehousesizearray)
#     print("the burn size", burnsizearray)
# except:
#     print("non")

s = '{"success": "true", "status": 200, "message": "Hello"}'
f = open("Text_Files\Decomantation", "w")
f.write(s)
f.close()
f = open("Text_Files\Decomantation", "r")
s= f.readline()
d = json.loads(s)

print(d["success"])





#------- try to do run away solider task
# X_Cord = 5
# Y_Cord =10
# elem = driver.find_element_by_id("movements")
# kind = elem.find_elements_by_class_name("troopMovements")
# movment = elem.find_elements_by_class_name("mov")
# print("this is the map diteils:", elem.text)
# driver.get("https://latesummer10x.travian.com//build.php?tt=2&id=39")
# time.sleep(1)
# xcotd = driver.find_elements_by_class_name("xCoord")[0].find_element_by_name("x")
# ycord = driver.find_elements_by_class_name("yCoord")[0].find_element_by_name("y")
# xcotd.send_keys(X_Cord)
# ycord.send_keys(Y_Cord)
# troopstext = driver.find_element_by_id("troops")
# texts = troopstext.find_elements_by_class_name("text")
# amount = troopstext.find_element_by_class_name("line-first‭")
#
# for i in texts:
#     i.send_keys(1)
# element1 = driver.find_elements_by_class_name("radio")
# attack = element1[2]
# attack.click()
# button = driver.find_element_by_name("s1")
# button.click()
# okbutton =  driver.find_element_by_name("a")

# for i in movment:
#     print(i.text)


















'''
element = driver.find_elements_by_class_name("movements")
for i in element:
    attaksarray = i.text.split("\n")
outforces = []
inforces = []
for i in attaksarray:
    word= attaksarray[0]
    if(word != "כוחות נכנסים"):
        outforces.append(i)



wood = Wood(driver,urlgame)
wheet = Wheet(driver,urlgame)
clay = Clay(driver,urlgame)
iron = Iron(driver,urlgame)
wherehousesize , burnsize = FindWherehouseAndBurnSize(driver)
ResourceList = [wood, clay, iron, wheet]
wood.Production, clay.Production, iron.Production, wheet.Production = FindOutHowMuchMakingPerSecond(driver)
wood.Holding, clay.Holding, iron.Holding, wheet.Holding = ChecHowMuchReasourceIHave(driver)
spaceleftwherehouse = wherehousesize
mintimetofillwherehouse = wherehousesize/min(wood.Production,iron.Production,clay.Production,wheet.Production)
soliderlist = SolidersList(driver,urlgame,"https://tx3.travian.co.il/build.php?tt=2&id=39","רומאים")



attakerslist = []
for i in element1:
    array =  str(i.text).split("\n")
for i in range(0,array.__len__()):
    if array[i].find("בוזז")>0:
        arriveltim = array[i+4].split()[1]
        arriveltim=MaketimetoInt(arriveltim)
        attakerslist.append(arriveltim)









soliderlist.InitiateSolidersList()
soliderstosend = []
soliderstosend.append(soliderlist.Getsolider(10))
soliderlist.Runsoliders(soliderstosend)
'''