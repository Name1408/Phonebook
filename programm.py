# Создать телефонный справочник с возможностью импорта и экспорта данных в формате 
# .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

 

def show_contact():
    with open("C:\\Users\\PETR\\Desktop\\Phonebook\\fork_Phonebook\\contact.txt", 'r', encoding="utf-8") as file:
        for line in file:
           print(line)
        
 
def save_contact():
    with open("C:\\Users\\PETR\\Desktop\\Phonebook\\fork_Phonebook\\contact.txt",'a', encoding="utf-8") as file:
        info_line = input("Введите ФИО и номер: ")
        file.write(info_line.upper() + '\n')

def search_contact():
    with open("C:\\Users\\PETR\\Desktop\\Phonebook\\fork_Phonebook\\contact.txt",'r', encoding="utf-8") as file:
        search_info = input("Введите данные для поиска: ")
        for line in file:
            if search_info.upper() in line:
                print(line)
       
   
def change_contact():
    old_name = input('Кого переименовать?: ')
    new_name = input('Введите новое имя: ')
    with open("C:\\Users\\PETR\\Desktop\\Phonebook\\fork_Phonebook\\contact.txt",'r+', encoding="utf-8") as file:
        contacts = file.read()
        for contact in contacts:
            if old_name.upper() != contact:
               file.write(contact)
            else:
                file.write(new_name.upper() + "\n")

def delete_contact():
    delete_info = input('Введите кого удалить: ')
    with open("C:\\Users\\PETR\\Desktop\\Phonebook\\fork_Phonebook\\contact.txt",'r+', encoding="utf-8") as file:
        contacts = file.read()
        for line in contacts:
            if delete_info.upper() != line:
                file.write(line)

   
command = '0'
while command != '6':
    command  = input('\n\n1 - Вывод данных\n2 - Сохранить данныe\n3 - Найти запись\n4 - Изменить данные \n5 - Удалить данные \n6 - Закрыть программу\n Введите нужную команду: ')
    match command:
        case '1':
            show_contact()
        case '2':
            save_contact()
        case '3':
            search_contact()
        case '4':
            change_contact()
        case '5':
             delete_contact()
        case '6':
            break
