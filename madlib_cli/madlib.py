import re


def read_template(filepath: str):
    with open(filepath, 'r') as file:
        file_content = file.read()
        file.close()
    return file_content.strip()


def parse_template(text: str):
    # text = re.sub(find, replace, text)

    items = []
    text_stripped = text_stripped = re.sub(r'\{.*?\}', '{}', text)
    res = re.findall(r'\{.*?\}', text)
    for i in res:
        items.append(i.strip("{ }"))
    items = tuple(items)
    return text_stripped, items


def merge(text: str, items: tuple):
    mergedText = text.format(*items)
    return mergedText


def write_new_file(content: str):
    with open('assets/dark_and_stormy_night_template_results.txt', 'w') as potato:
        potato.write(content)


if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("lets start the game with adding some words:")
    wordLst = []
    text = read_template("assets/dark_and_stormy_night_template.txt")
    text_stripped, items = parse_template(text)
    print(text)
    print(text_stripped)
    print(items)
    for i in range(0, len(items)):
        inp = input('type a word  ')
        wordLst.append(inp)
    wordLst = tuple(wordLst)
    mergedText = merge(text_stripped, wordLst)
    print(mergedText)
    write_new_file(mergedText)
