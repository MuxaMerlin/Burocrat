import random

greetings = ["'Чем я могу Вам помочь?'", "'...'", "'Следующий'"]
MOODS = ('плохом', 'нормальном', 'хорошем')
RANKS = ('низкого', 'среднего', 'высокого')


class Bureaucrat:
    """Государственный служащий, работающий в учереждении"""

    def __init__(self):
        self.rank = random.choice(RANKS)
        self.mood = random.choice(MOODS)

    def greet(self):
        """Случайное приветсвие государственного служащего"""

        print(random.choice(greetings))
        print('Бюрократ {} ранга.'.format(Bureaucrat.rank))
        print('Бюрократ находится в {} настроении'.format(Bureaucrat.mood))


bureaucrat = Bureaucrat()
bureaucrat.greet()