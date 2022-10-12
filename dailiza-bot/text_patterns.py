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

    [r"Soll ich (.*) kaufen?",
    ["Brauchst du {0}?",
    "Willst du {0} essen?",
    "Wenn du {0} magst?"]],
    
    [r"Soll ich nach (.*) reisen?",
    ["Warst du schon mal in {0}?",
    "Würde es dir in {0} gefallen?",
    "Ist {0} sicher?"]],
    
    [r"Soll ich (.*) lesen?",
    ["Würde es dich weiterbringen, {0} zu lesen?",
    "Interessiert dich {0}?",
    "Hast du {0} nicht schon gelesen?"]],
]
