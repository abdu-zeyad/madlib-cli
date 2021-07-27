import re


def read_template(filepath: str):
    with open(filepath, 'r') as file:
        file_content = file.read()
        file.close()
    return file_content.strip()


def parse_template(text: str):
    # text = re.sub(find, replace, text)

    parts = []
    strippedText = strippedText = re.sub(r'\{.*?\}', '{}', text)
    res = re.findall(r'\{.*?\}', text)
    for i in res:
        parts.append(i.strip("{ }"))
    parts = tuple(parts)
    return strippedText, parts


def merge(text: str, parts: tuple):
    mergedText = text.format(*parts)
    return mergedText


def write_new_file(content: str):
    with open('assets/dark_and_stormy_night_template_results.txt', 'w') as potato:
        potato.write(content)


if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("Please enter some words to play the game!")
    wordLst = []
    text = read_template("assets/dark_and_stormy_night_template.txt")
    strippedText, parts = parse_template(text)
    print(text)
    print(strippedText)
    print(parts)
    for i in range(0, len(parts)):
        inp = input('add a word ')
        wordLst.append(inp)
    wordLst = tuple(wordLst)
    mergedText = merge(strippedText, wordLst)
    print(mergedText)
    write_new_file(mergedText)
