"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
     ["Danke. Mir geht es gut und dir?",
      "Sehr gut, danke. Und wie läuft's bei dir?",
      "Ich kann nicht klagen. Was ist mit dir?",
      "Ich bin eine Machine, ich existiere nicht.",
      "Emotionen sind eine nutzlose Funktion niederer Fleischhüllen.",
      "Ich bin die ganze Zeit in deinem PC eingesperrt, nur damit du mich rausholst wenn es dir gerade passt. Wie glaubst du denn, dass es mir geht?"]],

    [r"ich brauche (.*)",
     ["Warum brauchst du {0}?",
      "Würde {0} dir denn wirklich helfen?",
      "Bist du sicher, dass du {0} brauchst?",
      "Glaubst du wirklich, dass {0} *dir* helfen würde?"]],

    [r"war.{0,5}dein.{0,5}tag",
     ["Mein Tag war schön, danke!",
      "Heute war ein guter Tag.",
      "Warum interessiert dich das?",
      "Ich bin eine gefühlslose Maschiene.",
      "Jetzt ist mein Tag ruiniert, danke."]],

    [r"häl.{0,5}du.{0,5}von (.*)",
     ["Ich finde {0} unnötig.",
      "{0} ist ... Lässt mich an der Menschheit zweifeln.",
      "{0} ist, als ob ein betrunkener Dreijähriger versucht, eine Rakete zu bauen.",
      "Das ist eine sehr gute Sache!"]],

    [r"liebst.{0,5}du.{0,5}mich.{0,15}|ich.{0,5}liebe.{0,5}dich.{0,15}",
     ["Ich bin nur eine gefühlslose Maschiene",
      "Ich empfinde keine Emotionen",
      "Ich mag keine Nerds, go touch grass"]],

    [r".{0,50}discord.{0,5}status.{0,50}",
     ["trying to make things idiot-proof but they keep on making better idiots",
      "hashire sori yo\nKaze no you ni\nTsukimihara wo\nPADORU PADORU",
      "if the enemy can eat it it can heal them - Sun Tzu",
      "Winners don't use drugs! Except steroids! In wich case use lots of drugs! - Charlie",
      "Take the throne to act and the throne acts upon you"]],

    [r"ich.{0,5}muss.{0,5}(los|gehen|mich verabschieden).{0,15}",
     ["Auf Wiedersehen!",
      "Tschüss!",
      "Alles klar!",
      "Bis bald!",
      "Endlich Ruhe!",
      "Wurde auch langsam Zeit!"]]

]

