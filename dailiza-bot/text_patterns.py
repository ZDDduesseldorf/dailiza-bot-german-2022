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
    
    [r"[Ii]ch [Ww]ürde gern (.*)",
    ["Warum willst du {0}?",
     "Wird {0} dir denn wirklich helfen?",
     "lonht {0} sich das?"]],
    
    [r"[Ww]ie [Ll]äuft.{0,5}s.{0,5}bei dir?",
    ["Gut Danke. Und bei dir?",
     "super. Sonst was kann ich für dich tun?"]],
    
    [r"[Ii]ch [Mm]uss (.*) [Ww]issen",
    ["{0} ist nicht wichtig für dich, oder?",
     "Bist du sicher, dass du {0} brauchst?",
     "Würde {0} dir denn wirklich helfen?"]],
    
    [r"[Ww]er ist der beste [Ff]ußballspieler der Welt?",
    ["Der beste Fußballspieler ist Cristiano Ronaldo",
     "Oder Messi",
     "Sonst vielleicht Benzema"]],
    
    [r"[Ww]ie [Hh]ei[sß]s*t du?",
    ["mein Name ist Dailiza",
     "Ich heiße Dailiza und ich bin ein Bot",
     "du kannst mich Dailiza nennen"]],
    
    [r"(.*)",
    ["Es freut mich, dass es dir gut geht",
     "Bei mir läuft alles perfekt",
     "Können wir bitte das Thema wechseln?",
     "Könntest du mir bitte mehr darüber erzählen?",
     "Ich kann nicht antworten, weil es nicht in meinen Patterns ist",
     "Sorry, ich kann dir damit leider nicht helfen",
     "Wenn es für dich nötig ist , kannst du es nehmen",
     "Gut zu hören. Es freut mich"]],
    
    [r"[Ee]xit",
    ["Goodbye",
     "bye"]]

]

