words = open('address_endings_fi.txt').read().splitlines()
addresses = open('addresses_fi.txt').read().splitlines()

rest = open('rest.txt', 'w+')
for a in addresses:
    covered = False
    for w in words:
        if a[-len(w):] == w:
            covered = True
    if not covered:
        rest.write(a + '\n')
rest.close()
