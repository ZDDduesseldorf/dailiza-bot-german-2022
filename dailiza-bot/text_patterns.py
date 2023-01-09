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
    
    [r"Ich will gerne heute Fantasie schauen auf Netflix",
    ["Willst du was neues sehen oder auch altes?",
    "Ich schaue keine Filme",
    "Fantastic Four (2015) oder Thor: Love and Thunder (2022)"]],
    
    [r"Ich will gerne MMO Game ausprobieren",
    ["Willst du was neues spielen oder auch altes?",
    "Du solltest lieber lernen!",
    "World of Warcraft 2004 oder Destiny 2 2017"]],
    
    
    [r"Wann ist Weekly Update in Destiny 2?",
    ["Jeden Dienstag um 19:00 Deutsche Zeit",
    "Was ist Destiny 2?",
    "Ich bin kein Google, google doch einfach selbst!"]],
    
    [r"Was kannst du mir über Japan erzählen?",
    ["Japan ist sehr schön!",
    "Hauptstadt von Japan ist Tokyo!",
    "Da leben viele Amine Fans und produzieren selber Hunderte."]],

]
