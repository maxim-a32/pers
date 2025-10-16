b = 0
a = input("a")
class Personag:
    name = None
    capability = None
    demeg = None
    def set_dat(self, name, capability, demeg):
        self.name = name
        self.capability = capability
        self.demeg = demeg
    def info(self):
        print("назва: ", self.name, "здібність: ", self.capability, "скільки урону наносить: ", self.demeg)
class Subject:
    name = None
    effect = None
    def set_dat(self, name, effect):
        self.name = name
        self.effect = effect
    def info(self):
        print(self.name, self.effect)
ic = Personag()
fire = Personag()
heal = Subject()
atac = Subject()
ic.set_dat("ice", "все сповільнює на 5 одиниць",  1)
fire.set_dat("fire", "Відсутні", 2)
heal.set_dat("heal", "+ 2 здоров'я")
atac.set_dat("atac", "+ 1 к урону")
if a == "ice":
    ic.info()
    b = 1
if a == "fire":
    fire.info()
    b = 1
if a == "heal":
    heal.info()
    b = 1
if a == "atac":
    atac.info()
    b = 1
if b == 0:
    print("Ви неправильно написали назву")
        
