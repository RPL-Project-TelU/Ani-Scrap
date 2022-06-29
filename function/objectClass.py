class Anime:
    objName:str = ""
    title:str = ""
    link:str = ""
    thumb:str = ""
    status:str = ""
    desc:str = ""
    eplist:list = None
    eps:str = ""

    def __new__(cls, title:str,status:str,eps:str,link:str,thumb:str):
        anime = object.__new__(cls)
        return anime

    def __init__(self, title:str,status:str,eps:str,link:str,thumb:str):
        if self.eplist is None:
            self.eplist = []
        self.objName = link[29:]
        self.title = title.replace("Nonton anime ", "").replace(" Sub Indo", "")
        self.status = status
        self.eps = eps
        self.link = link
        self.thumb = thumb