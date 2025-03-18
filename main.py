from stats import get_num_words, num_dict, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    count = get_num_words(file_path)
    nums_dict = num_dict(file_path)
    sorted_dict = sort_dict(nums_dict)

    # Print structured report
    print("============== BOOKBOT ==============")
    print(f"Analyzing book found at {file_path}...")
    print("------------- Word Count ------------")
    print(f"Found {count} total words")
    print("---------- Character Count ----------")
    for item in sorted_dict:
        print(f"{item['char']}: {item['count']}")

main()
