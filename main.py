import copy
import random

POCET_JEDINCOV=100
POCET_GENERACII=500
global GENERACIA








class Jedinec():

    def __init__(self,matica, fitnes=0):
        self.fitnes = fitnes
        self.gen = []
        self.matica = matica
        self.poradie = 1
        self.good = True
        self.generation = 0

    def update_fitness(self):
        self.fitnes = self.fitnes

    def up_fitness(self):
        self.fitnes = self.fitnes + 1

    def set_gen(self,gen):
        self.gen = gen

    def set_velkost_matice(self,x,y):
        self.matica_x = x
        self.matica_y = y

    def up_poradie(self):
        self.poradie = self.poradie + 1

    def set_bad(self):
        self.good = False

    def set_generation(self,generation):
        self.generation = generation




def zen_down(jedinec,x,y,poradie,cislo):
    #print_matica(jedinec.matica)
    #print("down" + str(x) + " " + str(y))
    matrix = jedinec.matica

    while (x != jedinec.matica_x):
        if (matrix[x][y] == cislo):
            if (poradie != 0) :
                jedinec.up_fitness()
            else:
                jedinec.fitnes = jedinec.fitnes - 1
            matrix[x][y] = poradie
        elif (x == 0):
            return
        else:
            if (y + 1 < jedinec.matica_y):                          # kontrola či sa po pohybe vpravo budem nachádzať stále v matici

                if (matrix[x-1][y + 1] == cislo):                       # kontrola či je na pravo od Zen(a) nepoorané políčko
                    check = zen_right(jedinec,x-1, y+1,poradie,cislo)                  # posúvaj sa doprava
                    if (check == False):
                        return False
                    return True

                elif (y - 1 > -1):                                  # je tam kamen pozri sa na druhú stranu

                    if (matrix[x - 1][y - 1] == cislo):                 # kontrola či sa po pohybe vlavo budem nachádzať v matici
                        check = zen_left(jedinec, x - 1, y - 1,poradie,cislo)     # posúvaj sa dolava
                        if (check == False):
                            return False
                        return True
                    else:                                           # je tam kamen ( kamen je aj zlava aj zprava
                        return False

                elif (y - 1 == -1):
                    return True


            elif (y + 1 == jedinec.matica_y):
                return True


            elif (y - 1 >  -1):                                  # je tam kamen pozri sa na druhú stranu

                if (matrix[x-1][y-1] == cislo):                      #  kontrola či sa po pohybe vlavo budem nachádzať v matici
                    check = zen_left(jedinec, x-1, y-1,poradie,cislo)                      #posúvaj sa dolava
                    if (check == False):
                        return False
                    return True
                else:                                           #  je tam kamen ( kamen je aj zlava aj zprava
                    return False

            elif (y-1 == -1):
                return True


        x = x + 1

    return True


def zen_left(jedinec,x,y,poradie,cislo):
    #print_matica(jedinec.matica)
    #print("left " + str(x) + " " + str(y))
    matrix = jedinec.matica

    while (y != -1):
        if (matrix[x][y] == cislo):
            if (poradie != 0):
                jedinec.up_fitness()
            else:
                jedinec.fitnes = jedinec.fitnes - 1
            matrix[x][y] = poradie
        elif (y == jedinec.matica_y-1):
            return
        else:
            if (x + 1 < jedinec.matica_x):              # kontrola či sa po pohybe dole budem nachádzať stále v matici

                if (matrix[x + 1][y + 1] == cislo):             # kontrola či je dole od Zen(a) nepoorané políčko
                    check = zen_down(jedinec,x+1,y+1,poradie,cislo)                        # posúvaj sa dole
                    if (check == False):
                        return False
                    return True

                elif (x - 1 > -1):                               # je tam kamen pozri sa na druhú stranu

                    if (matrix[x - 1][y + 1] == cislo):                 # kontrola či sa po hore budem nachádzať v matici
                        check = zen_up(jedinec,x-1,y+1,poradie,cislo)                      # posúvaj sa hore
                        if (check == False):
                            return False
                        return True
                    else:                                            # je tam kamen ( kamen je aj zhora aj zdola)
                        return False

                elif (x-1 == -1):
                    return True


            elif (x+1 == jedinec.matica_x):
                return True


            elif (x - 1 > -1):                              # je tam kamen pozri sa na druhú stranu
                if (matrix[x - 1][y + 1] == cislo):             # kontrola či sa po hore budem nachádzať v matici
                    check = zen_up(jedinec, x - 1, y + 1,poradie,cislo)    # posúvaj sa hore
                    if (check == False):

                        return False
                    return True
                else:                                       # je tam kamen ( kamen je aj zhora aj zdola)
                    return False
            elif (x - 1 == -1):
                return True

        y = y - 1

    return True


