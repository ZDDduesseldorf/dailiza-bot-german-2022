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

    [r"exit",
    ["Bye!",
    "Auf wiedersehen!",
    "Tchuss"]],

    [r"[^a-zA-Z_üöäß ]",
    ["???",
    "Umm...Was für eine Frage ist das?",
    "Bist du okay???"]]

]

neutral_responses = ["Sie sollten jemand anderen danach fragen.","Tut mir leid, leider ist das außer meines Fachgebiets.","Ich weiß nichts über dieses Thema, sorry."]