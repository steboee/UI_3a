import copy
import random

POCET_JEDINCOV=10
GENERACIA=10

class Jedinec():

    def __init__(self,matica, fitnes=0):
        self.fitnes = fitnes
        self.gen = []
        self.matica = matica
        self.poradie = 1
        self.good = True

    def update_fitness(self,new_fitness):
        self.fitnes = new_fitness

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
                    check = zen_right(jedinec,x-1, y+1,poradie,0)                  # posúvaj sa doprava
                    if (check == False):
                        return False
                    return True

                elif (y - 1 > -1):                                  # je tam kamen pozri sa na druhú stranu

                    if (matrix[x - 1][y - 1] == cislo):                 # kontrola či sa po pohybe vlavo budem nachádzať v matici
                        check = zen_left(jedinec, x - 1, y - 1,poradie,0)     # posúvaj sa dolava
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
                    check = zen_left(jedinec, x-1, y-1,poradie,0)                      #posúvaj sa dolava
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
                    check = zen_down(jedinec,x+1,y+1,poradie,0)                        # posúvaj sa dole
                    if (check == False):
                        return False
                    return True

                elif (x - 1 > -1):                               # je tam kamen pozri sa na druhú stranu

                    if (matrix[x - 1][y + 1] == cislo):                 # kontrola či sa po hore budem nachádzať v matici
                        check = zen_up(jedinec,x-1,y+1,poradie,0)                      # posúvaj sa hore
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
                    check = zen_up(jedinec, x - 1, y + 1,poradie,0)    # posúvaj sa hore
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
                    check = zen_right(jedinec,x+1, y+1,poradie,0)               # posúvaj sa vpravo
                    if (check == False):
                        return False
                    return True

                elif (y - 1 > -1):                                 # je tam kamen pozri sa na druhú stranu

                    if (matrix[x+1][y-1] == cislo):                   # kontrola či sa po hore budem nachádzať v matici
                        check = zen_left(jedinec, x+1, y-1,poradie,0)               # posúvaj sa hore
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
                    check = zen_left(jedinec, x + 1, y - 1,poradie,0)  # posúvaj sa hore
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
                    check = zen_down(jedinec, x+1, y-1,poradie,0)             # posúvaj sa dole
                    if (check == False):
                        return False
                    return True

                elif (x - 1 > -1):                                # je tam kamen pozri sa na druhú stranu

                    if (matrix[x - 1][y-1] == cislo):                 # kontrola či sa po hore budem nachádzať v matici
                        check = zen_up(jedinec, x-1, y-1,poradie,0)             # posúvaj sa hore
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
                    check = zen_up(jedinec, x - 1, y - 1,poradie,0)  # posúvaj sa hore
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



def main():
    buffer = []

    vstup = open("vstup.txt", "r")
    for riadok in vstup:
        buffer.append(riadok.strip())
    x_velkost = int(buffer[0])
    y_velkost = int(buffer[1])
    pocet_kamenov = len(buffer)-2

    matica = create_table(buffer,x_velkost,y_velkost)


    list = []

    for i in range(50):
        copy_of_matica = copy.deepcopy(matica)
        gen = create_gens(x_velkost, y_velkost, pocet_kamenov)
        jedinec = Jedinec(copy_of_matica)
        jedinec.set_gen(gen)
        jedinec.set_velkost_matice(x_velkost, y_velkost)
        pokus(jedinec)
        list.append(jedinec)

    maximum = list[0].fitnes
    bigone = list[0]
    for i in range(len(list)):
        if list[i].fitnes > maximum:
            bigone = list[i]
            maximum = list[i].fitnes
        if list[i].fitnes == x_velkost*y_velkost - pocet_kamenov:
            print("Výsledné riešenie je : ")
            print_matica(list[i].matica)
            print(list[i].gen)

            break

    list.sort(key=lambda x:x.fitnes,reverse=True)

    print(maximum)
    print_matica(bigone.matica)
    print(bigone.gen)
    print(bigone.good)



















if __name__ == '__main__':
    main()

