import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# جلب توكن البوت بأمان من متغيرات البيئة
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# قائمة الردود الجاهزة
AUTO_RESPONSES = {
    "سماعه": """لطلب السماعه 📦

ادخل هنا هتلاقي ريڤيوهات وتجارب ناس قبلك في التعامل معانا https://t.me/m0ster_1

هتبعت بياناتك هنا للمسؤول عن الشحن ⬇️
https://wa.me/qr/65P6M34NP5WOE1
أو
https://wa.me/qr/PGJQAHQXFEZBK1

1-اسمك 
2-عنوانك
3-المنتج الي عايزه بالتفصيل


⚠️ملحوظه 

روابط التواصل في هذه الرساله هي الوحيده للحجز من خلالنا يرجي الضغط عليها و ارسال بياناتك🔴""",

    "دعم": """للدعم 
https://wa.me/qr/PGJQAHQXFEZBK1

أو 

https://wa.me/qr/65P6M34NP5WOE1""",

    "جروب": """الجروب الاول 
https://chat.whatsapp.com/CevqfOpt3zSI2BYZiabwdP?s=cl&p=a&ilr=2&amv=1
الجروب التاني 
https://chat.whatsapp.com/D0ipZDyhFy67wKWCJP4AvG
الجروب التالت 
https://chat.whatsapp.com/Hxb4sGIcpV96k9pXhKd2ns
الجروب الرابع 
https://chat.whatsapp.com/BQ22y49cfqKHCe0FAQA4E6

قناه الواتس ✅
https://whatsapp.com/channel/0029VbAGNa81NCrTZB2fka29
قناه التليجرام
https://t.me/m0ster_1""",
}


# الرد على أمر /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """مرحبا بك يا بطل!♥️

قناه التليجرام فيها كل الروابط📊
https://t.me/m0ster_1


لطلب سماعه اكتب كلمه(سماعه)📦

للدعم الفني اكتب كلمه (دعم)👨🔧

للحصول علي الجروبات اكتب كلمه (جروب)👥


ل للمحادثه المباشره واتساب ♻️
https://wa.me/qr/65P6M34NP5WOE1"""
    await update.message.reply_text(welcome_text)


# معالجة الرسائل الواردة والرد عليها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()

    reply_found = False
    for keyword, response in AUTO_RESPONSES.items():
        if keyword in user_text:
            await update.message.reply_text(response)
            reply_found = True
            break

    if not reply_found:
        default_reply = "شكراً لتواصلك! تم استلام رسالتك وسنقوم بالرد عليك، إذا كنت تريد رداً سريعاً برجاء التواصل علي https://wa.me/qr/PGJQAHQXFEZBK1"
        await update.message.reply_text(default_reply)


def main():
    if not TOKEN:
        print("خطأ: لم يتم ضبط قيمة TELEGRAM_BOT_TOKEN في متغيرات البيئة!")
        return

    # إنشاء تطبيق البوت
    app = Application.builder().token(TOKEN).build()

    # إضافة الأوامر والرسائل
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    # تشغيل البوت واستقبال الرسائل
    print("البوت يعمل الآن...")
    app.run_polling()


if __name__ == "__main__":
    main()