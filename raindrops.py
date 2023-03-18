import webbrowser as wb
import random as rd
while True:
        x = int(input("escolha entre 1 e 4 para flutuar:"))
        if x == 1:
            wb.open("https://www.youtube.com/watch?v=2WqI50mc7Jo")
        elif x == 2:
            wb.open("https://www.youtube.com/watch?v=2agCnyknvJA&list=RD2agCnyknvJA&start_radio=1")
        elif x == 3:
            wb.open("https://www.youtube.com/watch?v=MHryuYVyHhk&list=RD2agCnyknvJA&index=6")
        elif x == 4:
            wb.open("https://www.youtube.com/watch?v=_WCD3Z9UmJ4&list=RD2agCnyknvJA&index=9")
            break
        else:
            print("tente novamente!")
