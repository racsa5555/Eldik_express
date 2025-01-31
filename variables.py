PRICE_WEIGHT_KEMIN = 3.1
ADMIN_PASSWORD = '1'

LINK_WHATSAPP = 'https://wa.me/79261068788'


ADRESS_KEMIN = '刘影(JKA-{})\n13845320678{}: \n广东省佛山市南海区里水镇岗美村老船长创意园米莎288库房({}){} \n 刘影'
PINDUODUO = 'https://youtube.com/shorts/eW9HNJ_OiMM?si=k4Pvx9B9JJP_rM4F'
TAOBAO = 'https://youtube.com/shorts/JHp78xqBDwg?si=x5HZNp56I6CRQT0N'
ONE_AND_SIX = 'https://youtube.com/shorts/KHVRE2nC8Fk?si=Z_JFZzAJk0aAr0GC' #1688
POIZON = 'https://youtube.com/shorts/PL473nyMvsM?si=2PH_SX1VhrurwvoI'

def send_adress(id,phone_number,lang, ADRESS_KEMIN):
    if lang == 'RU':
        return ADRESS_KEMIN.format(id[4:],'Полный адрес',id,phone_number)
    else:
        return ADRESS_KEMIN.format(id[4:],'Толук адрес',id,phone_number)
    

def send_profile(kwargs):
    if kwargs['language'] == 'RU':
        text = '📃Ваш профиль📃\n🪪 Персональный id: {}\n👤 Имя: {}\n👤 Фамилия: {}\n📞 Номер: {}\n🌍 Геопозиция: {}'
    if kwargs['language'] == 'KG':
        text = '📃Сиздин профилиниз📃\n🪪 Жеке id: {}\n👤 Аты: {}\n👤 Фамилия: {}\n📞 Номер: {}\n🌍 Турган жери: {}'

    if kwargs['language'] == 'RU':
        return text.format(str(kwargs['id']), kwargs['name'], kwargs['full_name'], kwargs['phone_number'], kwargs['city'])
    elif kwargs['language'] == 'KG':
        return text.format(str(kwargs['id']), kwargs['name'], kwargs['full_name'], kwargs['phone_number'], kwargs['city'])

def cancel_sender(lang):
    if lang == 'RU':
        return f'Вы отменили последнее действие'
    else:
        return f'Акыркы аракетиңизди артка кайтардыңыз'

zapret_text = (
    "❌ Запрещено к перевозке ❌\n"
    "• Живые животные\n"
    "• Военные товары\n"
    "• Взрывоопасные вещества и легковоспламеняющиеся\n"
    "• Наркотические вещества\n\n"
    "⚠️ Не рекомендуется к перевозке:\n"
    "Предметы из хрупких материалов:\n"
    "• Хрусталь\n"
    "• Керамика\n"
    "• Фарфор\n"
    "• Гипс\n"
    "• Зеркала\n"
    "• Предметы с хрупкими вставками\n"
    "• Изделия из стекла\n"
    "• Мобильные телефоны, мониторы компьютеров, ноутбуки.\n"
    "(Эти изделия дорогие и легко повреждаются.\n\n"
    "МЫ НЕ МОЖЕМ НЕСТИ ОТВЕТСТВЕННОСТЬ ЗА ИХ ЦЕЛОСТНОСТЬ!!!"
)

support_text = (
    "Если у вас есть вопросы,\n"
    "жалобы и предложения\n"
    "свяжитесь с нами\n\n"
    "Наш WhatsApp\n"
    "📩📩 wa.me/996702863610 📩📩\n\n"
    "Наш Instagram:\n"
    "https://www.instagram.com/kemin_eldik_cargo?igsh=NHVsNjAwaDBwbWFl\n\n"
    "❌☎️ ЗВОНКИ НЕ ПРИНИМАЮТСЯ.\n"
    "ТОЛЬКО WHATSAPP"
)

dop_text = (
    "После того как заполните адрес, обязательно отправьте его скрин нашему "
    "менеджеру на проверку, нажав на эту ссылку⤵️\n\n"
    "wa.me/996702863610\n\n"
    "*Без проверки адреса не рекомендуем оформлять заказы"
)