
from Useful_Function import*


def InitiateResource(Resource_List):
    for i in Resource_List:
        i.FindLevel()


def InitiateResource2(driver,gameurl,Woodlist,Claylist,Ironlist,Wheetlist):
    for i in range(1,19):
        resource = Resource(driver,i,gameurl,None)
        resource.FindLevel2(Woodlist,Claylist,Ironlist,Wheetlist)







class Resource(object):
    def __init__(self, driver , id , game_url,name):
        self.Url_Game = game_url + "/build.php?id=" + str(id)
        self.Id = id
        self.Driver = driver
        self.Level = 0
        self.Name = name
        self.Holding = 0
        self.Production = 0
        self.Last_Time_Check = 0

    def FindLevel(self):
        self.Driver.get(self.Url_Game)
        x = self.Driver.find_elements_by_xpath("//*[@id='content']/h1")
        array = str(x.__getitem__(0).text).split()
        self.Level=int(array[array.__len__()-1])

    def FindLevel2(self,Woodlist,Claylist,Ironlist,Wheetlist):
        try:
            self.Driver.get(self.Url_Game)
            time.sleep(TimeToSleep)
            x = self.Driver.find_elements_by_xpath("//*[@id='content']/h1")
            array = str(x.__getitem__(0).text).split()
            self.Level=int(array[array.__len__()-1])
            name = array[0]
            if(name == "Woodcutter"):
                self.SetName("Wood")
                Woodlist.Resource_List.append(self)
            elif (name == "Clay"):
                self.SetName("Clay")
                Claylist.Resource_List.append(self)

            elif (name == "Iron"):
                self.SetName("Iron")
                Ironlist.Resource_List.append(self)
            else:
                self.SetName("Wheet")
                Wheetlist.Resource_List.append(self)
        except:
            Decomantation_File = open("Text_Files\Decomantation", "a")
            Decomantation_File.write("coudnt iniate resources properly\n")
            Decomantation_File.close()
            print("coudnt iniate resources properly")

    def SetName(self,name):
        self.Name = name

    def Upgrade2(self):
         self.Driver.get(self.Url_Game)
         time.sleep(TimeToSleep)
         taskispossible = CheckIfCanBuild(self.Driver,self.Url_Game)
         if(taskispossible == False):
             Decomantation_File = open("Text_Files\Decomantation", "a")
             Decomantation_File.write("Didnt have enogh resources and in Upgrade Resource\n")
             Decomantation_File.close()
             print("Didnt have enogh resources and in Upgrade Resource")
             self.Driver.back()
             time.sleep(TimeToSleep)
             return taskispossible
         else:
             taskispossible = False
             taskispossible = ClickHardButton(self.Driver)
             if(taskispossible == True):
                 self.Level+=1
             if(taskispossible == False):
                self.Driver.back()
                time.sleep(TimeToSleep)
                Decomantation_File = open("Text_Files\Decomantation", "a")
                Decomantation_File.write("Coudnt press the build button in Upgrade Resource\n")
                Decomantation_File.close()
                print("Coudnt press the build button in Upgrade Resource")
         return taskispossible


    def GetBuildTime(self):
        self.Driver.get(self.Url_Game)
        x = self.Driver.find_element_by_class_name("section1")
        y = str(x.text).split()
        for i in y:
          s = MaketimetoInt(i)
          if(s != 0):
             return s
        print(" Didnt Find Any Time")


## the list of all woods resources
class Wood(object):
    def __init__(self,driver = None,game_url = None):
        if(driver!= None and game_url!=None):
            self.Resource_List = []
            self.Url_Game = game_url
            self.Driver = driver
            self.Name = "Wood"
            self.Holding = 0
            self.Production = 0
            self.Precrence = 1
            self.Last_Time_Check = 0
        else:
            self.Wood_List = []
            self.Url_Game = game_url
            self.Driver = driver
    def GetHolding(self):
        return self.Holding
    def GetProduction(self):
        return self.Production
    def GetResource_List(self):
        return self.Resource_List
    def EnterRecourceTOTHeList(self,resource):
        self.Resource_List.append(resource)




class Clay(object):
    def __init__(self,driver = None,game_url = None):
        if (driver != None and game_url != None):
            self.Resource_List=[]
            self.Url_Game = game_url
            self.Driver = driver
            self.Name = "Clay"
            self.Holding = 0
            self.Production = 0
            self.Precrence = 1
            self.Last_Time_Check = 0
        else:
            self.Resource_List = []
            self.Url_Game = game_url
            self.Driver = driver

    def GetResource_List(self):
        return self.Resource_List

class Iron(object):
    def __init__(self,driver = None,game_url = None):
        if (driver != None and game_url != None):
            self.Resource_List=[]
            self.Url_Game=game_url
            self.Driver = driver
            self.Name = "Iron"
            self.Holding = 0
            self.Production = 0
            self.Precrence = 2
            self.Last_Time_Check = 0
        else:
            self.Resource_List = []
            self.Url_Game = game_url
            self.Driver = driver

    def GetResource_List(self):
        return self.Resource_List


class Wheet(object):
    def __init__(self,driver = None,game_url = None):
        if (driver != None and game_url != None):
            self.Resource_List=[]
            self.Url_Game=game_url
            self.Driver = driver
            self.Name = "Wheet"
            self.Holding = 0
            self.Production = 0
            self.Precrence = 3
            self.Last_Time_Check = 0
        else:
            self.Resource_List = []
            self.Url_Game = game_url
            self.Driver = driver

    def GetResource_List(self):
        return self.Resource_List

def FindMinimunLevel(Resource_List) -> Resource:
    minlevel = 21
    resource = None
    for i in Resource_List.Resource_List:
        if(i.Level< minlevel and i.Level< 10):
            minlevel=i.Level
            resource = i
    return resource


