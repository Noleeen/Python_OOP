
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
# class Auto:
#     # атрибут класса:
#     auto_count = 0
#
#     # методы класса
#     def start(self, name, model, year):
#         self.auto_name = name
#         self.auto_model = model
#         self.auto_year = year
#
# a = Auto()  # создаём объект
# a.start('mazda','cx-50',2018) # записываем в него атрибуты
# # print(a.auto_name)
# # print(a.auto_model)
# # print(a.auto_year)
#
# b = Auto()
# b.start('ford','edge',2017)
# # print(b.auto_name)
# # print(b.auto_model)

# print(Auto.auto_name) - ошибка так как у класса нет такого атрибута, атрибут есть только у объекта созданного с помощью этого класса

#   ТОЖЕ САМОЕ ТОЛЬКО С МАГИЧЕСКИМ МЕТОДОМ _ИНИТ_

# class Auto2:
#     auto_count = 0 #атрибут класса
#
#     def __init__(self,name,model,year):
#         self.auto_name = name
#         self.auto_model = model
#         self.auto_year = year
#         Auto2.auto_count +=1
#
#
# print(Auto2.auto_count)
#
# a = Auto2('mazda', 'cx-50', 2018)
# print(a.auto_name, a.auto_year)
# print(Auto2.auto_count)
#
# b = Auto2('honda', 'civic', 2014)
# print(b.auto_name, b.auto_model)
# print(Auto2.auto_count)
# print(b.auto_count)
# print(a.auto_count)





#########################################################

# class Button:
#     count = 0
#     def click (self):
#         Button.count += 1
#     def click_count(self):
#         return Button.count
#
#     def reset(self):
#         Button.count = 0
#
#
# b = Button()
# b.click_count()
# b.click()
# b.click()
# a = Button()
# a.click()
# print(b.click_count())

########################################
# напишите класс Balance для описания весов с двумя чашами.
# На левую и правую чаши будут подаваться грузы с разным весом.
# Ваша задача определить положение чаш.
#
# Метод add_r принимает целое число - вес, положенный на правую чашу. Метод add_l - на левую.
# Метод result выводит "=", если чаши равны, "R" если в правой больше, "L" если в левой больше

# class Balance:
#
#     weigh_R = 0
#     weigh_L = 0
#
#     def add_r(self,w):
#         self.weigh_R += w # тут и далее пишем self.weigh_R вместо Balance.weigh_R, чтоб новые значения записывались не в атрибуты класса, а отдельно в атрибуты объекта, чтоб при создании нового объекта атрибуты обнулялись!
#
#     def add_l(self,w):
#         self.weigh_L += w
#
#     def result(self):
#         r = self.weigh_R
#         l = self.weigh_L
#         if r == l:
#             print('=')
#         elif r > l:
#             print('R')
#         elif r < l:
#             print('L')
#
# b = Balance()
# b.result()
# b.add_r(10)
# b.add_l(7)
# b.add_l(5)
# b.result()
#
# b2 = Balance()
# b2.result()
# b2.add_l(10)
# b2.add_r(7)
# b2.add_r(5)
# b2.result()
########################################
########################################

# напишите класс BigBell который при вызове метода sound печатает попеременно ding и dong

# class BigBell:
#     check = 1
#
#     # def sound(self):
#     #     if BigBell.check:
#     #         print('ding')
#     #         BigBell.check = 0
#     #     else:
#     #         print('dong')
#     #         BigBell.check = 1

#       # ЛУчшЕ ТАК:
#     def sound(self):
#         if self.check:
#             print('ding')
#             self.check = 0
#         else:
#             print('dong')
#             self.check = 1
#
# b = BigBell()
#
# b2 = BigBell()
# b2.sound()
# b.sound()
# b2.sound()
# b2.sound()


################################################################################
################################################################################

class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentenses(self, line: str):
        self.words += line.split()

    def short(self):
        min_ = len(sorted(self.words, key=len)[0])
        return list(filter(lambda x: len (x) == min_, self.words))

    def long(self):
        max_ = len(sorted(self.words, key=len)[-1])
        res = list(filter(lambda x:len(x) == max_, self.words))
        res = " ".join(res)
        return res



add_str = MinMaxWordFinder()
add_str.add_sentenses(" hgfdhsh sdf sdfe eassd t anklj;g")
add_str.add_sentenses("hgfdhsh i 5 ")
print(add_str.words)
print(sorted(add_str.words, key=len))

print(add_str.short())
print(add_str.long())
