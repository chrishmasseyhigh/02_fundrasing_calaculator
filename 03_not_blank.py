#makes sure input is not blank
def not_blank(question,error):
    while True:
        response = input(question).strip()

        if response == "":
            print()
            print("{}. Please try again".format(error))
            print()

        else:
            return response


hi= not_blank("what? ", "answer is blank")