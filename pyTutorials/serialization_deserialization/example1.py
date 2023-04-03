import os

# Open the file for writing and write some data
with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
        myFile.write("I am a Panda\nAnd I love to eat Bamboo\nNot necessarily cotton \n")

# Open the file for reading and I can read line by line
with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1

    # Indicating that I'll loop till I break
    while True:
        line = myFile.readline()    
        
        # Check if line doesn't have any data, if it does, break
        if not line:
            break
       
        # split()
        wordList = line.split()

        #len
        print("No of words: ", len(wordList))

        # Loop Count characters in word list
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # Get average word length
        avgNumChar = charCount/len(wordList)
        print("Average: ", avgNumChar)

        #Else, print the line num and Incread lineNum by 1
        print("Line", lineNum, " : ", line, end="")
        lineNum += 1
