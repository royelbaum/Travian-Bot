import time
from selenium import webdriver
import time

TimeToSleep = 0.5
MainUrl= "https://tx3.anglosphere.travian.com/dorf1.php"

woodcapacityfull = 0
claycapacityfull = 0
ironcapacityfull = 0
wheetcapacityfull = 0
def ClickHardButton(driver):
    try:
        time.sleep(TimeToSleep)
        element = driver.find_elements_by_class_name("section1")
        time.sleep(TimeToSleep)
        for i in element:
            x = str(i.text).split('\n')
            if(x[0]!= "Construct with master builder1"):
                i.find_element_by_class_name('textButtonV1').click()
                return True
            else:
                print("non")
                return False
    except:
        print("There is already a building")

def ClickHardButton2(driver, gameurl):
    try:
        time.sleep(TimeToSleep)
        element = driver.find_elements_by_class_name("section1")
        time.sleep(TimeToSleep)
        for i in element:
            x = str(i.text).split('\n')
            if(x[0]!= "בניה בעזרת בנאי מומחה1"):
                try:
                    i.find_element_by_css_selector('button').click()
                    driver.get(gameurl)
                    return True
                except:
                    print("coudnt click on hard button")

            else:
                print("There was to many building in progress")
                driver.get(gameurl)
                return False
    except:
        print("There is already a building")

def ChecHowMuchReasourceIHave(driver):
    time.sleep(TimeToSleep)
    try:
       # driver.get(MainUrl)
       resources = driver.find_elements_by_class_name("stockBarButton")
       woodcapacity = float(Make_Str_to_int(resources[0].text))
       claycapacity = float(Make_Str_to_int(resources[1].text))
       ironcapacity = float(Make_Str_to_int(resources[2].text))
       wheetcapacity = float(Make_Str_to_int(resources[3].text))
       #wherehousesize , burnsize = FindWherehouseSize(driver)
       if(woodcapacity % 1000 == 0):  #or woodcapacity>wherehousesize):
           woodcapacity = woodcapacity/1000
       if(claycapacity % 1000 == 0):  #or claycapacity>wherehousesize):
           claycapacity = claycapacity / 1000
       if(ironcapacity % 1000 == 0): #or ironcapacity>wherehousesize):
           ironcapacity = ironcapacity / 1000
       if (wheetcapacity % 1000 == 0):  #or wheetcapacity > burnsize):
           wheetcapacity = wheetcapacity / 1000
       return woodcapacity, claycapacity, ironcapacity, wheetcapacity
    except:
        print("coudnt find out how much reasurce i have")


def ChecHowMuchReasourceIHave2(driver):
    try:
       driver.get(MainUrl)
       resources = driver.find_elements_by_class_name("stockBarButton")
       woodcapacity = float(resources[0].text) * 1000
       claycapacity = float(resources[1].text) * 1000
       ironcapacity = float(resources[2].text) * 1000
       wheetcapacity = float(resources[3].text) * 1000
       #wherehousesize , burnsize = FindWherehouseSize(driver)
       if(woodcapacity % 1000 == 0):  #or woodcapacity>wherehousesize):
           woodcapacity = woodcapacity/1000
       if(claycapacity % 1000 == 0):  #or claycapacity>wherehousesize):
           claycapacity = claycapacity / 1000
       if(ironcapacity % 1000 == 0): #or ironcapacity>wherehousesize):
           ironcapacity = ironcapacity / 1000
       if (wheetcapacity % 1000 == 0):  #or wheetcapacity > burnsize):
           wheetcapacity = wheetcapacity / 1000
       return woodcapacity, claycapacity, ironcapacity, wheetcapacity
    except:
        print("cooudnt find out how much reasurce i have")


def CheckHowMuchBuildIsCost(driver,building_url):## need to enter the url of the building that want to check
   # driver.get(building_url)
    try:
        claycost = int(str(driver.find_elements_by_xpath("//*[@id='contract']/div[1]/div[2]").__getitem__(0).text))
        woodcost = int(str(driver.find_elements_by_xpath("//*[@id='contract']/div[1]/div[1]").__getitem__(0).text))
        ironcost = int(str(driver.find_elements_by_xpath("//*[@id='contract']/div[1]/div[3]").__getitem__(0).text))
        wheetcost = int(str(driver.find_elements_by_xpath("//*[@id='contract']/div[1]/div[4]").__getitem__(0).text))
        return woodcost,claycost,ironcost,wheetcost
    except:
        print("non")

