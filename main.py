import copy
import random

POCET_JEDINCOV=10
POCET_GENERACII=500
TOURNAMENT_SIZE=0
MUTATION_RATE=0
global GENERACIA
OPTION=0








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

# pokus o pohrabanie zahrady ( vyskúšanie génu a vypočítanie fitnes)
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






# funkcia ktorá vytvorí náhodný gen pre jedinca
def create_gens(x,y,k):
    max_gens = (x+y)+k
    gen=[]
    choices = list(range((x+y)*2))
    random.shuffle(choices)
    while len(gen) != max_gens:
        chromozon = choices.pop()
        gen.append(chromozon)
    return gen


# funkcia vytvorí maticu s kamenmi
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



def create_mutation_rate_list():
    new = [0]*100
    for i in range(MUTATION_RATE):
        new[i] = 1
    random.shuffle(new)
    return new


# funkcia zmutuje daný gén
def mutuj(gen,jedinec):
    choices = list(range((jedinec.matica_x + jedinec.matica_y) * 2))
    zmutovany = copy.deepcopy(gen)
    mutation_rate = create_mutation_rate_list()
    for i in range(int(len(zmutovany))):
        x = random.choice(mutation_rate)
        if (x == 1):
            mutated = random.choice(choices)
            zmutovany[i] = mutated
    return zmutovany


    """  
    prvy = random.choice(gen)
    druhy = random.choice(gen)
    while druhy == prvy:
        druhy = random.choice(gen)

    prvy_index = gen.index(prvy)
    druhy_index = gen.index(druhy)
    
    while first in zmutovany:
        first = random.choice(choices)
    zmutovany[prvy_index] = first
    second = random.choice(choices)
    while second in zmutovany:
        second = random.choice(choices)

    zmutovany[druhy_index] = second

    return zmutovany
    """

#funkcia skríži 2 jedincov
def krizenie(jedinec1,jedinec2):
    gen1 = jedinec1.gen
    gen2 = jedinec2.gen
    i=0
    newgen = []
    dlzka = len(gen1)
    for i in range(dlzka):
        if (i < int(dlzka/2)):
            newgen.append(gen1[i])
        else:
            newgen.append(gen2[i])


    return newgen



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


def tournament(list):
    turnaj = []
    for i in range(TOURNAMENT_SIZE):
        jedinec = random.choice(list)
        turnaj.append(jedinec)

    best_jedinec = turnaj[0]
    for jedinec in turnaj:
        if jedinec.fitnes > best_jedinec.fitnes:
            best_jedinec = jedinec

    return jedinec


def elitarstvo(list):
   new=copy.deepcopy(list)
   new.sort(key=lambda x: x.fitnes, reverse=True)
   return new


# funkcia vytvára novú generáciu
def new_generation(list,matica, x_velkost, y_velkost,OPTION):

    if OPTION == 1 :
        new_list = weight(list)
    elif OPTION == 0:
        new_list = elitarstvo(list)
    elif OPTION == 2:
        new_list = copy.deepcopy(list)

    generation_new = []

    for i in range(POCET_JEDINCOV):
        novy_gen = []
        if OPTION == 1:             # výber Ruletou (proporciálne)
            parent1 = random.choice(new_list)
            parent2 = random.choice(new_list)
            while (parent2.gen == parent1.gen):
                parent2 = random.choice(new_list)
            copy_of_matica = copy.deepcopy(matica)
            jedinec = Jedinec(copy_of_matica)
            jedinec.set_velkost_matice(x_velkost, y_velkost)
            novy_gen = krizenie(parent1, parent2)
            novy_gen = mutuj(novy_gen,jedinec)

            jedinec.set_gen(novy_gen)

            pokus(jedinec)  # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
            jedinec.update_fitness()
            generation_new.append(jedinec)

        elif OPTION == 0:
            pocet_najlepsich = int(POCET_JEDINCOV/10)   # do novej generácie sa dostane 50% najlepších (bez zmeny)
            if i == pocet_najlepsich:
                copied = copy.deepcopy(list)
                copied.sort(key=lambda x: x.fitnes, reverse=True)
                copied = copied[pocet_najlepsich:]
                new_list = weight(copied)
            if i > pocet_najlepsich:

                parent1 = random.choice(new_list)
                parent2 = random.choice(new_list)
                while (parent2.gen == parent1.gen):
                    parent2 = random.choice(new_list)
                copy_of_matica = copy.deepcopy(matica)
                jedinec = Jedinec(copy_of_matica)
                jedinec.set_velkost_matice(x_velkost, y_velkost)
                novy_gen = krizenie(parent1, parent2)
                novy_gen = mutuj(novy_gen,jedinec)

                jedinec.set_gen(novy_gen)

                pokus(jedinec)  # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
                jedinec.update_fitness()
                generation_new.append(jedinec)

            else:
                generation_new.append(new_list[i])

        elif OPTION ==2:
            parent1 = tournament(new_list)
            parent2 = tournament(new_list)
            while parent2.gen == parent1.gen:
                parent2 = tournament(new_list)
            copy_of_matica = copy.deepcopy(matica)
            jedinec = Jedinec(copy_of_matica)
            jedinec.set_velkost_matice(x_velkost, y_velkost)
            novy_gen = krizenie(parent1, parent2)
            novy_gen = mutuj(novy_gen, jedinec)

            jedinec.set_gen(novy_gen)

            pokus(jedinec)  # vypočíta sa fitness funkcia a priradí sa danému jedincovi ( prebehne hrabanie zahrady)
            jedinec.update_fitness()
            generation_new.append(jedinec)






    return generation_new




# spustenie genetického algoritmu
def start_algo(matica, x_velkost, y_velkost, pocet_kamenov,OPTION):

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
    global POCET_JEDINCOV
    global POCET_GENERACII
    global OPTION
    global TOURNAMENT_SIZE
    global MUTATION_RATE
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
    print("POCET JEDINCOV: ")
    POCET_JEDINCOV = int(input())
    print("MAXIMALNY POČET GENERÁCIÍ: ")
    POCET_GENERACII = int(input())
    print("Pravdepodobnosť mutácie génu: (1 = 1%, 100 = 100%")
    MUTATION_RATE = int(input())
    print("MENU_2")
    print("0 -> Výber jedincov na základe elity (prvých 10%) ostatných 90% sa vytvorí výberom selekciou všetkých jedincov a následným križenim, mutáciou")
    print("1 -> Výber jedincov na základe rulety")
    print("2 -> Výber jedincov na zákade turnaju")
    print("Váš výber: ")
    OPTION = int(input())
    if OPTION == 2:
        print("Veľkosť turnaju: ")
        TOURNAMENT_SIZE = int(input())

    start_algo(matica,x_velkost,y_velkost,pocet_kamenov,OPTION)





















if __name__ == '__main__':
    main()

