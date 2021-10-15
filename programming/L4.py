from itertools import chain
list = ['pog', 'poop', 'cum']

class countList:
    def main(self, x):
        return len(x)

    def main1(self, x):
        coom=0
        for i in x:
            coom += 1
        return coom

    def main2(self, x, y):
        x.append(y)

    def sort(self, x):
        return sorted(x)

    def main3(self, x, y):
        x.extend([y])
        return x




if __name__ == '__main__':
    # c = countList()
    # # c.main2(x = list, y = input('enta smth: '))
    # c.main3(x = list, y = input('enta smth: '))
    # print(c.main1(x = list))
    # print(', '.join(list))
    # print (', '.join(c.sort(x = list)))