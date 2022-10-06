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

    [r"[Ii]ch kann (.*) nicht",
    ["Wie kommst du darauf, dass du {0} nicht kannst",
    "Vielleicht wirst du es schaffen, wenn du {0} versuchst",
    "{0} zu können ist meiner Meinung nach nicht so wichtig"]],

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
