def sort(arr):# Сортировка пузырьком
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)

def binary_search(array, element, left, right): 
    if left > right: 
        return False
    
    middle = (right+left) // 2
    if array[middle] < element and array[middle+1]>= element :  #Проверяем что элемент меньше введеного числа и последующий элемент больше либо равен введеному числу
        return middle 
    elif element < array[middle]: 
        
        return binary_search(array, element, left, middle-1)
    else: 
        return binary_search(array, element, middle+1, right)


while True:
    n=input('Введите последовательность чисел через пробел: ')
    try:
        rez=[int(x) for x in n.split()]
        break
    except: print('Ошибка ввода, введите корректные данные')
while True:
    n=input('Введите число: ')
    try:
        n=int(n)
        break
    except: print('Ошибка ввода')
sort(rez)
ans=binary_search(rez, n,1,len(rez)-2) # так как граничные занчения не могут являтся ответом их не учитываем
if ans==False:
    print("Такого числа нет")
else:
    print('Элемент под номером',ans,'(Не забываем что отсчет начинается с 0)')
