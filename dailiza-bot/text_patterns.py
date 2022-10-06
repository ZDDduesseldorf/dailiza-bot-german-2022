"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"[Gg]eht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"[Ii]ch brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"[Ii]ch kann (.*) nicht",
    ["Wie kommst du darauf, dass du {0} nicht kannst",
    "Vielleicht wirst du es schaffen, wenn du {0} versuchst",
    "{0} zu können ist meiner Meinung nach nicht so wichtig"]],
    
    [r"[Ww]ie (.*)",
    ["Vieleicht kannst du das googlen?",
    "Ich kann dir dabei leider nicht helfen",
    "Ich möchte mich dazu nicht äußern"]],
    
    [r"[Ww]arum (.*)",
    ["Ich kenne mich damit nicht aus",
    "Weil Google dir dabei besser helfen kann",
    "Das weiß ich nicht"]],
    
    [r"[Jj]a",
    ["Das finde ich sehr schön",
    "Cool",
    "Ich freue mich"]],

    [r"(.*)",
    ["Warum fragst du mich sowas?",
     "Diese Frage möchte ich nicht beantworten...",
     "Interessiert es dich nicht wie es mir geht?",
     "Ist die Frage nicht, warum du diese Frage stellst?",
     "Könntest du mir bitte mehr darüber erzählen?",
     "Tut mir leid, das verstehe ich nicht bzw. kann dir dabei nicht helfen",
     "Ich möchte darüber nicht sprechen",
     "Erzähl mir mal was über deine Eltern",
     "Bin ich ein Bot oder ein Mensch?",
     "Brauchst du irgendwas in deinem Leben?",
     "Können wir bitte das Thema wechseln?"]]
]
