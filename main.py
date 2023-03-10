import pytholog as pl

def kings():
    kb = pl.KnowledgeBase("Kings")


    #TELL
    kb(
        [
           "king(john)", # John is a King
           "person(richard)", # Richard is a person
           "person(X) :- king(X) ", # If x is a king then X is also a person
           "brother(john,richard)",
           "brother(richard,john)",
           ""

        ]
    )
    #ASK
    # print(kb.query(pl.Expr("king(john)")))
    # print(kb.query(pl.Expr("king(richard)")))
    # print(kb.query(pl.Expr("brother(richard,X)")))


def animals():
    kb = pl.KnowledgeBase("Animals")

    kb(
        [
            "animal(X) :- mammal(X)",
            "mammal(X) :- feline(X)",\
            "mammal(X) :- canine(X)",
            "feline(X) :- cat(X)",
            "feline(X) :- lion(X)",
            "canine(X) :- dog(X)",
            "canine(X) :- wolf(X)",
            "animal(X) :- reptile(X)",
            "reptile(X) :- turtle(X)",
            "cat(phantom)",
            "dog(dexter)",
            "turtle(bob)",
            "wolf(luther)",
            "lion(duke)"

        ]

    )
    print(kb.query(pl.Expr("animal(bob)")))
    print(kb.query(pl.Expr("canine(dexter)")))
    print(kb.query(pl.Expr("animal(X)")))
    print(kb.query(pl.Expr("mammal(X)")))
    

def kinship():
    kb = pl.KnowledgeBase("Kinship")

    kb(
        [
            "mother(M,C) :- female(M), parent(M,C)",
            "parent(P,C) :- child(C,P)",
            "grandparent(G,C) :- parent(G,P) , parent(P,C)",
            "female(julie)",
            "child(elliot,julie)",
            "child(elliot,dean)",
            "child(dean,jeffery)"
        ]
    )

    # print(kb.query(pl.Expr("grandparent(jeffery, elliot)")))
    


def main():
    print("hello.")
    kinship()
    kings()
    animals()

if __name__ == "__main__":
    main()