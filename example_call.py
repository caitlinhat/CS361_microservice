import time


def get_input():
    with open("rng_output.txt", 'w') as file:
        file.write("request")
    file.close()

    with open("rng_output.txt", 'r') as file:
        time.sleep(5)
        poke_num = file.readline()
    file.close()

    return poke_num

get_input()