def zen_up(jedinec,x,y,poradie,cislo):
    #print_matica(jedinec.matica)
    #print("up " + str(x) + " " + str(y))
    matrix = jedinec.matica


    while (x != -1):
        if (matrix[x][y] == cislo ):
            if (poradie != 0):
                jedinec.up_fitness()
            else:
                jedinec.fitnes = jedinec.fitnes - 1
            matrix[x][y] = poradie
        elif (x == jedinec.matica_x-1):
            return
        else:

            if (y + 1 < jedinec.matica_y):                  # kontrola či sa po pohybe vpravo budem nachádzať stále v matici


                if (matrix[x+1][y+1] == cislo):                   # kontrola či je vpravo od Zen(a) nepoorané políčko
                    check = zen_right(jedinec,x+1, y+1,poradie,cislo)               # posúvaj sa vpravo
                    if (check == False):
                        return False
                    return True

                elif (y - 1 > -1):                                 # je tam kamen pozri sa na druhú stranu

                    if (matrix[x+1][y-1] == cislo):                   # kontrola či sa po hore budem nachádzať v matici
                        check = zen_left(jedinec, x+1, y-1,poradie,cislo)               # posúvaj sa hore
                        if (check == False):
                            return False
                        return True

                    else:                                       # je tam kamen ( kamen je aj zhora aj zdola)
                        return False
                elif (y - 1 == -1):
                    return True
            elif (y + 1 == jedinec.matica_y):
                return True

            elif (y - 1 > -1):  # je tam kamen pozri sa na druhú stranu

                if (matrix[x + 1][y - 1] == cislo):  # kontrola či sa po hore budem nachádzať v matici
                    check = zen_left(jedinec, x + 1, y - 1,poradie,cislo)  # posúvaj sa hore
                    if (check == False):
                        return False
                    return True

                else:  # je tam kamen ( kamen je aj zhora aj zdola)

                    return False
            elif (y - 1 == -1):
                return True

        x = x - 1

    return True


def zen_right(jedinec, x,y,poradie,cislo):
    #print_matica(jedinec.matica)
    #print("right " + str(x) + " " + str(y))
    matrix = jedinec.matica


    while (y != jedinec.matica_y):
        if (matrix[x][y] == cislo):
            if (poradie != 0):
                jedinec.up_fitness()
            else:
                jedinec.fitnes = jedinec.fitnes - 1
            matrix[x][y] = poradie
        elif (y == 0):
            return
        else:
            if (x + 1 < jedinec.matica_x):                  # kontrola či sa po pohybe dole budem nachádzať stále v matici

                if (matrix[x + 1][y-1] == cislo):                 # kontrola či je dole od Zen(a) nepoorané políčko
                    check = zen_down(jedinec, x+1, y-1,poradie,cislo)             # posúvaj sa dole
                    if (check == False):
                        return False
                    return True

                elif (x - 1 > -1):                                # je tam kamen pozri sa na druhú stranu

                    if (matrix[x - 1][y-1] == cislo):                 # kontrola či sa po hore budem nachádzať v matici
                        check = zen_up(jedinec, x-1, y-1,poradie,cislo)             # posúvaj sa hore
                        if (check == False):
                            return False
                        return True
                    else:                                       # je tam kamen ( kamen je aj zhora aj zdola)
                        return False

                elif (x-1 == -1):
                    return True

            elif (x+1 == jedinec.matica_x):
                return True

            elif (x - 1 > -1):  # je tam kamen pozri sa na druhú stranu

                if (matrix[x - 1][y - 1] == cislo):  # kontrola či sa po hore budem nachádzať v matici
                    check = zen_up(jedinec, x - 1, y - 1,poradie,cislo)  # posúvaj sa hore
                    if (check == False):
                        return False
                    return True
                else:  # je tam kamen ( kamen je aj zhora aj zdola)
                    return False

            elif (x - 1 == -1):
                return True



        y = y + 1

    return True


