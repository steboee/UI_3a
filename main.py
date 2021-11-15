import copy
import random
import time

POCET_JEDINCOV=0
POCET_GENERACII=0
MUTATION_RATE=0
ELITISM=0
global GENERACIA
OPTION=0




class Jedinec():
    def __init__(self,matica, fitnes=0):
        self.fitnes = fitnes
        self.chromozom = []
        self.matica = matica
        self.poradie = 1
        self.good = True
        self.generation = 0

    def update_fitness(self):
        self.fitnes = self.fitnes

    def up_fitness(self):
        self.fitnes = self.fitnes + 1

    def set_chromozom(self, chromozom):
        self.chromozom = chromozom

    def set_velkost_matice(self,x,y):
        self.matica_x = x
        self.matica_y = y

    def up_poradie(self):
        self.poradie = self.poradie + 1

    def set_bad(self):
        self.good = False

    def set_generation(self,generation):
        self.generation = generation


# pohyb zena dole
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

# pohyb zena dolava
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

# pohyb zena hore
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

# pohyb zena doprava
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

# pokus o pohrabanie zahrady (vyskúšanie génu a vypočítanie fitnes)
def pokus(jedinec):
    global check
    for gen in jedinec.chromozom:
        #print("gen: " + str(gen) + "\n")
        if (0 <= gen  and gen < jedinec.matica_y):              # gen je taký , že pohyb jedinca bude smerom dole
            check = zen_down(jedinec,0,gen,jedinec.poradie,0)
            if (check == False):                                            # ak daný gén nebol úspešný a jedinec sa zasekol
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)                    # treba vynulovať jeho posledný gén ktorým vstúpil na záhradku
                jedinec.set_bad()
                break

        elif (jedinec.matica_y + jedinec.matica_x > gen and gen >= jedinec.matica_y):            # gen je taký , že pohyb jedinca bude smerom dolava
            check = zen_left(jedinec,gen - jedinec.matica_y, jedinec.matica_y-1,jedinec.poradie,0)
            if (check == False):                                                        # ak daný gén nebol úspešný a jedinec sa zasekol
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)                            # treba vynulovať jeho posledný gén ktorým vstúpil na záhradku
                jedinec.set_bad()
                break

        elif (jedinec.matica_x + 2*(jedinec.matica_y) > gen and gen >= jedinec.matica_x + jedinec.matica_y):        # gen je taký , že pohyb jedinca bude smerom hore

            # výpočet kde na záhradke sa má jedinec postaviť
            x = (jedinec.matica_x) - 1
            y = abs(gen - 2*(jedinec.matica_y) - jedinec.matica_x + 1)

            check = zen_up(jedinec, x ,y,jedinec.poradie,0)
            if (check == False):                                            # ak daný gén nebol úspešný a jedinec sa zasekol
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)                    # treba vynulovať jeho posledný gén ktorým vstúpil na záhradku
                jedinec.set_bad()
                break

        elif (gen >= jedinec.matica_x + 2*(jedinec.matica_y)):              # gen je taký , že pohyb jedinca bude smerom doprava

            # výpočet kde na záhradke sa má jedinec postaviť
            x = abs(gen - 2*(jedinec.matica_y) - 2*(jedinec.matica_x) + 1)
            y = 0

            check = zen_right(jedinec,x,y,jedinec.poradie,0)
            if (check == False):                                            # ak daný gén nebol úspešný a jedinec sa zasekol
                #print("Jedinec to nezvladol")
                vynuluj_gen(gen,jedinec,jedinec.poradie)                    # treba vynulovať jeho posledný gén ktorým vstúpil na záhradku
                jedinec.set_bad()
                break
        if (check == True):                                                       # ak daný gén prešiel cez záhradku a jedinec sa nezasekol tak zvýš poradie hrabania
            jedinec.up_poradie()


    #print("SDADAD")
    #print(jedinec.chromozom)
    #print(jedinec.matica)
    #print_matica(jedinec.matica)
    #print(jedinec.fitnes)
    #print((jedinec.matica_x * jedinec.matica_y)-6)

# vynuluj gen ktorý sa zasekol
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



# funkcia ktorá vytvorí náhodný chromozom pre jedinca
def create_gens(x,y,k):
    max_gens = (x+y)+k
    chromozom=[]
    choices = list(range((x+y)*2))
    random.shuffle(choices)
    while len(chromozom) != max_gens:
        gen = choices.pop()
        chromozom.append(gen)
    return chromozom


# funkcia vytvorí maticu s kameňmi
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

