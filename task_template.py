'''
author = Kristyna Brunova
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

registered = [('bob', '123'), ('ann', 'pass123'), ('mike', 'password123'), ('liz', 'pass123')]

print("-"*50)
print("Welcome to the app. Please log in:")

username = input("USERNAME: ")
password = input("PASSWORD: ")

if (username, password) not in registered:
    print("Access denied")
else:
    print("You can start analyzing, honey!")
    print("-"*50)
    print("We have {} texts to be analyzed.".format(len(TEXTS)))


    index = int(input("Enter a number btw. {} and {} to select: ".format(1, len(TEXTS))))
    print("-"*50)

    text_list = TEXTS[index-1].split()
    num_words = len(text_list)

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    lengths = []
    numerics = []

    while text_list:
        word = text_list.pop()
        word = word.replace(",", "")
        word = word.replace(".", "")
        if word[0] == word[0].capitalize() and not word.isnumeric():
            sum1 += 1
        if word == word.upper() and not word.isnumeric():
            sum2 += 1
        if word == word.lower() and not word.isnumeric():
            sum3 += 1
        if word.isnumeric():
            sum4 += 1
            numerics.append(float(word))
        lengths.append(len(word))



    print("There are {} words in the selected text.".format(num_words))
    print("There are {} titlecase words.".format(sum1))
    print("There are {} uppercase words.".format(sum2))
    print("There are {} lowercase words.".format(sum3))
    print("There are {} numeric strings.".format(sum4))



    print("-"*50)

    lengths.sort()

    prev_str = ""
    new_str = ""

    for i in lengths:
        new_str = str(i) + lengths.count(i)*"*" + str(lengths.count(i))

        if new_str != prev_str:
            print(new_str)

        prev_str = new_str

    print("-"*50)

    print("If we summed all the numbers in this text we would get: {}".format(sum(numerics)))



