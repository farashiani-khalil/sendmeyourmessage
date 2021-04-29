from pyrogram import Client, filters


app = Client(
    "my_bot",
    bot_token="1740908550:AAEn1xHJjfJlPZUg2HsEvY1nwTQ5UxcwigY"
)


@app.on_message(filters.private & ~filters.command('start'))
def crypto_get(client, message):
    if str(message.from_user.id) == '123624067':
        masg = message.text
        try:
            masg = masg.split('؟')
            print(masg)
            des_user = masg[1]
            masg1 = masg[0]
            print(des_user)
            print(masg1)
            app.send_message(des_user, masg1)
            app.send_message('123624067', 'پیامت ارسال شد')
        except:
            app.send_message('123624067', 'format is encorrect')
    else:
        user_id = str(message.from_user.id) + '  ' + str(message.from_user.first_name)
        try:
            user_id2 = str(message.from_user.username)
        except:
            user_id2 = """ he/she hasen't username """        
        try:
            app.send_message('123624067', user_id)
            app.send_message('123624067', user_id2)
            message.forward('123624067')
            app.send_message(str(message.from_user.id), "پیامت ارسال شد 🤟 ")
        except:
            app.send_message(str(message.from_user.id), "یه مشکلی پیش اومده :(")

    
@app.on_message(filters.command("start"))
def crypto_get(client, message):
    print(message)
    user_id = str(message.from_user.id)
    app.send_message(user_id, "hi dear!! you are sending message to Khalil, notice that You will remain annonymous")


app.run()
