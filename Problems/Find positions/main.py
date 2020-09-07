number_seq = list(str(input()).split())
number_pos = input()

founded = [str(i) for i, n in enumerate(number_seq) if n == number_pos]

if founded:
    print(' '.join(founded))
else:
    print('not found')
