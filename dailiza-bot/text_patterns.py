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
    "Bist du sicher, dass du {0} brauchst? "]],

    [r"Ich habe (.*)",
    ["Warum hast du {0}?",
    "Hat {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} hast?"]],
    
    [r"Bist du (.*)",
    ["Warum fragst du ob ich {0} bin?",
    "Ob ich {0} bin, kann ich nicht genau sagen.",
    "Denkst du, dass ich {0} bin?"]],
    
    [r"Ich denke (.*)",
    ["Interessant, warum denkst du {0}?",
    "Bringt dich {0} zu denken weiter?",
    "Was genau meinst du mit {0} denken?"]],
    
    [r"Magst du (.*)",
    ["Warum sollte ich {0} mögen?",
    "Das weiß ich nicht genau. Magst du {0}?",
    "Schwierige Frage, ich kann dir nicht dirket sagen ob ich {0} mag."]],
]
