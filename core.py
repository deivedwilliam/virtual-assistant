import datetime


class SystemCore:

    def __init__(self):
        pass

    @staticmethod
    def get_time():

        now = datetime.datetime.now()
        answer = 'São {} horas, {} minutos e {} segundos'.format(now.hour, now.minute, now.second)

        return answer