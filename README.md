# smsSender

## 1. Создание объекта
#####   Создаем объект, атрибутами которого являются логин и пароль(пароль потом хэшируется).
        `sms = SMS(login, psw)`
        
## 2. Метод sendSMS
#####   У метода есть два аргумента: телефон в формате 7xxxxxxxxxx(если введете что-нибудь другое то смс не отправиться, формат телефона проверяется) и сообщение.
        `sms.sendSMS(phone, message)`
        
#####   У этого метода также есть третий аргумент sender - это имя отправителя, но для того чтобы его исспользовать, имя нужно зарегистрировать в базе данных. 
        `sms.sendSMS(phone, message, sender)`
        
## 3. Метод balance.
##### Позволяет проверить баланс. 
        `sms.balance()`