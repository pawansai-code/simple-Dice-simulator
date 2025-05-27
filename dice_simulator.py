import random
#to generate random numbers
def roll_dice(amount: int = 2)->list[int]:
    if amount <=0:
        raise ValueError
    rolls: list[int] = []
    for i in range(amount):
        random_roll:int=random.randint(1, 6)
        rolls.append(random_roll)
        return rolls
def main():
    while True:
        try:
            user_input: str = input("how many dice would u like to roll?")
            if user_input.lower() =='exit':
                print("thanks for playing")
                break
            print(*roll_dice(int(user_input)), sep=", ")
        except ValueError:
            print("please enter the valid number")

if __name__=='__main__':
    main()
