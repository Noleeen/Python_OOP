# class LittleBel:
#     def sound (self):
#         print('ding')
#
#
# a = LittleBel()
# a.sound()


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
