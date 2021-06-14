import  random
dicenumbers = [1,2,3,4,5,6,]

def rolldice():
    random.shuffle(dicenumbers)
    print(dicenumbers[0])


while True:
    a = input()
    if a == "rolldice":
        rolldice()
