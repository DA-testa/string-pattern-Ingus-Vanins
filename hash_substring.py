# python3


def read_input():
    c = input()

    if "F" in c:
        useFile = 'tests/06'
        f1 = open(useFile, 'r')
        l = f1.readlines()
        pattern = l[0].rstrip()
        text = l[1].rstrip()

    elif "I" in c:
        pattern = input().rstrip()
        text = input().rstrip()
    return (pattern, text)
def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    q = 1
    ind = []
    a_len = 256
    p_len = len(pattern)
    t_len = len(text)
    phash_val = 0
    thash_val = 0
    for i in range(p_len):
        phash_val = (a_len * phash_val + ord(pattern[i])) % q
        thash_val = (a_len * thash_val + ord(text[i])) % q

    i = 0
    j = 0
    h = 1

    for i in range(p_len - 1):
        h = (h * a_len) % q
    for i in range(t_len - p_len + 1):
        if phash_val == thash_val:
            for j in range(p_len):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1
            if j == p_len:
                ind.append(str(i))
        if i < t_len - p_len:
            thash_val = (a_len * (thash_val - ord(text[i]) * h) + ord(text[i + p_len])) % q
            if thash_val < 0:
                thash_val = thash_val + q

    return ind

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
