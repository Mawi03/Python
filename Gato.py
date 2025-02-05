import Tablero


def main():
    
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    g = Tablero.juego(dsimbolos)
    if g is not None:
        print(f'The winner is: {g}')
    else:
        print('Draw')    
    
    
if __name__ =='__main__':
    main()    