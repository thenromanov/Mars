from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotionImage():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                         integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                         crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.png"
                             alt="изображение не нашлось"
                             width="200"
                             height="200">
                        <figcaption>Вот она какая, красная планета</figcaption>
                        <div class="alert alert-dark" role="alert">Человечество вырастает из детства.</div>
                        <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
                        <div class="alert alert-dark" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
                        <div class="alert alert-danger" role="alert">Присоединяйся!</div>
                    </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        return '''<!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="/static/css/style.css">
                            <title>Отбор астронавтов</title>
                        </head>
                        <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="participant_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="education">Какое у Вас образование?</label>
                                        <select class="form-control" id="education" name="education">
                                            <option>Начальное</option>
                                            <option>Среднее</option>
                                            <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="profession">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="engineer" value="engineer">
                                            <label class="form-check-label" for="engineer">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="pilot">
                                            <label class="form-check-label" for="pilot">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="builder" value="builder">
                                            <label class="form-check-label" for="builder">Строитель</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="exobiologist" value="exobiologist">
                                            <label class="form-check-label" for="exobiologist">Экзобилог</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="doctor" value="doctor">
                                            <label class="form-check-label" for="doctor">Врач</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="climatologist" value="climatologist">
                                            <label class="form-check-label" for="climatologist">Климатолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="astrogeologist" value="astrogeologist">
                                            <label class="form-check-label" for="astrogeologist">Астрогеолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="glaciologist" value="glaciologist">
                                            <label class="form-check-label" for="glaciologist">Гляциолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="checkbox" name="profession" id="meteorologist" value="meteorologist">
                                            <label class="form-check-label" for="meteorologist">Метеоролог</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">Мужской</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">Женский</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы готовы принять участие в миссии?</label>
                                        <textarea class="form-control" id=motivation" rows="3" name="motivation"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                        </body>
                    </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['motivation'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planetName>')
def planeChoice(planetName):
    return '''<!DOCTYPE html>
              <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                </head>
                <body>
                    <h1><b>Моё предложение: {}</b></h1>
                    <h2 class="p-3 mb-2 bg-primary text-white">Эта планета близка к Земле;</h2>
                    <h2 class="p-3 mb-2 bg-success text-white">На ней много необходимых ресурсов;</h2>
                    <h2 class="p-3 mb-2 bg-danger text-white">На ней есть вода и атмосфера</h2>
                    <h2 class="p-3 mb-2 bg-warning text-dark">На ней есть небольшое магнитное поле;</h2>
                    <h2 class="p-3 mb-2 bg-info text-white">Наконец, она просто красива!</h2>
                </body>
              </html>
           '''.format(planetName)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return '''<!DOCTYPE html>
              <html>
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                    crossorigin="anonymous">
                    <title>Результаты</title>
                </head>
                <body>
                    <h1><b>Результаты отбора</b></h1>
                    <h2>Претендента на участие в миссии {}:</h2>
                    <h2 class="p-3 mb-2 bg-success text-white">Поздравляем! Ваш рейтинг после {} этапа отбора</h2>
                    <h2 class="p-3 mb-2 bg-info text-white">составляет {}!</h2>
                    <h2 class="p-3 mb-2 bg-warning text-dark">Желаем удачи!</h2>
                </body>
              </html>'''.format(nickname, level, rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
