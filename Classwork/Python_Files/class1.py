#!/usr/bin/python
class Mard():
    __anun = "Vagharsh"
    __azganun = None
    tariq = None


class Usucich(Mard):
    mard=Mard()	
    asxhatanqin_stazh = None

    def setter(self,mard,ashxatanqain_stazh):
        self.mard=mard
        self.asxhatanqin_stazh = ashxatanqain_stazh

    def getUsucich(self):
        print("______Usucchi Tvyalner@______"'\n' "Anun :",self.mard.__anun.title(),'\n'"Azganun :",self.mard.__azganun.title(),'\n'"Tariq :",self.mard.tariq,'\n'"Stazh :",self.asxhatanqin_stazh)

    def addUsucich(self,mard,ashxatanqain_stazh):
        n = []
        n.append(self.setter(anun,azganun,tariq,ashxatanqain_stazh))


class Usanox(Mard):
    kurs = None
    mard=Mard()
    def setter(self,mard,kurs):
        self.mard=mard
        self.kurs=kurs

    def getUsanox(self):
        print("____Usanoxi Tvyalner@_____"'\n'"Anun :",self.__anun.title(),'\n'"Azgnun :",self.__azganun.title(),'\n'"Tariq :",self.tariq,'\n'"Kurs :",self.kurs)
        return '\n'"Anun :",self.mard.__anun.title(),'\n'"Azgnun :",self.mard.__azganun.title(),'\n'"Tariq :",self.mard.tariq,'\n'"Kurs :",self.kurs,'\n'" "

    def addUsanox(self,anun,azganun,tariq,kurs):
        n = []
        n.append(self.setter(anun,azganun,tariq,kurs))
        file1 = open('Usanoxner.txt', 'a')
        for i in self.getUsanox():
            file1.write(str(i))

class Institut():
	dekanatner = None
	ambionner = None
	kurser = None


	





usucich = Usucich()

usanox = Usanox()



usucich.setter('dsadasdas','dasdasd',23,2)
usucich.getUsucich()
usucich.addUsucich('xcvxcvxc','vcxxcvxcv',21,1)
usucich.getUsucich()
usanox.setter("yuiyuiyu","yuiuyiyu",24,1)
usanox.getUsanox()
usanox.addUsanox('nbmbnmbn','kljlkjljk',21,1)
usanox.addUsanox('gfdgdfn','gdfk',21,1)
usanox.addUsanox('nrturutymbn','gfdgdfgdf',21,1)
usanox.addUsanox('SDASDASDAS','KJHJKHdasdasf',21,1)




usanox.getUsanox()









