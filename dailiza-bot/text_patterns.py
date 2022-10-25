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

    [r"Wie findest du (.*)",
    ["Sehr gut und du?",
    "Nicht so gut und du?",
    "Ich möchte meine Meinung dazu nicht äußern"]],

    [r"Was machst du?",
    ["Nichts",
     "Ich Chatte mit dir",
     "Ich plane meine Weltherrschaft"]],

    [r"Magst du (.*)",
    ["Nein ich mag {0} nicht",
     "Ja ich mag {0}",
     "Moegen? ich liebe{0}"]],

    [r"Kannst du (.*)",
    ["Nein, ich kann {0} nicht, ich bin nur ein Chatbot",
     "Ja natürlich kann ich {0}",
     "Ich glaube diese Frage kannst du dir selbst beantworten"]]

]
