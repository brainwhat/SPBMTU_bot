import telebot
import config
import random
import os
import sys

from telebot import types

def printPhoto(image_folder,message):
    # Получаем путь к папке скрипта
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Полный путь к папке с изображениями
    folder_path = os.path.join(script_dir, image_folder)

    # Получаем список файлов в папке
    image_files = os.listdir(folder_path)
    media = []

    for image_file in image_files:
        # Полный путь к файлу
        image_path = os.path.join(folder_path, image_file)
        # Проверяем, является ли файл изображением PNG
        if os.path.isfile(image_path) and image_file.lower().endswith('.png'):
            # Открываем изображение для бинарного чтения
            with open(image_path, 'rb') as image:
                # Отправляем изображение в текущий чат
                media.append(telebot.types.InputMediaPhoto(image.read()))

    if media:
        # Отправляем группу медиа-файлов одним сообщением
        bot.send_media_group(message.chat.id, media)

# Отсылаем к файлу config.py
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    # Клавиатура под полем ввода. Бот обрабатывает только эти запросы
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Как поступить?")
    item2 = types.KeyboardButton("Зачем поступать?")
    item3 = types.KeyboardButton("Общежития")
    item4 = types.KeyboardButton("Учебные аудитории")
    item5 = types.KeyboardButton("Практические занятия")
    item6 = types.KeyboardButton("Корабельная практика")
    item7 = types.KeyboardButton("Учебные сборы")
    item8 = types.KeyboardButton("Войсковая стажировка")
    item9 = types.KeyboardButton("Спорт")
    item10 = types.KeyboardButton("Выпускники")
    
    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)

    # Приветственное сообщение
    bot.send_message(message.chat.id, "Здравствуйте!\n<b>{1.first_name}</b> предлагает вам ознакомиться с возможностями, представляемыми поступающим".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.chat.type == "private":
        if message.text == "Как поступить?":
            bot.send_message(message.chat.id, 'Для поступления в ВУЦ при СПбГМТУ необходимо предоставить стандартный набор документов на техническую специальность (смотри правила приёма в СПбГМТУ на сайте www.smtu.ru: Абитуриенту – Поступление в ВУЦ) в число которых входят обязательные документы: \n  •Аттестат о среднем (полном) общем образовании.\n  •Результаты о сдаче ЕГЭ: по русскому языку, математике и физике – (база данных ЕГЭ России).\nКроме этого, граждане изъявившие желание обучаться в ВУЦ при СПбГМТУ должны своевременно пройти предварительный отбор в военном комиссариате по месту своего жительства (смотрите положение о проведении предварительного отбора граждан, изъявивших желание пройти военную подготовку в ВУЦ при СПбГМТУ на сайте: www.smtu.ru, пункт: Порядок проведения отбора граждан для прохождения военной подготовки в ВУЦ при СПбГМТУ).\nПодробная информация на сайте в контакте: vk.com/uvc_korabelka ')
        elif message.text == "Зачем поступать?":
            bot.send_message(message.chat.id, '1. Получение бесплатного высшего образования по выбранной специальности в одной из ведущей образовательной организации высшего образования страны - СПбГМТУ.\n2. Поступление в СПбГМТУ на целевую подготовку за счёт средств федерального бюджета проводится по отдельному конкурсу .\n3. Обеспечение комфортабельным общежитием иногородних студентов, проходящих военную подготовку в ВУЦ при СПбГМТУ.\n4. Получение ежемесячной дополнительной стипендии (базовая гражданская стипендия выплачивается по результатам сдачи промежуточной аттестации) в размере 2805 руб. –  первый год обучения, 5610 - 7480 руб. – второй и последующие годы обучения, а также 5000 руб. для приобретения формы одежды (единовременно).\n5. Одновременное получение образования по военной и гражданской специальностям, получение государственного диплома о высшем образовании.\n6. Гарантированное трудоустройство (прохождение военной службы) по специальности на кораблях или в воинских частях ВМФ, а также в других видах и родах ВС РФ.\n7. Получение первого офицерского звания лейтенанта и выплат, установленных при заключении первого контракта о прохождении военной службы.\n8. Предоставление по окончании университета отпуска и бесплатного проезда выпускнику и членам его семьи к месту прохождения военной службы.')
            
        elif message.text == "Общежития":
            printPhoto('media/dorms',message)

        elif message.text == "Учебные аудитории":
            printPhoto('media/classes',message)
            
        elif message.text == "Практические занятия":
            printPhoto('media/practice', message)

        elif message.text == "Корабельная практика":
            printPhoto('media/ship_practice', message)

        elif message.text == "Учебные сборы":
            printPhoto('media/field', message)

        elif message.text == "Войсковая стажировка":
            printPhoto('media/army', message)

        elif message.text == "Спорт":
            printPhoto('media/sport', message)

        elif message.text == "Выпускники":
            printPhoto('media/dates', message)

#Run
bot.polling(non_stop=True)
