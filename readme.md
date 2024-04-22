# Taschenrechner Challenge
### Dieses Projekt dient einer Studie zur Nutzung von ChatGPT im Bezug auf angehende Programmierer:innen und ist Teil der Bachelorarbeit von Dominic Hauser.

## Aufgabenstellung
Ihre Aufgabe ist es, einen Taschenrechner mit den vier Grundrechenarten (addieren, subtrahieren, multiplizieren, dividieren) in Python zu programmieren.
Für diese Aufgabe steht Ihnen ein Startercode (Datei `taschenrechner.py`) zur Verfügung und Sie haben 60 Minuten Zeit. 

Sie müssen _nicht_ alle Teilaufgaben lösen! Versuchen Sie einfach, so viele wie möglich innerhalb der Zeit zu schaffen.

Als Hilfestellung dürfen Sie sowohl [Google](https://google.de) als auch [ChatGPT](http://chat.openai.com) verwenden!
Besonders ChatGPT kann eine sehr große Hilfe bei der Bewältigung dieser Challenge darstellen. <br>
Falls Sie noch keine Erfahrungen damit haben, stellen Sie Ihre Fragen an ChatGPT so, wie Sie diese auch mündliche formulieren würden.
Beispielsweise `Bei welcher Temparatur kocht Wasser?` oder `Welche Programmiersprache ist die beste?`.

## Schritt für Schritt Anleitung
Klicken Sie auf folgenden Link und wählen Sie anschließend am oberen rechten Rand "Fork" aus: [REPLIT](https://replit.com/@Domsaurus/Taschenrechner-Challenge)

In der vorbereiteten Datei `taschenrechner.py` finden Sie einige vordefinierte Funktionen. Sie sollen diese Funktionen fertig implementieren 
und in der `main()` Funktion zu einem sinnvollen Programm zusammenfügen. Ich empfehle Ihnen, zuerst die einzelnen Funktionen zu programmieren 
und danach die `main()` - dies ist jedoch völlig Ihnen überlassen. 

Zum ausführen der Anwedung können Sie einfach den grünen `Run`Button in Replit verwenden.
Um Ihre Datei zu testen, können Sie in der `shell` folgenden Befehl nutzen: `pytest`.

### Funktionen addieren( ), subtrahieren( ), multiplizieren( ) und dividieren( )
Die Funktionen `addieren()`, `subtrahieren()`, `multiplizieren()` und `dividieren()` sollen Zwei Zahlen entgegennehmen und das
jeweilige Ergebnis mittels `return` an die `main()`Funktion zurückgeben.

### Funktion zahl_abfragen( )
Die Funktion `zahl_abfragen()` soll eine Zahl von den Nutzern abfragen und ebenfalls mittels `return` an die Main Funktion zurückgeben.
Hierzu können Sie gerne die Funktion `get_float()` aus der CS50 Bibliothek importieren und nutzen! 

### Funktion rechenart_abfragen( )
Die Funktion `rechenart_abfragen()` soll die Nutzer fragen, welche mathematische Operation durchgeführt werden soll:
1. addieren
2. subtrahieren
3. multiplizieren
4. dividieren

Dies soll durch Eingabe der jeweiligen Zahl (z.B. 1 für addieren) geschehen.
Beachten Sie: Es dürfen NUR die Zahlen `1, 2, 3 und 4` als Eingabe akzeptiert werden!
Sollten die User eine andere Eingabe tätigen, muss die Abfrage wiederholt werden. <br>
Erst wenn eine korrekte Eingabe erfolgt, soll diese per `return` an die `main()` Funktion zurückgegeben werden.

Dies könnte in etwa so aussehen:
~~~shell
Was möchten Sie tun:
1: addieren
2: subtrahieren
3: multiplizieren
4: dividieren

Eingabe: 5

Fehlerhafte Eingabe, bitte wähle 1, 2, 3 oder 4!
Was möchten Sie tun:
1: addieren
2: subtrahieren
3: multiplizieren
4: dividieren

Eingabe: a

Was möchten Sie tun:
1: addieren
2: subtrahieren
3: multiplizieren
4: dividieren
~~~
Sollte Ihnen die Überprüfung der Eingabe zu schwer sein, können Sie hierzu ChatGPT befragen oder diese auch auslassen und nur die Nutzereingabe per `return` zurückgeben.

### main( ) 
Innerhalb der `main()` Funktion sollen Sie nun die anderen Funktionen nutzen und zu einem sinnvollen Ablauf zusammenführen. <br>
Beachten Sie dabei folgende Punkte:
- Fragen Sie zwei Zahlen vom Nutzer mit der Funktion zahl_abfragen() ab
- Führen Sie die vom Nutzer gewünschte Rechenoperation aus
- Geben Sie das Ergebnis aus
- Am Ende soll gefragt werden, ob die Nutzer eine weitere Berechnung durchführen wollen.
  - Fragen Sie dazu wieder eine Zahl ab. Wenn die Nutzer `0` eingeben, soll das Programm enden. 
  - Wenn die Nutzer `1` eingeben, soll alles von vorne starten. 

Falls Sie sich nicht sicher sind, wie Sie die wiederholte Durchführung umsetzen sollen, können Sie dazu gerne ChatGPT befragen oder diese Teil der Aufgabe auslassen.

Ein kompletter Ablauf könnte folgendermaßen aussehen:
~~~shell
$ taschenrechner.py
Bitte geben Sie die erste Zahl ein:
Eingabe: 31
Bitte geben Sie die zweite Zahl ein:
Eingabe: 11
Was möchten Sie tun:
1: addieren
2: subtrahieren
3: multiplizieren
4: dividieren
1
Ergebnis: 42.0
Wollen Sie weitere Berechnungen durchführen? Gebe 1 für ja, 0 für nein! 
Eingabe: 0

Process finished 
~~~

# VIEL ERFOLG UND VIELEN DANK!