# funkcia na vizualizáciu matice
def print_matica(matica):


    for a in matica:
        for b in a:
            if len(str(b)) == 1:
                print(" " + str(b)+ " ",end="")
            else:
                print(str(b) + " " ,end = "")
        print("\n",end="")



# prvá generácia (0-tá) s náhodnými génmi jedincov
def first_generacia(prazdna_matica,x_velkost,y_velkost,pocet_kamenov):
    list = []
    matica = copy.deepcopy(prazdna_matica)
    for i in range(POCET_JEDINCOV):
        copy_of_matica = copy.deepcopy(matica)
        chromozom = create_gens(x_velkost, y_velkost, pocet_kamenov)
        jedinec = Jedinec(copy_of_matica)
        jedinec.set_chromozom(chromozom)
        jedinec.set_velkost_matice(x_velkost, y_velkost)
        pokus(jedinec)   # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
        jedinec.update_fitness()

        list.append(jedinec)

    for i in range(len(list)):
        if list[i].fitnes == x_velkost * y_velkost - pocet_kamenov:
            #print("Výsledné riešenie je : ")
            #print_matica(list[i].matica)
            #print(list[i].chromozom)
            #print("jedinec pochádza z " + str(0) + " generácie")
            return True

    nn = copy.deepcopy(list)
    nn.sort(key=lambda x: x.fitnes, reverse=True)
    sum = 0
    for jedinec in nn:
        sum = sum + jedinec.fitnes
    avg = sum / POCET_JEDINCOV
    #print("GENERATION " + str(0) + " MAX fitness : " + str(nn[0].fitnes) + " MIN fitness: " + str(nn[POCET_JEDINCOV-1].fitnes) + "  AVG:  " + str(avg))
    return list



def create_mutation_rate_list():
    new = [0]*100
    for i in range(MUTATION_RATE):
        new[i] = 1
    random.shuffle(new)
    return new


# funkcia zmutuje gen v chromozome
def mutuj(chromozom,jedinec):
    choices = list(range((jedinec.matica_x + jedinec.matica_y) * 2))
    zmutovany = copy.deepcopy(chromozom)
    mutation_rate = create_mutation_rate_list()
    for i in range(int(len(zmutovany))):
        x = random.choice(mutation_rate)
        if (x == 1):
            mutated = random.choice(choices)
            zmutovany[i] = mutated
    return zmutovany


#funkcia skríži 2 jedincov
def krizenie(jedinec1,jedinec2):
    chromozom1 = jedinec1.chromozom
    chromozom2 = jedinec2.chromozom
    i=0
    newchromzom = []
    dlzka = len(chromozom1)
    randomizer = (1,0)
    for i in range(dlzka):
        x = random.choice(randomizer)
        if x==1:
            newchromzom.append(chromozom1[i])
        elif x==0:
            newchromzom.append(chromozom2[i])

    return newchromzom



# funkcia vráti list jedincov pričom jedinci s najväčším fitnes budú mať najväčšie zastúpenie
# a jedinci s najmenšími hodnotami fitnes budú mať najmenšie zastúpenie
# jedinec sa bude vyskytovať vo výsledon liste toľko-krát aká je jeho fitnes funkcia
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


def elitarstvo(list):
   new=copy.deepcopy(list)
   new.sort(key=lambda x: x.fitnes, reverse=True)
   return new


def tournament(list):
    turnaj = []
    for i in range(TOURNAMENT_SIZE):
        jedinec = random.choice(list)
        while jedinec in turnaj:
            jedinec = random.choice(list)
        turnaj.append(jedinec)

    best_jedinec = turnaj[0]
    for jedinec in turnaj:
        if jedinec.fitnes > best_jedinec.fitnes:
            best_jedinec = jedinec

    return jedinec


