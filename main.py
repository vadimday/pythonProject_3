def main():
   try:

       elements = input("Ввести: ").split()

       elements = [int(element) for element in elements]

       number_to_find = int(input("Ввести: "))

       count = elements.count(number_to_find)
       print(f"Число {number_to_find} есть в списке {count} раз.")

   except ValueError:

       print("Ввести.")

if __name__ == "__main__":

   main()