# Dictionary

A dictionary, sometimes called map, hash map, or hash set, is a data structure that maps keys to values. The "key" is used
as an index into the dictionary. Values are retrieved using their key. Each key must be unique. Unlike a list, the dictionary
does not have an explicit order.

For example we might be interested in mapping student IDs to a student's name:

        myDictionary = {
            "u0921789" : "Jane",
            "u9234781" : "Michael",
            "u3427891" : "Alice"
        }

I have defined a dictionary with 3 students in it. If I want to find a student's name I can lookup their ID in the dictionary.

        print(myDictionary["u0921789"])

        output: "Jane"

## Create a dictionary

A dictionary is defined with each item between curly braces.

        dictionary = {}

Each item in a dictioanry is a key value pair

        "key" : "value"

We can intialize a dictionary with something in it:

        dictionary = {"key" : "value"}

## Access elements

We can access an item in dictionary via its key. For example:

        myDictionary["u0921789"]

OR

        myDictionary.get("u0921789")


We can also get a list of all the keys in the dictionary

        # Keys is a python list containing all the keys in the dict
        keys = myDicionary.keys()

Similarly we can get a list of all the values

        values = myDictionary.values()

### Check if a key is in the dictionary

        if "u0921789" in myDictionary:
            return True

## Modify a dictionary

We can update items in the dictionary with `dictionary.update()`. If the key doesn't exist it will be added:

        myDictionary.update({"u934791" : "Mitchell"})

## Remove from a dictionary

        myDictionary.pop("key")

OR

        del myDictionary["key"]


## Dictionary loop examples

        for key,value in myDictionary.items():
            print(key, value)

        for key in myDictionary.keys():
            print(key)

        for value in myDictionary.values():
            print(value)

