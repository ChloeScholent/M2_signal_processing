import random

wordlist = ["mother", "nether", "within", "that", "these", "though", "lathe", "bathe", "breathe", "beth", "booth", "health", "thaw", "thought", "Ethiopia", "authority", "theory", "lethal", "cat", "tax", "attest", "bees", "misery", "zone", "medical", "mood", "day", "face", "coffee", "beef", "massage", "cyan", "miss", "vibe", "arrive", "evidence"]

for i in range(len(wordlist)):
    word = random.choice(wordlist)
    print(i+1, word)
    wordlist.remove(word)