def MaketimetoInt(timer):
    try:
        if(str(timer).__contains__(":")):
            array = str(timer).split(":")
            sumtime = 0
            for i in range(0, array.__len__()):
                sumtime = pow(60, 2 - i) * int(array[i]) + sumtime
            return sumtime
    except:
        print("non")
        return 0
    return 0

def checkifbiulding(driver):
    mintime = 60*60*10
    array = driver.find_elements_by_xpath("//*[@id='content']/div[2]/div[10]")
    if (array.__len__() > 0):
        array = array.__getitem__(0).find_elements_by_class_name("buildDuration")
        if(array.__len__()>1):
            for i in array:
                timer = MaketimetoInt(str(i.text).split()[0])
                if (timer < mintime):
                        mintime = timer
            f = open("Decomantation", "a")
            f.write("There was " +str(array.__len__()) + "Buildings and the minimum time was  " +str(mintime) + " in checkifbuilding\n")
            f.close()
            return mintime
    return 0

def CheckIfCanBuild(driver,url_building):
    woodcost,claycost,ironcost,wheetcost = CheckHowMuchBuildIsCost(driver,url_building)
    woodholding,clayholding,ironholding,wheetholding =  ChecHowMuchReasourceIHave(driver)
    if(woodholding>woodcost and clayholding>claycost and ironholding>ironcost and wheetholding>wheetcost):
        return True
    else:
        return False


def loginTravian(driver,username, password,urlgame):
    try:
        driver.get(urlgame + "/dorf1.php")
        driver.find_element_by_name("name").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("s1").click()
    except:
        try:
            cookies = driver.find_elements_by_class_name("CybotCookiebotDialogBodyButton")
            cookies[2].click()
            driver.get(urlgame + "/dorf1.php")
            driver.find_element_by_name("name").send_keys(username)
            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_name("s1").click()
        except:
            print("coudnt click on cookies")
        pass

def FindTimeToWaitForResouce(driver,buildingurl):
    driver.get(buildingurl)
    maxtime=0
    woodcost,claycost,ironcost,wheetcost =CheckHowMuchBuildIsCost(driver,buildingurl)
    costsArray = [woodcost,claycost,ironcost,wheetcost]
    woodholding,clayholding,ironholding,wheetholding = ChecHowMuchReasourceIHave(driver)
    holdingArray= [wheetholding,clayholding,ironholding,wheetholding]
    woodproduction,clayproduction,ironproduction,wheetproduction = FindOutHowMuchMakingPerSecond(driver)
    ProductionArray = [woodproduction,clayproduction,ironproduction,wheetproduction]
    timeResourceArray = [0,0,0,0]
    for i in range (0,4):
        if(holdingArray[i]-costsArray[i]>timeResourceArray[i]):
            timeResourceArray[i]=(holdingArray[i]-costsArray[i])/ProductionArray[i]
    for k in timeResourceArray:
        if(k>maxtime):
            maxtime=k
    return maxtime



def FindOutHowMuchMakingPerSecond(driver):
    # driver.get(MainUrl)
    try:
        time.sleep(TimeToSleep)
        element = driver.find_elements_by_id("production")
        for i in element:
            array = str(i.text).split(":")
            goodarray = []
            for k in range(1,array.__len__()):
                temparray = array[k].split("\n")
                for p in temparray:
                    if(p != "" and p!= None):
                        goodarray.append(p)
            for t in range(0,goodarray.__len__()):
                if(goodarray[t]=="Lumber"):
                    x= goodarray[t+1]
                    x= int(x[2:len(x)-1])
                    woodproduction = x
                elif (goodarray[t] == "Clay"):
                    x = goodarray[t + 1]
                    x = int(x[2:len(x) - 1])
                    clayproduction =x
                elif (goodarray[t] == "Iron"):
                    x = goodarray[t + 1]
                    x = int(x[2:len(x) - 1])
                    ironproduction =x
                elif (goodarray[t] == "Crop"):
                    x = goodarray[t + 1]
                    x = int(x[2:len(x) - 1])
                    wheetproduction =x
        return woodproduction, clayproduction, ironproduction, wheetproduction
    except:
        print("coudnt find how much makking per scound")


