import random

gen1 = [[random.random()for x in range(5)]for x in range(8)]
f = ["Overweight","Hypertension","Diabetes","Cancer","Asthma"]

class Person:
    chromo = ""
    age = 0
    genre = ""
    infected = False
    features = []
    probi = 0.0
    probd
    mul = 1.0
    ##Sobrepeso, hipertensión, diabetes, EnPulmonar, Cáncer, Asma, EnCardiovascular

    def __init__(self,c):
        self.features = []
        self.chromo = c
        self.age = random.randint(6,90)
        self.genre = random.choice(["Male","Female"])
        
        for i in range(5):
            j = random.randint(1,10)
            if j == 1:
                self.features.append(f[i])
        if c[0] == '1': self.infected = True
        else: self.infected = False
        self.calprobi()
    
    def calprobi(self):
        if self.infected: 
            self.mul += 2.0
            self.probi += 3
        if self.age >= 80: self.probi += 15.0
        elif self.age >= 65: self.probi += 8.0
        
        for i in range(len(self.features)):
            if self.features[i] == "Overweight": self.mul += 0.5
            elif self.features[i] == "Diabetes": self.mul += 0.5
            elif self.features[i] == "Cancer": self.mul += 1.0
            elif self.features[i] == "Asthma": self.mul += 1.0
            elif self.features[i] == "Hypertension": self.mul += 1.0
        
        for i in range(0,len(self.chromo)-1):
            if i == 1 and self.chromo[i] == '1':
                if "Asthma" in self.features: self.mul += 0.3
                else :self.mul += 0.1
            elif i == 1 and self.chromo[i] == '0':
                if "Asthma" in self.features: self.mul -= 0.5
                else :self.mul -= 1.0
            if i == 2 and self.chromo[i] == '1':
                if "Hypertension" in self.features: self.mul += 0.3
                else :self.mul += 0.1
            elif i == 2 and self.chromo[i] == '0':
                if "Hypertension" in self.features: self.mul -= 0.5
                else :self.mul -= 1.0
        self.prob *= self.mul





def generatePerson(g):
    gen = []
    for i in range(8):
        b = '1'
        for j in range(1,3):
            if g[i][j] < 0.15:
                b += '1'
            else:
                b += '0'
        b +='00'
        p = Person(b)
        gen.append(p)
    return gen

gen = generatePerson(gen1)
gen2 = [[random.random()for x in range(5)]for x in range(8)]

def generateChromosome(g):
    gen = []
    for i in range(8):
        b = '1'
        for j in range(1,3):
            if g[i][j] < 0.45:
                b += '1'
            else:
                b += '0'
        if g[i][3] < 0.15: b+= '1'
        else: b += '0'
        b += '0'
        gen.append(b)
    return gen

def selection(g2,p):
    comparados = []
    g = deepcopy(g2)
  
    return g


def PrintPerson(p):
    print(p.age)
    print(p.genre)
    print(p.chromo)
    print(p.infected)
    print(p.features)
    print(p.prob)
    print(p.mul, "\n")

for i in range(7):
    PrintPerson(gen[i])
