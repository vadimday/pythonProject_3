def простое(число):
   if число < 2:

       return False
   for дільник in range(2, int(число**0.5) + 1):

       if число % дільник == 0:

           return False

   return True

число = 27

результат = простое(число)

print(f"Число {число}  простое: {результат}")

