# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define v = Character('вова грач', color="#3ba2e7")
# define m = Character('максим коняев', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show image "characters/tati.png"

    v "я пидарас"

    return
