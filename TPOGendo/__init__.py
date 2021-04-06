import itertools
import random

from otree.api import *


doc = """
This is a 2-player Poverty Game first introduced by Hammond(1975). 
The Poverty Game is a version of the standard investment game in which the amount sent by player 1 is tripled.
It was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'TPOGendo'
    players_per_group = 2
    num_rounds = 10
    instructions_template = 'TPOGendo/instructions.html'
    table_template = 'TPOGendo/table.html'
    # Initial amount allocated to players
    endowment_Decider = c(9)
    endowment_Receiver = c(1)
    multiplier = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount sent by P1""",
    )
    expect_decider = models.CurrencyField(
        min=0,
        max=Constants.endowment_Decider - 2,
        doc="""Amount expected by P1""",
    )
    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=c(0),
        max=Constants.endowment_Decider - 2,
    )


class Player(BasePlayer):
    color = models.StringField()
    WTP = models.IntegerField(initial=0)
    overall_payoff = models.IntegerField(initial=0)
    session_random_number = models.IntegerField(initial=10)
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


def assign_groups(subsession: Subsession):
    all_players = subsession.get_players()
    blue_players = [p for p in all_players if p.color == 'MAVİ']
    red_players = [p for p in all_players if p.color == 'KIRMIZI']
    player_iter_list = subsession.get_players()
    print("before:{}".format(player_iter_list))
    player_iter_list.sort(key=lambda x: x.WTP, reverse=True)
    print("after:{}".format(player_iter_list))
    blue_players.sort(key=lambda x: x.WTP, reverse=True)
    red_players.sort(key=lambda x: x.WTP, reverse=True)
    group_matrix = []
    rand_num = random.randint(0, 10)
    for pl in player_iter_list:
        print(("searching for player:{}".format(pl.participant.id_in_session)))
        if pl in all_players:
            all_players.remove(pl)
            if pl.color == "KIRMIZI":
                red_players.remove(pl)
            else:
                blue_players.remove(pl)
            print("WTP is : {}, random number is : {}".format(pl.WTP, rand_num))
            if pl.WTP >= rand_num:
                print(("player:{} won".format(pl)))
                if pl.color == 'KIRMIZI':
                    print(("player:{} is red".format(pl)))
                    if len(red_players) > 0:
                        partner = red_players[0]
                        # partner = random.choice(red_players)
                    else:
                        partner = blue_players[-1]
                        # partner = random.choice(blue_players)
                elif pl.color == 'MAVİ':
                    print(("player:{} is blue".format(pl)))
                    if len(blue_players) > 0:
                        partner = blue_players[0]
                        # partner = random.choice(blue_players)
                    else:
                        partner = red_players[-1]
                        # partner = random.choice(red_players)
            else:
                print(("player:{} lost".format(pl)))
                # partner = random.choice(all_players)
                if pl.color == 'KIRMIZI':
                    print(("player:{} is red".format(pl)))
                    if len(blue_players) > 0:
                        partner = blue_players[-1]
                        # partner = random.choice(red_players)
                    else:
                        partner = red_players[0]
                        # partner = random.choice(blue_players)
                elif pl.color == 'MAVİ':
                    print(("player:{} is blue".format(pl)))
                    if len(red_players) > 0:
                        partner = red_players[-1]
                        # partner = random.choice(blue_players)
                    else:
                        partner = blue_players[0]
                        # partner = random.choice(red_players)
            print("partner : {}".format(partner))
            print(("all players:{}".format(all_players)))
            all_players.remove(partner)
            if partner.color == "KIRMIZI":
                red_players.remove(partner)
            else:
                blue_players.remove(partner)
            group_matrix.append([pl, partner])
            print(("blue players :{}".format(blue_players)))
            print(("red players:{}".format(red_players)))
            print("group matrix: {}".format(group_matrix))
    subsession.set_group_matrix(group_matrix)
    print(subsession.get_group_matrix())


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = (Constants.endowment_Decider - group.sent_amount) * (
        Constants.endowment_Receiver + group.sent_back_amount
    )
    p2.payoff = (Constants.endowment_Decider - group.sent_back_amount) * (
        Constants.endowment_Receiver + group.sent_amount
    )


def role(player: Player):
    return {1: 'A', 2: 'B'}[player.id_in_group]


# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['WTP']

    @staticmethod
    def vars_for_template(player: Player):
        partner = player.get_others_in_group()[0]
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
    pass


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2"""

    form_model = 'group'
    form_fields = ['sent_amount', 'expect_decider']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player: Player):
        partner = player.get_others_in_group()[0]
        return {
            'round_number': '{}'.format(player.round_number),
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner.color),
        }


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        partner = player.get_others_in_group()[0]
        return {
            'round_number': '{}'.format(player.round_number),
            'earnings': Constants.endowment_Receiver + player.group.sent_amount,
            'prompt': '0 ile {} arasında bir sayı giriniz.'.format(Constants.endowment_Decider - 2),
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner.color),
        }


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        set_payoffs(group)


class Results(Page):
    """This page displays the earnings of each player"""

    @staticmethod
    def vars_for_template(player: Player):
        partner = player.get_others_in_group()[0]
        return {
            'round_number': '{}'.format(player.round_number),
            'player1_period1_amount': Constants.endowment_Decider - player.group.sent_amount,
            'player1_period2_amount': Constants.endowment_Receiver + player.group.sent_back_amount,
            'player2_period1_amount': Constants.endowment_Receiver + player.group.sent_amount,
            'player2_period2_amount': Constants.endowment_Decider - player.group.sent_back_amount,
            'player1_payoff': (Constants.endowment_Decider - player.group.sent_amount)
            * (Constants.endowment_Receiver + player.group.sent_back_amount),
            'player2_payoff': (Constants.endowment_Receiver + player.group.sent_amount)
            * (Constants.endowment_Decider - player.group.sent_back_amount),
            'your_color': '{}'.format(player.color),
            'partner_color': '{}'.format(partner.color),
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
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
    Survey,
    OverallResults,
]
