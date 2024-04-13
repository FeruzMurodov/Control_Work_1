import json
from datetime import datetime
from operator import itemgetter

list_of_notes = []

def add_note(list_of_notes):
    note = []
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    date = datetime.now().strftime('%d-%m-%Y-%H-%M')
    note.append(title)
    note.append(body)
    note.append(date)
    list_of_notes.append(note)
    print("Заметка успешно создан!")
    return list_of_notes

def save_note():
    with open("notes.json", "w", encoding="utf-8") as writer:
        writer.write(json.dumps(list_of_notes, ensure_ascii=False))
        print("Файл успешно сохранен в notes.json!")

def load_note():
    global list_of_notes
    with open("notes.json", "r", encoding="utf-8") as reader:
        list_of_notes = json.load(reader)
        print("Заметки успешно загружены!")

def show_notes():
    for i in range(len(list_of_notes)):
        print(f'ID: {i} {list_of_notes[i]}')

def edit_note():
    print("Вот список заметок: ")
    show_notes()
    index = int(input("Введите ID заметки которого хотите изменить: "))
    print(f'Изменяется заметка: {list_of_notes[index]}')
    edited_note = []
    title = input("Введите новый заголовок: ")
    body = input("Введите новое тело заметки: ")
    date = datetime.now().strftime('%d-%m-%Y-%H-%M')
    edited_note.append(title)
    edited_note.append(body)
    edited_note.append(date)
    list_of_notes[index] = edited_note
    print("Заметка успешно отредактирован!")

def delete_note(list_of_notes):
    print("Вот список заметок: ")
    show_notes()
    index = int(input("Введите ID заметки которого хотите удалить: "))
    print(f'Заметка - {list_of_notes[index]} удален!')
    del list_of_notes[index]

def sort_by_date():
    sorted_data = sorted(list_of_notes, key=itemgetter(2))
    for i in range(len(sorted_data)):
        print(sorted_data[i])

try:
    load_note()
except:
    print("Файл не найден!")

while True:
    command  = input("Введите команду: ")
    if command == '/add':
        add_note(list_of_notes)
    elif command == "/save":
        save_note()
    elif command == "/show":
        show_notes()
    elif command == "/show_sorted":
        sort_by_date()
    elif command == "/edit":
        edit_note()
    elif command == "/delete":
        delete_note(list_of_notes)
    elif command == "/stop":
        save_note()
        print("Программа завершенa. Спасибо за использование!")
        break
    elif command == "/help":
        print("Список команд:\n"
              "/load - загрузить файл\n"
              "/add - создать новую заметку\n"
              "/save - сохранить заметку в файл\n"
              "/show - показать список заметок\n"
              "/edit - редактировать заметку\n"
              "/delete - удалить\n"
              "/stop - завершить программу\n"
              "/show_sorted - отсортировать по дате")
    else:
        print("Неопознанная команда. Введите /help для помощи.")