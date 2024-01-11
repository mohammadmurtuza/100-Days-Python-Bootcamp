'''here the keyword letter in the for loop below is the word from the list which we will compare with the user input like 
 the word is "nemo" and user input "m" so when the for loop starts first "letter" will be set as "n" and checked with the if 
 statement inside that is "n" == userinput i.e "o" spo basically "n" == "o" which is false so prints the else and soo on as much 
 as the length of the word whenever "o" == "o" then only print "right".'''
word = ["hello","bye"]
char = input()
for letter in word:
    if letter == char:
        print("right")
    else:
        print("wrong")