# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define v = Character('Вова Грач', color="#3ba2e7")
define m = Character('Максим Коняев', color="#3ba2e7")
define a = Character('Закадровый Голос', color="#3ba2e7")
define c = Character('zxcursed', color="#fa3cbb")
image tati = "characters/tati.png"
image tati2 = "characters/tati 4.png"
image cursed = "characters/cursed.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    scene image "scenes/scene.jpg"
    show tati
    v "Привет! Это техно-демо."
    hide tati
    show tati2
    v "Мы учимся работать с движком, поэтому даже в этой маленькой демке будут косяки."
    v "Мы во всю готовы работать с игрой, но наши сценаристы ничего не делают!"
    hide tati2
    show tati at right
    v " а еще нам не несут гонорар."
    show cursed at left 
    play music "audio/newera.mp3" volume 0.5
    c "всем привет я ZXCURSED я тоже разработчик этой игры."
    c "тише тише"
    c "НА МНЕ ДЖЕТПАК ЭТО ПУТЬ ВВЕРХ ИО"
    hide cursed
    show cursed at center
    m "нам впадлу писать код честно."
    m "кто пидор епта"
    hide tati
    hide cursed
   
menu:
    "КТО ПИДОР"
    
    "вова пидор":
        show cursed at center
        m "ТУДА ЕГО НАХУЙ"
        jump izhesk

    "макс пидор":
        show tati at center
        v "ТУДА ЕГО НАХУЙ"
        jump buguruslan

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