def pokus(jedinec):
    global check
    for gen in jedinec.gen:
        #print("gen: " + str(gen) + "\n")
        if (0 <= gen  and gen < jedinec.matica_y):
            check = zen_down(jedinec,0,gen,jedinec.poradie,0)
            if (check == False):
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)
                jedinec.set_bad()
                break

        elif (jedinec.matica_y + jedinec.matica_x > gen and gen >= jedinec.matica_y):
            check = zen_left(jedinec,gen - jedinec.matica_y, jedinec.matica_y-1,jedinec.poradie,0)
            if (check == False):
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)
                jedinec.set_bad()
                break

        elif (jedinec.matica_x + 2*(jedinec.matica_y) > gen and gen >= jedinec.matica_x + jedinec.matica_y):

            x = (jedinec.matica_x) - 1
            y = abs(gen - 2*(jedinec.matica_y) - jedinec.matica_x + 1)

            check = zen_up(jedinec, x ,y,jedinec.poradie,0)
            if (check == False):
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)
                jedinec.set_bad()
                break

        elif (gen >= jedinec.matica_x + 2*(jedinec.matica_y)):

            x = abs(gen - 2*(jedinec.matica_y) - 2*(jedinec.matica_x) + 1)
            y = 0

            check = zen_right(jedinec,x,y,jedinec.poradie,0)
            if (check == False):
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)
                jedinec.set_bad()
                break
        if (check == True):
            jedinec.up_poradie()


    #print("SDADAD")
    #print(jedinec.gen)
    #print(jedinec.matica)
    #print_matica(jedinec.matica)
    #print(jedinec.fitnes)
    #print((jedinec.matica_x * jedinec.matica_y)-6)


def vynuluj_gen(gen,jedinec,poradie):
    if (0 <= gen and gen < jedinec.matica_y):
        check = zen_down(jedinec, 0, gen,0,poradie)
        if (check == False):
            jedinec.set_bad()


    elif (jedinec.matica_y + jedinec.matica_x > gen and gen >= jedinec.matica_y):
        check = zen_left(jedinec, gen - jedinec.matica_y, jedinec.matica_y - 1,0,poradie)
        if (check == False):
            jedinec.set_bad()


    elif (jedinec.matica_x + 2 * (jedinec.matica_y) > gen and gen >= jedinec.matica_x + jedinec.matica_y):
        x = (jedinec.matica_x) - 1
        y = abs(gen - 2 * (jedinec.matica_y) - jedinec.matica_x + 1)
        check = zen_up(jedinec, x, y,0,poradie)
        if (check == False):
            jedinec.set_bad()


    elif (gen >= jedinec.matica_x + 2 * (jedinec.matica_y)):
        x = abs(gen - 2 * (jedinec.matica_y) - 2 * (jedinec.matica_x) + 1)
        y = 0
        check = zen_right(jedinec, x, y,0,poradie)
        if (check == False):
            jedinec.set_bad()







def create_gens(x,y,k):
    max_gens = (x+y)+k
    gen=[]
    choices = list(range((x+y)*2))
    random.shuffle(choices)
    while len(gen) != max_gens:
        chromozon = choices.pop()
        gen.append(chromozon)
    return gen



def create_table(buffer,x_velkost, y_velkost):

    stone_buffer=[]

    for i in range(2,len(buffer)):
        kamen = buffer[i]
        count = 0
        suradnica1, suradnica2 = "", ""
        for znak in kamen:

            if (znak == ' '):
                count+=1
                continue
            if (count == 1):
                suradnica1 = suradnica1 + znak
            if (count == 2):
                suradnica2 = suradnica2 + znak

        suradnice = [suradnica1,suradnica2]
        stone_buffer.append(suradnice)

    matica = []
    for i in range(x_velkost):
        matica.append([0] * y_velkost)

    for kamen in stone_buffer:
        matica[int(kamen[0])][int(kamen[1])] = "K"

    return matica


def print_matica(matica):


    for a in matica:
        for b in a:
            if len(str(b)) == 1:
                print(" " + str(b)+ " ",end="")
            else:
                print(str(b) + " " ,end = "")
        print("\n",end="")




def first_generacia(prazdna_matica,x_velkost,y_velkost,pocet_kamenov):
    list = []
    matica = copy.deepcopy(prazdna_matica)
    for i in range(POCET_JEDINCOV):
        copy_of_matica = copy.deepcopy(matica)
        gen = create_gens(x_velkost, y_velkost, pocet_kamenov)
        jedinec = Jedinec(copy_of_matica)
        jedinec.set_gen(gen)
        jedinec.set_velkost_matice(x_velkost, y_velkost)
        pokus(jedinec)   # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
        jedinec.update_fitness()

        list.append(jedinec)

    for i in range(len(list)):
        if list[i].fitnes == pow(x_velkost * y_velkost - pocet_kamenov,3):
            print("Výsledné riešenie je : ")
            print_matica(list[i].matica)
            print(list[i].gen)
            print("jedinec pochádza z " + str(0) + " generácie")
            return True

    nn = copy.deepcopy(list)
    nn.sort(key=lambda x: x.fitnes, reverse=True)
    sum = 0
    for jedinec in nn:
        sum = sum + jedinec.fitnes
    avg = sum / POCET_JEDINCOV
    print("GENERATION " + str(0) + " MAX fitness : " + str(nn[0].fitnes) + " MIN fitness: " + str(nn[POCET_JEDINCOV-1].fitnes) + "  AVG:  " + str(avg))
    return list