# funkcia vytvára novú generáciu
def new_generation(list,matica, x_velkost, y_velkost,OPTION):

    if OPTION == 1 :
        new_list = weight(list)
    elif OPTION == 0:
        new_list = elitarstvo(list)
    elif OPTION == 2:
        new_list = copy.deepcopy(list)

    generation_new = []
    all_chromozoms = []

    for i in range(POCET_JEDINCOV):
        novy_chromozom = []
        if (OPTION == 1):             # výber Ruletou (proporciálne)
            parent1 = random.choice(new_list)
            parent2 = random.choice(new_list)
            while (parent2.chromozom == parent1.chromozom):
                parent2 = random.choice(new_list)
            copy_of_matica = copy.deepcopy(matica)
            jedinec = Jedinec(copy_of_matica)
            jedinec.set_velkost_matice(x_velkost, y_velkost)
            novy_chromozom = krizenie(parent1, parent2)
            while novy_chromozom in all_chromozoms:
                novy_chromozom = mutuj(novy_chromozom, jedinec)


            jedinec.set_chromozom(novy_chromozom)

            pokus(jedinec)  # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
            jedinec.update_fitness()
            one_chromozom = copy.deepcopy(novy_chromozom)
            all_chromozoms.append(one_chromozom)
            generation_new.append(jedinec)

        elif (OPTION == 0):
            pocet_najlepsich = POCET_JEDINCOV/10 * ELITISM   # do novej generácie sa dostane x% najlepších (bez zmeny)
            if i == pocet_najlepsich:
                new_list = weight(list)
            if i >= pocet_najlepsich:
                parent1 = random.choice(new_list)
                parent2 = random.choice(new_list)
                while (parent2.chromozom == parent1.chromozom):
                    parent2 = random.choice(new_list)
                copy_of_matica = copy.deepcopy(matica)
                jedinec = Jedinec(copy_of_matica)
                jedinec.set_velkost_matice(x_velkost, y_velkost)
                novy_chromozom = krizenie(parent1, parent2)
                while novy_chromozom in all_chromozoms:
                    novy_chromozom = mutuj(novy_chromozom, jedinec)

                jedinec.set_chromozom(novy_chromozom)
                pokus(jedinec)  # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
                jedinec.update_fitness()
                one_chromozom = copy.deepcopy(novy_chromozom)
                all_chromozoms.append(one_chromozom)
                generation_new.append(jedinec)

            else:
                one_chromozom = copy.deepcopy(new_list[i].chromozom)
                generation_new.append(new_list[i])
                all_chromozoms.append(one_chromozom)

        elif (OPTION == 2):
            parent1 = tournament(new_list)
            parent2 = tournament(new_list)
            while (parent1.chromozom == parent2.chromozom):
                parent2 = tournament(new_list)

            copy_of_matica = copy.deepcopy(matica)
            jedinec = Jedinec(copy_of_matica)
            jedinec.set_velkost_matice(x_velkost, y_velkost)
            novy_chromozom = krizenie(parent1, parent2)
            novy_gen = mutuj(novy_chromozom, jedinec)

            jedinec.set_chromozom(novy_gen)

            pokus(jedinec)  # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
            jedinec.update_fitness()
            generation_new.append(jedinec)

    return generation_new


# spustenie genetického algoritmu
def start_algo(matica, x_velkost, y_velkost, pocet_kamenov,OPTION,moznost):

    generation_count = 1
    global BEST
    list = first_generacia(matica, x_velkost, y_velkost, pocet_kamenov)
    if (list != True) :
        BEST = list[0]
        while (generation_count != POCET_GENERACII):
            list = new_generation(list,matica, x_velkost, y_velkost,OPTION)
            for i in range(len(list)):
                list[i].set_generation(generation_count)
                if list[i].fitnes == x_velkost * y_velkost - pocet_kamenov:
                    if (moznost == 1):
                        nn = copy.deepcopy(list)
                        nn.sort(key=lambda x: x.fitnes, reverse=True)
                        sum = 0
                        for jedinec in nn:
                            sum = sum + jedinec.fitnes
                        avg = sum / POCET_JEDINCOV
                        print("GENERATION " + str(generation_count) + " MAX fitness : " + str(nn[0].fitnes) + " MIN fitness: " + str(nn[POCET_JEDINCOV-1].fitnes)+ "  AVG:  " + str(avg))
                        print("Výsledné riešenie je : ")
                        print("")
                        print("FITNES: " + str(list[i].fitnes))
                        print_matica(list[i].matica)
                        print("\nChromozóm jedinca: ")
                        print(list[i].chromozom)
                        print("jedinec pochádza z " + str(generation_count) + " generácie")

                    return generation_count
                elif (list[i].fitnes > BEST.fitnes):
                    BEST = list[i]
            if(moznost ==1):
                nn = copy.deepcopy(list)
                nn.sort(key=lambda x: x.fitnes, reverse=True)
                sum = 0
                for jedinec in nn:
                    sum = sum+jedinec.fitnes
                avg=sum/POCET_JEDINCOV
                print("GENERATION " + str(generation_count) + " MAX fitness : " + str(nn[0].fitnes) + " MIN fitness: " + str(nn[POCET_JEDINCOV-1].fitnes)  + "  AVG:  " + str(avg))

            generation_count = generation_count + 1

        if (moznost == 1):
            print("\nNajlepšie dosiahnuté riešenie je :")
            print("")
            print("FITNES: " + str(BEST.fitnes))
            print_matica(BEST.matica)
            print(BEST.chromozom)

            print("jedinec pochádza z " + str(BEST.generation) + " generácie")

    return 0


