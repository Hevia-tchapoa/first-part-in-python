def collatz(num:int)->None:
    if num == 1:
        print(num)
        return
    
    if num % 2 == 0:
        num // 2
        return collatz(num)
    



def main()->None:
    collatz(15)

if __name__== "__main__":
    main()
