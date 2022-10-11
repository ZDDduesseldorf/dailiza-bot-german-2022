"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"[Ii]ch brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"(?<=mir\s)+[\w\s]*(schlecht|nicht[\w\s]*gut)", 
    ["Das klingt wirklich nicht so gut, kann ich dir irgendwie helfen",
    "Was fehlt dir denn, weshalb es dir schlecht geht?",
    "das tut mir leid, brauchst du irgendetwas?"]],
    
    [r"(?<=mir\s)[\w\s]*gut", 
    ["Das freut mich, hast du noch irgendeine andere Fragen?",
    "Kann ich dir noch mit irgendetwas anderem behilflich sein?",
    "OK cool, brauchst du noch irgendetwas?"]],
    
    [r"[bB]ist du ein (.*)", 
    ["Das sag ich dir nicht ob ich ein {0} bin",
    "Ich bin kein {0}, ich bin Dailiza :)",
    "EIN {0}?!... Darauf antworte ich nicht"]],
    
    [r".", 
    ["Das verstehe ich leider nicht, frag mich was anderes",
    "Keine Ahnung wovon du sprichst, erzähl mir liber etwas über dich",
    "Brauchst du irgendetwas?"]],

]
