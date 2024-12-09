"""
Создайте класс Zebra, внутри которого есть метод
    which_stripe, который поочередно печатает фразы «Полоска белая»,
    «Полоска черная» без кавычек, начиная именно с фразы «Полоска белая».

    Также реализуйте метод run_away, который печатает фразу «Oh, Sugar Honey Ice Tea».
"""


class Zebra:
    count = 0

    def which_stripe(self):
        self.count += 1
        if self.count % 2 != 0:
            print('Полоска белая')
        else:
            print('Полоска черная')

    def run_away(self):
        print('Oh, Sugar Honey Ice Tea')


if __name__ == '__main__':
    zebra = Zebra()
    zebra.run_away()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.which_stripe()
    zebra.run_away()
    print()

    zebra_1 = Zebra()
    zebra_2 = Zebra()
    zebra_1.which_stripe()
    zebra_2.which_stripe()
    zebra_1.which_stripe()
    zebra_1.which_stripe()
    zebra_1.which_stripe()
    zebra_2.which_stripe()
    zebra_2.which_stripe()
