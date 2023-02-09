import time

def get_random_number():
    while True:
        command = input("Do you want to generate a random number using the RNG microservice? (y/n) ")

        if command.lower() == 'y':
            with open('number.txt', 'w') as f:
                f.write('run')

            time.sleep(1)
            with open('number.txt', 'r+') as f:
                random_int = f.readline()
                f.truncate(0)   # this line is just to clean up the text file, could comment out to see value in number.txt

            print("The RNG microservice produced the number " + random_int)

        elif command.lower() == 'n':
            break

        else:
            print('Invalid response, must be y or n')




if __name__ == '__main__':
    get_random_number()