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

    [r"(?<=mir\s)*[\w\s]*gut", 
    ["Das freut mich, hast du noch irgendeine andere Fragen?",
    "Kann ich dir noch mit irgendetwas anderem behilflich sein?",
    "OK cool, brauchst du noch irgendetwas?"]],
]
