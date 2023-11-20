# CS361_microservice

README - CS361 Microservice

COMMUNICATION CONTRACT
1. The standard response time is 24 hours.
2. When there is an assignment due within 2 days, the maximum response time is 8 hours
3. We will communicate on Discord
4. Discuss any issues, be open to other opinions, and ask for help or clarification when a topic
is unclear.
5. If someone is to become behind schedule, they will let their teammate know as soon as
possible. If the circumstances are going to have a long-term impact, the team member
should reach out to the TA and instructor to inform them of the situation and create a plan
that still allows the team to be successful.

How to: REQUEST DATA
To request data, the program should write “request” to the text file. This will trigger the microservice to run and write the result to the output file. An example of how the PRNG service can be used is held in example_call.py and is also shown below:

Example call:
    import time
    
    
    def get_input():
        with open("rng_output.txt", 'w') as file:
            file.write("request")
        file.close()
    
        with open("rng_output.txt", 'r') as file:
            time.sleep(5)
            poke_num = file.readline()
        file.close()
    
    
    get_input()

How to: RECEIVE DATA
To receive data, the output file (rng_output.txt) should be read using this example:

    with open("rng_output.txt", 'r') as file:
        time.sleep(5)
        poke_num = file.readline()
    file.close()
