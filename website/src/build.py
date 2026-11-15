#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Builds the luxyos.com coming-soon pages for every language.

Usage: python3 website/src/build.py
Writes website/index.html (English) and website/<code>/index.html for the
other languages. The pages load nothing from other websites.
"""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SITE = "https://luxyos.com/"
GITHUB = "https://github.com/nijazo/luxyos"
PAYPAL = "https://paypal.me/nijazo"

# Order of the language menu: code, native name. English is the default at /.
LANGS = [
    ("en", "English"), ("nl", "Nederlands"), ("de", "Deutsch"), ("fr", "Français"),
    ("es", "Español"), ("hr", "Hrvatski"), ("bs", "Bosanski"), ("sr", "Српски"),
    ("sq", "Shqip"), ("mk", "Македонски"), ("tr", "Türkçe"),
]

# Images: Dutch screens for Dutch, English screens for every other language.
IMG_LANG = {"nl": "nl"}

T = {}

T["en"] = dict(
    title="LuxyOS — coming soon",
    desc="LuxyOS is a fast, free and honest operating system. It only starts what you use, runs Windows programs and sends nothing without your permission.",
    home="LuxyOS, go to the home page", lang="Language", soon="Coming soon",
    h1="A fast, free and <em>honest</em> operating system.",
    intro="LuxyOS only starts what you use, runs your Windows programs and sends nothing without your permission.",
    building="We are building it. More here soon.",
    promises="What LuxyOS promises",
    fast=("Fast", "Only what you use runs. Close a program and it really stops."),
    win=("Windows programs", "Install the programs you know with a double click."),
    priv=("Privacy", "No ads and no telemetry. Nothing leaves your computer without your permission."),
    free=("Free", "LuxyOS is free. Registering is always optional."),
    look="A first look",
    look_sub="Designs of what LuxyOS will look like. Not the final product; names and numbers are examples.",
    img=dict(
        desktop=("LuxyOS desktop with the start menu open and the services panel", "Desktop with the start menu. Only the services you use are running."),
        explorer=("Explorer with Documents open: folders on the left, files with date, type and size", "Explorer: your folders and files where you expect them."),
        store=("Store with Windows programs and compatibility labels", "Store: Windows programs with honest compatibility labels."),
        privacy=("Privacy overview showing which app connected to what", "Privacy overview: see which app connected to what."),
    ),
    join="We are looking for developers and sponsors",
    join_p="LuxyOS is a free, non-commercial project. To make it real, we need people and support.",
    dev=("Developers", "Help build LuxyOS. The plans, designs and first tasks are on GitHub.", "View on GitHub"),
    spon=("Sponsors and donations", "Support the project financially. Sponsors get no influence on the product and no user data.", "Donate to LuxyOS"),
    vol="A voluntary donation to LuxyOS: the money goes to the LuxyOS project.",
    vol_small="Via PayPal (paypal.me/nijazo). A donation is voluntary and gives no rights or influence.",
    status="Where are we now?",
    status_p="LuxyOS is being designed. Our goal is a first test version in 2027. You can download it once everything works.",
    phases="Phases", steps=("Design", "Prototype", "Test version 2027", "Download"),
    foot="This website uses no cookies and does not track you.",
)

T["nl"] = dict(
    title="LuxyOS — binnenkort",
    desc="LuxyOS is een snel, gratis en eerlijk besturingssysteem. Het start alleen wat je gebruikt, draait Windows-programma's en stuurt niets door zonder jouw toestemming.",
    home="LuxyOS, naar de startpagina", lang="Taal", soon="Binnenkort",
    h1="Een snel, gratis en <em>eerlijk</em> besturingssysteem.",
    intro="LuxyOS start alleen wat jij gebruikt, draait je Windows-programma’s en stuurt niets door zonder jouw toestemming.",
    building="We bouwen eraan. Hier lees je straks meer.",
    promises="Wat LuxyOS belooft",
    fast=("Snel", "Alleen wat je gebruikt draait. Sluit je een programma, dan stopt het echt."),
    win=("Windows-programma’s", "Installeer je vertrouwde programma’s gewoon met dubbelklikken."),
    priv=("Privacy", "Geen advertenties en geen telemetrie. Niets verlaat je computer zonder jouw toestemming."),
    free=("Gratis", "LuxyOS is gratis. Registreren is altijd vrijwillig."),
    look="Een eerste blik",
    look_sub="Ontwerpen van hoe LuxyOS eruit gaat zien. Nog niet het eindproduct; namen en getallen zijn voorbeelden.",
    img=dict(
        desktop=("Bureaublad van LuxyOS met het startmenu open en het overzicht van diensten", "Bureaublad met startmenu. Alleen de diensten die je gebruikt, draaien."),
        explorer=("Verkenner met Documenten open: mappen links, bestanden met datum, type en grootte", "Verkenner: je mappen en bestanden waar je ze verwacht."),
        store=("App-winkel met Windows-programma’s en labels die zeggen of ze werken", "App-winkel: Windows-programma’s met eerlijke labels."),
        privacy=("Privacyoverzicht dat laat zien welke app waarmee verbinding maakte", "Privacyoverzicht: zie welke app waarmee verbinding maakte."),
    ),
    join="We zoeken ontwikkelaars en sponsors",
    join_p="LuxyOS is een gratis, niet-commercieel project. Om het waar te maken, hebben we mensen en steun nodig.",
    dev=("Ontwikkelaars", "Help LuxyOS bouwen. De plannen, ontwerpen en eerste taken staan op GitHub.", "Bekijk op GitHub"),
    spon=("Sponsors en donaties", "Steun het project financieel. Sponsors krijgen geen invloed op het product en geen gegevens van gebruikers.", "Donatie LuxyOS"),
    vol="Een vrijwillige donatie voor LuxyOS: het geld gaat naar het LuxyOS-project.",
    vol_small="Via PayPal (paypal.me/nijazo). Een donatie is vrijwillig en geeft geen rechten of invloed.",
    status="Waar staan we?",
    status_p="LuxyOS is in ontwerp. Ons doel is een eerste testversie in 2027. Pas als alles werkt, kun je het downloaden.",
    phases="Fasen", steps=("Ontwerp", "Prototype", "Testversie 2027", "Download"),
    foot="Deze website gebruikt geen cookies en volgt je niet.",
)

T["de"] = dict(
    title="LuxyOS — bald verfügbar",
    desc="LuxyOS ist ein schnelles, kostenloses und ehrliches Betriebssystem. Es startet nur, was du nutzt, führt Windows-Programme aus und sendet nichts ohne deine Zustimmung.",
    home="LuxyOS, zur Startseite", lang="Sprache", soon="Bald verfügbar",
    h1="Ein schnelles, kostenloses und <em>ehrliches</em> Betriebssystem.",
    intro="LuxyOS startet nur, was du nutzt, führt deine Windows-Programme aus und sendet nichts ohne deine Zustimmung.",
    building="Wir bauen daran. Bald mehr hier.",
    promises="Was LuxyOS verspricht",
    fast=("Schnell", "Nur was du nutzt, läuft. Schließt du ein Programm, wird es wirklich beendet."),
    win=("Windows-Programme", "Installiere deine vertrauten Programme einfach per Doppelklick."),
    priv=("Privatsphäre", "Keine Werbung und keine Telemetrie. Nichts verlässt deinen Computer ohne deine Zustimmung."),
    free=("Kostenlos", "LuxyOS ist kostenlos. Die Registrierung ist immer freiwillig."),
    look="Ein erster Blick",
    look_sub="Entwürfe, wie LuxyOS aussehen wird. Noch nicht das fertige Produkt; Namen und Zahlen sind Beispiele.",
    img=dict(
        desktop=("LuxyOS-Desktop mit geöffnetem Startmenü und Dienste-Übersicht", "Desktop mit Startmenü. Nur die Dienste, die du nutzt, laufen."),
        explorer=("Explorer mit geöffnetem Ordner Dokumente: Ordner links, Dateien mit Datum, Typ und Größe", "Explorer: deine Ordner und Dateien dort, wo du sie erwartest."),
        store=("Store mit Windows-Programmen und Kompatibilitätsangaben", "Store: Windows-Programme mit ehrlichen Kompatibilitätsangaben."),
        privacy=("Datenschutzübersicht, die zeigt, welche App sich womit verbunden hat", "Datenschutzübersicht: sieh, welche App sich womit verbunden hat."),
    ),
    join="Wir suchen Entwickler und Sponsoren",
    join_p="LuxyOS ist ein kostenloses, nicht-kommerzielles Projekt. Damit es Wirklichkeit wird, brauchen wir Menschen und Unterstützung.",
    dev=("Entwickler", "Hilf mit, LuxyOS zu bauen. Pläne, Entwürfe und erste Aufgaben stehen auf GitHub.", "Auf GitHub ansehen"),
    spon=("Sponsoren und Spenden", "Unterstütze das Projekt finanziell. Sponsoren erhalten keinen Einfluss auf das Produkt und keine Nutzerdaten.", "An LuxyOS spenden"),
    vol="Eine freiwillige Spende für LuxyOS: Das Geld geht an das Projekt LuxyOS.",
    vol_small="Über PayPal (paypal.me/nijazo). Eine Spende ist freiwillig und gibt keine Rechte und keinen Einfluss.",
    status="Wo stehen wir?",
    status_p="LuxyOS wird gerade entworfen. Unser Ziel ist eine erste Testversion im Jahr 2027. Herunterladen kannst du es, sobald alles funktioniert.",
    phases="Phasen", steps=("Entwurf", "Prototyp", "Testversion 2027", "Download"),
    foot="Diese Website verwendet keine Cookies und verfolgt dich nicht.",
)

NB = " "  # no-break space, used before French : ; ? !
T["fr"] = dict(
    title="LuxyOS — bientôt disponible",
    desc="LuxyOS est un système d’exploitation rapide, gratuit et honnête. Il ne démarre que ce que vous utilisez, exécute les programmes Windows et n’envoie rien sans votre permission.",
    home="LuxyOS, aller à l’accueil", lang="Langue", soon="Bientôt disponible",
    h1="Un système d’exploitation rapide, gratuit et <em>honnête</em>.",
    intro="LuxyOS ne démarre que ce que vous utilisez, exécute vos programmes Windows et n’envoie rien sans votre permission.",
    building="Nous y travaillons. Plus d’informations bientôt.",
    promises="Ce que LuxyOS promet",
    fast=("Rapide", "Seul ce que vous utilisez fonctionne. Fermez un programme, il s’arrête vraiment."),
    win=("Programmes Windows", "Installez vos programmes habituels d’un simple double-clic."),
    priv=("Vie privée", "Pas de publicité, pas de télémétrie. Rien ne quitte votre ordinateur sans votre permission."),
    free=("Gratuit", "LuxyOS est gratuit. L’inscription reste toujours facultative."),
    look="Un premier aperçu",
    look_sub=f"Des maquettes de LuxyOS. Ce n’est pas encore le produit final{NB}; les noms et les chiffres sont des exemples.",
    img=dict(
        desktop=("Bureau de LuxyOS avec le menu Démarrer ouvert et le panneau des services", "Bureau avec le menu Démarrer. Seuls les services que vous utilisez fonctionnent."),
        explorer=(f"Explorateur avec le dossier Documents ouvert{NB}: dossiers à gauche, fichiers avec date, type et taille", f"Explorateur{NB}: vos dossiers et fichiers là où vous les attendez."),
        store=("Boutique avec des programmes Windows et leurs indications de compatibilité", f"Boutique{NB}: des programmes Windows avec des indications de compatibilité honnêtes."),
        privacy=("Vue d’ensemble de la vie privée montrant quelle application s’est connectée à quoi", f"Vie privée{NB}: voyez quelle application s’est connectée à quoi."),
    ),
    join="Nous recherchons des développeurs et des sponsors",
    join_p="LuxyOS est un projet gratuit et non commercial. Pour le réaliser, nous avons besoin de personnes et de soutien.",
    dev=("Développeurs", "Aidez à construire LuxyOS. Les plans, les maquettes et les premières tâches sont sur GitHub.", "Voir sur GitHub"),
    spon=("Sponsors et dons", "Soutenez le projet financièrement. Les sponsors n’obtiennent aucune influence sur le produit ni aucune donnée d’utilisateur.", "Faire un don à LuxyOS"),
    vol=f"Un don volontaire pour LuxyOS{NB}: l’argent va au projet LuxyOS.",
    vol_small=f"Via PayPal (paypal.me/nijazo). Un don est volontaire et ne donne ni droits ni influence.",
    status=f"Où en sommes-nous{NB}?",
    status_p=f"LuxyOS est en cours de conception. Notre objectif{NB}: une première version de test en 2027. Vous pourrez le télécharger dès que tout fonctionnera.",
    phases="Étapes", steps=("Conception", "Prototype", "Version de test 2027", "Téléchargement"),
    foot="Ce site n’utilise pas de cookies et ne vous suit pas.",
)

T["es"] = dict(
    title="LuxyOS — próximamente",
    desc="LuxyOS es un sistema operativo rápido, gratuito y honesto. Solo inicia lo que usas, ejecuta programas de Windows y no envía nada sin tu permiso.",
    home="LuxyOS, ir a la página de inicio", lang="Idioma", soon="Próximamente",
    h1="Un sistema operativo rápido, gratuito y <em>honesto</em>.",
    intro="LuxyOS solo inicia lo que usas, ejecuta tus programas de Windows y no envía nada sin tu permiso.",
    building="Lo estamos construyendo. Pronto habrá más aquí.",
    promises="Lo que promete LuxyOS",
    fast=("Rápido", "Solo funciona lo que usas. Cierra un programa y se detiene de verdad."),
    win=("Programas de Windows", "Instala los programas que conoces con un doble clic."),
    priv=("Privacidad", "Sin anuncios y sin telemetría. Nada sale de tu ordenador sin tu permiso."),
    free=("Gratuito", "LuxyOS es gratuito. Registrarse siempre es opcional."),
    look="Un primer vistazo",
    look_sub="Diseños de cómo será LuxyOS. Aún no es el producto final; los nombres y las cifras son ejemplos.",
    img=dict(
        desktop=("Escritorio de LuxyOS con el menú Inicio abierto y el panel de servicios", "Escritorio con el menú Inicio. Solo funcionan los servicios que usas."),
        explorer=("Explorador con la carpeta Documentos abierta: carpetas a la izquierda, archivos con fecha, tipo y tamaño", "Explorador: tus carpetas y archivos donde los esperas."),
        store=("Tienda con programas de Windows y etiquetas de compatibilidad", "Tienda: programas de Windows con etiquetas de compatibilidad honestas."),
        privacy=("Resumen de privacidad que muestra qué aplicación se conectó a qué", "Resumen de privacidad: mira qué aplicación se conectó a qué."),
    ),
    join="Buscamos desarrolladores y patrocinadores",
    join_p="LuxyOS es un proyecto gratuito y sin ánimo de lucro. Para hacerlo realidad, necesitamos personas y apoyo.",
    dev=("Desarrolladores", "Ayuda a construir LuxyOS. Los planes, los diseños y las primeras tareas están en GitHub.", "Ver en GitHub"),
    spon=("Patrocinadores y donaciones", "Apoya el proyecto económicamente. Los patrocinadores no obtienen influencia sobre el producto ni datos de usuarios.", "Donar a LuxyOS"),
    vol="Una donación voluntaria para LuxyOS: el dinero va al proyecto LuxyOS.",
    vol_small="A través de PayPal (paypal.me/nijazo). Una donación es voluntaria y no da derechos ni influencia.",
    status="¿Dónde estamos?",
    status_p="LuxyOS está en fase de diseño. Nuestro objetivo es una primera versión de prueba en 2027. Podrás descargarlo cuando todo funcione.",
    phases="Fases", steps=("Diseño", "Prototipo", "Versión de prueba 2027", "Descarga"),
    foot="Este sitio web no usa cookies y no te rastrea.",
)

T["hr"] = dict(
    title="LuxyOS — uskoro",
    desc="LuxyOS je brz, besplatan i pošten operacijski sustav. Pokreće samo ono što koristiš, radi s Windows programima i ništa ne šalje bez tvog dopuštenja.",
    home="LuxyOS, idi na početnu stranicu", lang="Jezik", soon="Uskoro",
    h1="Brz, besplatan i <em>pošten</em> operacijski sustav.",
    intro="LuxyOS pokreće samo ono što koristiš, radi s tvojim Windows programima i ništa ne šalje bez tvog dopuštenja.",
    building="Gradimo ga. Uskoro više ovdje.",
    promises="Što LuxyOS obećava",
    fast=("Brz", "Radi samo ono što koristiš. Kad zatvoriš program, on se stvarno zaustavi."),
    win=("Windows programi", "Instaliraj poznate programe jednostavnim dvostrukim klikom."),
    priv=("Privatnost", "Bez oglasa i bez telemetrije. Ništa ne napušta tvoje računalo bez tvog dopuštenja."),
    free=("Besplatan", "LuxyOS je besplatan. Registracija je uvijek dobrovoljna."),
    look="Prvi pogled",
    look_sub="Dizajni izgleda LuxyOS-a. Još nije gotov proizvod; imena i brojevi su primjeri.",
    img=dict(
        desktop=("Radna površina LuxyOS-a s otvorenim izbornikom Start i pregledom usluga", "Radna površina s izbornikom Start. Rade samo usluge koje koristiš."),
        explorer=("Preglednik datoteka s otvorenom mapom Dokumenti: mape lijevo, datoteke s datumom, vrstom i veličinom", "Preglednik datoteka: tvoje mape i datoteke tamo gdje ih očekuješ."),
        store=("Trgovina s Windows programima i oznakama kompatibilnosti", "Trgovina: Windows programi s poštenim oznakama kompatibilnosti."),
        privacy=("Pregled privatnosti koji pokazuje koja se aplikacija s čime povezala", "Pregled privatnosti: vidi koja se aplikacija s čime povezala."),
    ),
    join="Tražimo programere i sponzore",
    join_p="LuxyOS je besplatan, nekomercijalan projekt. Da bi postao stvarnost, trebamo ljude i podršku.",
    dev=("Programeri", "Pomozi izgraditi LuxyOS. Planovi, dizajni i prvi zadaci nalaze se na GitHubu.", "Pogledaj na GitHubu"),
    spon=("Sponzori i donacije", "Podrži projekt financijski. Sponzori ne dobivaju utjecaj na proizvod ni podatke korisnika.", "Doniraj LuxyOS-u"),
    vol="Dobrovoljna donacija za LuxyOS: novac ide projektu LuxyOS.",
    vol_small="Putem PayPala (paypal.me/nijazo). Donacija je dobrovoljna i ne daje prava ni utjecaj.",
    status="Gdje smo sada?",
    status_p="LuxyOS je u fazi dizajna. Cilj nam je prva testna verzija 2027. godine. Moći ćeš ga preuzeti kad sve bude radilo.",
    phases="Faze", steps=("Dizajn", "Prototip", "Testna verzija 2027", "Preuzimanje"),
    foot="Ova web-stranica ne koristi kolačiće i ne prati te.",
)

T["bs"] = dict(
    title="LuxyOS — uskoro",
    desc="LuxyOS je brz, besplatan i pošten operativni sistem. Pokreće samo ono što koristiš, radi s Windows programima i ništa ne šalje bez tvoje dozvole.",
    home="LuxyOS, idi na početnu stranicu", lang="Jezik", soon="Uskoro",
    h1="Brz, besplatan i <em>pošten</em> operativni sistem.",
    intro="LuxyOS pokreće samo ono što koristiš, radi s tvojim Windows programima i ništa ne šalje bez tvoje dozvole.",
    building="Gradimo ga. Uskoro više ovdje.",
    promises="Šta LuxyOS obećava",
    fast=("Brz", "Radi samo ono što koristiš. Kad zatvoriš program, on se zaista ugasi."),
    win=("Windows programi", "Instaliraj poznate programe jednostavnim dvostrukim klikom."),
    priv=("Privatnost", "Bez reklama i bez telemetrije. Ništa ne napušta tvoj računar bez tvoje dozvole."),
    free=("Besplatan", "LuxyOS je besplatan. Registracija je uvijek dobrovoljna."),
    look="Prvi pogled",
    look_sub="Dizajni izgleda LuxyOS-a. Još nije gotov proizvod; imena i brojevi su primjeri.",
    img=dict(
        desktop=("Radna površina LuxyOS-a s otvorenim Start menijem i pregledom servisa", "Radna površina sa Start menijem. Rade samo servisi koje koristiš."),
        explorer=("Pretraživač datoteka s otvorenim folderom Dokumenti: folderi lijevo, datoteke s datumom, vrstom i veličinom", "Pretraživač datoteka: tvoji folderi i datoteke tamo gdje ih očekuješ."),
        store=("Prodavnica s Windows programima i oznakama kompatibilnosti", "Prodavnica: Windows programi s poštenim oznakama kompatibilnosti."),
        privacy=("Pregled privatnosti koji pokazuje koja se aplikacija s čime povezala", "Pregled privatnosti: vidi koja se aplikacija s čime povezala."),
    ),
    join="Tražimo programere i sponzore",
    join_p="LuxyOS je besplatan, nekomercijalan projekat. Da bi postao stvarnost, trebaju nam ljudi i podrška.",
    dev=("Programeri", "Pomozi izgraditi LuxyOS. Planovi, dizajni i prvi zadaci nalaze se na GitHubu.", "Pogledaj na GitHubu"),
    spon=("Sponzori i donacije", "Podrži projekat finansijski. Sponzori ne dobijaju uticaj na proizvod niti podatke korisnika.", "Doniraj LuxyOS-u"),
    vol="Dobrovoljna donacija za LuxyOS: novac ide projektu LuxyOS.",
    vol_small="Putem PayPala (paypal.me/nijazo). Donacija je dobrovoljna i ne daje prava niti uticaj.",
    status="Gdje smo sada?",
    status_p="LuxyOS je u fazi dizajna. Cilj nam je prva testna verzija 2027. godine. Moći ćeš ga preuzeti kad sve bude radilo.",
    phases="Faze", steps=("Dizajn", "Prototip", "Testna verzija 2027", "Preuzimanje"),
    foot="Ova web-stranica ne koristi kolačiće i ne prati te.",
)

T["sr"] = dict(
    title="LuxyOS — ускоро",
    desc="LuxyOS је брз, бесплатан и поштен оперативни систем. Покреће само оно што користиш, ради са Windows програмима и ништа не шаље без твоје дозволе.",
    home="LuxyOS, иди на почетну страницу", lang="Језик", soon="Ускоро",
    h1="Брз, бесплатан и <em>поштен</em> оперативни систем.",
    intro="LuxyOS покреће само оно што користиш, ради са твојим Windows програмима и ништа не шаље без твоје дозволе.",
    building="Градимо га. Ускоро више овде.",
    promises="Шта LuxyOS обећава",
    fast=("Брз", "Ради само оно што користиш. Кад затвориш програм, он се заиста угаси."),
    win=("Windows програми", "Инсталирај познате програме једноставним двоструким кликом."),
    priv=("Приватност", "Без реклама и без телеметрије. Ништа не напушта твој рачунар без твоје дозволе."),
    free=("Бесплатан", "LuxyOS је бесплатан. Регистрација је увек добровољна."),
    look="Први поглед",
    look_sub="Дизајни изгледа LuxyOS-а. Још није готов производ; имена и бројеви су примери.",
    img=dict(
        desktop=("Радна површина LuxyOS-а са отвореним Старт менијем и прегледом сервиса", "Радна површина са Старт менијем. Раде само сервиси које користиш."),
        explorer=("Претраживач датотека са отвореном фасциклом Документи: фасцикле лево, датотеке са датумом, врстом и величином", "Претраживач датотека: твоје фасцикле и датотеке тамо где их очекујеш."),
        store=("Продавница са Windows програмима и ознакама компатибилности", "Продавница: Windows програми са поштеним ознакама компатибилности."),
        privacy=("Преглед приватности који показује која се апликација са чим повезала", "Преглед приватности: види која се апликација са чим повезала."),
    ),
    join="Тражимо програмере и спонзоре",
    join_p="LuxyOS је бесплатан, некомерцијалан пројекат. Да би постао стварност, потребни су нам људи и подршка.",
    dev=("Програмери", "Помози да се изгради LuxyOS. Планови, дизајни и први задаци налазе се на GitHub-у.", "Погледај на GitHub-у"),
    spon=("Спонзори и донације", "Подржи пројекат финансијски. Спонзори не добијају утицај на производ нити податке корисника.", "Донирај LuxyOS-у"),
    vol="Добровољна донација за LuxyOS: новац иде пројекту LuxyOS.",
    vol_small="Преко PayPal-а (paypal.me/nijazo). Донација је добровољна и не даје права нити утицај.",
    status="Где смо сада?",
    status_p="LuxyOS је у фази дизајна. Циљ нам је прва тест верзија 2027. године. Моћи ћеш да га преузмеш кад све буде радило.",
    phases="Фазе", steps=("Дизајн", "Прототип", "Тест верзија 2027", "Преузимање"),
    foot="Овај сајт не користи колачиће и не прати те.",
)

T["sq"] = dict(
    title="LuxyOS — së shpejti",
    desc="LuxyOS është një sistem operativ i shpejtë, falas dhe i ndershëm. Nis vetëm atë që përdor, punon me programet e Windows dhe nuk dërgon asgjë pa lejen tënde.",
    home="LuxyOS, shko te faqja kryesore", lang="Gjuha", soon="Së shpejti",
    h1="Një sistem operativ i shpejtë, falas dhe <em>i ndershëm</em>.",
    intro="LuxyOS nis vetëm atë që përdor, punon me programet e tua të Windows dhe nuk dërgon asgjë pa lejen tënde.",
    building="Po e ndërtojmë. Së shpejti më shumë këtu.",
    promises="Çfarë premton LuxyOS",
    fast=("I shpejtë", "Punon vetëm ajo që përdor. Kur mbyll një program, ai ndalon vërtet."),
    win=("Programet e Windows", "Instalo programet që njeh me një klikim të dyfishtë."),
    priv=("Privatësia", "Pa reklama dhe pa telemetri. Asgjë nuk largohet nga kompjuteri yt pa lejen tënde."),
    free=("Falas", "LuxyOS është falas. Regjistrimi është gjithmonë vullnetar."),
    look="Një vështrim i parë",
    look_sub="Dizajne se si do të duket LuxyOS. Ende jo produkti përfundimtar; emrat dhe numrat janë shembuj.",
    img=dict(
        desktop=("Desktopi i LuxyOS me menynë Start të hapur dhe panelin e shërbimeve", "Desktopi me menynë Start. Punojnë vetëm shërbimet që përdor."),
        explorer=("Eksploruesi me dosjen Dokumentet të hapur: dosjet majtas, skedarët me datë, lloj dhe madhësi", "Eksploruesi: dosjet dhe skedarët e tu aty ku i pret."),
        store=("Dyqani me programe Windows dhe etiketa përputhshmërie", "Dyqani: programe Windows me etiketa të ndershme përputhshmërie."),
        privacy=("Përmbledhja e privatësisë që tregon cili aplikacion u lidh me çfarë", "Përmbledhja e privatësisë: shih cili aplikacion u lidh me çfarë."),
    ),
    join="Kërkojmë zhvillues dhe sponsorë",
    join_p="LuxyOS është një projekt falas dhe jofitimprurës. Për ta bërë realitet, na duhen njerëz dhe mbështetje.",
    dev=("Zhvilluesit", "Ndihmo të ndërtojmë LuxyOS. Planet, dizajnet dhe detyrat e para janë në GitHub.", "Shiko në GitHub"),
    spon=("Sponsorë dhe dhurime", "Mbështet projektin financiarisht. Sponsorët nuk marrin ndikim mbi produktin dhe as të dhëna të përdoruesve.", "Dhuro për LuxyOS"),
    vol="Një dhurim vullnetar për LuxyOS: paratë shkojnë te projekti LuxyOS.",
    vol_small="Përmes PayPal (paypal.me/nijazo). Një dhurim është vullnetar dhe nuk jep të drejta apo ndikim.",
    status="Ku jemi tani?",
    status_p="LuxyOS është në fazën e dizajnit. Synimi ynë është një version i parë testues në vitin 2027. Mund ta shkarkosh sapo gjithçka të funksionojë.",
    phases="Fazat", steps=("Dizajni", "Prototipi", "Versioni testues 2027", "Shkarkimi"),
    foot="Kjo faqe interneti nuk përdor cookies dhe nuk të gjurmon.",
)

T["mk"] = dict(
    title="LuxyOS — наскоро",
    desc="LuxyOS е брз, бесплатен и чесен оперативен систем. Го стартува само она што го користиш, работи со Windows програми и не испраќа ништо без твоја дозвола.",
    home="LuxyOS, оди на почетната страница", lang="Јазик", soon="Наскоро",
    h1="Брз, бесплатен и <em>чесен</em> оперативен систем.",
    intro="LuxyOS го стартува само она што го користиш, работи со твоите Windows програми и не испраќа ништо без твоја дозвола.",
    building="Го градиме. Наскоро повеќе тука.",
    promises="Што ветува LuxyOS",
    fast=("Брз", "Работи само она што го користиш. Кога ќе затвориш програма, таа навистина запира."),
    win=("Windows програми", "Инсталирај ги програмите што ги знаеш со двоен клик."),
    priv=("Приватност", "Без реклами и без телеметрија. Ништо не го напушта твојот компјутер без твоја дозвола."),
    free=("Бесплатен", "LuxyOS е бесплатен. Регистрацијата е секогаш доброволна."),
    look="Прв поглед",
    look_sub="Дизајни за тоа како ќе изгледа LuxyOS. Сè уште не е конечниот производ; имињата и бројките се примери.",
    img=dict(
        desktop=("Работна површина на LuxyOS со отворено Старт мени и преглед на услугите", "Работна површина со Старт менито. Работат само услугите што ги користиш."),
        explorer=("Прегледувач на датотеки со отворена папка Документи: папки лево, датотеки со датум, тип и големина", "Прегледувач на датотеки: твоите папки и датотеки таму каде што ги очекуваш."),
        store=("Продавница со Windows програми и ознаки за компатибилност", "Продавница: Windows програми со чесни ознаки за компатибилност."),
        privacy=("Преглед на приватноста што покажува која апликација со што се поврзала", "Преглед на приватноста: види која апликација со што се поврзала."),
    ),
    join="Бараме програмери и спонзори",
    join_p="LuxyOS е бесплатен, некомерцијален проект. За да стане реалност, ни требаат луѓе и поддршка.",
    dev=("Програмери", "Помогни да се изгради LuxyOS. Плановите, дизајните и првите задачи се на GitHub.", "Види на GitHub"),
    spon=("Спонзори и донации", "Поддржи го проектот финансиски. Спонзорите не добиваат влијание врз производот ниту податоци за корисниците.", "Донирај за LuxyOS"),
    vol="Доброволна донација за LuxyOS: парите одат во проектот LuxyOS.",
    vol_small="Преку PayPal (paypal.me/nijazo). Донацијата е доброволна и не дава права ниту влијание.",
    status="Каде сме сега?",
    status_p="LuxyOS е во фаза на дизајн. Нашата цел е прва тест-верзија во 2027 година. Ќе можеш да го преземеш штом сè ќе работи.",
    phases="Фази", steps=("Дизајн", "Прототип", "Тест-верзија 2027", "Преземање"),
    foot="Оваа веб-страница не користи колачиња и не те следи.",
)

T["tr"] = dict(
    title="LuxyOS — çok yakında",
    desc="LuxyOS hızlı, ücretsiz ve dürüst bir işletim sistemidir. Yalnızca kullandığını başlatır, Windows programlarını çalıştırır ve iznin olmadan hiçbir şey göndermez.",
    home="LuxyOS, ana sayfaya git", lang="Dil", soon="Çok yakında",
    h1="Hızlı, ücretsiz ve <em>dürüst</em> bir işletim sistemi.",
    intro="LuxyOS yalnızca kullandığını başlatır, Windows programlarını çalıştırır ve iznin olmadan hiçbir şey göndermez.",
    building="Üzerinde çalışıyoruz. Yakında burada daha fazlası olacak.",
    promises="LuxyOS’un vaatleri",
    fast=("Hızlı", "Yalnızca kullandığın şey çalışır. Bir programı kapattığında gerçekten durur."),
    win=("Windows programları", "Bildiğin programları çift tıklamayla kur."),
    priv=("Gizlilik", "Reklam yok, telemetri yok. İznin olmadan hiçbir şey bilgisayarından çıkmaz."),
    free=("Ücretsiz", "LuxyOS ücretsizdir. Kayıt olmak her zaman isteğe bağlıdır."),
    look="İlk bakış",
    look_sub="LuxyOS’un nasıl görüneceğine dair tasarımlar. Henüz son ürün değil; adlar ve sayılar örnektir.",
    img=dict(
        desktop=("Başlat menüsü ve hizmetler paneli açık LuxyOS masaüstü", "Başlat menüsüyle masaüstü. Yalnızca kullandığın hizmetler çalışır."),
        explorer=("Belgeler klasörü açık Dosya Gezgini: solda klasörler, tarih, tür ve boyutla dosyalar", "Dosya Gezgini: klasörlerin ve dosyaların beklediğin yerde."),
        store=("Windows programları ve uyumluluk etiketleri olan mağaza", "Mağaza: dürüst uyumluluk etiketleriyle Windows programları."),
        privacy=("Hangi uygulamanın neye bağlandığını gösteren gizlilik özeti", "Gizlilik özeti: hangi uygulamanın neye bağlandığını gör."),
    ),
    join="Geliştirici ve sponsor arıyoruz",
    join_p="LuxyOS ücretsiz ve ticari olmayan bir projedir. Hayata geçirmek için insanlara ve desteğe ihtiyacımız var.",
    dev=("Geliştiriciler", "LuxyOS’u birlikte inşa et. Planlar, tasarımlar ve ilk görevler GitHub’da.", "GitHub’da gör"),
    spon=("Sponsorlar ve bağışlar", "Projeyi maddi olarak destekle. Sponsorlar ürün üzerinde etki ya da kullanıcı verisi elde etmez.", "LuxyOS’a bağış yap"),
    vol="LuxyOS için gönüllü bir bağış: para LuxyOS projesine gider.",
    vol_small="PayPal üzerinden (paypal.me/nijazo). Bağış gönüllüdür ve hiçbir hak ya da etki sağlamaz.",
    status="Şu an neredeyiz?",
    status_p="LuxyOS tasarım aşamasında. Hedefimiz 2027’de ilk test sürümü. Her şey çalıştığında indirebileceksin.",
    phases="Aşamalar", steps=("Tasarım", "Prototip", "Test sürümü 2027", "İndirme"),
    foot="Bu web sitesi çerez kullanmaz ve seni izlemez.",
)

CSS = r"""
:root {
  --zon: #F5A524; --nacht: #13243b; --hemel: #2563c9;
  --bg: #ffffff; --bg-zacht: #eef4fb; --tekst: #13243b; --tekst-zacht: #3d4b61;
  --rand: #dfe5ee; --kaart: #ffffff; --ring: #13243b;
}
@media (prefers-color-scheme: dark) {
  :root { --bg: #0e1828; --bg-zacht: #13213a; --tekst: #f1f5fb; --tekst-zacht: #c3cedd; --rand: #26354f; --kaart: #15233b; --ring: #ffffff; --hemel: #8fb8ff; }
}
/* Logo animation: the ring loads, then the sun switches on */
@keyframes lxRing { from { stroke-dashoffset: 99; } to { stroke-dashoffset: 0; } }
@keyframes lxSun { 0%, 68% { opacity: 0; transform: scale(0.2); } 84% { opacity: 1; transform: scale(1.35); } 100% { opacity: 1; transform: scale(1); } }
@keyframes lxGlow { 0%, 72% { opacity: 0; transform: scale(0.4); } 88% { opacity: 0.55; transform: scale(1.5); } 100% { opacity: 0.28; transform: scale(1.15); } }
.lx-ring { animation: lxRing 1.1s cubic-bezier(.4,0,.2,1) both; }
.lx-sun, .lx-glow { transform-box: fill-box; transform-origin: center; }
.lx-sun { animation: lxSun 1.6s ease-out both; }
.lx-glow { animation: lxGlow 1.6s ease-out both; }
@media (prefers-reduced-motion: reduce) { .lx-ring, .lx-sun, .lx-glow { animation: none; } }
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--bg); color: var(--tekst); font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif; line-height: 1.5; }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px; }
header .wrap { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-top: 22px; padding-bottom: 22px; }
.merk { display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--tekst); }
.merk svg { width: 44px; height: 44px; color: var(--ring); }
.woordmerk { font-size: 24px; font-weight: 800; letter-spacing: -0.01em; }
.woordmerk span { font-weight: 400; color: var(--hemel); }
.rechts { display: flex; align-items: center; gap: 10px; }
.label { white-space: nowrap; display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; border-radius: 999px; background: var(--bg-zacht); color: var(--tekst); font-size: 14px; font-weight: 600; }
.label i { width: 8px; height: 8px; border-radius: 50%; background: var(--zon); display: inline-block; }
/* Language menu: works without JavaScript */
.talen { position: relative; }
.talen summary { list-style: none; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border: 1px solid var(--rand); border-radius: 999px; font-size: 13px; font-weight: 700; color: var(--tekst); user-select: none; }
.talen summary::-webkit-details-marker { display: none; }
.talen summary::after { content: ""; width: 7px; height: 7px; border-right: 2px solid currentColor; border-bottom: 2px solid currentColor; transform: translateY(-2px) rotate(45deg); }
.talen[open] summary::after { transform: translateY(1px) rotate(-135deg); }
.talen summary:focus-visible { outline: 3px solid var(--zon); outline-offset: 2px; }
.talen ul { position: absolute; right: 0; top: calc(100% + 8px); z-index: 10; margin: 0; padding: 6px; list-style: none; min-width: 180px; background: var(--kaart); border: 1px solid var(--rand); border-radius: 12px; box-shadow: 0 12px 32px rgba(10,20,40,0.18); }
.talen a { display: flex; justify-content: space-between; gap: 12px; padding: 8px 10px; border-radius: 8px; color: var(--tekst); text-decoration: none; font-size: 14px; }
.talen a span { color: var(--tekst-zacht); font-size: 12px; font-weight: 600; text-transform: uppercase; }
.talen a:hover { background: var(--bg-zacht); }
.talen a[aria-current] { font-weight: 700; background: var(--bg-zacht); }
.hero { position: relative; overflow: hidden; background: var(--bg-zacht); }
.hero .label { background: var(--kaart); border: 1px solid var(--rand); }
.hero .wrap { position: relative; z-index: 1; padding-top: 72px; padding-bottom: 200px; display: flex; flex-direction: column; align-items: flex-start; gap: 20px; }
h1 { margin: 0; font-size: clamp(34px, 6vw, 64px); line-height: 1.05; letter-spacing: -0.02em; font-weight: 800; max-width: 860px; overflow-wrap: break-word; hyphens: auto; }
h1 em { font-style: normal; color: var(--hemel); }
.intro { margin: 0; max-width: 640px; font-size: clamp(17px, 2.2vw, 20px); color: var(--tekst-zacht); }
.heuvels { position: absolute; left: 0; right: 0; bottom: 0; width: 100%; height: 180px; display: block; }
.zon { position: absolute; right: 12%; bottom: 96px; width: 120px; height: 120px; border-radius: 50%; background: var(--zon); opacity: 0.85; }
section.beloftes .wrap { padding-top: 64px; padding-bottom: 24px; }
h2 { margin: 0 0 24px; font-size: clamp(24px, 3.4vw, 32px); letter-spacing: -0.01em; }
.raster { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; }
.kaart { background: var(--kaart); border: 1px solid var(--rand); border-radius: 16px; padding: 22px; display: flex; flex-direction: column; gap: 10px; }
.kaart > svg { width: 40px; height: 40px; color: var(--hemel); }
.kaart h3 { margin: 0; font-size: 18px; }
.kaart p { margin: 0; color: var(--tekst-zacht); font-size: 15px; }
section.blik .wrap { padding-top: 40px; padding-bottom: 8px; }
.blik .sub, .mee .sub { margin: -14px 0 22px; color: var(--tekst-zacht); max-width: 680px; }
.blik figure { margin: 0; }
.blik a { display: block; border-radius: 12px; }
.blik a:focus-visible, .knop:focus-visible { outline: 3px solid var(--zon); outline-offset: 3px; }
.blik img { display: block; width: 100%; height: auto; border-radius: 12px; border: 1px solid var(--rand); box-shadow: 0 10px 30px rgba(19,36,59,0.12); background: var(--bg-zacht); }
.blik figcaption { margin-top: 10px; font-size: 14px; color: var(--tekst-zacht); }
.raster3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 22px; margin-top: 26px; }
section.mee .wrap { padding-top: 56px; padding-bottom: 8px; }
.raster2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 18px; }
.mee .kaart { padding: 26px; gap: 12px; }
.mee .kaart .knop { align-self: flex-start; }
.vrijwillig { margin: 0; padding: 10px 12px; border-radius: 10px; background: var(--bg-zacht); font-size: 14px; font-weight: 600; color: var(--tekst); }
.klein { margin: 0; font-size: 13px; color: var(--tekst-zacht); }
.knop { display: inline-flex; align-items: center; gap: 10px; padding: 13px 20px; border-radius: 12px; background: var(--hemel); color: #ffffff; font-weight: 700; font-size: 16px; text-decoration: none; }
.knop.tweede { background: var(--nacht); }
.knop:hover { filter: brightness(1.08); }
.knop svg { width: 20px; height: 20px; flex-shrink: 0; }
@media (prefers-color-scheme: dark) { .knop { color: #0e1828; } .knop.tweede { background: #ffffff; } }
section.status .wrap { padding-top: 40px; padding-bottom: 72px; }
.status-blok { border-radius: 18px; background: var(--nacht); color: #ffffff; padding: 32px; display: flex; flex-wrap: wrap; gap: 24px; align-items: center; justify-content: space-between; }
@media (prefers-color-scheme: dark) { .status-blok { background: #15233b; } }
.status-blok h2 { margin: 0 0 8px; color: #ffffff; }
.status-blok p { margin: 0; color: #c9d5e6; max-width: 600px; }
.stappen { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 10px; }
.stappen li { padding: 8px 14px; border-radius: 999px; background: rgba(255,255,255,0.1); font-size: 14px; font-weight: 600; }
.stappen li.nu { background: var(--zon); color: #13243b; }
.stappen li.doel { box-shadow: inset 0 0 0 2px var(--zon); }
footer { border-top: 1px solid var(--rand); }
footer .wrap { padding-top: 24px; padding-bottom: 32px; display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: space-between; color: var(--tekst-zacht); font-size: 14px; }
@media (max-width: 560px) {
  header .wrap { gap: 8px; }
  .merk { gap: 8px; }
  .merk svg { width: 34px; height: 34px; }
  .woordmerk { font-size: 20px; }
  .rechts { gap: 6px; }
  header .label { padding: 5px 10px; font-size: 13px; }
  .talen summary { padding: 5px 10px; font-size: 12px; }
  .hero .wrap { padding-top: 48px; padding-bottom: 170px; }
  .zon { width: 80px; height: 80px; right: 8%; bottom: 90px; }
  .status-blok { padding: 24px; }
  .mee .kaart { padding: 22px; }
}
@media (max-width: 380px) { header .label { display: none; } }
"""

FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%2313243b'/%3E%3Ccircle cx='32' cy='32' r='19' fill='none' stroke='%23fff' stroke-width='6' stroke-linecap='round' stroke-dasharray='89 30' transform='rotate(-30 32 32)'/%3E%3Ccircle cx='36.9' cy='13.6' r='5.5' fill='%23F5A524'/%3E%3C/svg%3E"
LOGO = '<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="21" fill="none" stroke="currentColor" stroke-opacity="0.1" stroke-width="6"/><circle class="lx-ring" cx="32" cy="32" r="21" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-dasharray="99 200" transform="rotate(-30 32 32)"/><circle class="lx-glow" cx="37.4" cy="11.7" r="10" fill="#F5A524" opacity="0.28"/><circle class="lx-sun" cx="37.4" cy="11.7" r="5.5" fill="#F5A524"/></svg>'
ICON = {
    "fast": '<path d="M3 12h4l3-7 4 14 3-7h4"/>',
    "win": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8h18M7 6h.01M10 6h.01"/>',
    "priv": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "free": '<path d="M20 12v8a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-8M2 7h20v5H2zM12 21V7M12 7H8.5a2.5 2.5 0 1 1 0-5C11 2 12 7 12 7zM12 7h3.5a2.5 2.5 0 1 0 0-5C13 2 12 7 12 7z"/>',
    "dev": '<path d="m8 9-4 3 4 3M16 9l4 3-4 3M14 5l-4 14"/>',
    "spon": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
}
GH = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/></svg>'
HEART = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + ICON["spon"] + '</svg>'
HILLS = '''<svg class="heuvels" viewBox="0 0 1440 180" preserveAspectRatio="none" aria-hidden="true">
<path d="M0 60 C 200 10, 380 70, 600 40 C 820 10, 980 80, 1180 45 C 1300 25, 1380 40, 1440 35 L1440 180 L0 180 Z" fill="#7aa3c8"/>
<path d="M0 110 C 240 60, 460 120, 720 90 C 960 60, 1180 115, 1440 80 L1440 180 L0 180 Z" fill="#4d7aa6"/>
<path d="M0 150 C 300 120, 560 160, 860 140 C 1100 125, 1300 150, 1440 135 L1440 180 L0 180 Z" fill="#2f5682"/>
</svg>'''


def e(s):
    """Escape text for HTML, keeping the <em> in the headline."""
    return html.escape(s, quote=True).replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")


def icon(key):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[key]}</svg>'


def page(code):
    t = T[code]
    root = "" if code == "en" else "../"
    def href(c):
        return f"{root}index.html" if c == "en" else f"{root}{c}/index.html"
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{SITE}{"" if c == "en" else c + "/"}">' for c, _ in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}">'
    menu = "\n".join(
        f'<li><a href="{href(c)}" hreflang="{c}" lang="{c}"{" aria-current=\"page\"" if c == code else ""}>{e(n)}<span>{c}</span></a></li>'
        for c, n in LANGS
    )
    native = dict(LANGS)[code]
    il = IMG_LANG.get(code, "en")
    def fig(key, sizes):
        alt, cap = t["img"][key]
        big = f"{root}img/{key}-{il}-1440.webp"
        small = f"{root}img/{key}-{il}-720.webp"
        return (f'<figure><a href="{big}"><img src="{big}" srcset="{small} 720w, {big} 1440w" sizes="{sizes}" '
                f'width="1440" height="900" alt="{e(alt)}" loading="lazy" decoding="async"></a><figcaption>{e(cap)}</figcaption></figure>')
    cards = "\n".join(
        f'<article class="kaart">\n{icon(k)}\n<h3>{e(t[k][0])}</h3>\n<p>{e(t[k][1])}</p>\n</article>'
        for k in ("fast", "win", "priv", "free")
    )
    steps = t["steps"]
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
{alternates}
<link rel="icon" href="{FAVICON}">
<!--
  Generated by website/src/build.py; edit that file, not this one.
  This page loads nothing from other websites: no fonts, scripts, trackers or cookies.
-->
<style>{CSS}</style>
</head>
<body>

<header>
<div class="wrap">
<a class="merk" href="{href(code)}" aria-label="{e(t["home"])}">
{LOGO}
<span class="woordmerk">Luxy<span>OS</span></span>
</a>
<div class="rechts">
<span class="label"><i aria-hidden="true"></i>{e(t["soon"])}</span>
<details class="talen">
<summary aria-label="{e(t["lang"])}: {e(native)}">{code.upper()}</summary>
<ul>
{menu}
</ul>
</details>
</div>
</div>
</header>

<main>
<section class="hero">
<div class="wrap">
<h1>{e(t["h1"])}</h1>
<p class="intro">{e(t["intro"])}</p>
<span class="label"><i aria-hidden="true"></i>{e(t["building"])}</span>
</div>
<div class="zon" aria-hidden="true"></div>
{HILLS}
</section>

<section class="beloftes">
<div class="wrap">
<h2>{e(t["promises"])}</h2>
<div class="raster">
{cards}
</div>
</div>
</section>

<section class="blik">
<div class="wrap">
<h2>{e(t["look"])}</h2>
<p class="sub">{e(t["look_sub"])}</p>
{fig("desktop", "(max-width: 1100px) 100vw, 1040px")}
<div class="raster3">
{fig("explorer", "(max-width: 700px) 100vw, 340px")}
{fig("store", "(max-width: 700px) 100vw, 340px")}
{fig("privacy", "(max-width: 700px) 100vw, 340px")}
</div>
</div>
</section>

<section class="mee" id="join">
<div class="wrap">
<h2>{e(t["join"])}</h2>
<p class="sub">{e(t["join_p"])}</p>
<div class="raster2">
<article class="kaart">
{icon("dev")}
<h3>{e(t["dev"][0])}</h3>
<p>{e(t["dev"][1])}</p>
<a class="knop tweede" href="{GITHUB}" rel="noopener">{GH}{e(t["dev"][2])}</a>
</article>
<article class="kaart">
{icon("spon")}
<h3>{e(t["spon"][0])}</h3>
<p>{e(t["spon"][1])}</p>
<p class="vrijwillig">{e(t["vol"])}</p>
<a class="knop" href="{PAYPAL}" rel="noopener">{HEART}{e(t["spon"][2])}</a>
<p class="klein">{e(t["vol_small"])}</p>
</article>
</div>
</div>
</section>

<section class="status">
<div class="wrap">
<div class="status-blok">
<div>
<h2>{e(t["status"])}</h2>
<p>{e(t["status_p"])}</p>
</div>
<ol class="stappen" aria-label="{e(t["phases"])}">
<li class="nu">1 · {e(steps[0])}</li>
<li>2 · {e(steps[1])}</li>
<li class="doel">3 · {e(steps[2])}</li>
<li>4 · {e(steps[3])}</li>
</ol>
</div>
</div>
</section>
</main>

<footer>
<div class="wrap">
<span>© 2026 LuxyOS</span>
<span>{e(t["foot"])}</span>
</div>
</footer>

</body>
</html>
"""


def main():
    keys = set(T["en"])
    for code, _ in LANGS:
        missing = keys - set(T[code])
        assert not missing, (code, missing)
        path = os.path.join(OUT, "index.html") if code == "en" else os.path.join(OUT, code, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(code))
        print("wrote", os.path.relpath(path, OUT))


if __name__ == "__main__":
    main()
