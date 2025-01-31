def count_chars(txt: str) -> dict:
    d = {}

    for ch in txt:
        c = ch.lower()

        if d.get(c) is None:
            d[c] = 1
        else:
            d[c] += 1

    return d


def count_words(txt: str) -> int:
    return len(txt.split())


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_chars(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        for key in char_count:
            if ord(key) >= ord('a') and ord(key) <= ord('z'):
                print(f"the \'{key}\' chracter was found {char_count[key]} times")

        print("--- End report ---")


main()
