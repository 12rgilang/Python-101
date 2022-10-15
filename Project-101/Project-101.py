import random

# Project--101 
# randomize 
# while
# inputprint formating 
# comparison operators
# break and continue

#Using While first because we want it constanly running until its find True input
while True:
    welcome = "Halo selamat datang di Python Project-101, kita akan bermain batu gunting kertas"
    print(welcome)
    my_answer  = input("Choose wisely(ketik pilihan mu)")
    keluar = "Kalo mau keluar ketik (quit) ya"
    my_answer = my_answer.lower()
    keluar = keluar.lower()

    if my_answer == "quit":
        break

    #!=(is not)
    if my_answer != "batu" and my_answer != "kertas" and my_answer != "gunting":
        print("Pilih salah satu ya ! Batu, Kertas, or Gunting")
        continue

    computer_answer = random.choice(["batu", "kertas", "gunting"])
    print(f"Komputer milih: {computer_answer}")

    if my_answer == computer_answer:
        print("Kamu seri")
        continue
    elif my_answer == "kertas" and computer_answer == "batu":
        print("Anda Menang!!")
        break
    elif my_answer == "batu" and computer_answer == "gunting":
        print("Anda Menang!!")
        break
    elif my_answer == "gunting" and computer_answer == "kertas":
        print("Anda Menang!!")
        break
    else:
        print("Kasian deh kalah, coba lagi!")
        print(keluar)
