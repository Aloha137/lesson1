def get_answer(question):
    return {
        'привет': 'И тебе привет!',
        'как дела': 'Лучше всех',
        'пока': 'увидимся',
    }[question.lower()]

print(get_answer('ПриВеТ'))

