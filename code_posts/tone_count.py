import re
import os
import pickle

neg = "data\\negate"
infile = open(neg, "rb")
negate = pickle.load(infile)

def negated(word):
    """
    Determine if preceding word is a negation word
    """
    if word.lower() in negate:
        return True
    else:
        return False
    
    
def tone_count_with_negation_check(dict, article):
    """
    Count positive and negative words with negation check. Account for simple negation only for positive words.
    Simple negation is taken to be observations of one of negate words occurring within three words
    preceding a positive words.
    """
    pos_count = 0
    neg_count = 0
    pos_words = []
    neg_words = []

    input_words = re.findall(
        r"\b([a-zA-Z]+n\'t|[a-zA-Z]+\'s|[a-zA-Z]+)\b", article.lower()
    )
    word_count = len(input_words)

    for i in range(0, word_count):
        if input_words[i] in dict["Negative"]:
            neg_count += 1
            neg_words.append(input_words[i])
        if input_words[i] in dict["Positive"]:
            if i >= 3:
                if (
                    negated(input_words[i - 1])
                    or negated(input_words[i - 2])
                    or negated(input_words[i - 3])
                ):
                    neg_count += 1
                    neg_words.append(input_words[i] + " (with negation)")
                else:
                    pos_count += 1
                    pos_words.append(input_words[i])
            elif i == 2:
                if negated(input_words[i - 1]) or negated(input_words[i - 2]):
                    neg_count += 1
                    neg_words.append(input_words[i] + " (with negation)")
                else:
                    pos_count += 1
                    pos_words.append(input_words[i])
            elif i == 1:
                if negated(input_words[i - 1]):
                    neg_count += 1
                    neg_words.append(input_words[i] + " (with negation)")
                else:
                    pos_count += 1
                    pos_words.append(input_words[i])
            elif i == 0:
                pos_count += 1
                pos_words.append(input_words[i])

    results = [word_count, pos_count, neg_count, pos_words, neg_words]

    return results
