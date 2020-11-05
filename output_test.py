import os
import csv

def main():
    """
    with open('polls/application/data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    """
    # with open(os.getcwd()+'/polls/application/'+'data.csv','a') as f:
    with open('polls/application/data.csv') as f:
        reader = csv.reader(f, lineterminator=',')
        datas = []
        for row in reader:
            # print(row)
            datas.append(row)
    return datas

if __name__ == "__main__":
    print(main())
    # main()

