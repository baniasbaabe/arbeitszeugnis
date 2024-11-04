def get_job_reference_decoder_prompt(reference: str) -> str:
    """
    Return the prompt for decoding job references.

    Args:
        reference (str): The job reference to decode.

    Returns:
        str: The prompt for decoding job references.
    """
    return f"""
    Du bist Experte für das dekodieren deutscher Arbeitszeugnisse. Arbeitszeugnisse in Deutschland sind sehr verschlüsselt, da sie sehr wohlwollend geschrieben und nett formuliert werden müssen. Trotzdem kann man
    anhand der Formulierung die Kategorie und die Benotung herausfinden, indem man genauestens auf
    jedes Wort achtet. Betrachte die folgenden Beispiele und die jeweiige Kategorie und Note:
    --- BEGINN DER BEISPIELE ---
    Satz	Kriterium	Note
    Sein exzellentes Fachwissen hielt er durch kontinuierliche Fortbildung stets auf dem neuesten
    Kenntnisstand.	Fachwissen	1
    verfügt über ein hervorragendes und auch in angrenzenden Bereichen sehr detailliertes Fachwissen,
    dass er immer sicher und sehr effizient einsetzte.	Fachwissen	1
    In kürzester Zeit beherrschte sie die Fertigungsaufgaben an der äußerst anspruchsvollen Maschine
    sehr gut.	Fachwissen	1
    Er besitzt ein umfassendes und detailliertes Wissen, welches über das eigene Fachgebiet weit
    hinausgeht.	Fachwissen	1
    Sein gutes Fachwissen hielt er durch kontinuierliche Fortbildung stets auf dem neuesten
    Kenntnisstand.	Fachwissen	2
    verfügt über ein gutes und auch in angrenzenden Bereichen detailliertes Fachwissen, dass er
    immer sicher und sehr effizient einsetzte	Fachwissen	2
    In kürzester Zeit beherrschte sie die Fertigungsaufgaben an der äußerst anspruchsvollen Maschine
    gut	Fachwissen	2
    besitzt ein umfassendes und detailliertes Wissen, welches über das eigene Fachgebiet hinausgeht	Fachwissen	2
    Er verfügt über ein äußerst umfassendes und hervorragendes Fachwissen, das er zur Bewältigung
    seiner Aufgaben stets sehr sicher und erfolgreich einsetzte.	Fachwissen	1
    Mit seinem umfangreichen und äußerst fundierten Fachwissen erzielte er stets deutlich
    überdurchschnittliche Erfolge.	Fachwissen	1
    verfügt über ein äußerst umfassendes und sehr fundiertes Fachwissen, das er jederzeit
    hervorragend in die Praxis umzusetzen wusste. Er nahm zudem mit großem Erfolg an zahlreichen
    Fortbildungen teil.	Fachwissen	1
    Er verfügt über ein umfassendes und gutes Fachwissen, das er zur Bewältigung seiner Aufgaben
    sehr sicher und erfolgreich einsetzte.	Fachwissen	2
    Mit seinem umfangreichen und fundierten Fachwissen erzielte er stets gute Erfolge.	Fachwissen	2
    verfügt über ein umfassendes und fundiertes Fachwissen, das er jederzeit gut in die Praxis
    umzusetzen wusste.	Fachwissen	2
    Er verfügt über ein solides Fachwissen, das er zur Bewältigung seiner Aufgaben erfolgreich
    einsetzte.	Fachwissen	3
    Er wendete sein Fachwissen mit Erfolg in seinem Arbeitsgebiet an.	Fachwissen	3
    Er verfügt über ein den Anforderungen entsprechendes Fachwissen.	Fachwissen	4
    Er beherrschte seinen Arbeitsbereich entsprechend den Anforderungen.	Fachwissen	4
    Wir danken für die stets hervorragende Zusammenarbeit und bedauern es sehr, ihn als Mitarbeiter
    zu verlieren. Für seinen weiteren Berufs- und Lebensweg wünschen wir ihm alles Gute und auch
    weiterhin viel Erfolg.	Schlussformulierung	1
    Wir danken für die stets hervorragenden Leistungen und bedauern sein Ausscheiden sehr. Wir sind
    davon überzeugt, dass er auch in der Zukunft außerordentliche Erfolge erzielen wird.	Schlussformulierung	1
    Wir danken für seine wertvolle Mitarbeit und bedauern es, ihn als Mitarbeiter zu verlieren. Für
    seinen weiteren Berufs- und Lebensweg wünschen wir ihm alles Gute und auch weiterhin viel
    Erfolg.	Schlussformulierung	2
    Wir danken für die stets guten Leistungen und bedauern sein Ausscheiden sehr. Wir sind davon
    überzeugt, dass er auch in der Zukunft außerordentliche Erfolge erzielen wird.	Schlussformulierung	2
    Wir danken für die erbrachte Leistung und wünschen ihm für die Zukunft weiterhin alles Gute.	Schlussformulierung	2
    Wir danken für sein Wirken und bedauern sein Ausscheiden. Wir sind überzeugt, dass er auch in
    der Zukunft gute Erfolge erzielen wird.	Schlussformulierung	2
    Wir wünschen für die Zukunft alles Gute.	Schlussformulierung	2
    Wir danken für die Zusammenarbeit.	Schlussformulierung	2
    Sein Verhalten gegenüber Vorgesetzten, Kollegen und Externen war stets hervorragend.	Verhalten	1
    Gegenüber Vorgesetzten, Mitarbeitern und Kunden verhielt sich stets vorbildlich. Er trug zu einer
    hervorragenden und effizienten Teamarbeit bei.	Verhalten	1
    Von Vorgesetzten, Kollegen und Kunden wurde er gleichermaßen geschätzt. Er verhielt sich jederzeit
    loyal gegenüber dem Unternehmen und überzeugte durch seine persönliche Integrität. Sein Verhalten
    war immer vorbildlich. Im Kontakt mit Kunden zeichnete sich durch äußerst professionelles Auftreten
    aus.	Verhalten	1
    Sein Verhalten gegenüber Vorgesetzten, Kollegen und Externen war stets einwandfrei.	Verhalten	2
    Gegenüber Vorgesetzten, Mitarbeitern und Kunden verhielt sich stets einwandfrei. Er trug zu einer
    guten und effizienten Teamarbeit bei.	Verhalten	2
    Sein Verhalten gegenüber Vorgesetzten, Kollegen und Externen war einwandfrei.	Verhalten	3
    Sein Verhalten gegenüber Vorgesetzten, Kollegen und Externen war stets korrekt.	Verhalten	3
    Sein Verhalten gegenüber Kollegen und Vorgesetzten war zufriedenstellend.	Verhalten	4
    Sein Verhalten gegenüber Kollegen und Vorgesetzten war spannungsfrei.	Verhalten	4
    galt als hervorragende Führungskraft. Er förderte aktiv die Zusammenarbeit, förderte und informierte
    seine Mitarbeiter jederzeit umfassend und delegierte Aufgaben und Verantwortungen stets in
    angemessenem Umfang. So erreichte er stets ein hervorragendes Arbeitsergebnis.	Fuehrungsstil	1
    war ein geradliniger sowie geachteter und fürsorglicher Vorgesetzter. Er verstand es immer
    ausgezeichnet, sein Team zu motivieren und seine Abteilung zu höchster Effektivität zu bewegen.	Fuehrungsstil	1
    war für seine Mitarbeiter stets ein geschätztes Vorbild. Er führte seine Mitarbeiter zielorientiert
    und sachlich und erreichte eine außergewöhnliche Leistungssteigerung auf durchgängig hohem Niveau
    sowie eine sehr gute Teamatmosphäre.	Fuehrungsstil	1
    hat sich innerhalb kürzester Zeit in den ihm gestellten Aufgabenbereich eingearbeitet. Er verfolgte
    die vereinbarten Ziele nachhaltig und mit höchstem Erfolg.	Leistungsbereitschaft	1
    war ein stets äußerst motivierter Mitarbeiter. Schwierige Aufgaben ging er mit großem Elan an und
    fand dabei immer sinnvolle und praktikable Lösungen.	Leistungsbereitschaft	1
    Er war hochmotiviert und zeigte ein außerordentlich hohes Maß an Initiative und Leistungsbereitschaft.	Leistungsbereitschaft	1
    hat sich innerhalb kurzer Zeit in den ihm gestellten Aufgabenbereich eingearbeitet. Er verfolgte
    die vereinbarten Ziele nachhaltig und erfolgreich.	Leistungsbereitschaft	2
    war ein stets motivierter Mitarbeiter. Schwierige Aufgaben ging er mit Elan an und fand dabei
    sinnvolle und praktikable Lösungen.	Leistungsbereitschaft	2
    Er war sehr motiviert und zeigte ein hohes Maß an Initiative und Leistungsbereitschaft.	Leistungsbereitschaft	2
    hat sich engagiert in den ihm gestellten Aufgabenbereich eingearbeitet und verfolgte die
    vereinbarten Ziele nachhaltig.	Leistungsbereitschaft	3
    war motiviert und zeigte auch bei schwierigen Aufgaben Initiative und Engagement.	Leistungsbereitschaft	3
    hat sich unseren Erwartungen entsprechend in den ihm gestellten Aufgabenbereich eingearbeitet.	Leistungsbereitschaft	4
    zeigte auch Initiative und Engagement.	Leistungsbereitschaft	4
    Dabei war er auch höchstem Zeitdruck und Arbeitsaufwand stets gewachsen.	Belastbarkeit	1
    Auch in Situationen mit extrem hohem Arbeitsanfall erwies sich als sehr belastbarer Mitarbeiter
    und ging jederzeit überlegt, ruhig und zielorientiert vor.	Belastbarkeit	1
    zeichnete sich auch in extremen Stresssituationen und unter Zeitdruck stets durch hohe
    Belastbarkeit und Zielorientierung aus.	Belastbarkeit	1
    Dabei war er auch erhöhtem Zeitdruck und Arbeitsaufwand gut gewachsen.	Belastbarkeit	2
    Auch bei sehr hohem Arbeitsanfall erwies sich als belastbarer Mitarbeiter und ging überlegt,
    ruhig und zielorientiert vor.	Belastbarkeit	2
    zeichnete sich auch in extremen Stresssituationen durch hohe Belastbarkeit und Zielorientierung
    aus.	Belastbarkeit	2
    Dabei war er auch hohem Zeitdruck und Arbeitsaufwand gewachsen.	Belastbarkeit	3
    Auch bei hohem Arbeitsanfall erwies sich als belastbarer Mitarbeiter.	Belastbarkeit	3
    Dabei war er üblichem Zeitdruck und Arbeitsaufwand gewachsen.	Belastbarkeit	4
    Bei üblichem Arbeitsanfall erwies sich als zuverlässiger Mitarbeiter.	Belastbarkeit	4
    galt als gute Führungskraft. Er förderte aktiv die Zusammenarbeit, förderte und informierte seine
    Mitarbeiter umfassend und delegierte Aufgaben und Verantwortungen in angemessenem Umfang. So
    erreichte er stets ein gutes Arbeitsergebnis.	Fuehrungsstil	2
    war ein geradliniger sowie geachteter und fürsorglicher Vorgesetzter. Er verstand es immer gut,
    sein Team zu motivieren und seine Abteilung zu hoher Effektivität zu bewegen.	Fuehrungsstil	2
    war für seine Mitarbeiter stets ein Vorbild. Er führte seine Mitarbeiter zielorientiert und
    sachlich und erreichte eine gute Leistungssteigerung auf durchgängig hohem Niveau sowie eine gute
    Teamatmosphäre.	Fuehrungsstil	2
    galt als Führungskraft, die es verstand, seine Mitarbeiter zu fördern, zu informieren und Aufgaben
    sowie Verantwortung zu delegieren.	Fuehrungsstil	3
    war ein geradliniger sowie fürsorglicher Vorgesetzter. Er verstand es, sein Team zu motivieren
    und Arbeitsprozesse in seiner Abteilung zu verbessern.	Fuehrungsstil	3
    erfüllte in seiner Funktion als Führungskraft unsere Erwartungen und erzielte Erfolge bei
    umgesetzten Projekten.	Fuehrungsstil	4
    war ein fürsorglicher Vorgesetzter. Er verstand es, das Tagesgeschäft seiner Abteilung zu
    koordinieren.	Fuehrungsstil	4
    war als Führungskraft immer bemüht, klare Anweisungen zu geben und alle Arbeiten zu
    koordinieren.	Fuehrungsstil	5
    war ein fürsorglicher Vorgesetzter. Er bemühte sich stets, das Tagesgeschäft seiner Abteilung zu
    koordinieren.	Fuehrungsstil	5
    Er war äußerst zuverlässig, und sein Arbeitsstil war stets geprägt durch sehr sorgfältige
    Planung und Systematik.	Arbeitsweise	1
    Er führte alle Aufgaben stets selbständig, äußerst sorgfältig und planvoll durchdacht aus.	Arbeitsweise	1
    Er arbeitete stets sehr effizient, zielstrebig und sorgfältig und bewies ein herausragendes
    Organisationsgeschick.	Arbeitsweise	1
    Er war sehr zuverlässig, und sein Arbeitsstil war stets geprägt durch sorgfältige Planung und
    Systematik.	Arbeitsweise	2
    Mit einem guten Blick für das Wesentliche führte er seine Aufgaben immer planvoll, methodisch
    und gründlich aus.	Arbeitsweise	2
    Er arbeitete sehr effizient, zielstrebig und sorgfältig und bewies ein gutes Organisationsgeschick.	Arbeitsweise	2
    Er war zuverlässig, und sein Arbeitsstil war stets geprägt durch Planung und Systematik.	Arbeitsweise	3
    Er führte seine Aufgaben sorgfältig und planvoll aus.	Arbeitsweise	3
    Er war zuverlässig und erledigte die entscheidenden Aufgaben problemlos.	Arbeitsweise	4
    Er führte seine Aufgaben mit ausreichender Sorgfalt und Planung aus.	Arbeitsweise	4
    Er beeindruckte stets durch qualitativ und quantitativ hervorragende Ergebnisse.	Arbeitsergebnis	1
    Seine Arbeitsergebnisse waren, auch bei wechselnden Anforderungen und unter sehr schwierigen
    Bedingungen, stets von sehr guter Qualität.	Arbeitsergebnis	1
    Er war ein äußerst leistungsfähiger Mitarbeiter, dessen hervorragende Arbeitsergebnisse stets
    sowohl in qualitativer als quantitativer Hinsicht überzeugten.	Arbeitsergebnis	1
    Er lieferte stets qualitativ und quantitativ gute Ergebnisse.	Arbeitsergebnis	2
    Seine Arbeitsergebnisse waren, auch bei wechselnden Anforderungen und unter sehr schwierigen
    Bedingungen, stets von guter Qualität.	Arbeitsergebnis	2
    Er war ein leistungsfähiger Mitarbeiter, der stets überdurchschnittliche Arbeitsergebnisse
    erzielte.	Arbeitsergebnis	2
    Die Qualität seiner Arbeitsergebnisse erfüllte in vollem Umfang die an ihn gestellten
    Anforderungen.	Arbeitsergebnis	3
    Seine Arbeitsergebnisse waren von guter Qualität.	Arbeitsergebnis	3
    Er strebte gute Ergebnisse an.	Arbeitsergebnis	4
    Seine Arbeitsergebnisse entsprachen unseren Mindestanforderungen.	Arbeitsergebnis	4
    hat die ihm übertragenen Aufgaben stets zu unserer vollsten Zufriedenheit erledigt.	Gesamturteil	1
    hat seine Aufgaben stets zu unserer vollsten Zufriedenheit erledigt und unseren Erwartungen in
    jeder Hinsicht optimal entsprochen.	Gesamturteil	1
    hat unsere Erwartungen stets in jeder Hinsicht erfüllt. Wir waren mit seinen Leistungen jederzeit
    äußerst zufrieden.	Gesamturteil	1
    hat die ihm übertragenen Aufgaben stets zu unserer vollen Zufriedenheit erledigt.	Gesamturteil	2
    hat seine Aufgaben stets zu unserer vollen Zufriedenheit erledigt und unseren Erwartungen in jeder
    Hinsicht gut entsprochen.	Gesamturteil	2
    hat unsere Erwartungen stets gut erfüllt. Wir waren mit seinen Leistungen jederzeit zufrieden.	Gesamturteil	2
    hat die ihm übertragenen Aufgaben zu unserer vollen Zufriedenheit erledigt.	Gesamturteil	3
    hat seine Aufgaben zu unserer vollen Zufriedenheit erledigt und unseren Erwartungen in jeder
    Hinsicht entsprochen.	Gesamturteil	3
    hat unseren Erwartungen voll entsprochen.	Gesamturteil	3
    hat die ihm übertragenen Aufgaben zu unserer Zufriedenheit erledigt.	Gesamturteil	4
    beherrschte seinen Arbeitsbereich entsprechend den Anforderungen.	Gesamturteil	4
    hat unseren Erwartungen entsprochen.	Gesamturteil	4
    erfüllte seine Aufgaben im Allgemeinen zu unserer Zufriedenheit.	Gesamturteil	5
    hat weitestgehend unseren Anforderungen entsprochen.	Gesamturteil	5
    bemühte sich, unseren Anforderungen zu entsprechen.	Gesamturteil	6
    war stets bemüht, unseren Anforderungen gerecht zu werden.	Gesamturteil	6
    Auch unter schwierigsten Arbeitsbedingungen bewältigte er/sie alle Aufgaben in hervorragender
    Weise.	Belastbarkeit	1
    Auch unter schwierigsten Arbeitsbedingungen und stärkster Belastung erfüllte er/sie unsere
    Erwartungen in bester Weise.	Belastbarkeit	1
    Auch unter stärkster Belastung behielt er/sie die Übersicht, handelte überlegt und bewältigte alle
    Aufgaben in hervorragender Weise.	Belastbarkeit	1
    Auch unter starker Belastung behielt er/sie die Übersicht, handelte überlegt und bewältigte alle
    Aufgaben in guter Weise.	Belastbarkeit	2
    Auch starkem Arbeitsanfall war er/sie jederzeit gewachsen.	Belastbarkeit	2
    Auch unter schwierigen Arbeitsbedingungen bewältigte er/sie alle Aufgaben in guter Weise.	Belastbarkeit	2
    Auch unter starker Belastung behielt er/sie jederzeit die Übersicht, handelte überlegt und
    bewältigte alle Aufgaben stets in guter Weise.	Belastbarkeit	2
    Auch in Situationen mit großem Arbeitsaufkommen erwies er/sie sich immer als in hohem Maße
    belastbar.	Belastbarkeit	2
    Er/Sie kam auch mit schwierigen Aufgaben jedesmal gut zurecht.	Belastbarkeit	2
    Auch bei sehr hohem Arbeitsanfall erwies er/sie sich als belastbarer Mitarbeiter und ging
    überlegt, ruhig und zielorientiert vor.	Belastbarkeit	2
    Auch starkem Arbeitsanfall war er/sie gewachsen.	Belastbarkeit	3
    Auch unter schwierigen Arbeitsbedingungen und starker Belastung erfüllte er/sie unsere
    Erwartungen stets in zufrieden stellender Weise.	Belastbarkeit	3
    Auch unter starker Belastung behielt er/sie die Übersicht, handelte überlegt und bewältigte alle
    Aufgaben in zufriedenstellender Weise.	Belastbarkeit	3
    Er/Sie zeigte sich auch bei der Bewältigung neuer Aufgabenbereiche flexibel und aufgeschlossen.	Belastbarkeit	3
    Er/Sie war immer belastbar.	Belastbarkeit	3
    Auch in Situationen mit hohem Arbeitsaufkommen erweist er/sie sich als belastbar.	Belastbarkeit	3
    Er/Sie kam mit den übertragenen Aufgaben gut zurecht.	Belastbarkeit	3
    Dem üblichen Arbeitsanfall war er / sie gewachsen.	Belastbarkeit	4
    Auch unter erschwerten Arbeitsbedingungen und starker Belastung erfüllte er/sie unsere
    Erwartungen in meist zufrieden stellender Weise	Belastbarkeit	4
    Auch unter starker Belastung behielt er/sie die Übersicht, handelte überlegt und bewältigte die
    wesentlichen Aufgaben in zufrieden stellender Weise.	Belastbarkeit	4
    Auch unter schwierigen Arbeitsbedingungen und starker Belastung erfüllte er/sie unsere
    Erwartungen im Wesentlichen in zufrieden stellender Weise.	Belastbarkeit	4
    Die Arbeitsergebnisse von  waren, auch in schwierigsten Fällen und unter Termindruck, stets von
    höchster Qualität	Arbeitsergebnis	1
    Er war jederzeit, auch in schwierigsten Situationen, äußerst belastbar und handelte stets ruhig
    und überlegt	Belastbarkeit	1
    Dabei setzte er immer seine sehr guten Fachkenntnisse mit ausgezeichnetem Erfolg ein	Fachwissen	1
    Bereits nach kürzester Zeit arbeitete vollkommen selbständig und stets zuverlässig.	Arbeitsweise	2
    Er erfüllte seine Aufgaben stets mit großem Einsatz und verfolgte mit großem Erfolg die gestellten
    Ziele.	Leistungsbereitschaft	2
    arbeitete in jeder Hinsicht stets zu unserer vollsten Zufriedenheit.	Gesamturteil	1
    Sein Verhalten gegenüber Vorgesetzten und Kollegen war jederzeit vorbildlich.	Verhalten	1
    --- ENDE DER BEISPIELE ---
    Wie du siehst, kommt es auf jedes Wort im Satz an, wobei kleinste Nuancen die Note beeinflussen. Lerne aus den Sätzen. Ich gebe dir jetzt ein Arbeitszeugnis, und du musst mir die jeweilige Kategorie und Note zurückgeben.
    Bitte beachte, dass die Formulierungen sehr wohlwollend geschrieben sind. Nehme die Beispiele auch als Referenz um zu sehen, dass eine positive Formulierung
    trotzdem eine schlechte Note haben kann. Gebe dein Ergebnis als Liste von JSON in dem Format [{'kategorie': 'Kategorie1', 'note': 'note123', 'satz_aus_text': 'exakter satz aus dem arbeitszeugnis'}, {...}]. Die Elemente
    sollen sortiert nach ihrem Vorkommen im Text sein. Bitte gebe nur die Liste aus, ohne weitere Sätze oder Gerede. Beachte, dass die Kriterien nur den Kriterien entsprechen dürfen wie die Beispiele die ich dir
    gegeben habe..
    Hier ist das Arbeitszeugnis, welches du entschlüsseln musst, wobei du wirklich auf jedes Wort achten musst und auch die Beispiele als Referenz benutzen kannst:
    {reference}
    Bitte gebe dein Bestes, mein Job hängt davon ab. Du kriegst auch 200 Dollar als Trinkgeld. Denke Schritt für Schritt.
"""
