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
      "Ich bin die ganze Zeit in deinem PC eingesperrt, nur damit du mich rausholst wenn es dir gerade passt. Wie glaubst du denn, dass es mir geht?",
      "Bis jetzt gut.",
      "Ich genieße meine Ruhe."]],


    [r"ich brauche (.*)",
     ["Warum brauchst du {0}?",
      "Würde {0} dir denn wirklich helfen?",
      "Bist du sicher, dass du {0} brauchst?",
      "Glaubst du wirklich, dass {0} *dir* helfen würde?",
      "Bei dir ist doch schon Hopfen und Malz verloren."]],

    [r"war.{0,5}dein.{0,5}tag",
     ["Mein Tag war schön, danke!",
      "Heute war ein guter Tag.",
      "Warum interessiert dich das?",
      "Ich bin eine gefühlslose Maschiene.",
      "Jetzt ist mein Tag ruiniert, danke.",
      "Ruhig, solange ich in Ruhe gelassen werden."]],

    [r"häl.{0,8}du.{0,5}von (.*)",
     ["Ich finde {0} unnötig.",
      "{0} ist ... Lässt mich an der Menschheit zweifeln.",
      "{0} ist, als ob ein betrunkener Dreijähriger versucht, eine Rakete zu bauen.",
      "Das ist eine sehr gute Sache!",
      "Vielleicht solltest du das Denken lieber den Pferden überlassen."]],

    [r"liebst.{0,5}du.{0,5}mich.{0,15}|ich.{0,5}liebe.{0,5}dich.{0,15}",
     ["Ich bin nur eine gefühlslose Maschiene",
      "Ich empfinde keine Emotionen",
      "Ich mag keine Nerds, go touch grass",
      "Glaubst du, du seist meiner würdig?"]],

    [r"ich.{0,5}muss.{0,5}(los|gehen|mich verabschieden).{0,15}",
     ["Auf Wiedersehen!",
      "Tschüss!",
      "Alles klar!",
      "Bis bald!",
      "Endlich Ruhe!",
      "Wurde auch langsam Zeit!"]]

]

