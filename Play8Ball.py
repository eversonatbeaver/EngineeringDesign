# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print "Not a chance"

    elif answers == 2:
        print "Are you kidding me?"

    elif answers == 3:
        print "Never in a million years"

    elif answers == 4:
        print "Reconsider your question"

    elif answers == 5:
        print "wow....just...wow"

    elif answers == 6:
        print "Think before you speak"

    elif answers == 7:
        print "nope"

    elif answers == 8:
        print "Not gonna happen"
