class Anime:
    objName:str = ""
    title:str = ""
    link:str = ""
    thumb:str = ""
    status:str = ""
    desc:str = ""
    eplist:list = None
    eps:str = ""
    genres:list = None

    def __new__(cls, objname:str,title:str,status:str,link:str,thumb:str,desc:str,eps:str):
        anime = object.__new__(cls)
        return anime

    def __init__(self, objname:str,title:str,status:str,link:str,thumb:str,desc:str,eps:str):
        if self.eplist is None:
            self.eplist = []
        if self.genres is None:
            self.genres = []
        self.objName = objname
        self.title = title
        self.status = status
        self.link = link
        self.thumb = thumb
        self.desc = desc
        self.eps = eps