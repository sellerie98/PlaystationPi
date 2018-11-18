# Playstation Pi

## Konzept:

Playstation 2 per Netzwerk mit einem Raspberry Pi zur Steuerung und zum streamen von Spielen via Samba (und evtl von dvd, mal abwarten) von einem USB-Speichermedium bzw. von einer Festplatte, welche per USB mit dem Raspberry Pi angeschlossen ist.
Die Steuerung erfolgt über Kurzschließen von GPIOs für einen bestimmten Zeitintervall bzw. über Relays, die gesteuert werden.
Die LEDs werden über GPIOs gesteuert, die jeweils ein- oder ausgeschaltet werden.
Verbunden werden die beiden Geräte über einen Netzwerkswitch, welcher ebenfalls mit verbaut wird.

## Backlog:

- Evtl nötige Ausgaben:
	- 1 Netzteil 12V 5-10A (10-20€)
	- Multitap wäre weniger Frickelarbeit und billiger (7-8€)
	- 1-2 Fans für Kühlung
	- 2x(?) USB verl. Kabel (~1€/p max)
	- Flachband ethernet Kabel (kann ich die nicht evtl doch noch durch IDE-Flachband o.ä. ersetzen? bzw. selbst crimpen? (unerheblich-70ct/1x25cm)
	- ethernet Kupplung/ethernet male-female Kabel (0,6-1€)
	- PS2 to HDMI Adapter (5€)
	- HDMI female female (2x0,6€)
	- zwei Eisenplatten

### Innen:


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
	- Ja, wenn ich ne zweite Ebene ins Gehäuse baue.
		- Blechplatten:
			- 1.: Pi + Switch
			- 2.: PS2

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


### Außen:

- Kann ich den State der PS2 ordentlich ermitteln?
	- Ja, wenn ich den LED pin finde, der die rote/grüne LED auf dem front panel versorgen würde
		- an GPIO hängen und ermitteln, ob Spannung anliegt (Im Falle, dass dort 3,3V landen)
			- GPIO ist zum ermitteln von <3,3V oder >3,3V geeignet

- Was mache ich mit dem Powerbutton (bzw. Reset button, falls vorhanden)
	- Brauche ich mehr status LEDs?
		- Benötigt:
			- Status des Pis
			- Status der PS2 (on/off)
			- Load des Pis
			- Lade d. PS2  "offen/zu" (dies ist eh nur noch emuliert)
		- Habe ich:
			- Power LED des Gehäuses
			- HDD LED des Gehäuses
				- Load des Extra-Massenspeichers abbilden?
			- LED Ring
				- PS2 an?
				- Lade offen/zu?
				- (Fancy Animations bei Statusänderungen?)

	- LED Ring für Designkram und so vorne drankleben?
		- XBOX 360 Ring Startanimation beim Start der PS2 nachbauen?
		- Was zeige ich wie an?
			- Ist das sinnvoll?

- (Wie) führe ich die Controller/Memcard Ports nach Außen?
	- Extension cords existieren bei aliexpress
	- Passt das alles mit dem anderen Kram in das Gehäuse? Wo soll das alles hin?

- Wie führe ich Video/audio nach Außen?
	- HDMI Adapter und HDMI nach außen legen!	

- Wie führe ich Ethernet nach außen?
	- Kabel von hinten und Kupplung an Blende heißklebern...

- Strom/Video/Eth/USB auf ne I/O Blende?
	- Strom evtl nicht so, dafür eher PSUplatz benutzen
	- Video/Eth sind sinnvoll
	- blanke I/O Blende bei thingiverse ziehen und modifizieren?

- USB Ports?
	- Vorne: Pi?
		- Kabel zerschneiden notwendig? (Vermutlich ja :/)
	- Hinten: PS2?
		- USB verl. Kabel nötig

## Done:

### Innen:
! Die Ps2 startet nur wenn man sie lang genug mit Strom maltretiert.
	Solved: Dicken Kondensator zwischen + und - vom Stepdown angeschlossen

### Außen:

! Kann ich die FP LEDs/den FP switch mit dem Pi sinnvoll betreiben?
	- (Angaben nach https://developer-blog.net/wp-content/uploads/2013/09/raspberry-pi-rev2-gpio-pinout.jpg )
	- LEDs leuchten erfolgreich und Switch switched:
		- exportieren der GPIOS 11, 25 und 10 notwendig
		- HDD LED an: GND/GPIO11
		- Power LED an: GND/GPIO25
		- Switch an: GPIO10/3V3(P17)	
