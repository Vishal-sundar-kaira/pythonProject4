import textwrap

def wrap(string, max_width):
    i=0
    while int(len(string[i:])>=max_width):
        a=print(string[i:i+max_width])
        i+=max_width
    b=print(string[i:])
    return print(f"{a}\n{b}")

if __name__ == '__main__':
    string, max_width = input("write string"), int(input("max width"))
    result = wrap(string, max_width)
    print(result)