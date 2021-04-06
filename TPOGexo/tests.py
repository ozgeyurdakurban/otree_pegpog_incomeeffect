from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot


class PlayerBot(Bot):

    def play_round(self):

        yield (Introduction)

        if self.player.id_in_group == 1:
            yield (Send, {"sent_amount": 4})

        else:
            yield (SendBack, {'sent_back_amount': 8})

        yield (Results)
