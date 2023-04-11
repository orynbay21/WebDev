

def split_and_join(line):
    news=""
    for i in range(len(line)):
        if(line[i]==" "):
            news+="-"
        else:
            news+=line[i]
    return(news)
            

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    
    print(result)