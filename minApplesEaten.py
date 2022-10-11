from random import randint


# Generate a list of random apples for each bag
def generateScenario(totalBags, maxRange):

    bags =  totalBags

    applesPerBag = []
    
    for bag in range(bags):

        applesPerBag.append(randint(1,maxRange))
        

    return {"bags": bags, "applesPerBag": applesPerBag}

# Display scenario info
def displayScenarioInfo(scenario):
    print("Scenario Info:")
    print("-"*60)
    print("Scenario Bags = ", scenario["bags"])
    print("Scenario Apples Per Bag List = ", scenario["applesPerBag"])
    for bag in range(scenario["bags"]):
        print(f"Apples in Bag #{bag+1}: {scenario['applesPerBag'][bag]}")
    print("-"*60)

# Find min apples to be eaten
# O(n), depends on length of the list
# Because list length is fixed at 5 therefore, it is O(5)
def findMinApplesToEat(appleBags):
    
    totalApples = appleBags[0]
    for i in range(1,len(appleBags)):
        totalApples += appleBags[i]

    return totalApples % len(appleBags)

# Find min apples to be eaten using built-in sum()
# O(n), depends on length of the list
# Because list length is fixed at 5 therefore, it is O(5)
def altFindMinApplesToEat(appleBags):
    
    return sum(appleBags) % len(appleBags)


# Considering that an efficient algo earlier is O(n) or O(5) if fixed to 5
# A brute force or inefficient algo would be anything higher than O(n)
# Such as O(n^2), quadratic time complexity
# But I haven’t found any idea that makes sense for O(n^2) implementation
# So I settled for O(2n) which is ultimately O(n)

def bruteFindMinApplesToEat(appleBags):

    totalApples = appleBags[0]
    minApples = 0
    
    for item in appleBags[1:]:
        totalApples += item

    temp = totalApples
    for i in range(totalApples):
        temp -= len(appleBags)
        if(temp < len(appleBags) ):
            minApples = temp
            break
            
      
    return minApples
    
# Initialize Scenario 
scenario = generateScenario(7,50)

# Display Scenario Info
displayScenarioInfo(scenario)


# find min apples and print result
toBeEaten = bruteFindMinApplesToEat(scenario["applesPerBag"])

print(f"Apples to be eaten: {toBeEaten}")









