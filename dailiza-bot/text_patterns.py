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
    
    [r"Denkst du (.*)",
    ["Warum sollte ich {0} denken?",
    "Warum ist es dir wichtig was ich denke?",
    "Wichtiger ist doch was du denkst."]],
    
    [r"Ich denke (.*)",
    ["Warum denkst du {0}?",
    "Warum denkst du über {0} nach?",
    "Gut dass du dir über Dinge gedanken machst!"]],
    
    [r":[)D]",
    [":D",
    ":))",
    ":0"]],
    
    [r"Bist du ein [Rr]?.[bB]ot[er]*",
    ["Ja",
    "Nein",
    "Was geht dich das an, Pisser?"]],

]
