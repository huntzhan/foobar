from __future__ import division


# !
def answer(minions):
    minions_expect = [time / (numerator / denominator)
                      for time, numerator, denominator in minions]
    get_expect = lambda x: minions_expect[x]
    return sorted(range(len(minions)), key=get_expect)
