#-*- coding: utf-8 -*-
print("BMI RECHNER")
print(" ")
#Geschlecht
print("Welches Geschlecht hast du? \nM = Männlich \nW = Weiblich")
M = "Männlich"
m = "Männlich"
W = "Weiblich"
w = "Männlich"
geschlecht_input=input()
geschlecht = str(geschlecht_input)
print(" ")
#Gewicht
print("Gewicht (kg):")
gewicht_input=input()
Gewicht=float(gewicht_input)
print(" ")
#Grösse
print("grösse (meter):")
grösse_input=input()
grösse=float(grösse_input)
#BMI
print(' ')
print("Hier ist dein BMI:")
if geschlecht_input==[W, w]:
    BMI=(Gewicht/(grösse*grösse)*1.1)
else:
    BMI=(Gewicht/(grösse*grösse))
print(BMI)
#Typ
if BMI < 16:
    print("\nDu bist schwer untergewichtig.")
elif 16 <= BMI < 18.5:
    print("\nDu bist untergewichtig.")
elif 18.5 <= BMI < 24:
    print("\nDu bist normalgewichtig.")
elif 24 <= BMI < 30:
    print("\nDu bist übergewichtig.")
elif 30 <= BMI < 35:
    print("\nDu bist fettleibig im 1. Grad.")
elif 35 <= BMI < 40:
    print("\nDu bist fettleibig im 2. Grad.")
else:
    print("\nDu bist fettleibig im 3. Grad.")
print(" ")
#Ratschläge.
print("Rat:")
if BMI < 16:
    print("Wenn du schwer untergewichtig bist, konsultiere sofort einen Gesundheitsprofi wie einen Arzt oder einen Ernährungsberater. Eine ausgewogene und gesunde Ernährung, die reich an Proteinen, Kohlenhydraten und gesunden Fetten ist, kann dir helfen, ein gesundes Körpergewicht zu erreichen. Vermeide plötzliche Änderungen in deiner Ernährung ohne medizinische Aufsicht.")
elif 16 <= BMI < 18.5:
    print("Ein wichtiger Ratschlag für Untergewichtige ist, sich auf die Qualität und Menge der verzehrten Lebensmittel zu konzentrieren. Stelle sicher, dass deine Ernährung nährstoffreiche und kalorienreiche Lebensmittel wie Obst, Gemüse, mageres Eiweiß, Vollkornprodukte und gesunde Fette enthält. Erwäge auch, häufig kleine Mahlzeiten und Snacks zu essen, um die tägliche Kalorienaufnahme zu erhöhen.")
elif 18.5 <= BMI < 24:
    print("Herzlichen Glückwunsch, mach weiter so!")
elif 24 <= BMI < 30:
    print("Ein wichtiger Tipp für Übergewichtige ist, sich auf die Entwicklung gesünderer Ernährungs- und Lebensgewohnheiten zu konzentrieren. Beginne mit kleinen Veränderungen, wie das Reduzieren der Portionsgrößen, das Erhöhen des Konsums von Obst und Gemüse, das Bevorzugen von Vollkornprodukten und das Einschränken von Zucker sowie verarbeiteten Lebensmitteln. Regelmäßige Bewegung, selbst ein täglicher Spaziergang, kann den Stoffwechsel verbessern und die Gewichtsabnahme fördern. Denke daran: Der Schlüssel liegt in Beständigkeit und Geduld, um einen gesunden Lebensstil zu erreichen.")
elif 30 <= BMI < 35:
    print("Ein wichtiger Ratschlag für Personen mit Adipositas Grad 1 ist, professionelle Unterstützung zu suchen. Sprich mit einem Arzt oder Ernährungsberater, um einen individuellen Plan zu entwickeln, der eine Kombination aus ausgewogener Ernährung, regelmäßiger Bewegung und nachhaltigen Lebensstiländerungen umfasst. Realistische Ziele zu setzen und Fortschritte zu überwachen, kann dir helfen, motiviert zu bleiben und langfristig eine bessere Gesundheit zu erreichen.")
elif 35 <= BMI < 40:
    print("Für Personen mit Adipositas Grad 2 ist es entscheidend, spezialisierte medizinische Unterstützung zu suchen. Wende dich an einen Endokrinologen, Ernährungsberater oder bariatrischen Chirurgen, um die für deinen Fall am besten geeigneten Behandlungsoptionen zu bewerten. Eine ausgewogene Ernährung, regelmäßige körperliche Aktivität und die Berücksichtigung medizinischer Therapien oder chirurgischer Eingriffe können Teil eines umfassenden Ansatzes sein, um Adipositas Grad 2 sicher und effektiv zu bewältigen.")
else:
    print("Für Personen mit Adipositas Grad 3 ist es entscheidend, dringend medizinische Hilfe in Anspruch zu nehmen. Konsultiere einen auf Adipositas spezialisierten Arzt oder einen bariatrischen Chirurgen, um die für deinen Fall am besten geeigneten Behandlungsoptionen zu besprechen. In einigen Fällen können aggressivere Maßnahmen wie eine bariatrische Operation notwendig sein, begleitet von Lebensstiländerungen und regelmäßiger medizinischer Überwachung. Ein individuell abgestimmter Behandlungsplan unter der Anleitung von Gesundheitsexperten kann dir helfen, Adipositas Grad 3 sicher und gezielt zu bewältigen.")
input("\nDrücke Enter, um die Ausführung zu beenden.")