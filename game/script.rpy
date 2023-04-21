# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define v = Character('Айко', color="#3ba2e7")
define m = Character('Максим Коняев', color="#3ba2e7")
define gay = 0
define a = Character('Закадровый Голос', color="#3ba2e7")
define c = Character('zxcursed', color="#fa3cbb")
image tati = "characters/tati normal.png"
image tati2 = "characters/tati 4.png"
image cursed = "characters/cursed.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    scene image "scenes/ladder.png" with Dissolve(1)
    show tati
    v "Привет!"
    hide tati
    show tati at right
    v " Я все еще жду гонорар. "
    show cursed at left 
    play music "audio/newera.mp3" volume 0.5
    c "всем привет я ZXCURSED я тоже разработчик этой игры."
    c "тише тише"
    c "НА МНЕ ДЖЕТПАК ЭТО ПУТЬ ВВЕРХ ИО"
    hide cursed
    show cursed at center
    m "нам впадлу писать код честно."
    hide cursed

menu:
    "debuug"
    
    "дебаг переменных":
        show tati at center
        v "добро пожаловать в дебаг переменных"
        jump debug

label debug:
    menu:
        "Тест на сколько процентов ты гей, выбирай"
        
        "Я слушаю зхскурседа":
            m "Хорошо! + 1 к общему числу!"
            $ gay = gay + 1  
            jump test

        "Я люблю ебаться в жопу":
            v "Следующий вопрос!"
            jump test

label test: 
    menu:
        "Следующий вопрос"
        
        "Я играю в доту":
            m "Хорошо! + 1 к общему числу!"
            $ gay = gay + 1 
            jump test2

        "я играю с хуем отца":
            v "готово!!"
            jump test2

label test2:
    m " сейчас решится твоя судьба "
    if gay == 0:
        m "ты не гей!"
        pass
    else:
        m "ты пидорс! "
    return

label izhesk:
    scene image "scenes/izhesk.jpg"
    a "после того как вы послали вови грача нахуй, вы попали в ижевск, поздравляем!"
    "лучшая концовка"
    return

label buguruslan:
    scene image "scenes/buguruslan.jpg"
    a "после того как вы послали макса нахуй, вы класть асфальт в бугуруслан, не поздравляем!"
    play music "audio/outro.mp3"
    "худшая концовка"
    return