def FindWherehouseAndBurnSize(driver):
    try:
        element = driver.find_elements_by_class_name("capacity")
        wherehousesizearray = Make_Str_to_int(element[0].text[1:len(element[0].text)-1])
        # x = wherehousesizearray[0]
        # if (len(wherehousesizearray) > 1):
        #     y = wherehousesizearray[1]
        #     y = int(y[0:len(y) - 1])
        #     x = int(x[1:])
        #     x = x * 1000 + y
        # else:
        #     x = int(x)
        # wherehousesize = x
        burnsizearray = Make_Str_to_int(element[1].text[1:len(element[1].text)-1])
        # x = burnsizearray[0]
        # if(len(burnsizearray) > 1):
        #     x = int(x[1:])
        #     y = burnsizearray[1]
        #     y = int(y[0:len(y) - 1])
        #     x = x * 1000 + y
        # else:
        #     x = int(x)
        # burnsize = x
        return wherehousesizearray, burnsizearray
    except:
        print("coundt find the wherehouse and or burn size")

def CheckWhenHeroReturn(driver):
        try:
            element = driver.find_elements_by_class_name("movements")[0].find_elements_by_class_name("timer")
            timearray = []
            mintime = 3600*10
            for i in element:
                timearray.append(MaketimetoInt(i.text))
            for k in timearray:
                if(k<mintime):
                    mintime=k
            return mintime
        except:
            print("non")

def CheckHowMuchTimeToSleep(driver,timetoattack):
    driver.get(MainUrl)
    timetosleep = float('inf')
    time.sleep(TimeToSleep)
    minwherehousefull = CheckWhenWherehouseFull(driver)
    minbuildingtime = minwherehousefull
    try:
       # driver.get(MainUrl)
        minbuildingtime = CheckBuildingFinishTime(driver)
    except:
        print ("There was no building accure")
    finally:
        timetosleep = min(timetoattack, minbuildingtime, minwherehousefull)
        return timetosleep




def CheckBuildingFinishTime(driver):
    try:
       # driver.get(MainUrl)
        box = driver.find_element_by_class_name("buildingList")
        times = driver.find_elements_by_class_name("buildDuration")
        mintime = []
        for i in times:
            time = MaketimetoInt(i.text.split(" ")[0])
            mintime.append(time)
        min = mintime[0]
        for i in mintime:
            if(i<min):
                min=i
        return min
    except:
        print ("nothing was build")

def CheckWhenWherehouseFull(driver):
    try:
        wood, clay, iron, wheet = ChecHowMuchReasourceIHave(driver)
        wherehouse, burn = FindWherehouseAndBurnSize(driver)
        woodproduction, clayproduction, ironproduction, wheetproduction = FindOutHowMuchMakingPerSecond(driver)
        mintimewood = float((wherehouse - wood) / woodproduction) * 3600
        mintimeclay = float((wherehouse - clay) / clayproduction) * 3600
        mintimeiron = float((wherehouse - iron) / ironproduction) * 3600
        mintimewheet = float((burn - wheet) / wheetproduction) * 3600
        mintime = int(min(mintimewood, mintimeclay, mintimeiron, mintimewheet)) + 1
        return mintime
    except:
        print ("cannot check when wherehouse is full")

def CheckHowManyBuildingTaskInProgress(driver):
    times = []
    try:
      #  driver.get(MainUrl)
        box = driver.find_element_by_class_name("buildingList")
        times = driver.find_elements_by_class_name("buildDuration")
    except:
        print ("coundt find how much building in progress")
    return len(times)

def Make_Str_to_int(number):
    arr =  number.split(",")
    if(len(arr)<2):
        return int(arr[0])
    else:
        x = int(arr[0])
        y= int(arr[1])
        return x*1000+y







#driver = webdriver.Chrome(r"C:\Users\royel\Pyton Project\drivers\chromedriver.exe")
#urlgame= "https://tx3.travian.co.il"
#loginTravian(driver,"royelbaum12","1q3e5t7u9o",urlgame)
#FindWherehouseSize(driver)