import json
import logging
from pathlib import Path

from utils.reader import prochitat_chisla
from utils.statistics import poschitat_srednee, nayti_minimum, nayti_maksimum

def proverit_dannye(spisok_chisel):
    if len(spisok_chisel) == 0:
        raise ValueError("Список измерений пуст")

def main():
    bazovaya_papka = Path.cwd()
    print(f"Текущий рабочий каталог: {bazovaya_papka}")
    
    papka_logov = bazovaya_papka / "logs"
    papka_logov.mkdir(exist_ok=True) 

    put_k_konfigu = bazovaya_papka / "config.json"
    with open(put_k_konfigu, "r", encoding="utf-8") as fayl_konfiga:
        nastroiki = json.load(fayl_konfiga)
    
    put_k_dannym = bazovaya_papka / nastroiki["input_file"]
    put_k_logam = bazovaya_papka / nastroiki["log_file"]

    logging.basicConfig(
        filename=put_k_logam,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )

    logging.info("Программа запущена")

    if not put_k_dannym.exists():
        logging.error(f"Файл не найден: {put_k_dannym}")
        print("Ошибка: Файл с данными не найден!")
        return

    try:
        dannye = prochitat_chisla(put_k_dannym)
        logging.info(f"Успешно прочитано значений: {len(dannye)}")
        
        proverit_dannye(dannye)
        
        srednee = poschitat_srednee(dannye)
        minimum = nayti_minimum(dannye)
        maksimum = nayti_maksimum(dannye)
        
        print(f"Количество: {len(dannye)}")
        print(f"Мин: {minimum}, Макс: {maksimum}, Среднее: {srednee}")
        
    except FileNotFoundError:
        logging.error("Ошибка: Файл не найден")
        print("Ошибка: Файл не найден")
    except ValueError as oshibka:
        logging.error(f"Ошибка данных: {oshibka}")
        print(f"Ошибка данных: {oshibka}")
    
    logging.info("Программа завершена")

if __name__ == "__main__":
    main()