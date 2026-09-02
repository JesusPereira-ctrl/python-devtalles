class CoffeeMaker:
    def make_coffee(self):
        self.__boil_water()
        self.__mix()
        print('PIP PIP')
        print('Tu café esta listo')

    def __boil_water(self):
        print('Hirviendo agua...')

    def __mix(self):
        print('Combinando café y agua...')


coffee_maker = CoffeeMaker()
coffee_maker.make_coffee()
