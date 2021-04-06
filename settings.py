from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.05,
    'participation_fee': 10,
    'doc': "",
}

SESSION_CONFIGS = [

    {
    'name': 'my_TPoG_control',
    'display_name': "TPoGGameControl",
    'num_demo_participants': 2,
    'app_sequence': ['TPOGcont'],
    }
]
    
"""   ,
	{
    'name': 'my_TPoG_controlN',
    'display_name': "TPoGGameControlN",
    'num_demo_participants': 2,
    'app_sequence': ['TPOGcontN'],
    },
	{
    'name': 'my_TPoG_exo',
    'display_name': "TPoGGameExo",
    'num_demo_participants': 2,
    'app_sequence': ['TPOGexo'],
    },
    {
    'name': 'my_TPoG_endo',
    'display_name': "TPoGGameEndo",
    'num_demo_participants': 2,
    'app_sequence': ['TPOGendo'],
    },
    {
    'name': 'my_TPeG_control',
    'display_name': "TPeGGameControl",
    'num_demo_participants': 8,
    'app_sequence': ['TPEGcont'],
    },
	{
    'name': 'my_TPeG_exo',
    'display_name': "TPeGGameExo",
    'num_demo_participants': 8,
    'app_sequence': ['TPEGexo'],
    },
    {
    'name': 'my_TPeG_endoR',
    'display_name': "TPeGGameEndoR",
    'num_demo_participants': 8,
    'app_sequence': ['TPEGendoR'],
    },
    {
    'name': 'my_TPeG_endoL',
    'display_name': "TPeGGameEndoL",
    'num_demo_participants': 8,
    'app_sequence': ['TPEGendoL'],
    }
"""
   



# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'tr'
# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'TL'
USE_POINTS = True

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '{{ secret_key }}'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

