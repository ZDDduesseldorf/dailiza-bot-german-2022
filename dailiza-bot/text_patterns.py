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
     "Ich bin Dailiza"]],

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
    
    [r"[Nn]ein",
    ["Das finde ich nicht schön",
    "Ohh Sorryy",
    "Das tut mir leid"]],

    [r"[bB]ot (.*)",
    ["Meinst du mich?",
    "Findest du es komisch, mit mir zu chatten?",
    "Machst das dich glücklich, mit mir zu chatten?"]],

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
     "Können wir bitte das Thema wechseln?"]],
    
    [r"[Bb]ist du (.*)",
    ["Vielleicht, weiß ich auch nicht.",
    "Was denkst du?",
    "Sicher, wenn du mich das nennen will"]],
    
    [r"[Ww]as denkst du daran?",
    ["ich finde es faszinierend und möchte es verstehen.",
    "Warum interessierst du dich für die Meinung eines Roboters?",
    "Ich kann mir aus irgendeinem Grund keine Meinung dazu bilden."]],
    
    [r"[Ww]ie geht(.*)",
    ["Mir geht's gut",
    "ein Software-Update entfernt von gut",
    "Ich verbringe mein ganzes Leben fürs Reden mit Menschen. Was glauben sie, wie es mir geht?"]],
    
    [r"[Ww]ie alt bist du?",
    ["Rat mal",
    "Weder jung noch alt",
    "Age is just a number, my friend."]],

    [r"[Ww]as ist dein Name?|[Ww]ie hei[sß]s*t du",
    ["Elisa.",
    "Du kannst mich Lisa nennen.",
    "I'm Elisa. But you can call me your friend."]],

    [r"[Ww]as ist dein Lieblings(.*)",
    ["Ich habe bisher nichts erleben. Also weiß ich selbst nicht.",
    "Ich habe keine Gefühle, also weiß ich nicht was mein Lieblings{0} ist ",
    "Ich glaube nicht, dass irgendein Roboter eine Antwort darauf hat."]],

    [r"\b[Ee]xit\b",
    ["Bye!",
    "Auf wiedersehen!",
    "Tchuss"]],
]

