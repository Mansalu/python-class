"""
Word counting assignment. Given a text file, find the most common words.
Some starter code is provided to help parse the file and remove puntuation.

Think about how you can use a dictionary to solve this problem. We need to store a count
for every unique word we might enocunter in a text.

What about a dictionary that maps each word to a count

    {"word" : 5}

"""
import re

def TopTenWords(text):
    """
    Given a text string, returns the 10 most common words, and how many times each word appeared.
    """
    # TODO Start here
    print("Not implemented")


# ==================================================================
# Driver code
# ==================================================================
def main():
    inputText = ""
    # Prompt for a file name in a loop until a valid file is read in
    while(True):
        try:
            # Prompt the user for a file name
            fileName = input("Enter the name of a text file:")
            # Open the file for reading
            inputFile = open(fileName, 'r', encoding='utf-8')
            # Read the entire file contents into our string
            inputText = inputFile.read(-1)
            # Once we succesfully read a file we can break the loop
            break
        except OSError as Error:
            # If there's an error, print it and prompt the user again
            print("File could not be opened:", fileName)
            continue
        finally:
            # Always close the file
            inputFile.close()

    # Merge words split across lines
    text = text.replace('-\n', '')
    # Remove all punctuation
    text = re.sub("[^\w\s]", '' , text)
    # Shrink multiple spaces
    text = re.sub('\s{2,}', ' ', text)
    text = text.replace('\n', ' ')
    
    # Call *your* function on the input
    TopTenWords(inputText)

if __name__ == "__main__":
    main()