import random

def randum_number_generator():
    print("RNG microservice is listening...")
    while True:
        with open('number.txt', 'r') as f:
            command = f.readline()

        if command == "run":
            num = random.randint(1, 10)
            with open('number.txt', 'w') as f:
                f.write(str(num))
            print('Wrote the number ' + str(num) + ' to number.txt')





if __name__ == '__main__':
    randum_number_generator()