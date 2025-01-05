# При запросе к адресу birthday/ вызывается view-функция birthday(),
# в которой должен быть создан экземпляр класса формы BirthdayForm.
# Этот экземпляр нужно передать в HTML-шаблон через словарь context.
from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown


def birthday(request):
    form = BirthdayForm(request.GET or None)
    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}
    # Если форма валидна...
    if form.is_valid():
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'birthday/birthday.html', context)

# def birthday(request):
#     # Если есть GET-параметры — передаём их в форму:
#     form = BirthdayForm(request.GET or None)
#     if form.is_valid():
#         pass
#     # Форму с переданным в неё объектом request.GET
#     # записываем в словарь контекста...
#     context = {'form': form}
#     # ...и отправляем в шаблон.
#     return render(request, 'birthday/birthday.html', context)
#     # в шаблон отправлена форма, в которую передан объект
#     # request.GET — словарь с данными из запроса.
#     # При отрисовке формы на странице эти данные отобразились в полях формы.
#     # Чтобы получить пустую форму, надо удалить все параметры
#     # из адресной строки и отправить GET-запрос без параметров.

# Его логика такова: если в GET-запросе были переданы параметры — значит,
# объект request.GET не пуст и этот объект передаётся в форму; если же объект
# request.GET пуст — срабатывает условиe or и форма создаётся без параметров,
# через BirthdayForm(None) — это идентично обычному BirthdayForm().


# def birthday(request):
#     # Если есть параметры GET-запроса...
#     if request.GET:
#         # ...передаём параметры запроса в конструктор класса формы.
#         form = BirthdayForm(request.GET)
#         # Если данные валидны...
#         if form.is_valid():
#             # ...то считаем, сколько дней осталось до дня рождения.
#             # Пока функции для подсчёта дней нет — поставим pass:
#             pass
#     # Если нет параметров GET-запроса.
#     else:
#         # То просто создаём пустую форму.
#         form = BirthdayForm()
#     # Передаём форму в словарь контекста:
#     context = {'form': form}
#     return render(request, 'birthday/birthday.html', context)

# def birthday(request):
#     # Создаём экземпляр класса формы.
#     # print(request.GET)  # Напечатаем.
#     form = BirthdayForm()
#     # Добавляем его в словарь контекста под ключом form:
#     context = {'form': form}
#     # Указываем нужный шаблон и передаём в него словарь контекста.
#     return render(request, 'birthday/birthday.html', context)
