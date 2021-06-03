import string
import function
import SudokuSolver
import sympy as sp

if __name__ == '__main__' :

    print("----------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------Made by Phien-------------------------------------------------")
    print("Options: \n\n Encode Ceasar Code (1) \n\n Decode Ceasar Code (2) \n\n Encode VigenegeCode (3) \n\n SudokuSolver (4) \n\n DaoHam (5) \n\n Quit (9) \n\n")
    open = True
    while open :
        Option = int(input("Option: "))
        if Option == 9: 
            open = False
        if Option == 1:
            text = input("Text you want to encode: ")
            shift = int(input("Step to fall back: "))
            print("Encoded CeasarCode:", function.EncodeCeasarCode(text,shift,[string.ascii_uppercase, string.ascii_lowercase, string.punctuation]))
        if Option == 2:
            text = input("Code you want to decode: ")
            print("Decoded CeasarCode:", function.DecodeCeasarCode(text,[string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
        if Option == 3:
            code = input("Code you want to decode: ")
            key = input("Key: ")
            if len(code) != len(key):
                print("Error!! Key has to equal to code !!")
            else:
                print("Decoded Vigenege Code:", function.DecodeVigenege(code, key))
        if Option == 4:
            columns = 9
            rows = 9
            table = []
            for i in range (0,rows):
                    table.append([])
                    for j in range (0, columns):
                        table[i].append(int(input()))
            print("Board: ")
            SudokuSolver.print_board(table)
            SudokuSolver.solve(table)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("Solved Board: ")
            SudokuSolver.print_board(table)
        if Option == 5:
            bienso = int(input("số biến: "))
            if bienso == 1:
                x = sp.Symbol('x')
                n = input("nhap dao ham: ")
                print(function.daoham(n,bienso))
            if bienso == 2:
                x, y = sp.symbols('x y')
                n = input("nhap dao ham: ")
                print(function.daoham(n,bienso))
                
