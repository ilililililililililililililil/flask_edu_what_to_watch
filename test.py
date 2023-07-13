def score(cf: float, *scores: list):
    for i in scores:
        print(cf * i)

cf = 0.2
scores = [4, 5, 4]

score(cf, scores)



# Какой вариант изменений в этом коде НЕ исправит возникающей синтаксической ошибки?

# def score(cf, *scores):
#     for i in scores:
#         print(cf * i)

# cf = 0.2
# scores = [4, 5, 4]

# score(cf, scores)
# Обязательный ответ
# Замена def score(cf, *scores): на def score(cf, scores):
# Замена def score(cf, *scores): на def score(cf: float, scores: list):
# Замена def score(cf, *scores): на def score(cf: float, *scores: list):
# Замена score(cf, scores) на score(cf, *scores)
# Использование цикла for для обращения к каждому элементу списка scores