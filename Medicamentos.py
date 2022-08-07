# utf -8
import shutil

columns = shutil.get_terminal_size().columns
print("Olá, Jesiel Vieira, vamos calcular quantos dias seus medicamentos irão durar!".center(columns))

quantidade1 = float((input("Quantos comprimidos de 500MG você possui? ")))
quantidade2 = float((input("Quantos comprimidos de 100MG você possui? ")))
quantidade3 = float((input("Quantos comprimidos de 25MG você possui? ")))
quantidade4 = float((input("Quantos comprimidos de 10MG você possui? ")))
quantidade5 = float((input("Quantos comprimidos de 2MG você possui? ")))
quantidade6 = float((input("Quantos comprimidos de 1MG você possui? ")))
dosagem = float((input("Quantos MG você toma diariamente? ")))

total_mg = (quantidade1 * 500) + (quantidade2 * 100) + (quantidade3 * 25) + (quantidade4 * 10) + (quantidade5 * 2) + (quantidade6 * 1)

dias = (total_mg / dosagem)
meses = int((dias / 30))

if dias < 30:
    print("Seus medicamentos irão durar %.2f dias!".center(columns) % dias)
elif 60 > dias >= 30:
    dias -= 30
    print("Seus medicamentos irão durar %d mês e %d dias!".center(columns) % (meses, dias))
else:
    dias -= (meses * 30)
    print("Seus medicamentos irão durar %d meses e %d dias!".center(columns) % (meses, dias))
