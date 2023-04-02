"""
Let's create the classic guessing game I Spy. We'll need...
- A list of things to guess
  - Each thing should be a dictionary with name and hints attributes
  - name is a string
  - hints is a list of strings
"""

things = [
    {
        "name" : "car",
        "hints" : [
            "it starts with C",
            "it has 4 wheels",
            "it is a vichle"
        ]
    },
    {
        "name" : "table",
        "hints" : [
            "it starts with T",
            "it has 4 legs",
            "you can eat using it"
        ]
    }
]

def i_spy(q_num):
    thing = things[q_num-1]
    answer = thing["name"]
    hints = thing["hints"]
    guess = input("I spy with my little eye ...")

    while len(hints):
        if guess==answer:
            break
        else:
            hint = hints.pop(0)
            print("No, but here is a hint: "+hint)
            guess = input("I spy with my little eye ...")

    if guess==answer:
        print("Bravoo...")
    else:
        print("Game Over !")

            
    

if __name__=="__main__":
    num_of_questions = len(things)
    count=0

    response = input("Do you want to play? (y,n)")

    while response != 'n':
        count +=1
        i_spy(count)

        if count > len(things)-1:
            break



