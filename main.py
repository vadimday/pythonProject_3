def найти_максимум(a, b, c, d):

   максимум = max(a, max(b, max(c, d)))

   return максимум



число1 = 17

число2 = 27

число3 = 3

число4 = 19

результат = найти_максимум(число1, число2, число3, число4)

print("Максимальное число:", результат)