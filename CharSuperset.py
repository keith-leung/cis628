
all_char_list = ['data/Chinese_common.txt', 'data/hiragana_AND_katakana_Japanese.txt',
                 'data/Hongkong_Chinese.txt', 'data/Kanji_Japanese_N1_N5.txt',
                 'data/Korean_Hangul.txt', 'data/Korean_Hanja_high_school.txt']

dictionary_all_chars = {}

for filename in all_char_list:

    with open(filename, encoding="utf8") as f:
        content = f.readlines()

        for line in content:
            char = line.strip()
            if len(char) == 1 and (char not in dictionary_all_chars.keys()):
                dictionary_all_chars[char] = 0

print(dictionary_all_chars)