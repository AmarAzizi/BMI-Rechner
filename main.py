print("CALCOLATORE BMI")
print(" ")
print(" ")
#Genere
print("Di che genere sei? \nM = Maschio \nF = Femmina")
M="Maschio"
m="Maschio"
F="Femmina"
f="Femmina"
genere_input=input()
genere=str(genere_input)
print(" ")
#Peso
print("Peso (kg):")
peso_input=input()
peso=float(peso_input)
print(" ")
#Altezza
print("Altezza (metri):")
altezza_input=input()
altezza=float(altezza_input)
#BMI
print(' ')
print("Ecco il tuo BMI:")
if genere_input==[F, f]:
    BMI=(peso/(altezza*altezza)*1.1)
else:
    BMI=(peso/(altezza*altezza))
print(BMI)
#Classe
if BMI < 16:
    print("\nSei gravemente sottopeso")
elif 16 <= BMI < 18.5:
    print("\nSei sottopeso")
elif 18.5 <= BMI < 24:
    print("\nSei normopeso")
elif 24 <= BMI < 30:
    print("\nSei sovrappeso")
elif 30 <= BMI < 35:
    print("\nSei obeso di 1° grado")
elif 35 <= BMI < 40:
    print("\nSei obeso di 2° grado")
else:
    print("\nSei obeso di 3° grado")
print(" ")
#Consigli
print("Consiglio:")
if BMI < 16:
    print("Se sei gravemente sottopeso, consulta immediatamente un professionista della salute, come un medico o un dietologo. Seguire una dieta equilibrata e sana, ricca di proteine, carboidrati e grassi sani, può aiutarti a raggiungere un peso corporeo sano. Evita di fare cambiamenti improvvisi nella tua alimentazione senza supervisione medica.")
elif 16 <= BMI < 18.5:
    print("Un consiglio importante per chi è sottopeso è quello di concentrarsi sulla qualità e sulla quantità degli alimenti consumati. Assicurati di includere nella tua dieta cibi nutrienti e calorici come frutta, verdura, proteine magre, cereali integrali e grassi sani. Considera anche di mangiare frequentemente piccoli pasti e spuntini per aumentare l'apporto calorico giornaliero.")
elif 18.5 <= BMI < 24:
    print("Complimenti, continua così!")
elif 24 <= BMI < 30:
    print("Un suggerimento importante per chi è sovrappeso è quello di concentrarsi sulla creazione di abitudini alimentari e di vita più sane. Inizia con piccoli cambiamenti, come ridurre le porzioni, aumentare il consumo di frutta e verdura, preferire alimenti integrali e limitare gli zuccheri e gli alimenti processati. L'esercizio regolare, anche solo una passeggiata quotidiana, può aiutare a migliorare il metabolismo e favorire la perdita di peso. E ricorda, la chiave è la costanza e la pazienza nel perseguire uno stile di vita sano.")
elif 30 <= BMI < 35:
    print("Un consiglio importante per chi è obeso di primo grado è quello di cercare un sostegno professionale. Parla con un medico o un nutrizionista per sviluppare un piano personalizzato che includa una combinazione di dieta equilibrata, esercizio fisico regolare e cambiamenti dello stile di vita sostenibili. Impostare obiettivi realistici e monitorare i progressi può aiutarti a mantenere la motivazione e raggiungere una migliore salute nel lungo termine.")
elif 35 <= BMI < 40:
    print("Per chi è obeso di secondo grado, è fondamentale cercare un supporto medico specializzato. Rivolgiti a un endocrinologo, un nutrizionista o un chirurgo bariatrico per valutare le opzioni di trattamento più adatte al tuo caso. Seguire una dieta bilanciata, praticare regolarmente esercizio fisico e considerare terapie mediche o interventi chirurgici possono essere parte di un approccio completo per gestire l'obesità di secondo grado in modo sicuro ed efficace.")
else:
    print("Per chi è obeso di terzo grado, è cruciale cercare assistenza medica urgente. Consulta un medico specializzato in obesità o un chirurgo bariatrico per discutere delle opzioni di trattamento più appropriate per il tuo caso. Potrebbero essere necessari interventi più aggressivi, come la chirurgia bariatrica, insieme a cambiamenti dello stile di vita e monitoraggio medico regolare. Seguire un piano di trattamento sotto la guida di professionisti sanitari può aiutarti a gestire l'obesità di terzo grado in modo sicuro e mirato.")
input("\nPremi invio per terminare l'esecuzione")