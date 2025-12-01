import math

def calculate_flow_velocity(
    flow_rate_m3h: float,
    diameter_mm: float
) -> float:
    """
    Рассчитать скорость потока жидкости в трубопроводе.

    Параметры:
        flow_rate_m3h (float): Объёмный расход, м³/ч.
        diameter_mm (float): Внутренний диаметр трубы, мм.

    Возвращает:
        float: Скорость потока, м/с.

    Raises:
        TypeError: Если введены не числовые значения.
        ValueError: Если входные значения некорректны.
    """
    
    #Проверка входных данных
    if not isinstance(flow_rate_m3h, (int, float)):
        raise TypeError("Введите числовое значение расхода.")
    if not isinstance(diameter_mm, (int, float)):
        raise TypeError("Введите числовое значение диаметра трубы.")
    if flow_rate_m3h <= 0:
        raise ValueError("Расход должен быть положительным (> 0 м³/ч).")
    if diameter_mm <= 0:
        raise ValueError("Диаметр трубы должен быть положительным (> 0 мм).")  
    
    try:
        # Расчет скорости потока
        velocity = (4 * (flow_rate_m3h / 3600)) / (math.pi * (diameter_mm / 1000)**2)
        return velocity
        
    except (TypeError, ValueError) as err:
        print(err)


    



