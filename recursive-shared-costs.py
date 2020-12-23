
# An algorithm using recursive function to help people split costs evenly. 
# Takes into account initial spend of each person.
# Instructions are just printed.

### ENTER AN ARRAY WITH HOW MUCH EACH PERSON HAS SPENT ###
spends = [15, 10, 16, 21]

# Print initial spends
print(f'spends: {spends}')

# Calculate average cost -- amount that each person should contribute
cost_per_person = sum(spends)/len(spends)
print(f'cost_per_person: {cost_per_person}')

# Calculate whether each person is in credit or debt
credits = [spend - cost_per_person for spend in spends]
print(f'credits: {credits}')

def pay_fair_share(person_num, costs): #take input of person number and current credit/debt of people
    
    # amount by which the current person is below the target cost (cost_per_person)
    owes = -costs[person_num]

    # If in credit/nothing owed, then move on
    if owes<=0:
        pass
    
    else:

        # Create variables for tracking who is currently owed the most
        max_cost = 0
        index_max_cost = 0

        for i, cost in enumerate(costs): # iterate through credits/debts 

            # Don't pay youself anything
            if i==person_num:
                pass
            
            # If cost > current max cost
            elif cost>max_cost:
                max_cost = cost # new max cost
                index_max_cost = i # update position (person)

        
        # If the person paying can pay all their debt to the max_cost_person
        if max_cost >= owes:
            # print('Case A')
            print(f'Person {person_num+1} pays person {index_max_cost+1} £{owes}.') #pay all debt to max person
            costs[person_num] += owes #erase debt (add amount paid in credit to bring back to 0)
            costs[index_max_cost] -= owes #subtract amount received from recipient's credit

        # If the person paying cannot pay all their debt to one person in one go
        elif max_cost < owes:
            # print('Case B')
            print(f'Person {person_num+1} pays person {index_max_cost+1} £{max_cost}.') #reimburse max person
            costs[person_num] += max_cost #erase some of debt (add amount paid to -ve debt to bring closer to 0)
            costs[index_max_cost] -= max_cost #erase credit (subtract amount received from recipeint's credit)

            # Call the function again, to try the same process with the same person paying debt, but updated costs (credit and debt) array
            costs = pay_fair_share(person_num, costs)

    return costs        

# Use the function
for i, _ in enumerate(credits): #iterate through each person
    credits = pay_fair_share(i, credits)