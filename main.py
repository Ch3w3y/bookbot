from stats import count_words
from stats import char_count
from stats import sorted_dictionary
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

# Read the file and process its contents
path = sys.argv[1]
with open(path) as f:
    text = f.read()

word_count = count_words(text)
char_counts = char_count(text)
sorted_chars = sorted_dictionary(char_counts)

# Now call the function after it's been defined
print_report(path, word_count, sorted_chars)