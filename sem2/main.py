# Блок констант
PVmin = 0
PVmax = 75
MaxOutputSignal = 20
MinOutputSignal = 4
minNormalCowTemperature = 37.5
maxNormalCowTemperature = 39.0
maxValidCowTemperature = 39.5
minValidCowTemperature = 35.0

"""
Пересчитывает выходной сигнал датчика в температуру коровы

Args: 
    raw_signal: выходной сигнал датчика

Returns:
    Температура тела, на которое прикреплен датчик
"""
def calculate_signal_to_temperature(raw_signal: float) -> float|None:
    if not is_input_signa_valid(raw_signal):
        return None

    temp = float((raw_signal-4)*(PVmax-PVmin)/(MaxOutputSignal-MinOutputSignal) + PVmin)
    print("Результат пересчета: ", temp)
    return temp


"""
Валидирует выходящий сигнал датчика

Args: 
    input_signal: выходной сигнал датчика

Returns:
    true - значение валидное, false - значение не валидное
"""
def is_input_signa_valid(input_signal: float) -> bool:
    if type(input_signal) != float:
        print("Неправильное значение сигнала!")
        return False

    if MinOutputSignal <= input_signal <= MaxOutputSignal:
        return True

    if input_signal == 0:
        print("Датчик отключен")
        return False

    print("Датчик не исправен")
    return False


"""
Валидирует температуру, посчитанную из сигнал датчика

Args: 
    temperature: температура

Returns:
    true - значение валидное, false - значение не валидное
"""
def is_input_temperature_valid(temperature: float) -> bool:
    if type(temperature) != float:
        print("Неправильное значение сигнала!")
        return False
    return True


"""
Проверяет температуру коровы

Args: 
    input_temperature: температура коровы
"""
def check_temperature(input_temperature: float):
    if not is_input_temperature_valid(input_temperature):
        return

    if minValidCowTemperature <= input_temperature < minNormalCowTemperature:
        print("Требуется обогрев")
        return

    if maxNormalCowTemperature < input_temperature <= maxValidCowTemperature:
        print("Требуется охлаждение")
        return

    if input_temperature > maxValidCowTemperature:
        print("Вызывайте врача!")
        return

    if input_temperature < minValidCowTemperature:
        print("Требуется внимание!")
        return

    print("Температура в норме")
    return


def main():
    signal = float(input("Введите размер входного сигнала: "))

    temperature = calculate_signal_to_temperature(signal)
    if type(temperature) == float:
        check_temperature(temperature)




if __name__ == "__main__":
    main()