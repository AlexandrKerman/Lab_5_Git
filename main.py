# Вычисление варианта (мне лень самому считать)

def variant ():
    Student = {
        "Group": 13,
        "Num": 7
    }
    N = ((Student["Group"]-1)*10+Student["Num"])%187
    print (N)

def main ():
    pass

if __name__ == "__main__":
    variant()
    main ()