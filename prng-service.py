import random
import time


def prng_service():
    """
    Opens a .txt file and checks if it contains "run".
    If so, generate a random integer from 1 to 1000.
    Function then overwrites the file with the generated integer.
    """
    time.sleep(1)
    # open prng service
    with open('rng_output.txt', 'r') as file:
        total_entries = 151
        # if file says "run", run the generator then erase run
        if "request" in file:
            with open('rng_output.txt', 'w') as open_file:
                num = str(random.randint(1, 1000) % total_entries)
                open_file.write(num)

    # close prng service
    file.close()


while True:
    prng_service()
