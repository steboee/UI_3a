




class Jedinec():

    def __init__(self,fitnes=0):
        self.fitnes = fitnes







def create_table():
    buffer=[]
    vstup = open("vstup.txt", "r")
    for riadok in vstup:
        buffer.append(riadok.strip())
    x_velkost = int(buffer[0])
    y_velkost = int(buffer[1])

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
        matica.append(["_"] * y_velkost)

    for kamen in stone_buffer:
        matica[int(kamen[0])][int(kamen[1])] = "K"

    return matica




def main():
    matica = create_table()
    for line in matica:
        print('  '.join(map(str, line)))




if __name__ == '__main__':
    main()