def tester(opakovanie,OPTION,matica,x_velkost,y_velkost,pocet_kamenov):
    total_time = 0
    total_count = 0
    x = copy.deepcopy(opakovanie)
    for i in range(opakovanie):
        t = time.process_time()
        count = start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION,0)
        if count == 0:
            x = x - 1

        else:
            total_count = total_count + count
            elapsed_time = time.process_time() - t
            total_time = total_time + elapsed_time

    if OPTION == 0:
        print("Výber na základe elity")
    else:
        print("Výber na základe rulety")

    print("POCET JEDINCOV= " + str(POCET_JEDINCOV) +"\nPOCET GENERACII= " + str(POCET_GENERACII) + "\nMUTATION_RATE=" + str(MUTATION_RATE) + "%")
    if OPTION == 0:
        print("ELITISM= " + str(ELITISM) + "0%")

    total_time = total_time / x
    total_count = total_count / x
    print("TOTAL AVG TIME : " + str(total_time))
    print("TOTAL AVG generation : " + str(total_count))
    uspesnost = x/opakovanie*100
    print("Úspešnosť nájdeného riešenia = " + str(uspesnost) + "%")
    print("")


def main():
    global POCET_JEDINCOV
    global POCET_GENERACII
    global OPTION
    global TOURNAMENT_SIZE
    global MUTATION_RATE
    global ELITISM
    global moznost
    buffer = []
    GENERACIA = 1
    vstup = open("vstup.txt", "r")
    for riadok in vstup:
        buffer.append(riadok.strip())
    x_velkost = int(buffer[0])
    y_velkost = int(buffer[1])
    pocet_kamenov = len(buffer)-2

    matica = create_table(buffer,x_velkost,y_velkost)


    print("###########################################################")
    print("Problém - Zenova záhrada")
    print("Algoritmus: Genetický algoritmus")
    print("Veľkosť záhrady načítanej zo súboru vstup.txt:")
    print("počet riadkov = 10")
    print("počet stĺpcov = 12")
    print("MENU_1: ")
    print("0 -> Tester")
    print("1 -> Program")
    print("Vaša voľba: ")
    moznost = int(input())


    print("POČET JEDINCOV V 1 GENERÁCIÍ: ")
    POCET_JEDINCOV = int(input())
    print("MAXIMALNY POČET GENERÁCIÍ: ")
    POCET_GENERACII = int(input())
    print("Pravdepodobnosť mutácie génu: (1 = 1%, 100 = 100%)")
    MUTATION_RATE = int(input())

    print("MENU_2")
    print("0 -> Výber jedincov na základe elitárstva (+ruleta)")
    print("1 -> Výber jedincov na základe rulety")
    print("2 -> Výber jedincov na základe turnaja")
    print("Váš výber: ")
    OPTION = int(input())
    if OPTION ==0:
        print("ELITISM mnoŽstvo vyvolených : (1 = 10%    10 = 100%)")
        ELITISM = int(input())

    if OPTION == 2:
        print("TOURNAMENT SIZE : ")
        TOURNAMENT_SIZE = int(input())
    if (moznost == 0):
        print("Koľkokrát sa má vykonať test pre zadané hodnoty ? ")
        opakovanie = int(input())
        tester(opakovanie,OPTION,matica,x_velkost,y_velkost,pocet_kamenov)

    elif (moznost == 1):
        start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION,1)



    """
    for k in range(5):
        if k == 0 :
            MUTATION_RATE = 1
        elif k == 1:
            MUTATION_RATE = 3
        elif k==2:
            MUTATION_RATE = 5
        elif k==3:
            MUTATION_RATE = 10
        elif k ==4:
            MUTATION_RATE = 20
        POCET_JEDINCOV = 10
        POCET_GENERACII = 500
        ELITISM=1
        OPTION = 0
        total_time = 0
        total_count = 0
        x=100
        for i in range(100):
            t = time.process_time()
            count = start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION)
            if count == 0:
                x=x-1

            else:
                total_count = total_count + count
                elapsed_time = time.process_time() - t
                total_time = total_time + elapsed_time


            #print("TIME: " + str(elapsed_time))

        print("POCET JEDINCOV=100\nPOCET GENERACII=100\nMUTATION_RATE="+str(MUTATION_RATE)+"\nELITISM=1")
        total_time = total_time / x
        total_count = total_count / x
        print("OPTION-0")
        print("TOTAL AVG TIME : " + str(total_time))
        print("TOTAL AVG generation : " + str(total_count))
        print(x)
        print("")

    for k in range(5):
        if k == 0:
            MUTATION_RATE = 1
        elif k == 1:
            MUTATION_RATE = 3
        elif k == 2:
            MUTATION_RATE = 5
        elif k == 3:
            MUTATION_RATE = 10
        elif k == 4:
            MUTATION_RATE = 20
        POCET_JEDINCOV = 10
        POCET_GENERACII = 500
        ELITISM = 3
        OPTION = 0
        total_time = 0
        total_count = 0
        x=100
        for i in range(100):
            t = time.process_time()
            count = start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION)
            if count == 0:
                x = x - 1

            else:
                total_count = total_count + count
                elapsed_time = time.process_time() - t
                total_time = total_time + elapsed_time


        print("POCET JEDINCOV=100\nPOCET GENERACII=100\nMUTATION_RATE="+str(MUTATION_RATE)+"\nELITISM=3")
        total_time = total_time / x
        total_count = total_count / x
        print("OPTION-0")
        print("TOTAL AVG TIME : " + str(total_time))
        print("TOTAL AVG generation : " + str(total_count))
        print(x)
        print("")

    for k in range(5):
        if k == 0:
            MUTATION_RATE = 1
        elif k == 1:
            MUTATION_RATE = 3
        elif k == 2:
            MUTATION_RATE = 5
        elif k == 3:
            MUTATION_RATE = 10
        elif k == 4:
            MUTATION_RATE = 20
        POCET_JEDINCOV = 10
        POCET_GENERACII = 500
        ELITISM = 5
        OPTION = 0
        total_time = 0
        total_count = 0
        x=100
        for i in range(100):
            t = time.process_time()
            count = start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION)
            if count == 0:
                x=x-1

            else:
                total_count = total_count + count
                elapsed_time = time.process_time() - t
                total_time = total_time + elapsed_time

            # print("TIME: " + str(elapsed_time))

        print("POCET JEDINCOV=100\nPOCET GENERACII=100\nMUTATION_RATE="+str(MUTATION_RATE)+"\nELITISM=5")
        total_time = total_time / x
        total_count = total_count / x
        print("OPTION-0")
        print("TOTAL AVG TIME : " + str(total_time))
        print("TOTAL AVG generation : " + str(total_count))
        print(x)
        print("")

    for k in range(5):
        if k == 0:
            MUTATION_RATE = 1
        elif k == 1:
            MUTATION_RATE = 3
        elif k == 2:
            MUTATION_RATE = 5
        elif k == 3:
            MUTATION_RATE = 10
        elif k == 4:
            MUTATION_RATE = 20
        POCET_JEDINCOV = 10
        POCET_GENERACII = 500
        OPTION = 1
        total_time = 0
        total_count = 0
        x=100
        for i in range(100):
            t = time.process_time()
            count = start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION)
            if count == 0:
                x=x-1

            else:
                total_count = total_count + count
                elapsed_time = time.process_time() - t
                total_time = total_time + elapsed_time

            # print("TIME: " + str(elapsed_time))

        print("POCET JEDINCOV=100\nPOCET GENERACII=100\nMUTATION_RATE="+str(MUTATION_RATE))
        total_time = total_time / x
        total_count = total_count / x
        print("OPTION-1")
        print("TOTAL AVG TIME : " + str(total_time))
        print("TOTAL AVG generation : " + str(total_count))
        print(x)
    """














    """
    OPTION = 2
    TOURNAMENT_SIZE = 3
    total_time = 0
    total_count = 0
    for i in range(50):
        t = time.process_time()
        count = start_algo(matica, x_velkost, y_velkost, pocet_kamenov, OPTION)
        total_count = total_count + count
        elapsed_time = time.process_time() - t
        total_time = total_time + elapsed_time
        print("TIME: " + str(elapsed_time))

    total_time = total_time / 50
    total_count = total_count / 50
    print("OPTION-2")
    print("TOTAL AVG TIME : " + str(total_time))
    print("TOTAL AVG generation : " + str(total_count))
   """
























if __name__ == '__main__':
    main()

