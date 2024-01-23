def calculate_average(lst):
    if not lst:
        return 0
    total_sum = sum(lst)
    average = total_sum / len(lst)
    return average
def main():
    try:
        input_str = input("целое число: ")
        integer_list = [int(num) for num in input_str.split()]
        total_sum = sum(integer_list)
        average = calculate_average(integer_list)
        print(f"сумма елементов: {total_sum}")
        print(f"среднее: {average}")

    except ValueError:
        print("ошибка.")
if __name__ == "__main__":
    main()
