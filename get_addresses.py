import re
import operator
address_file = 'BAF_20161224.dat' # From http://www.posti.fi/business/send/postal-code-services/postal-code-files.html
fo = open('output.txt', 'w+')

municipalities = [x.replace('\n','') for x in open('municipalities.txt')]
municipalities += [x.replace('\n','') for x in open('municipalities_in_se.txt')]
municipalities = set(municipalities)
common_finnish_words = set([x.replace('\n','') for x in open('most_common_finnish_words.txt')])
first_names = set([x.replace('\n','').lower() for x in open('first_names.txt')])


def contains_no_digits(text):
    for c in text:
        if c.isdigit():
            return False
    return True

def not_capitalized(text):
    if text.upper() == text:
        return False
    return True

def not_a_municipality(text):
    if text.strip() in municipalities:
        return False
    return True

def not_funny_name(text):
    for s in text.split(" "):
        if len(s) == 1:
            return False 
    return True

def not_too_many_uppercases(text):
    n_uppercases = sum(1 for c in text if c.isupper())
    if n_uppercases > len(text.split(" ")) + 2:
        return False
    return True


streets = {}
for i, line in enumerate(open(address_file)):
    address = re.sub('  +', '  ', line).split("  ")
    for a_i, a in enumerate(address):
        if a_i > 1:
            if len(a) > 3:
                if contains_no_digits(a):
                    if not_capitalized(a):
                        if not_a_municipality(a):
                            if not_funny_name(a):
                                if not_too_many_uppercases(a):
                                    if a.lower() not in common_finnish_words:
                                        if a.lower() not in first_names:
                                            if a in streets:
                                                streets[a] += 1
                                            else:
                                                streets[a] = 1

#streets = sorted(streets.items(), key=operator.itemgetter(1))
streets = sorted(streets.keys())

out = ''
for s in streets:
    out += s + '\n'
fo.write(out)
