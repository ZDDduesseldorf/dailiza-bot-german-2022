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
    
    [r"Ich würde gern (.*)",
    ["Warum willst du {0}?",
     "Wird {0} dir denn wirklich helfen?",
     "lonht {0} sich das?"]],
    
    [r"wie läuft.{0,5}s.{0,5}bei dir?",
    ["Gut Danke. Und bei dir?",
     "super. Sonst was kann ich für dich tun?"]],
    
    [r"Ich muss (.*) wissen",
    ["{0} ist nicht wichtig für dich, oder?",
     "Bist du sicher, dass du {0} brauchst?",
     "Würde {0} dir denn wirklich helfen?"]],
    
    [r"Wer ist der beste Fußballspieler der Welt?",
    ["Der beste Fußballspieler ist Cristiano Ronaldo",
     "Oder Messi",
     "Sonst vielleicht Benzema"]]

]

