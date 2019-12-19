#Raise statement demo

def printbox(symbol,legnt,hight):
    if len(symbol) != 1:
        raise Exception ('Symbol needs to a string of lenght 1')
    if legnt<2 & hight<2:
        raise Exception('Legnth and hight should be greater than 2')
    print(symbol * legnt)

    for i in range(hight-2):
        print(symbol,(' ' * (legnt-2))+symbol)
    print(symbol*legnt)

printbox('*', 4 , 4)
