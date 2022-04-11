class Anime:
    objName:str = ""
    title:str = ""
    link:str = ""
    thumb:str = ""
    status:str = ""
    desc:str = ""
    eplist:list = []

    def __init__(self, title:str,status:str,link:str,thumb:str):
        self.objName = link[29:]
        self.title = title.replace("Nonton anime", "").replace(" Sub Indo", "")
        self.link = link
        self.thumb = thumb