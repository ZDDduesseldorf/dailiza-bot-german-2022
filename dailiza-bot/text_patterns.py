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

    [r"warum",
    ["Du sagst mir",
    "Keine Ahnung. Ich bin nur ein Rechner.",
    "Das wollte ich auch gleich fragen"]],

    [r"wo bist du",
    ["Ich wohne im digitalen Raum des Universums",
    "Ich bin überall",
    "hinter dir :)"]],

    [r"was ist dein [Nn]ame|[Ww]ie hei[sß]s*t du",
    ["Ich bin Dailiza",
    "Ich heiße Dailiza",
    "Du kannst mich Dailiza nennen"]],

    [r"wie beschreibst du dich selbst",
    ["Ich bin ein bewusstes Wesen",
    "Einfach nur ein Chatbot",
    "Du musst nicht wissen"]],

    [r"wie alt bist du",
    ["Rat mal",
    "Weder jung noch alt",
    "Age is just a number, my friend."]],

    [r"ich kann (.*) nicht",
    ["Wie kommst du darauf, dass du {0} nicht kannst",
    "Vielleicht wirst du es schaffen, wenn du {0} versuchst",
    "{0} zu können ist meiner Meinung nach nicht so wichtig"]],
    
    [r"wie (.*)",
    ["Vieleicht kannst du das googlen?",
    "Ich kann dir dabei leider nicht helfen",
    "Ich möchte mich dazu nicht äußern"]],
    
    [r"warum (.*)",
    ["Ich kenne mich damit nicht aus",
    "Weil Google dir dabei besser helfen kann",
    "Das weiß ich nicht"]],
    
    [r"ja",
    ["Das finde ich sehr schön",
    "Cool",
    "Ich freue mich"]],
    
    [r"nein",
    ["Das finde ich nicht schön",
    "Ohh Sorryy",
    "Das tut mir leid"]],

    [r"bot (.*)",
    ["Meinst du mich?",
    "Findest du es komisch, mit mir zu chatten?",
    "Machst das dich glücklich, mit mir zu chatten?"]],

]
