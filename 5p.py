# Code writed & idea by stefanlight (Стефан Мухин). https://www.stefanlight.ml/
# Пришлось все делать в одном файле, а так я хотел сделать в нескольких.
# Разбить код на классы и отдельные файлы, как любят в Java.

from random import choice
import requests
from urllib.parse import quote
from rich import print
from os import system, name

requests.Response


def clear_log():
    if name == "nt":
        system("cls")
    else:
        system("clear")


welcome_program_message = """
    [yellow]
    ███████ ███████
    ██      ██   ██   — Сценарий номер {index}             
    ███████ ██████      "{name}"    
         ██ ██        — {description}   
    ███████ ██  
    [/yellow]
"""


def first_program():
    """
    Калькулятор
    """
    clear_log()

    print(
        welcome_program_message.format(
            index=1,
            name="Калькулятор",
            description="Введите пример, который нам предстоит решить.",
        )
    )

    expression = input("— Напишите пример: ")
    resp = requests.get(f"https://api.mathjs.org/v4/?expr={quote(expression)}")
    res = resp.text
    res = res.replace("`", "\u200b`\u200b")[:500]

    if "Error" in res:
        return print(
            "[red]API не смог понять пример.\nПопробуйте изменить пример или его порядок.[/red]\n\nПерезапустите программу."
        )
    elif "NaN" in res:
        return print(
            "[red]API не смогло вывести нормальное число.\nПопробуйте изменить пример или его порядок.[/red]\n\nПерезапустите программу."
        )

    return print(f"{expression} = {res}\n\n[blue]•[/blue] Powered by MathJS API")


def second_program():
    """
    Погода
    """
    clear_log()
    print(
        welcome_program_message.format(
            index=2, name="Погода", description="Напишите город — мы подскажем погоду."
        )
    )

    place = input("— Выберете город: ")
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid=6d00d1d4e704068d70191bad2673e0cc&lang=ru&units=metric"
    )
    if resp.status_code != 200:
        return print(
            "[red]API не удалось найти этот город.\nПроверьте правильно ли вы написали название.[/red]\n\nПерезапустите программу."
        )

    res = resp.json()

    return print(
        f"""
        Погода в {res['name']} ({res['sys']['country']})
        {res['weather'][0]['description'].title()}

        ╭ [yellow]Температура[/yellow]
        │ Сейчас: {res['main']['temp']}°C
        ╰ Чуствуется как: {res['main']['feels_like']}°C

        ╭ [yellow]Окружение[/yellow]
        │ Давление: {res['main']['pressure']} Pa
        ╰ Влажность: {res['main']['humidity']}%

        ╭ [yellow]Ветер[/yellow]
        │ Скорость: {res['wind']['speed']} км/ч
        ╰ Направление: {res['wind']['deg']}°

        [blue]•[/blue] Powered by OpenWeatherAPI
        """
    )


def third_program():
    """
    Сортировка данных
    """
    clear_log()
    print(
        welcome_program_message.format(
            index=3,
            name="Сортировка данных",
            description="Напишите данные (цифры или буквы) через запятую и мы попытаемся сортировать их.",
        )
    )

    value = input("— Введите данные через запятую: ")
    value.replace(" ", "")
    return print(sorted(value.split(","), reverse=True))


def fourth_program():
    """
    Генератор никнеймов
    """
    clear_log()
    print(
        welcome_program_message.format(
            index=4,
            name="Генератор никнеймов",
            description="Напишите сколько никнеймов вам сгенерировать - и мы это сделаем.",
        )
    )
    number = input("— Количество никнеймов: ")

    if 20 < int(number):
        return print("Думаю вам не стоит генерировать более 20-и никнеймов.")

    resp = requests.get(f"https://names.drycodes.com/{number}")
    res = resp.json()

    return print("\n".join([str(nickname) for nickname in res]))


def fifth_program():
    """
    Рандомное число из периода
    """
    clear_log()
    print(
        welcome_program_message.format(
            index=5,
            name="Рандомное число из периода",
            description="Мы выберем рандомное число из выбранного вами периода.",
        )
    )
    first_number = input("— Введите первое число периода: ")
    second_number = input("— Введите второе число периода: ")

    if first_number > second_number:
        return print(
            "[red]Вы не можете сделать период у которого первое число больше чем второе.[/red]"
        )

    return print(f"Результат: {choice(range(int(first_number), int(second_number)+1))}")


def welcome():
    clear_log()

    welcome_message = """
        ┌──────────────────────────────────────────────────────────┐
        │                                                          │
        │                                                          │
        │                     ███████ ███████                      │
        │                     ██      ██   ██                      │
        │                     ███████ ██████                       │         
        │                          ██ ██                           │
        │                     ███████ ██                           │
        │                                                          │
        │                                                          │
        │   Эта программа сделана по заданию из домашней работы.   │
        │   Вас встречает консольный интерфейс 5programs.          │
        │   В дальнейшем, вам нужно выбрать номер сценария.        │
        │                                                          │
        │   ╭ Доступные сценарии                                   │
        │   │ 1 — калькулятор.                                     │
        │   │ 2 — погода в выбранном городе.                       │
        │   │ 3 — сортировать данные.                              │
        │   │ 4 — генератор никнеймов.                             │
        │   ╰ 5 — рандомное число из периода.                      │
        │                                                          │
        │                                                          │
        └──────────────────────────────────────────────────────────┘
    """

    def format_welcome_message(message: str, special_unicode: list) -> str:
        format_message = message

        for unicode in special_unicode:
            format_message = format_message.replace(
                unicode, f"[yellow]{unicode}[/yellow]"
            )

        return format_message

    print(
        format_welcome_message(
            welcome_message, ["┌", "┐", "└", "┘", "╰", "╭", "─", "│"]
        )
    )

    choosen_program = input(
        "— Выберете любой желаемый сценарий и он начнет выполняться: "
    )

    if len(choosen_program) == 1:
        match choosen_program:
            case "1":
                return first_program()
            case "2":
                return second_program()
            case "3":
                return third_program()
            case "4":
                return fourth_program()
            case "5":
                return fifth_program()
            case _:
                return print(
                    "[red]Мы не можем предоставить несуществующий сценарий.[/red]"
                )
    else:
        print("[red]Не пишите лишнего в выбор сценария.[/red]")


if __name__ == "__main__":
    welcome()
