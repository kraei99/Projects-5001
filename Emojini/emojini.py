'''
    CS5001
    2023 Fall
    Kayser Raei
    Homework 6 - Emojini
'''

def read_file_lines(file_name: str) -> list:
    """
    Reads the content of a text file and returns it as a list of lines.
    """
    try:
        with open(file_name, mode="r", encoding="utf8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return []
    except IOError as e:
        print(f"Unable to read file {file_name}: {e}")
        return []


def create_emoji_dictionary(emoji_file: str, input_lang: str, output_lang: str) -> dict:
    """
    Creates a dictionary for emoji translation based on the input and output languages.
    """
    emoji_lines = read_file_lines(emoji_file)
    if not emoji_lines:
        return {}

    headers = emoji_lines[0].strip().split()
    try:
        input_index = headers.index(input_lang.upper())-1
        output_index = headers.index(output_lang.upper())-1
    except ValueError as e:
        print(
            f"Error: The specified languages are not found in the metadata. {e}")
        return {}

    dictionary = {}
    for line in emoji_lines[1:]:
        split_line = line.strip().split()
        if len(split_line) < max(input_index, output_index) + 1:
            continue
        input_val = split_line[input_index]
        output_val = split_line[output_index]
        if input_lang.upper() == 'ENGLISH':
            input_val = input_val.lower()
        if output_lang.upper() == 'ENGLISH':
            output_val = output_val.lower()
        dictionary[input_val] = output_val
    # print('\tdic', dictionary)
    return dictionary


def translate_text(source_file: str, destination: str, dictionary: dict):
    """
    Translates a text file using the provided dictionary and writes to a new file.
    """
    # Empty dictionary check in case of empty file
    if not dictionary:
        return

    input_lines = read_file_lines(source_file)
    if not input_lines:
        return

    translated_lines = []
    for line in input_lines:
        words = line.split()
        # here converting the word in lower to get from the dictionary
        translated_line = " ".join(dictionary.get(word, word)
                                   for word in words)
        translated_lines.append(translated_line + "\n")

    try:
        with open(destination, mode="w", encoding="utf8") as file:
            file.writelines(translated_lines)
    except IOError as e:
        print(f"Unable to write to file {destination}: {e}")


def batch_translate(emoji_file_name: str, directives_file_name: str):
    """
    batch translation based on directives.
    """
    directives = read_file_lines(directives_file_name)
    if not directives:
        return

    for directive in directives:
        try:
            input_lang, output_lang, source_file, destination = directive.strip().split()
            print(f"Processing {source_file} -> {destination}: {input_lang} -> {output_lang}")
            dictionary = create_emoji_dictionary(
                emoji_file_name, input_lang, output_lang)
            if dictionary:  # Only proceed if a dictionary was successfully created
                translate_text(source_file, destination, dictionary)
        except ValueError as e:
            print(f"Error in processing directive: {directive.strip()} - {e}")
    print("done")


def main():
    batch_translate("emojis.txt", "emoji_directives.txt")


if __name__ == "__main__":
    main()