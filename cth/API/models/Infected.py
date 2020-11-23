class Infected:

    def __init__(cid , infcount, infcheckup , infdate , infname):
        self.cid = cid
        self.infcount = infcount
        self.infcheckup = infcheckup
        self.infdate = infdate
        self.infname = infname



    def get_cid(self):
        return self.cid

    def get_infocount(self):
        return self.infcount

    def get_infname(self):
        return self.infname

    def get_infcheckup(self):
        return self.infcheckup

    def set_infdate(self, infdate):
         self.infdate = infdate

    def set_cid(self, cid):
         self.cid = cid

    def set_infocount(self, infcount):
         self.infcount = infcount

    def set_infname(self, infname):
         self.infname = infname

    def set_infcheckup(self, infcheckup):
         self.infcheckup = infcheckup

    def set_infdate(self, infdate):
         self.infdate = infdate

    def to_dict(infected):
        list = []
        for result in list:
            
            list.append(sub)
        return list
