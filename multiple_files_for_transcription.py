import os

file = "final_words"

with open(file, "r") as f:
    for i in f:
        i = i.strip("\n")
        with open(f'{i}.lab', "w") as g:
            print(i)
            g.write(i)


# folder = "webmaus/p2"

# for file in os.listdir(folder):
#     name, ext = os.path.splitext(file)
#     file = name + ".lab"
#     word = name.split('_')
#     word = word[1]
#     print(word)
#     with open(file, "w") as g:
#         print(word)
#         g.write(word)






    # for word in sorted(os.listdir(folder)):
    #     path = os.path.join(folder, word)
    #     if ipa.syllable_count(word) == 1:
    #         for i in ipa.convert(word):
    #             if i in fricatives:
    #                 print(f'Writing {word} for {i}')
    #                 f.write(f'{i}\t{word}\t{ipa.convert(word)}\n')
    #     else:
    #         print(f'Removing {word}')
    #         shutil.rmtree(path)