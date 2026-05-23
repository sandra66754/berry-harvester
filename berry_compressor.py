def sum_for_position(i, berries, N):
    left = (i - 1 + N) % N
    right = (i + 1) % N
    return berries[left] + berries[i] + berries[right]

def find_max_sum(N, berries):
    max_sum = 0
    for i in range(N):
        current = sum_for_position(i, berries, N)
        if current > max_sum:
            max_sum = current
    return max_sum

def compress(berries):
    N = len(berries)
    return find_max_sum(N, berries)

if __name__ == "__main__":
    import sys
    
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ СБОРА ЧЕРНИКИ")
    print("=" * 50)
    print("Находит максимальную сумму ягод на трёх соседних кустах")
    print("(кусты расположены по кругу)")
    print("-" * 50)
    
    # Проверяем, переданы ли данные через pipe или перенаправление
    if not sys.stdin.isatty():
        # Данные идут из pipe или файла
        data = sys.stdin.read().strip().split()
        if not data:
            print("Ошибка: Нет входных данных")
            sys.exit(1)
        N = int(data[0])
        berries = list(map(int, data[1:1+N]))
    else:
        # Интерактивный режим - запрашиваем данные у пользователя
        try:
            N = int(input("Введите количество кустов (N от 3 до 1000): "))
            if N < 3 or N > 1000:
                print("Ошибка: N должно быть от 3 до 1000")
                sys.exit(1)
            
            print(f"Введите {N} чисел (количество ягод на каждом кусте, от 1 до 1000):")
            berries_input = input("→ ")
            berries = list(map(int, berries_input.split()))
            
            if len(berries) != N:
                print(f"Ошибка: нужно ввести ровно {N} чисел")
                sys.exit(1)
                
        except ValueError:
            print("Ошибка: Введите целые числа")
            sys.exit(1)
    
    print("-" * 50)
    print(f"Введено кустов: {N}")
    print(f"Ягод на кустах: {berries}")
    print("-" * 50)
    
    result = compress(berries)
    
    print(f"Максимальный сбор за один подход: {result}")
    print("=" * 50)