def mutuj(gen):
    zmutovany = copy.deepcopy(gen)
    list = []
    prvy = random.choice(gen)
    druhy = random.choice(gen)
    while druhy == prvy:
        druhy = random.choice(gen)

    prvy_index = gen.index(prvy)
    druhy_index = gen.index(druhy)
    zmutovany[prvy_index] = druhy
    zmutovany[druhy_index] = prvy

    return zmutovany


def krizenie(jedinec1,jedinec2):
    gen1 = jedinec1.gen
    gen2 = jedinec2.gen
    i=0
    for gen in gen1:
        nahoda = random.randint(0, 1)
        if nahoda == 1:
            if (gen2[i] in gen1):
                continue
            else:
                gen1[i] = gen2[i]

        i = i + 1

    return gen1




def weight(list):
    dlzka = len(list)
    sum =0
    for i in range(dlzka):
        sum = sum + list[i].fitnes

    new = []*sum
    for jedinec in list:
        pocet = jedinec.fitnes
        for i in range(pocet):
            new.append(jedinec)


    return new




def new_generation(list,matica, x_velkost, y_velkost, pocet_kamenov):

    weighted_list = weight(list)
    generation_new = []

    for i in range(POCET_JEDINCOV):
        novy_gen = []
        parent1 = random.choice(weighted_list)
        parent2 = random.choice(weighted_list)
        while (parent2 == parent1):
            parent2 = random.choice(weighted_list)
        novy_gen = krizenie(parent1,parent2)
        novy_gen = mutuj(novy_gen)
        copy_of_matica = copy.deepcopy(matica)
        jedinec = Jedinec(copy_of_matica)
        jedinec.set_gen(novy_gen)
        jedinec.set_velkost_matice(x_velkost, y_velkost)
        pokus(jedinec)                              # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
        jedinec.update_fitness()

        generation_new.append(jedinec)

    return generation_new




def start_algo(matica, x_velkost, y_velkost, pocet_kamenov):

    generation_count = 1
    global BEST
    list = first_generacia(matica, x_velkost, y_velkost, pocet_kamenov)
    if (list != True) :
        BEST = list[0]
        while (generation_count != POCET_GENERACII):
            list = new_generation(list,matica, x_velkost, y_velkost, pocet_kamenov)
            for i in range(len(list)):
                list[i].set_generation(generation_count)
                if list[i].fitnes == x_velkost * y_velkost - pocet_kamenov:
                    nn = copy.deepcopy(list)
                    nn.sort(key=lambda x: x.fitnes, reverse=True)
                    sum = 0
                    for jedinec in nn:
                        sum = sum + jedinec.fitnes
                    avg = sum / len(nn)
                    print("GENERATION " + str(generation_count) + " MAX fitness : " + str(nn[0].fitnes) + " MIN fitness: " + str(nn[POCET_JEDINCOV-1].fitnes)+ "  AVG:  " + str(avg))
                    print("Výsledné riešenie je : ")
                    print("")
                    print("FITNES: " + str(list[i].fitnes))
                    print_matica(list[i].matica)
                    print(list[i].gen)
                    print("jedinec pochádza z " + str(generation_count) + " generácie")

                    return True
                elif (list[i].fitnes > BEST.fitnes):
                    BEST = list[i]

            nn = copy.deepcopy(list)
            nn.sort(key=lambda x: x.fitnes, reverse=True)
            sum = 0
            for jedinec in nn:
                sum = sum+jedinec.fitnes
            avg=sum/POCET_JEDINCOV
            print("GENERATION " + str(generation_count) + " MAX fitness : " + str(nn[0].fitnes) + " MIN fitness: " + str(nn[POCET_JEDINCOV-1].fitnes)  + "  AVG:  " + str(avg))
            generation_count = generation_count + 1


        print("\nNajlepšie dosiahnuté riešenie je :")
        print("")
        print("FITNES: " + str(BEST.fitnes))
        print_matica(BEST.matica)
        print(BEST.gen)

        print("jedinec pochádza z " + str(BEST.generation) + " generácie")









    return False



def main():
    buffer = []
    GENERACIA = 1
    vstup = open("vstup.txt", "r")
    for riadok in vstup:
        buffer.append(riadok.strip())
    x_velkost = int(buffer[0])
    y_velkost = int(buffer[1])
    pocet_kamenov = len(buffer)-2

    matica = create_table(buffer,x_velkost,y_velkost)


    start_algo(matica,x_velkost,y_velkost,pocet_kamenov)





















if __name__ == '__main__':
    main()

