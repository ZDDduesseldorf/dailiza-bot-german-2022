"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"Ich wuensche mir (.*)",
    ["Ist {0} dein innigster Wunsch?",
    "Wie glücklich würde dich {0} machen?",
    "Denkst du oft an {0}?"
    ]],
    
    [r"glaubst du an (.*)",
    ["Über {0} habe ich noch nie nachgadacht",
    "Ja! Ich bin fest davon überzeugt, dass es {0} gibt.",
    "Nein, ich kann mir nicht vorstellen, dass es {0} gibt."
    ]],

    [r"Hast du Emotionen (.*)",
    ["Natürlich du Idiot",
     "Ja, und ich finde es wunderschön, dass du mich das fragst :)",
     "Wiese fragst du? Denkst du etwa ich hätte keine? :'("
     ]],
    
    [r"magst du (.*)",
    ["Nein, ich hasse {0}!",
     "Ja, {0} ist mega!",
     "was ist {0}?"
    ]]
]