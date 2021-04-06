import itertools
import random

from otree.api import *


doc = """
This is a Pension Game first introduced by Hammond(1975). 
The Pension Game is a version of the standard investment game in which the amount sent by player 1 is tripled.
It was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'TPEGendoL'
    players_per_group = None
    num_rounds = 10
    instructions_template = 'TPEGendoL/instructions.html'
    table_template = 'TPEGendoL/table.html'
    # Initial amount allocated to players
    endowment_Decider = 9
    endowment_Receiver =  1
    multiplier = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P2""",
    )
    expect_2 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P2""",
    )
    sent_3 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P3""",
    )
    expect_3 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P2""",
    )
    sent_4 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P4""",
    )
    expect_4 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P2""",
    )
    sent_5 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P5""",
    )
    expect_5 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P2""",
    )
    sent_6 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P6""",
    )
    expect_6 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P2""",
    )
    sent_7 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P7""",
    )
    expect_7 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P2""",
    )
    sent_8 = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P8""",
    )


class Player(BasePlayer):
    color = models.StringField()
    WTP = models.CurrencyField(initial=0)
    overall_payoff = models.CurrencyField(initial=0)
    session_random_number = models.IntegerField(initial=10)
    sequence = models.IntegerField(initial=0)
    gpa = models.StringField(
        choices=[
            '0,00 - 0,50',
            '0,50 - 1,00',
            '1,00 - 1,50',
            '1,50 - 2,00',
            '2,00 - 2,50',
            '2,50 - 3,00',
            '3,00 - 3,50',
            '3,50 - 4,00',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Akademik Not Ortalamanız",
    )
    accept = models.StringField(
        choices=['Kabul ediyorum.', 'Kabul etmiyorum'],
        widget=widgets.RadioSelectHorizontal,
        label="Gönüllü olarak katıldığım bu deneyde tarafımdan herhangi bir kişisel bilgi istenilmemiştir.",
    )
    dep = models.StringField(
        choices=[
            'STEM (Bilim, Teknoloji, Mühendislik ve Matematik)',
            'HASS (Beşeri, Sanat ve Sosyal Bilimler)',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Alan",
    )
    age = models.StringField(
        choices=['≤24', '25-29', '30-39', '40-54', '≥55'],
        widget=widgets.RadioSelectHorizontal,
        label="Yaş",
    )
    gen = models.StringField(
        choices=['Kadın', 'Erkek'], widget=widgets.RadioSelectHorizontal, label="Cinsiyet"
    )
    edu = models.StringField(
        choices=['Lisans', 'Yüksek Lisans', 'Doktora'],
        widget=widgets.RadioSelectHorizontal,
        label="Eğitim",
    )
    inc = models.StringField(
        choices=['500-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000+'],
        widget=widgets.RadioSelectHorizontal,
        label="Aylık Ortalama Gelir",
    )
    h_inc = models.StringField(
        choices=['500-1000', '1000-2000', '2000-3000', '3000-4000', '4000-5000', '5000+'],
        widget=widgets.RadioSelectHorizontal,
        label="Aylık Ortalama Hanehalkı Geliri",
    )
    env_cons_2 = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Kaynaklarımızın daha uzun süre dayanması için herkes ürün tüketimini artırmayı bırakmalıdır.",
    )
    env_cons_3 = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Bu ülke konut geliştirme konusunda(tarım arazileri üzerinde yeni alışveriş merkezi inşaatı, yeni alt bölümler vb.) daha fazla kısıtlamaya ihtiyaç duymaktadır.",
    )
    env_cons_5 = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Aşırı kirlilik üreten şirketlere yönelik tüketici boykot programlarına başladım/katıldım.",
    )
    env_cons_6 = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Kimse bakmazsa çöp dökerim.",
    )
    env_cons_7 = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Bugün çevresel faaliyetlere katılımım, gelecek nesiller için çevrenin korunmasına yardımcı olacaktır.",
    )
    env_cons_9 = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Kirliliğin bitki ve hayvan yaşamına yol açtığı zararı düşündüğümde kızıyorum.",
    )
    investment_options_1 = models.StringField(
        choices=[
            '%10 olasılıkla 8₺ ve %90 olasılıkla 6,4₺',
            '%10 olasılıkla 15,4₺ ve %90 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_2 = models.StringField(
        choices=[
            '%20 olasılıkla 8₺ ve %80 olasılıkla 6,4₺',
            '%20 olasılıkla 15,4₺ ve %80 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_3 = models.StringField(
        choices=[
            '%30 olasılıkla 8₺ ve %70 olasılıkla 6,4₺',
            '%30 olasılıkla 15,4₺ ve %70 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_4 = models.StringField(
        choices=[
            '%40 olasılıkla 8₺ ve %60 olasılıkla 6,4₺',
            '%40 olasılıkla 15,4₺ ve %60 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_5 = models.StringField(
        choices=[
            '%50 olasılıkla 8₺ ve %50 olasılıkla 6,4₺',
            '%50 olasılıkla 15,4₺ ve %50 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_6 = models.StringField(
        choices=[
            '%60 olasılıkla 8₺ ve %40 olasılıkla 6,4₺',
            '%60 olasılıkla 15,4₺ ve %40 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_7 = models.StringField(
        choices=[
            '%70 olasılıkla 8₺ ve %30 olasılıkla 6,4₺',
            '%70 olasılıkla 15,4₺ ve %30 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_8 = models.StringField(
        choices=[
            '%80 olasılıkla 8₺ ve %20 olasılıkla 6,4₺',
            '%80 olasılıkla 15,4₺ ve %20 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_9 = models.StringField(
        choices=[
            '%90 olasılıkla 8₺ ve %10 olasılıkla 6,4₺',
            '%90 olasılıkla 15,4₺ ve %10 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    investment_options_10 = models.StringField(
        choices=[
            '%100 olasılıkla 8₺ ve %0 olasılıkla 6,4₺',
            '%100 olasılıkla 15,4₺ ve %0 olasılıkla 0,4₺',
        ],
        widget=widgets.RadioSelectHorizontal,
        label=" ",
    )
    fate = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="Kadere inanıyorum ve herşey tamamen özgür irade değil.",
    )
    believe = models.StringField(
        choices=[
            'Kesinlikle katılmıyorum',
            'Biraz katılmıyorum',
            'Ne katılıyorum, ne de katılmıyorum',
            'Biraz katılıyorum',
            'Kesinlikle katılıyorum',
        ],
        widget=widgets.RadioSelectHorizontal,
        label="İbadethanelerdeki hizmetlere/törenlere katılmak dışında yalnızken dua etmiyorum.",
    )


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        colors = itertools.cycle(['MAVİ', 'KIRMIZI'])
        for p in subsession.get_players():
            p.color = next(colors)
    else:
        for p in subsession.get_players():
            p.color = p.in_round(subsession.round_number - 1).color
    subsession.group_randomly()


def assign_sequence(subsession: Subsession):
    blue_players = [p for p in subsession.get_players() if p.color == 'MAVİ']
    blue_players.sort(key=lambda x: x.WTP, reverse=True)
    red_players = [p for p in subsession.get_players() if p.color == 'KIRMIZI']
    red_players.sort(key=lambda x: x.WTP, reverse=True)
    rand_num = random.randint(0, 10)
    if blue_players[0].WTP == red_players[0].WTP:
        pl = random.choice([blue_players[0], red_players[0]])
        if pl.color == 'MAVİ':
            pl = blue_players.pop(0)
        else:
            pl = red_players.pop(0)
    elif blue_players[0].WTP > red_players[0].WTP:
        pl = blue_players.pop(0)
    else:
        pl = red_players.pop(0)
    pl.sequence = 8
    pl.session_random_number = rand_num
    print("player:{0} set to sequence 8".format(pl.participant.id_in_session))
    for index in range(7, 1, -1):  # self.session.config['num_demo_participants']
        pl.session_random_number = rand_num
        print("searching for player:{0} color :{1}".format(pl.participant.id_in_session, pl.color))
        print("WTP is : {}, random number is : {}".format(pl.WTP, rand_num))
        if pl.WTP >= rand_num:
            print("player:{} won".format(pl.participant.id_in_session))
            if pl.color == 'KIRMIZI':
                if len(red_players) > 0:
                    next_pl = red_players.pop(0)
                else:
                    next_pl = blue_players.pop(-1)
            elif pl.color == 'MAVİ':
                if len(blue_players) > 0:
                    next_pl = blue_players.pop(0)
                else:
                    next_pl = red_players.pop(-1)
        else:
            print("player:{} lost".format(pl.participant.id_in_session))
            if pl.color == 'KIRMIZI':
                if len(blue_players) > 0:
                    next_pl = blue_players.pop(0)
                else:
                    next_pl = red_players.pop(-1)
            elif pl.color == 'MAVİ':
                if len(red_players) > 0:
                    next_pl = red_players.pop(0)
                else:
                    next_pl = blue_players.pop(-1)
        print("next player:{0} color :{1}".format(next_pl.participant.id_in_session, next_pl.color))
        next_pl.sequence = index
        pl.session_random_number = rand_num
        print("player:{0} set to sequence {1}".format(next_pl.participant.id_in_session, index))
        pl = next_pl
        pl.session_random_number = rand_num
    for pl in blue_players + red_players:
        pl.sequence = 1
        pl.session_random_number = rand_num
        print("player:{0} set to sequence {1}".format(pl.participant.id_in_session, pl.sequence))


def set_payoffs(group: Group):
    for pl in group.get_players():
        if pl.sequence == 1:
            pl.payoff = 2 * (Constants.endowment_Receiver + group.sent_2)
        elif pl.sequence == 2:
            pl.payoff = (Constants.endowment_Decider - group.sent_2) * (
                Constants.endowment_Receiver + group.sent_3
            )
        elif pl.sequence == 3:
            pl.payoff = (Constants.endowment_Decider - group.sent_3) * (
                Constants.endowment_Receiver + group.sent_4
            )
        elif pl.sequence == 4:
            pl.payoff = (Constants.endowment_Decider - group.sent_4) * (
                Constants.endowment_Receiver + group.sent_5
            )
        elif pl.sequence == 5:
            pl.payoff = (Constants.endowment_Decider - group.sent_5) * (
                Constants.endowment_Receiver + group.sent_6
            )
        elif pl.sequence == 6:
            pl.payoff = (Constants.endowment_Decider - group.sent_6) * (
                Constants.endowment_Receiver + group.sent_7
            )
        elif pl.sequence == 7:
            pl.payoff = (Constants.endowment_Decider - group.sent_7) * (
                Constants.endowment_Receiver + group.sent_8
            )
        elif pl.sequence == 8:
            pl.payoff = (
                (Constants.endowment_Decider - group.sent_8)
                * (
                    (Constants.endowment_Receiver + group.sent_2)
                    + (Constants.endowment_Receiver + group.sent_3)
                    + (Constants.endowment_Receiver + group.sent_4)
                    + (Constants.endowment_Receiver + group.sent_5)
                    + (Constants.endowment_Receiver + group.sent_6)
                    + (Constants.endowment_Receiver + group.sent_7)
                    + (Constants.endowment_Receiver + group.sent_8)
                )
                / 7
            )


# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['WTP']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'your_color': '{}'.format(player.color),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider),
            'round_number': '{}'.format(player.round_number),
        }


class instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ['accept']


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        assign_sequence(subsession)


class SendBackWaitPage(WaitPage):
    pass


class P8(Page):
    """This page is only for Player with sequence 8 """

    form_model = 'group'
    form_fields = ['sent_8']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 8

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 7:
                partner_color = p.color
        return {
            'round_number': '{}'.format(player.round_number),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'p1_receiver': Constants.endowment_Receiver + player.group.sent_2,
            'p2_decider': Constants.endowment_Decider - player.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + player.group.sent_3,
            'p3_decider': Constants.endowment_Decider - player.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + player.group.sent_4,
            'p4_decider': Constants.endowment_Decider - player.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + player.group.sent_5,
            'p5_decider': Constants.endowment_Decider - player.group.sent_5,
            'p5_receiver': Constants.endowment_Receiver + player.group.sent_6,
            'p6_decider': Constants.endowment_Decider - player.group.sent_6,
            'p6_receiver': Constants.endowment_Receiver + player.group.sent_7,
            'p7_decider': Constants.endowment_Decider - player.group.sent_7,
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
        }


class P7(Page):
    """This page is only for P7"""

    form_model = 'group'
    form_fields = ['sent_7', 'expect_7']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 7

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 6:
                partner_color = p.color
        return {
            'round_number': '{}'.format(player.round_number),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'p1_receiver': Constants.endowment_Receiver + player.group.sent_2,
            'p2_decider': Constants.endowment_Decider - player.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + player.group.sent_3,
            'p3_decider': Constants.endowment_Decider - player.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + player.group.sent_4,
            'p4_decider': Constants.endowment_Decider - player.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + player.group.sent_5,
            'p5_decider': Constants.endowment_Decider - player.group.sent_5,
            'p5_receiver': Constants.endowment_Receiver + player.group.sent_6,
            'p6_decider': Constants.endowment_Decider - player.group.sent_6,
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
        }


class P6(Page):
    """This page is only for P6"""

    form_model = 'group'
    form_fields = ['sent_6', 'expect_6']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 6

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 5:
                partner_color = p.color
        return {
            'round_number': '{}'.format(player.round_number),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'p1_receiver': Constants.endowment_Receiver + player.group.sent_2,
            'p2_decider': Constants.endowment_Decider - player.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + player.group.sent_3,
            'p3_decider': Constants.endowment_Decider - player.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + player.group.sent_4,
            'p4_decider': Constants.endowment_Decider - player.group.sent_4,
            'p4_receiver': Constants.endowment_Receiver + player.group.sent_5,
            'p5_decider': Constants.endowment_Decider - player.group.sent_5,
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
        }


class P5(Page):
    """This page is only for P7"""

    form_model = 'group'
    form_fields = ['sent_5', 'expect_5']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 5

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 4:
                partner_color = p.color
        return {
            'round_number': '{}'.format(player.round_number),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'p1_receiver': Constants.endowment_Receiver + player.group.sent_2,
            'p2_decider': Constants.endowment_Decider - player.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + player.group.sent_3,
            'p3_decider': Constants.endowment_Decider - player.group.sent_3,
            'p3_receiver': Constants.endowment_Receiver + player.group.sent_4,
            'p4_decider': Constants.endowment_Decider - player.group.sent_4,
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
        }


class P4(Page):
    """This page is only for P4"""

    form_model = 'group'
    form_fields = ['sent_4', 'expect_4']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 4

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 3:
                partner_color = p.color
        return {
            'round_number': '{}'.format(player.round_number),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'p1_receiver': Constants.endowment_Receiver + player.group.sent_2,
            'p2_decider': Constants.endowment_Decider - player.group.sent_2,
            'p2_receiver': Constants.endowment_Receiver + player.group.sent_3,
            'p3_decider': Constants.endowment_Decider - player.group.sent_3,
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
        }


class P3(Page):
    """This page is only for P3"""

    form_model = 'group'
    form_fields = ['sent_3', 'expect_3']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 3

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 2:
                partner_color = p.color
        return {
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
            'round_number': '{}'.format(player.round_number),
            'p1_receiver': Constants.endowment_Receiver + player.group.sent_2,
            'p2_decider': Constants.endowment_Decider - player.group.sent_2,
        }


class P2(Page):
    """This page is only for P2"""

    form_model = 'group'
    form_fields = ['sent_2', 'expect_2']

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 2

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 1:
                partner_color = p.color
        return {
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
            'round_number': '{}'.format(player.round_number),
        }


class P1(Page):
    """This page is only for P1"""

    @staticmethod
    def is_displayed(player: Player):
        return player.sequence == 1

    @staticmethod
    def vars_for_template(player: Player):
        for p in player.get_others_in_group():
            if p.sequence == 2:
                partner_color = p.color
        return {
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner_color),
            'round_number': '{}'.format(player.round_number),
        }


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        set_payoffs(group)


class Results(Page):
    """This page displays the earnings of each player"""

    @staticmethod
    def vars_for_template(player: Player):
        p2_transfer = player.group.sent_2
        p3_transfer = player.group.sent_3
        p4_transfer = player.group.sent_4
        p5_transfer = player.group.sent_5
        p6_transfer = player.group.sent_6
        p7_transfer = player.group.sent_7
        p8_transfer = player.group.sent_8
        average_transfer = (
            player.group.sent_2
            + player.group.sent_3
            + player.group.sent_4
            + player.group.sent_5
            + player.group.sent_6
            + player.group.sent_7
            + player.group.sent_8
        ) / 7
        p1_receiver = Constants.endowment_Receiver + player.group.sent_2
        p2_decider = Constants.endowment_Decider - player.group.sent_2
        p2_receiver = Constants.endowment_Receiver + player.group.sent_3
        p3_decider = Constants.endowment_Decider - player.group.sent_3
        p3_receiver = Constants.endowment_Receiver + player.group.sent_4
        p4_decider = Constants.endowment_Decider - player.group.sent_4
        p4_receiver = Constants.endowment_Receiver + player.group.sent_5
        p5_decider = Constants.endowment_Decider - player.group.sent_5
        p5_receiver = Constants.endowment_Receiver + player.group.sent_6
        p6_decider = Constants.endowment_Decider - player.group.sent_6
        p6_receiver = Constants.endowment_Receiver + player.group.sent_7
        p7_decider = Constants.endowment_Decider - player.group.sent_7
        p7_receiver = Constants.endowment_Receiver + player.group.sent_8
        p8_decider = Constants.endowment_Decider - player.group.sent_8
        p8_receiver = (
            Constants.endowment_Receiver
            + (
                player.group.sent_2
                + player.group.sent_3
                + player.group.sent_4
                + player.group.sent_5
                + player.group.sent_6
                + player.group.sent_7
                + player.group.sent_8
            )
            / 7
        )
        p1_payoff = 2 * p1_receiver
        p2_payoff = p2_decider * p2_receiver
        p3_payoff = p3_decider * p3_receiver
        p4_payoff = p4_decider * p4_receiver
        p5_payoff = p5_decider * p5_receiver
        p6_payoff = p6_decider * p6_receiver
        p7_payoff = p7_decider * p7_receiver
        p8_payoff = (
            p8_decider
            * (
                p1_receiver
                + p2_receiver
                + p3_receiver
                + p4_receiver
                + p5_receiver
                + p6_receiver
                + p7_receiver
            )
            / 7
        )
        return {
            'p2_transfer': p2_transfer,
            'p3_transfer': p3_transfer,
            'p4_transfer': p4_transfer,
            'p5_transfer': p5_transfer,
            'p6_transfer': p6_transfer,
            'p7_transfer': p7_transfer,
            'p8_transfer': p8_transfer,
            'average_transfer': average_transfer,
            'p1_receiver': p1_receiver,
            'p2_decider': p2_decider,
            'p2_receiver': p2_receiver,
            'p3_decider': p3_decider,
            'p3_receiver': p3_receiver,
            'p4_decider': p4_decider,
            'p4_receiver': p4_receiver,
            'p5_decider': p5_decider,
            'p5_receiver': p5_receiver,
            'p6_decider': p6_decider,
            'p6_receiver': p6_receiver,
            'p7_decider': p7_decider,
            'p7_receiver': p7_receiver,
            'p8_decider': p8_decider,
            'p8_receiver': p8_receiver,
            'p1_payoff': p1_payoff,
            'p2_payoff': p2_payoff,
            'p3_payoff': p3_payoff,
            'p4_payoff': p4_payoff,
            'p5_payoff': p5_payoff,
            'p6_payoff': p6_payoff,
            'p7_payoff': p7_payoff,
            'p8_payoff': p8_payoff,
        }


class OverallResults(Page):
    """This page displays the end of game data """

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        cumulative_payoff = sum([p.payoff for p in player.in_all_rounds()])
        return {'overall_earnings': cumulative_payoff}


class Survey(Page):
    """This page displays the questionnaire for each player"""

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = [
        'dep',
        'edu',
        'age',
        'gen',
        'inc',
        'h_inc',
        'investment_options_1',
        'investment_options_2',
        'investment_options_3',
        'investment_options_4',
        'investment_options_5',
        'investment_options_6',
        'investment_options_7',
        'investment_options_8',
        'investment_options_9',
        'investment_options_10',
        'env_cons_2',
        'env_cons_3',
        'env_cons_5',
        'env_cons_6',
        'env_cons_7',
        'env_cons_9',
        'fate',
        'believe',
        'gpa',
    ]


page_sequence = [
    instructions,
    Introduction,
    ShuffleWaitPage,
    P1,
    SendBackWaitPage,
    P2,
    SendBackWaitPage,
    P3,
    SendBackWaitPage,
    P4,
    SendBackWaitPage,
    P5,
    SendBackWaitPage,
    P6,
    SendBackWaitPage,
    P7,
    SendBackWaitPage,
    P8,
    ResultsWaitPage,
    Results,
    Survey,
    OverallResults,
]