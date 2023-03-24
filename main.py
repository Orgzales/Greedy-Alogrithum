
import math

##Cities [0 = london | 1 = Berlin | 2 = Paris, France | 3 = Rome, | 4 = Spain | 5 = Austria]
London = [0, 325, 160, 280, 250, 425] ##london to other
Berlin = [325, 0, 415, 550, 675, 375] ##Berlin to other
Paris = [160, 415, 0, 495, 215, 545] ##Paris to other
Rome = [280, 550, 495, 0, 380, 480] ##Rome to other
Spain = [250, 675, 215, 380,  0 , 730] ##Spain to other
Austria = [425, 375, 545, 480, 730, 0] ##Austria to other
All = [London, Berlin, Paris, Rome, Spain, Austria]
STR = ["London ", "Berlin ", "Paris  ", "Rome   ", "Spain  ", "Austria"]

def intro():
    print("\nUsing the greedy Algorithum!"         )
    print(" ~Table~  | London | Berlin | Paris | Rome | Spain | Austria")
    for x in range(len(All)):
        print(STR[x] + ":    " + str(All[x][0]) + "     | " + str(All[x][1]) +  "    | " + str(All[x][2]) +  "    | " + str(All[x][3]) + "    | " + str(All[x][4]) +  "     | " + str(All[x][5]) )
    Greedy()

def Greedy():
    print("\nStarting from london")

    first_index = 0
    goto_index = 0 ##also change index
    from_index = 0;
    value_index = 0;
    pop_index = [];
    total = 0;
    for x in range(len(All)):

        if x == len(All) -1:
            total = total + All[goto_index][first_index]
            pop_index.append(goto_index)
            print("Min price of " + STR[goto_index] + ": $" + str(All[goto_index][first_index]))
            break;


        min_price = 0;
        for m in range(len(All)):
            min_price = min_price + All[0][m]


        for p in range(len(pop_index)):
            All[goto_index][pop_index[p]] = 0

        from_index = goto_index;

        for i in range(len(All)):
            if (All[goto_index][i] < min_price) and (All[goto_index][i] != 0):
                min_price = All[goto_index][i]
                value_index = i;
        pop_index.append(from_index)
        goto_index = value_index
        total = total + All[from_index][value_index]
        print("Min price of " + STR[from_index] + ": $" + str(All[from_index][value_index]))

    print("The total price (Cheapest) of airfare for the trip is: $" + str(total))
    Travel(pop_index, total)




def Travel(list, total):
    #print(list)
    print("\nTravel Trip: ")

    for x in range(len(list)):
        if x < len(list) -1:
            print("Trip " +str(x) + ": " + STR[x] + " -> " + STR[(x + 1)])
        else:
            print("Return Trip: " + STR[x] + " -> " + STR[0])

    print("The total price (Cheapest) of airfare for the trip is: $" + str(total))

intro()