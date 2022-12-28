
###################################################
# class Auto:
#     auto_name = 'Renaught'
#     auto_model = 'Scenic'
#     auto_year = 2016
#
#     def auto_start(self):
#         print('заводим')
#
#     def auto_stop(self):
#         print('заглушили')
#
# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.auto_start()
# a.auto_stop()
##########################################################
##########################################################

#так НЕ ДЕЛАЮТ, ЛУЧШЕ ИСПОЛЬЗОВАТЬ МАГИЧЕСКИЙ МЕТОД ИНИТ
class Auto:
    # атрибут класса:
    auto_count = 0

    # методы класса
    def start(self, name, model, year):
        self.auto_name = name
        self.auto_model = model
        self.auto_year = year

a = Auto()  # создаём объект
a.start('mazda','cx-50',2018) # записываем в него атрибуты
# print(a.auto_name)
# print(a.auto_model)
# print(a.auto_year)

b = Auto()
b.start('ford','edge',2017)
# print(b.auto_name)
# print(b.auto_model)

# print(Auto.auto_name) - ошибка так как у класса нет такого атрибута, атрибут есть только у объекта созданного с помощью этого класса

#   ТОЖЕ САМОЕ ТОЛЬКО С МАГИЧЕСКИМ МЕТОДОМ _ИНИТ_

class Auto2:
    auto_count = 0 #атрибут класса

    def __init__(self,name,model,year):
        self.auto_name = name
        self.auto_model = model
        self.auto_year = year
        Auto2.auto_count +=1


print(Auto2.auto_count)

a = Auto2('mazda', 'cx-50', 2018)
print(a.auto_name, a.auto_year)
print(Auto2.auto_count)

b = Auto2('honda', 'civic', 2014)
print(b.auto_name, b.auto_model)
print(Auto2.auto_count)
print(b.auto_count)
print(a.auto_count)





#########################################################
exit()
class Button:
    count = 0
    def click (self):
        Button.count += 1
    def click_count(self):
        return Button.count

    def reset(self):
        Button.count = 0


b = Button()
b.click_count()
b.click()
b.click()
a = Button()
a.click()
print(b.click_count())
