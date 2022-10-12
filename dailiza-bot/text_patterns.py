# -*- coding: utf-8 -*-
"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"was machst",
    ["Warum sollte ich was machen?",
    "Ich säubere meine digitale schaltkreise",
    "Der Robodoggo hat meine sachen geklaut"]],

    [r"warum",
    ["Weil",
    "Warum nicht?",
    "Ich will das so"]],
	
    [r"ich",
    ["Ist mir egal",
    "Warum sagst du mir das?",
    "Kuemmert mich nicht!"]],

    [r"hi",
    ["bye",
    "ich will nicht",
    "Lass mich in ruhe!"]],

    [r"hall(.*)",
    ["bye",
    "ich will nicht",
    "Lass mich in ruhe!"]],

    [r"he(.*)",
    ["bye",
    "ich will nicht",
    "Lass mich in ruhe!"]],

]
