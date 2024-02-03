import random
import time

def multiplicar():
    num1 = random.randint(10, 1000)
    num2 = random.randint(2, 10)
    # print(num1)
    # print(num2)

    print("\033[91m========= DESAFIO =========\033[0m")
    num_usuario = int(input(f"Quanto é {num1} x {num2}? \nR: "))

    time.sleep(1)
    print("\033[95mVerificando resultado...\033[0m")
    time.sleep(1.5)
    res_mult = int(num1 * num2)
    # print(res_mult)

    while num_usuario != res_mult:
        print("Hmmm, não está correto. Tente novamente.")
        num_usuario = int(input("R: "))
        time.sleep(1)
        print("\033[95mVerificando resultado...\033[0m")
        time.sleep(1.5)

    print("\033[92mACERTOU!!!\033[0m")

while True:
    multiplicar()
    again = input("Deseja fazer outra conta? (S/N)? ").upper()

    if not(again == "S"):
        time.sleep(2)
        print("\033[93mPROGRAMA ENCERRADO\033[0m")
        break
