from translate import Translator

try:
    with open('text.txt', mode='r') as my_file:
        text = my_file.read()
        print("Original Contents: ")
        print('\n')
        print(text)
except (FileNotFoundError, IOError) as err:
    print(err)

print('\n')
# Translate content
print("Translated Contents: ")
print('\n')
translator = Translator(to_lang="ja")  # translate to Japan
translation = translator.translate(text)

print(translation)

try:
    with open('text2.txt', mode='w') as my_file:
        text = my_file.write(translation)
    except (FileNotFoundError, IOError) as err:
        print(err)
