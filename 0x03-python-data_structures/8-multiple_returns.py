#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '\0':
        return (None)
    else:
        return(sentence[0], len(sentence))
