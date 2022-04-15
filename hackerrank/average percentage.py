if __name__ == '__main__':

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name,*line= input().split()
        # It help to store remaining after one in one list
        #here we use args because we cant store list in dictionary as key so we use args which make list a tuple and then store it.
        scores = list(map(float, line))
        student_marks[name] = scores
    l=len(line)
    query_name = input()
    a=sum(student_marks[query_name])/l
    b=format_float = "{:.2f}".format(a)  #this is use to make it go two decimal
    print(b)