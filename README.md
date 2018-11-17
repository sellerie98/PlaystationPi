# Playstation Pi

## Konzept:

Playstation 2 per Netzwerk mit einem Raspberry Pi zur Steuerung und zum streamen von Spielen via Samba (und evtl von dvd, mal abwarten) von einem USB-Speichermedium bzw. von einer Festplatte, welche per USB mit dem Raspberry Pi angeschlossen ist.
Die Steuerung erfolgt über Kurzschließen von GPIOs für einen bestimmten Zeitintervall bzw. über Relays, die gesteuert werden.
Die LEDs werden über GPIOs gesteuert, die jeweils ein- oder ausgeschaltet werden.
Verbunden werden die beiden Geräte über einen Netzwerkswitch, welcher ebenfalls mit verbaut wird.

## Backlog:

* Außen:

- Kann ich alle LEDs mit dem Pi ordentlich steuern?
	- Abhängig von Spannung
	- Evtl muss ich die Stecker zer/abschneiden

- Was mache ich mit dem Powerbutton (bzw. Reset button, falls vorhanden)
	- Brauche ich mehr status LEDs?
	- LED Ring für Designkram und so vorne drankleben?
		- XBOX 360 Ring Startanimation beim Start der PS2 nachbauen?
		- Was zeige ich wie an?
			- Ist das sinnvoll?

- (Wie) führe ich die Controller/Memcard Ports nach Außen?
	- Extension cords existieren bei aliexpress
	- Passt das alles mit dem anderen Kram in das Gehäuse? Wo soll das alles hin?

- Wie führe ich Video/audio nach Außen?
	- Kabel zerschneiden+richtigen Port nach Außen legen (Scart/composite)
	- Kabel innen anschließen, zugentlasten (Heißkleber) und direkt nach außen legen?

- Wie führe ich Ethernet nach außen?
	- Kabel von hinten und Kupplung an Blende heißklebern?

- Strom/Video/Eth/USB auf ne I/O Blende?
	- Strom evtl nicht so, dafür eher PSUplatz benutzen
	- Video/Eth sind sinnvoll
	- blanke I/O Blende bei thingiverse ziehen und modifizieren?

- USB Ports?
	- Vorne: Pi?
		- Kabel zerschneiden notwendig? (Vermutlich ja :/)
	- Hinten: PS2?
		- USB verl. Kabel nötig

* Innen:

! Die Ps2 startet nur wenn man sie lang genug mit Strom maltretiert.
	Solved: Dicken Kondensator zwischen + und - vom Stepdown angeschlossen

- Kann/werde ich das originale PS2 Laufwerk benutzen?
	- Habe ich genug Platz im Gehäuse für ne Disk?
		- Evtl will man Filzpads auslegen um die Disk zu schützen
	- Wie kann ich Disks auf dem Laufwerk fixieren?
		- Laufwerk hält sie selbst fest, aber wie sicher ist das?
		- Evtl eine art Abstandshalter an der Gehäuseklappe verbauen, um Disks an der PS2 zu halten

- Wie sieht mein Powerkonzept aus?
	- Festspannungsnetzteil auf 12V
		- PS2 an Stepdown auf 8,5V (3A reicht wohl)
		- Switch an 12V
		- Pi an Stepdown auf 5V (3A sollte reichen, brauch da evtl noch einen)
	- eigenes PCB mit z.B. Sicherungen, Stepdown etc.?
		- Pro: Weniger Kabelwirrwar, wäre ne richtig ordentliche Lösung
		- Contra: Recht Aufwändig, komm in KiCAD noch nicht wirklich zurecht

- Passt alles ins Gehäuse?
	- muss man ausprobieren
	- Passt das mit Netzteil und Kühlungskonzept zusammen?

- Wie fixiere ich die Geräte?	
	- Heißkleber: wird bei den Temperaturen weich, maximal für Switch machbar
	- Tape: Hält nicht besonders lange und ist auch nicht besonders temperaturstabil.
	- Epoxy: Ich würde den Kram irgendwann ganz gerne nochmal demontieren können.
	- Schraublöcher/Schraubhalter festnieten?
		- Wäre die ordentlichste Lösung
		- Geht das nicht irgendwie anders besser?
			- Schraubhalter mit Heißkleber fixieren?
				Pro: Wäre bedeutend weniger Aufwand
				Contra: Wärmetechnische Bedenken


- Kühlung?
	- Ist der stock fan zu laut?
	- Kann ich die Kühlung effizienter lösen?
		- Airflow durch das komplette Gehäuse, um Pi und Wandler noch mitzunehmen
	- Wärmeleitpads: Wäre ne Idee. LEiten einerseits Wärme recht gut ab, aber sind nicht leitend.
		- Brauche ich für CPU/GPU neue Pads?
			- Wie funktioniert die Kühlung der PS2 genau?
				-  Was haben evtl die Shields damit zu tun?


- (Wo) hätte ich Platz für eine Festplatte?
	- Pro: Konstante, zuverlässige Geschwindigkeit
	- Contra: Moving parts, fallen irgendwann aus, vebrauchen viel Platz
	- Alternativen:
		- SSD:
			- Pro: Schnell
			- Contra: teuer, Verbraucht immer noch viel Platz
		- USB Stick:
			- Pro: Billig, verbraucht kaum Platz
			- Contra: Lebensdauer fragwürdig, Speicherplatz fragwürdig, USB Hub?
		- SD Karte:
			- Pro: Klein, verbraucht keinen Mehrplatz
			- Contra: Teuer, Geschwindigkeit fragwürdig, Lebensdauer fragwürdig

- Lasse ich die Shields an der PS2?
	- Pro:
		- Evtl sinnvoll für Schutz for Schäden am Board der PS2
		- Ohne Shield kein PS2 Laufwerk
	- Contra:
		- behindert evtl Kühlung der PS2	
