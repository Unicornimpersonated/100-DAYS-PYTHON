# Putting one list or a dictionary into another

dictionary = {"Key": ["list"],
              "Key2":{"key a":10}
              }
print(dictionary)

capitals={
    "France":"Paris",
    "Germany":"Berlin"
}

travel_log={
    "France":["Paris","Lille","Lyon","Marseille"],
    "Germany":["Stuttgart","Berlin"]
}
# Print Lille
print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
# Printing  D
print(nested_list[2][1])

# More complicated travel log 
travel_log ={
    "France":{
        "cities visited":["Paris","Lille","Lyon","Marseille"],
        "total visits": 10

    },

    "Germany":{
        "cities visited":["Stuttgart","Berlin"],
        "total visits": 13

    }
}
# Print Berlin
print(travel_log["Germany"]["cities visited"][1])