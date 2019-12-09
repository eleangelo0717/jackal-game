import db
import logging
import declaration
import re
import utils
import user

def start(bot, update):
        u = user.User(update.message.from_user)
        update.message.reply_text(
                f'''Здравствуйте, {u.user['first_name']}!
этот бот помогает подать заявление через сайт ДАБЧ.
Вы указываете боту диапазон дат, на которые хотите записаться на прием, и данные для заполнения заявления.
Как только на сайте ДАБЧ ( http://www.aba.government.bg/?legal=9 ) открываются указанные вами дни приема, бот попытается отправить ваше заявление.   

🕹 Заполнить заявление: /declaration

Бот также понимает команды:
🕹 Проверить статус заявления: /status
🕹 Посмотреть заполненные данные: /view 
🕹 Удалить завление: /clear
🕹 Покинуть бота, удалить информацию: /stop
🕹 Вывести это сообщение: /start

Если возникнут вопросы по заполнению полей заявления, смотрите страницу подачи заявления на сайте ДАБЧ:
http://www.aba.government.bg/?legal=9

Будьте внимательны при заполнении данных.
Если ошиблись в заполнении заявления, удалите его: /clear
После этого сможете заполнить его заново.
'''
        )


def status(bot, update):
        u = user.User(update.message.from_user)
        if u.status == '' or u.status == 'stop':
                logging.info(u.status, u.step)
                if u.step == '':
                        update.message.reply_text(
                                f'''⚠️ Вы не заполнили данные своего заявления.

🕹 Заполнить заявление: /declaration
'''
                        )
                else:
                        update.message.reply_text(
                                f'''⚠️ Вы не закончили заполнять данные своего заявления.
                                
🕹 Заполнить заявление: /declaration'''
                        )
                return 
        
        if status == 'ready':
                update.message.reply_text(
                        f'''⏯ Ожидайте.
Ваше заявление готово к отправке.
Как только появятся подходящие даты, бот попытается его отправить.

🕹 Посмотреть заполненные данные: /view '''
                )
                return 

        if status == 'success':
                update.message.reply_text(
                        f'''✅ Ваше заявление успешно отправлено:

⌚️ {(u.info or {}).get('sended')}
✉️ {' '.join((u.info or {}).get('messages'))}
'''
                )
                return 

        if status == 'fail':
                update.message.reply_text(
                        f'''❌ Ваше заявление было отклонено:
⌚️{(u.info or {}).get('sended')}
✉️{' '.join((u.info or {}).get('messages'))}

🕹 Посмотреть заполненные данные: /view '''
                )
                return 


def stop(bot, update):
        _ = user.User(update.message.from_user)
        db.saveDeclaration(update.message.from_user, {}, None, 'stop')
        update.message.reply_text(f'Ваши данные удалены')


def clear(bot, update):
        _ = user.User(update.message.from_user)
        db.saveDeclaration(update.message.from_user, {}, None, '')
        update.message.reply_text(f'''Ваша заявка удалена.
Заполнить новую заявку: /declaration''')


def view(bot, update):
        u = user.User(update.message.from_user)
        txt = []
        dt = (u.request or {}).get('dt',{})
        txt.append(f"Даты: {dt.get('from','')} - {dt.get('to','')}")
        doc = (u.request or {}).get('doc',{})
        for key in doc:
                field = declaration.getField(key)
                txt.append(f'''{field_display(field)}:
{doc[key]}
🕹 Изменить: /edit_{key}
''')
        txt.append('''
🕹 Удалить завление: /clear''')
        result = '\n'.join(txt)
        update.message.reply_text(result)


def edit(bot, update):
        u = user.User(update.message.from_user)
        u.step = update.message.text[6:]
        request, _ = declaration.checkDeclaration(u)
        _, item = declaration.getRequestItem(u.step, request)
        if item is None:
                return
        u = db.saveDeclaration(update.message.from_user, request, u.step)
        step_request(bot, update, user, request, u['step'])


def field_display(field):
        if field is None:
                return ''
        return field.get("text") or field.get("key")


def step_request(bot, update, user, request, step):
        if step == '':
                user = db.saveDeclaration(update.message.from_user, request, step, 'ready')
                status(bot, update)
        else:
                user = db.saveDeclaration(update.message.from_user, request, step)
                field = declaration.getField(step)
                field_name = field_display(field)
                if field.get('required', False):
                        field_name = field_name + ' *'
                values = field.get('values')
                txt = []
                
                if values is None:
                        txt.append(f'Введите "{field_name}"')
                else:
                        txt.append(f'Введите код для "{field_name}":')
                        if field.get('multiple', False):
                                txt.append(f'Можно ввести несколько значений через запятую.')
                        for val in values:
                                txt.append(f'{val.get("key")} - {val.get("text")}')
                text = '\n'.join(txt)
                update.message.reply_text(text)


       
def next_step(bot, update, user):
        request, step = declaration.checkDeclaration(user)
        step_request(bot, update, user, request, step)


def check_declaration(bot, update):
        user = db.saveUser(update.message.from_user)
        update.message.reply_text('''РАЗРЕШЕНИТЕ ЗНАЦИ ПРИ ПОПЪЛВАНЕ СА БУКВИ НА КИРИЛИЦА И ЦИФРИ. МОЛЯ НЕ ИЗПОЛЗВАЙТЕ ""
Всички полета със * са задължителни.
Если не желаете заполнять поле, введите знак "-" (минус)
''')
        next_step(bot, update, user)
        


def text_input(bot, update):
        user = db.saveUser(update.message.from_user)
        request, step = declaration.checkDeclaration(user)
        text = update.message.text.strip()
        if text == '-':
                text = ""
        if step is not None:
                if step in [key for key in declaration.docFields]:
                        field = declaration.docFields.get(step) or {}
                        if text == '' and field.get('required', False):
                                update.message.reply_text(f'''Поле обязательно для заполнения.''')
                        else:
                                if field.get('multiple', False):
                                        request['doc'][step] = re.split(r'\W+', text)
                                else:
                                        request['doc'][step] = text
                                update.message.reply_text(f'''_Сохранено "{step}": {request['doc'][step]}_''',
                                parse_mode='Markdown')
                else:
                        dt = request['dt']

                        text, result = utils.checkDate(text)
                        if result is not None:
                                update.message.reply_text(result)
                                next_step(bot, update, user)
                                return

                        if step.get('key') == 'date_from':
                                dt['from'] = text
                        if step.get('key') == 'date_to':
                                dt['to'] = text
                        request['dt'] = dt
                _, step = declaration.checkDeclaration(user)
                user = db.saveDeclaration(update.message.from_user, request, step)
                next_step(bot, update, user)



