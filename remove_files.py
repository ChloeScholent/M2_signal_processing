import eng_to_ipa as ipa
import os
import shutil

folder = "en/clips"
candidates = "candidates.txt"

fricatives = ("θ", "ð", "s", "z", "f", "v", "t", "d")

with open(candidates, "w") as f:
    for word in sorted(os.listdir(folder)):
        path = os.path.join(folder, word)
        if ipa.syllable_count(word) == 1:
            for i in ipa.convert(word):
                if i in fricatives:
                    print(f'Writing {word} for {i}')
                    f.write(f'{i}\t{word}\t{ipa.convert(word)}\n')
        else:
            print(f'Removing {word}')
            shutil.rmtree(path)