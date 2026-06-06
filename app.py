from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import datetime
import requests

app = Flask(__name__)

# Твоя рабочая ссылка CallMeBot
URL = "https://api.callmebot.com/text.php?user=@maksforo&text=TEXT&apikey=8872428"

# Маршрут для подтверждения прав в Яндекс Вебмастере
@app.route('/yandex_d475dbee1f0f102c.html')
def yandex_verification():
    return send_from_directory('static', 'yandex_d475dbee1f0f102c.html')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("username")
    contact = request.form.get("contact")
    bungalow = request.form.get("bungalow") 
    
    # Сохраняем в bookings.txt
    data = f"{datetime.datetime.now()} | {name} | {contact} | {bungalow}\n"
    with open("bookings.txt", "a", encoding="utf-8") as f:
        f.write(data)
        
    # Отправляем красивое уведомление в Телеграм
    try:
        msg = f"Новая бронь!\nИмя: {name}\nКонтакты: {contact}\nДомик: {bungalow}"
        requests.get(URL.replace("TEXT", msg))
    except:
        pass
        
    return redirect(url_for('success'))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)