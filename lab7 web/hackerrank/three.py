#sWAP_cASE

def swap_case(s):
    x=""
    news=""
    for i in range(len(s)):
        if s[i].isupper():
            x=s[i].lower()
        else:
            x=s[i].upper()
        news+=x
    return news

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)