
import random, time
min = 1000000000
max = 9999999999


roll_again = "again"

while roll_again == "again" or roll_again == "ag":
    print """









Generating phone numbers to prank call...

    """
    time.sleep(1)
    print """The numbers are....

    """
    print random.randint(min, max)
    print random.randint(min, max)
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("If none of these are satisfactory, type 'again' ")
