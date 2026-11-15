#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Builds the luxyos.com coming-soon pages for every language.

Usage:
  python3 website/src/build.py
  python3 build.py --out /path/to/webroot --supporters /private/supporters.private.json

Writes index.html (English) and <code>/index.html for the other languages into
the output folder (default: website/). The pages load nothing from other
websites. The supporters list is read from --supporters, or else from
supporters.private.json next to this script, or else the empty public
supporters.json.
"""
import argparse
import datetime
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SITE = "https://luxyos.com/"
GITHUB = "https://github.com/nijazo/luxyos"
PAYPAL = "https://paypal.me/NOmanovic"
# Address donors write to when they want to be removed from the supporters list.
# The supporters block only appears on the site once this is filled in.
CONTACT = "sponsors@luxyos.com"

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
    join="We are looking for developers and sponsors",
    join_p="LuxyOS is a free, non-commercial project. To make it real, we need people and support.",
    dev=("Developers", "Help build LuxyOS. The plans, designs and first tasks are on GitHub.", "View on GitHub"),
    spon=("Sponsors and donations", "Support the project financially. Sponsors get no influence on the product and no user data.", "Donate to LuxyOS"),
    vol="A voluntary donation to LuxyOS: the money goes to the LuxyOS project.",
    vol_small="Via PayPal (paypal.me/NOmanovic). A donation is voluntary and gives no rights or influence.",
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
    join="We zoeken ontwikkelaars en sponsors",
    join_p="LuxyOS is een gratis, niet-commercieel project. Om het waar te maken, hebben we mensen en steun nodig.",
    dev=("Ontwikkelaars", "Help LuxyOS bouwen. De plannen, ontwerpen en eerste taken staan op GitHub.", "Bekijk op GitHub"),
    spon=("Sponsors en donaties", "Steun het project financieel. Sponsors krijgen geen invloed op het product en geen gegevens van gebruikers.", "Donatie LuxyOS"),
    vol="Een vrijwillige donatie voor LuxyOS: het geld gaat naar het LuxyOS-project.",
    vol_small="Via PayPal (paypal.me/NOmanovic). Een donatie is vrijwillig en geeft geen rechten of invloed.",
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
    join="Wir suchen Entwickler und Sponsoren",
    join_p="LuxyOS ist ein kostenloses, nicht-kommerzielles Projekt. Damit es Wirklichkeit wird, brauchen wir Menschen und Unterstützung.",
    dev=("Entwickler", "Hilf mit, LuxyOS zu bauen. Pläne, Entwürfe und erste Aufgaben stehen auf GitHub.", "Auf GitHub ansehen"),
    spon=("Sponsoren und Spenden", "Unterstütze das Projekt finanziell. Sponsoren erhalten keinen Einfluss auf das Produkt und keine Nutzerdaten.", "An LuxyOS spenden"),
    vol="Eine freiwillige Spende für LuxyOS: Das Geld geht an das Projekt LuxyOS.",
    vol_small="Über PayPal (paypal.me/NOmanovic). Eine Spende ist freiwillig und gibt keine Rechte und keinen Einfluss.",
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
    join="Nous recherchons des développeurs et des sponsors",
    join_p="LuxyOS est un projet gratuit et non commercial. Pour le réaliser, nous avons besoin de personnes et de soutien.",
    dev=("Développeurs", "Aidez à construire LuxyOS. Les plans, les maquettes et les premières tâches sont sur GitHub.", "Voir sur GitHub"),
    spon=("Sponsors et dons", "Soutenez le projet financièrement. Les sponsors n’obtiennent aucune influence sur le produit ni aucune donnée d’utilisateur.", "Faire un don à LuxyOS"),
    vol=f"Un don volontaire pour LuxyOS{NB}: l’argent va au projet LuxyOS.",
    vol_small=f"Via PayPal (paypal.me/NOmanovic). Un don est volontaire et ne donne ni droits ni influence.",
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
    join="Buscamos desarrolladores y patrocinadores",
    join_p="LuxyOS es un proyecto gratuito y sin ánimo de lucro. Para hacerlo realidad, necesitamos personas y apoyo.",
    dev=("Desarrolladores", "Ayuda a construir LuxyOS. Los planes, los diseños y las primeras tareas están en GitHub.", "Ver en GitHub"),
    spon=("Patrocinadores y donaciones", "Apoya el proyecto económicamente. Los patrocinadores no obtienen influencia sobre el producto ni datos de usuarios.", "Donar a LuxyOS"),
    vol="Una donación voluntaria para LuxyOS: el dinero va al proyecto LuxyOS.",
    vol_small="A través de PayPal (paypal.me/NOmanovic). Una donación es voluntaria y no da derechos ni influencia.",
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
    join="Tražimo programere i sponzore",
    join_p="LuxyOS je besplatan, nekomercijalan projekt. Da bi postao stvarnost, trebamo ljude i podršku.",
    dev=("Programeri", "Pomozi izgraditi LuxyOS. Planovi, dizajni i prvi zadaci nalaze se na GitHubu.", "Pogledaj na GitHubu"),
    spon=("Sponzori i donacije", "Podrži projekt financijski. Sponzori ne dobivaju utjecaj na proizvod ni podatke korisnika.", "Doniraj LuxyOS-u"),
    vol="Dobrovoljna donacija za LuxyOS: novac ide projektu LuxyOS.",
    vol_small="Putem PayPala (paypal.me/NOmanovic). Donacija je dobrovoljna i ne daje prava ni utjecaj.",
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
    join="Tražimo programere i sponzore",
    join_p="LuxyOS je besplatan, nekomercijalan projekat. Da bi postao stvarnost, trebaju nam ljudi i podrška.",
    dev=("Programeri", "Pomozi izgraditi LuxyOS. Planovi, dizajni i prvi zadaci nalaze se na GitHubu.", "Pogledaj na GitHubu"),
    spon=("Sponzori i donacije", "Podrži projekat finansijski. Sponzori ne dobijaju uticaj na proizvod niti podatke korisnika.", "Doniraj LuxyOS-u"),
    vol="Dobrovoljna donacija za LuxyOS: novac ide projektu LuxyOS.",
    vol_small="Putem PayPala (paypal.me/NOmanovic). Donacija je dobrovoljna i ne daje prava niti uticaj.",
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
    join="Тражимо програмере и спонзоре",
    join_p="LuxyOS је бесплатан, некомерцијалан пројекат. Да би постао стварност, потребни су нам људи и подршка.",
    dev=("Програмери", "Помози да се изгради LuxyOS. Планови, дизајни и први задаци налазе се на GitHub-у.", "Погледај на GitHub-у"),
    spon=("Спонзори и донације", "Подржи пројекат финансијски. Спонзори не добијају утицај на производ нити податке корисника.", "Донирај LuxyOS-у"),
    vol="Добровољна донација за LuxyOS: новац иде пројекту LuxyOS.",
    vol_small="Преко PayPal-а (paypal.me/NOmanovic). Донација је добровољна и не даје права нити утицај.",
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
    join="Kërkojmë zhvillues dhe sponsorë",
    join_p="LuxyOS është një projekt falas dhe jofitimprurës. Për ta bërë realitet, na duhen njerëz dhe mbështetje.",
    dev=("Zhvilluesit", "Ndihmo të ndërtojmë LuxyOS. Planet, dizajnet dhe detyrat e para janë në GitHub.", "Shiko në GitHub"),
    spon=("Sponsorë dhe dhurime", "Mbështet projektin financiarisht. Sponsorët nuk marrin ndikim mbi produktin dhe as të dhëna të përdoruesve.", "Dhuro për LuxyOS"),
    vol="Një dhurim vullnetar për LuxyOS: paratë shkojnë te projekti LuxyOS.",
    vol_small="Përmes PayPal (paypal.me/NOmanovic). Një dhurim është vullnetar dhe nuk jep të drejta apo ndikim.",
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
    join="Бараме програмери и спонзори",
    join_p="LuxyOS е бесплатен, некомерцијален проект. За да стане реалност, ни требаат луѓе и поддршка.",
    dev=("Програмери", "Помогни да се изгради LuxyOS. Плановите, дизајните и првите задачи се на GitHub.", "Види на GitHub"),
    spon=("Спонзори и донации", "Поддржи го проектот финансиски. Спонзорите не добиваат влијание врз производот ниту податоци за корисниците.", "Донирај за LuxyOS"),
    vol="Доброволна донација за LuxyOS: парите одат во проектот LuxyOS.",
    vol_small="Преку PayPal (paypal.me/NOmanovic). Донацијата е доброволна и не дава права ниту влијание.",
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
    join="Geliştirici ve sponsor arıyoruz",
    join_p="LuxyOS ücretsiz ve ticari olmayan bir projedir. Hayata geçirmek için insanlara ve desteğe ihtiyacımız var.",
    dev=("Geliştiriciler", "LuxyOS’u birlikte inşa et. Planlar, tasarımlar ve ilk görevler GitHub’da.", "GitHub’da gör"),
    spon=("Sponsorlar ve bağışlar", "Projeyi maddi olarak destekle. Sponsorlar ürün üzerinde etki ya da kullanıcı verisi elde etmez.", "LuxyOS’a bağış yap"),
    vol="LuxyOS için gönüllü bir bağış: para LuxyOS projesine gider.",
    vol_small="PayPal üzerinden (paypal.me/NOmanovic). Bağış gönüllüdür ve hiçbir hak ya da etki sağlamaz.",
    status="Şu an neredeyiz?",
    status_p="LuxyOS tasarım aşamasında. Hedefimiz 2027’de ilk test sürümü. Her şey çalıştığında indirebileceksin.",
    phases="Aşamalar", steps=("Tasarım", "Prototip", "Test sürümü 2027", "İndirme"),
    foot="Bu web sitesi çerez kullanmaz ve seni izlemez.",
)

# Supporters list and GitHub link, per language. {email} is filled in from CONTACT.
EXTRA = {
    "en": dict(spon_mail="Sponsoring as a company or organisation? Email {email}.", gh="LuxyOS on GitHub", sup_h="Thank you to our supporters",
        sup_p="Being on this list is voluntary. You choose whether your name, and the amount, appear here.",
        sup_remove="Changed your mind? Email {email} and we remove you in the next update.",
        sup_empty="No one is on the list yet."),
    "nl": dict(spon_mail="Sponsoren als bedrijf of organisatie? Mail naar {email}.", gh="LuxyOS op GitHub", sup_h="Dank aan onze supporters",
        sup_p="Op deze lijst staan is vrijwillig. Jij kiest of je naam, en het bedrag, hier komen te staan.",
        sup_remove="Toch liever niet? Mail naar {email}, dan halen we je weg bij de volgende update.",
        sup_empty="Er staat nog niemand op de lijst."),
    "de": dict(spon_mail="Als Unternehmen oder Organisation sponsern? Schreib an {email}.", gh="LuxyOS auf GitHub", sup_h="Danke an unsere Unterstützer",
        sup_p="Auf dieser Liste zu stehen ist freiwillig. Du entscheidest, ob dein Name und der Betrag hier erscheinen.",
        sup_remove="Doch lieber nicht? Schreib an {email}, dann entfernen wir dich beim nächsten Update.",
        sup_empty="Noch steht niemand auf der Liste."),
    "fr": dict(spon_mail="Vous souhaitez sponsoriser en tant qu’entreprise ou organisation\u00a0? Écrivez à {email}.", gh="LuxyOS sur GitHub", sup_h="Merci à nos soutiens",
        sup_p="Figurer sur cette liste est volontaire. Vous choisissez si votre nom, et le montant, apparaissent ici.",
        sup_remove="Vous changez d’avis ? Écrivez à {email} et nous vous retirerons lors de la prochaine mise à jour.",
        sup_empty="Personne n’est encore sur la liste."),
    "es": dict(spon_mail="¿Quieres patrocinar como empresa u organización? Escribe a {email}.", gh="LuxyOS en GitHub", sup_h="Gracias a quienes nos apoyan",
        sup_p="Aparecer en esta lista es voluntario. Tú eliges si tu nombre, y el importe, aparecen aquí.",
        sup_remove="¿Cambias de opinión? Escribe a {email} y te quitaremos en la próxima actualización.",
        sup_empty="Todavía no hay nadie en la lista."),
    "hr": dict(spon_mail="Želiš sponzorirati kao tvrtka ili organizacija? Piši na {email}.", gh="LuxyOS na GitHubu", sup_h="Hvala našim podržavateljima",
        sup_p="Biti na ovom popisu je dobrovoljno. Ti biraš hoće li se ovdje pojaviti tvoje ime i iznos.",
        sup_remove="Želiš da te uklonimo? Piši na {email} i uklonit ćemo te u sljedećem ažuriranju.",
        sup_empty="Na popisu još nema nikoga."),
    "bs": dict(spon_mail="Želiš sponzorisati kao firma ili organizacija? Piši na {email}.", gh="LuxyOS na GitHubu", sup_h="Hvala našim podržavaocima",
        sup_p="Biti na ovoj listi je dobrovoljno. Ti biraš hoće li se ovdje pojaviti tvoje ime i iznos.",
        sup_remove="Želiš da te uklonimo? Piši na {email} i uklonit ćemo te u sljedećem ažuriranju.",
        sup_empty="Na listi još nema nikoga."),
    "sr": dict(spon_mail="Желиш да спонзоришеш као фирма или организација? Пиши на {email}.", gh="LuxyOS на GitHub-у", sup_h="Хвала нашим подржаваоцима",
        sup_p="Бити на овој листи је добровољно. Ти бираш да ли ће се овде појавити твоје име и износ.",
        sup_remove="Желиш да те уклонимо? Пиши на {email} и уклонићемо те у следећем ажурирању.",
        sup_empty="На листи још нема никога."),
    "sq": dict(spon_mail="Dëshiron të sponsorizosh si kompani ose organizatë? Shkruaj te {email}.", gh="LuxyOS në GitHub", sup_h="Faleminderit mbështetësve tanë",
        sup_p="Të jesh në këtë listë është vullnetare. Ti zgjedh nëse emri yt dhe shuma shfaqen këtu.",
        sup_remove="Dëshiron të të heqim? Shkruaj te {email} dhe do të të heqim në përditësimin e radhës.",
        sup_empty="Ende nuk ka askënd në listë."),
    "mk": dict(spon_mail="Сакаш да спонзорираш како фирма или организација? Пиши на {email}.", gh="LuxyOS на GitHub", sup_h="Благодарност до нашите поддржувачи",
        sup_p="Да бидеш на оваа листа е доброволно. Ти избираш дали тука ќе се појават твоето име и износот.",
        sup_remove="Сакаш да те отстраниме? Пиши на {email} и ќе те отстраниме во следното ажурирање.",
        sup_empty="Сè уште нема никој на листата."),
    "tr": dict(spon_mail="Şirket ya da kuruluş olarak sponsor olmak mı istiyorsun? {email} adresine yaz.", gh="GitHub’da LuxyOS", sup_h="Destekçilerimize teşekkürler",
        sup_p="Bu listede yer almak gönüllüdür. Adının ve bağış miktarının burada görünüp görünmeyeceğine sen karar verirsin.",
        sup_remove="Listeden çıkmak mı istiyorsun? {email} adresine yaz, bir sonraki güncellemede seni kaldıralım.",
        sup_empty="Listede henüz kimse yok."),
}
for _c, _x in EXTRA.items():
    T[_c].update(_x)


# Texts around the supporters list, per language.
HOW = {'en': {'paid': 'You only appear on the list after your payment has succeeded.', 'logo_rule': 'Logos are shown small (at most 160 × 64 pixels, WebP) and without a link.', 'sp_h': 'Sponsors', 'su_h': 'Supporters', 'anon_count': 'Anonymous donors: {n}'}, 'nl': {'paid': 'Je komt pas op de lijst als je betaling gelukt is.', 'logo_rule': 'Logo’s tonen we klein (maximaal 160 × 64 pixels, WebP) en zonder link.', 'sp_h': 'Sponsors', 'su_h': 'Supporters', 'anon_count': 'Anonieme donateurs: {n}'}, 'de': {'paid': 'Du kommst erst auf die Liste, wenn deine Zahlung erfolgreich war.', 'logo_rule': 'Logos zeigen wir klein (höchstens 160 × 64 Pixel, WebP) und ohne Link.', 'sp_h': 'Sponsoren', 'su_h': 'Unterstützer', 'anon_count': 'Anonyme Spender: {n}'}, 'fr': {'paid': 'Vous n’apparaissez sur la liste qu’une fois votre paiement réussi.', 'logo_rule': 'Les logos sont affichés en petit (160 × 64 pixels maximum, WebP) et sans lien.', 'sp_h': 'Sponsors', 'su_h': 'Soutiens', 'anon_count': 'Donateurs anonymes\xa0: {n}'}, 'es': {'paid': 'Solo apareces en la lista cuando tu pago se ha completado.', 'logo_rule': 'Los logotipos se muestran en pequeño (máximo 160 × 64 píxeles, WebP) y sin enlace.', 'sp_h': 'Patrocinadores', 'su_h': 'Personas que nos apoyan', 'anon_count': 'Donantes anónimos: {n}'}, 'hr': {'paid': 'Na popis dolaziš tek kad je tvoja uplata uspješna.', 'logo_rule': 'Logotipe prikazujemo male (najviše 160 × 64 piksela, WebP) i bez poveznice.', 'sp_h': 'Sponzori', 'su_h': 'Podržavatelji', 'anon_count': 'Anonimni donatori: {n}'}, 'bs': {'paid': 'Na listu dolaziš tek kad je tvoja uplata uspješna.', 'logo_rule': 'Logotipe prikazujemo male (najviše 160 × 64 piksela, WebP) i bez linka.', 'sp_h': 'Sponzori', 'su_h': 'Podržavaoci', 'anon_count': 'Anonimni donatori: {n}'}, 'sr': {'paid': 'На листу долазиш тек кад твоја уплата успе.', 'logo_rule': 'Логое приказујемо мале (највише 160 × 64 пиксела, WebP) и без линка.', 'sp_h': 'Спонзори', 'su_h': 'Подржаваоци', 'anon_count': 'Анонимни донатори: {n}'}, 'sq': {'paid': 'Futesh në listë vetëm pasi pagesa jote të jetë kryer me sukses.', 'logo_rule': 'Logot i shfaqim të vogla (deri në 160 × 64 piksela, WebP) dhe pa lidhje.', 'sp_h': 'Sponsorët', 'su_h': 'Mbështetësit', 'anon_count': 'Dhurues anonimë: {n}'}, 'mk': {'paid': 'На листата доаѓаш дури откако уплатата ќе биде успешна.', 'logo_rule': 'Логата ги прикажуваме мали (најмногу 160 × 64 пиксели, WebP) и без линк.', 'sp_h': 'Спонзори', 'su_h': 'Поддржувачи', 'anon_count': 'Анонимни донатори: {n}'}, 'tr': {'paid': 'Listeye ancak ödemen başarıyla tamamlandıktan sonra girersin.', 'logo_rule': 'Logoları küçük (en fazla 160 × 64 piksel, WebP) ve bağlantısız gösteririz.', 'sp_h': 'Sponsorlar', 'su_h': 'Destekçiler', 'anon_count': 'Anonim bağışçılar: {n}'}}
for _c, _x in HOW.items():
    T[_c].update(_x)

# The story under 'A first look': one heading, one sentence and one design per row.
STORY_KEYS = ['desktop', 'explorer', 'store', 'gaming', 'network', 'accounts', 'privacy', 'security']
STORY = {k: dict(word=v[0], rows=v[1]) for k, v in {'en': ('Design', [('Works the way you are used to', 'Start menu, taskbar and windows where you expect them. Only the services you use are running.'), ('Your files where you expect them', 'Documents, Pictures and Downloads in the same place as on Windows.'), ('Windows and Linux apps in one system', 'One store for Windows programs, Linux apps and free software, with honest labels.'), ('Ready for games', 'Steam, controllers and graphics drivers, with a game mode for maximum performance.'), ('Network settings in one place', 'Wi-Fi, VPN, IP settings, encrypted DNS and a firewall per app.'), ('For home and work', 'Connect to Active Directory for company data, and add Microsoft 365, Google or Yahoo.'), ('Nothing leaves without your permission', 'See which app connected to what. No telemetry, no ads.'), ('IT DeXt Antivirus built in', 'Protection for Linux and Windows programs, built in and free.')]), 'nl': ('Ontwerp', [('Werkt zoals je gewend bent', 'Startmenu, taakbalk en vensters waar je ze verwacht. Alleen de diensten die je gebruikt, draaien.'), ('Je bestanden waar je ze verwacht', 'Documenten, Afbeeldingen en Downloads op dezelfde plek als in Windows.'), ('Windows- en Linux-apps in één systeem', 'Eén winkel voor Windows-programma’s, Linux-apps en gratis software, met eerlijke labels.'), ('Klaar om te gamen', 'Steam, controllers en grafische drivers, met een gamemodus voor de beste prestaties.'), ('Netwerk op één plek', 'Wifi, VPN, IP-instellingen, versleutelde DNS en een firewall per app.'), ('Voor thuis en op het werk', 'Koppel Active Directory voor bedrijfsgegevens en voeg Microsoft 365, Google of Yahoo toe.'), ('Niets verlaat je computer zonder toestemming', 'Zie welke app waarmee verbinding maakte. Geen telemetrie, geen advertenties.'), ('IT DeXt Antivirus ingebouwd', 'Bescherming voor Linux- en Windows-programma’s, ingebouwd en gratis.')]), 'de': ('Entwurf', [('Funktioniert, wie du es gewohnt bist', 'Startmenü, Taskleiste und Fenster dort, wo du sie erwartest. Nur die Dienste, die du nutzt, laufen.'), ('Deine Dateien dort, wo du sie erwartest', 'Dokumente, Bilder und Downloads am selben Ort wie unter Windows.'), ('Windows- und Linux-Apps in einem System', 'Ein Store für Windows-Programme, Linux-Apps und freie Software, mit ehrlichen Angaben.'), ('Bereit zum Spielen', 'Steam, Controller und Grafiktreiber, mit einem Spielmodus für beste Leistung.'), ('Netzwerk an einem Ort', 'WLAN, VPN, IP-Einstellungen, verschlüsseltes DNS und eine Firewall pro App.'), ('Für zu Hause und die Arbeit', 'Verbinde Active Directory für Firmendaten und füge Microsoft 365, Google oder Yahoo hinzu.'), ('Nichts verlässt deinen Computer ohne Zustimmung', 'Sieh, welche App sich womit verbunden hat. Keine Telemetrie, keine Werbung.'), ('IT DeXt Antivirus integriert', 'Schutz für Linux- und Windows-Programme, integriert und kostenlos.')]), 'fr': ('Maquette', [('Fonctionne comme vous en avez l’habitude', 'Menu Démarrer, barre des tâches et fenêtres là où vous les attendez. Seuls les services que vous utilisez fonctionnent.'), ('Vos fichiers là où vous les attendez', 'Documents, Images et Téléchargements au même endroit que sous Windows.'), ('Applications Windows et Linux dans un seul système', 'Une boutique pour les programmes Windows, les applications Linux et les logiciels libres, avec des indications honnêtes.'), ('Prêt pour le jeu', 'Steam, manettes et pilotes graphiques, avec un mode jeu pour des performances maximales.'), ('Le réseau au même endroit', 'Wi-Fi, VPN, paramètres IP, DNS chiffré et un pare-feu par application.'), ('À la maison et au travail', 'Connectez Active Directory pour les données de l’entreprise et ajoutez Microsoft 365, Google ou Yahoo.'), ('Rien ne sort sans votre permission', 'Voyez quelle application s’est connectée à quoi. Pas de télémétrie, pas de publicité.'), ('IT DeXt Antivirus intégré', 'Une protection pour les programmes Linux et Windows, intégrée et gratuite.')]), 'es': ('Diseño', [('Funciona como estás acostumbrado', 'Menú Inicio, barra de tareas y ventanas donde las esperas. Solo funcionan los servicios que usas.'), ('Tus archivos donde los esperas', 'Documentos, Imágenes y Descargas en el mismo lugar que en Windows.'), ('Apps de Windows y Linux en un solo sistema', 'Una tienda para programas de Windows, apps de Linux y software libre, con etiquetas honestas.'), ('Listo para jugar', 'Steam, mandos y controladores gráficos, con un modo juego para el máximo rendimiento.'), ('La red en un solo lugar', 'Wi-Fi, VPN, ajustes de IP, DNS cifrado y un cortafuegos por aplicación.'), ('Para casa y para el trabajo', 'Conecta Active Directory para los datos de la empresa y añade Microsoft 365, Google o Yahoo.'), ('Nada sale sin tu permiso', 'Mira qué aplicación se conectó a qué. Sin telemetría ni anuncios.'), ('IT DeXt Antivirus integrado', 'Protección para programas de Linux y Windows, integrada y gratuita.')]), 'hr': ('Dizajn', [('Radi onako kako očekuješ', 'Izbornik Start, programska traka i prozori tamo gdje ih očekuješ. Rade samo usluge koje koristiš.'), ('Tvoje datoteke tamo gdje ih očekuješ', 'Dokumenti, Slike i Preuzimanja na istom mjestu kao u Windowsima.'), ('Windows i Linux aplikacije u jednom sustavu', 'Jedna trgovina za Windows programe, Linux aplikacije i besplatni softver, s poštenim oznakama.'), ('Spremno za igre', 'Steam, kontroleri i grafički upravljački programi, s načinom za igre za najbolje performanse.'), ('Mreža na jednom mjestu', 'Wi-Fi, VPN, IP postavke, šifrirani DNS i vatrozid za svaku aplikaciju.'), ('Za kuću i posao', 'Poveži Active Directory za poslovne podatke i dodaj Microsoft 365, Google ili Yahoo.'), ('Ništa ne odlazi bez tvog dopuštenja', 'Vidi koja se aplikacija s čime povezala. Bez telemetrije, bez oglasa.'), ('IT DeXt Antivirus ugrađen', 'Zaštita za Linux i Windows programe, ugrađena i besplatna.')]), 'bs': ('Dizajn', [('Radi onako kako očekuješ', 'Start meni, traka zadataka i prozori tamo gdje ih očekuješ. Rade samo servisi koje koristiš.'), ('Tvoje datoteke tamo gdje ih očekuješ', 'Dokumenti, Slike i Preuzimanja na istom mjestu kao u Windowsu.'), ('Windows i Linux aplikacije u jednom sistemu', 'Jedna prodavnica za Windows programe, Linux aplikacije i besplatni softver, s poštenim oznakama.'), ('Spremno za igre', 'Steam, kontroleri i grafički drajveri, s režimom za igre za najbolje performanse.'), ('Mreža na jednom mjestu', 'Wi-Fi, VPN, IP postavke, šifrovani DNS i zaštitni zid za svaku aplikaciju.'), ('Za kuću i posao', 'Poveži Active Directory za poslovne podatke i dodaj Microsoft 365, Google ili Yahoo.'), ('Ništa ne odlazi bez tvoje dozvole', 'Vidi koja se aplikacija s čime povezala. Bez telemetrije, bez reklama.'), ('IT DeXt Antivirus ugrađen', 'Zaštita za Linux i Windows programe, ugrađena i besplatna.')]), 'sr': ('Дизајн', [('Ради онако како очекујеш', 'Старт мени, трака задатака и прозори тамо где их очекујеш. Раде само сервиси које користиш.'), ('Твоје датотеке тамо где их очекујеш', 'Документи, Слике и Преузимања на истом месту као у Windows-у.'), ('Windows и Linux апликације у једном систему', 'Једна продавница за Windows програме, Linux апликације и бесплатни софтвер, са поштеним ознакама.'), ('Спремно за игре', 'Steam, контролери и графички драјвери, са режимом за игре за најбоље перформансе.'), ('Мрежа на једном месту', 'Wi-Fi, VPN, IP подешавања, шифровани DNS и заштитни зид за сваку апликацију.'), ('За кућу и посао', 'Повежи Active Directory за пословне податке и додај Microsoft 365, Google или Yahoo.'), ('Ништа не одлази без твоје дозволе', 'Види која се апликација са чим повезала. Без телеметрије, без реклама.'), ('IT DeXt Antivirus уграђен', 'Заштита за Linux и Windows програме, уграђена и бесплатна.')]), 'sq': ('Dizajn', [('Punon ashtu siç je mësuar', 'Menyja Start, shiriti i detyrave dhe dritaret aty ku i pret. Punojnë vetëm shërbimet që përdor.'), ('Skedarët e tu aty ku i pret', 'Dokumentet, Fotot dhe Shkarkimet në të njëjtin vend si në Windows.'), ('Aplikacione Windows dhe Linux në një sistem', 'Një dyqan për programe Windows, aplikacione Linux dhe softuer falas, me etiketa të ndershme.'), ('Gati për lojëra', 'Steam, kontrollues dhe drajverë grafikë, me një modalitet lojërash për performancë maksimale.'), ('Rrjeti në një vend', 'Wi-Fi, VPN, cilësimet IP, DNS i enkriptuar dhe një mur zjarri për çdo aplikacion.'), ('Për shtëpinë dhe punën', 'Lidh Active Directory për të dhënat e kompanisë dhe shto Microsoft 365, Google ose Yahoo.'), ('Asgjë nuk largohet pa lejen tënde', 'Shih cili aplikacion u lidh me çfarë. Pa telemetri, pa reklama.'), ('IT DeXt Antivirus i integruar', 'Mbrojtje për programet Linux dhe Windows, e integruar dhe falas.')]), 'mk': ('Дизајн', [('Работи како што очекуваш', 'Старт мени, лента со задачи и прозорци таму каде што ги очекуваш. Работат само услугите што ги користиш.'), ('Твоите датотеки таму каде што ги очекуваш', 'Документи, Слики и Преземања на истото место како во Windows.'), ('Windows и Linux апликации во еден систем', 'Една продавница за Windows програми, Linux апликации и бесплатен софтвер, со чесни ознаки.'), ('Подготвено за игри', 'Steam, контролери и графички драјвери, со режим за игри за најдобри перформанси.'), ('Мрежата на едно место', 'Wi-Fi, VPN, IP-поставки, шифриран DNS и заштитен ѕид за секоја апликација.'), ('За дома и за работа', 'Поврзи Active Directory за деловни податоци и додај Microsoft 365, Google или Yahoo.'), ('Ништо не заминува без твоја дозвола', 'Види која апликација со што се поврзала. Без телеметрија, без реклами.'), ('IT DeXt Antivirus вграден', 'Заштита за Linux и Windows програми, вградена и бесплатна.')]), 'tr': ('Tasarım', [('Alıştığın gibi çalışır', 'Başlat menüsü, görev çubuğu ve pencereler beklediğin yerde. Yalnızca kullandığın hizmetler çalışır.'), ('Dosyaların beklediğin yerde', 'Belgeler, Resimler ve İndirilenler, Windows’taki ile aynı yerde.'), ('Windows ve Linux uygulamaları tek sistemde', 'Windows programları, Linux uygulamaları ve ücretsiz yazılımlar için tek mağaza, dürüst etiketlerle.'), ('Oyuna hazır', 'Steam, oyun kumandaları ve ekran kartı sürücüleri; en iyi performans için oyun modu.'), ('Ağ ayarları tek yerde', 'Wi-Fi, VPN, IP ayarları, şifreli DNS ve her uygulama için ayrı güvenlik duvarı.'), ('Evde ve işte', 'Şirket verileri için Active Directory’ye bağlan; Microsoft 365, Google veya Yahoo ekle.'), ('İznin olmadan hiçbir şey dışarı çıkmaz', 'Hangi uygulamanın neye bağlandığını gör. Telemetri yok, reklam yok.'), ('IT DeXt Antivirus yerleşik', 'Linux ve Windows programları için koruma; yerleşik ve ücretsiz.')])}.items()}
for _c, _x in STORY.items():
    T[_c]['story'] = _x

# PayPal QR code next to the donate button (shown on larger screens only).
QR = {'en': {'qr_scan': 'Or scan with your phone to donate via PayPal.', 'qr_alt': 'PayPal QR code for donating to LuxyOS'}, 'nl': {'qr_scan': 'Of scan met je telefoon om te doneren via PayPal.', 'qr_alt': 'PayPal-QR-code om te doneren aan LuxyOS'}, 'de': {'qr_scan': 'Oder scanne mit deinem Handy, um über PayPal zu spenden.', 'qr_alt': 'PayPal-QR-Code zum Spenden an LuxyOS'}, 'fr': {'qr_scan': 'Ou scannez avec votre téléphone pour faire un don via PayPal.', 'qr_alt': 'Code QR PayPal pour faire un don à LuxyOS'}, 'es': {'qr_scan': 'O escanea con tu móvil para donar a través de PayPal.', 'qr_alt': 'Código QR de PayPal para donar a LuxyOS'}, 'hr': {'qr_scan': 'Ili skeniraj mobitelom i doniraj putem PayPala.', 'qr_alt': 'PayPal QR kod za donaciju LuxyOS-u'}, 'bs': {'qr_scan': 'Ili skeniraj telefonom i doniraj putem PayPala.', 'qr_alt': 'PayPal QR kod za donaciju LuxyOS-u'}, 'sr': {'qr_scan': 'Или скенирај телефоном и донирај преко PayPal-а.', 'qr_alt': 'PayPal QR код за донацију LuxyOS-у'}, 'sq': {'qr_scan': 'Ose skano me telefon për të dhuruar përmes PayPal.', 'qr_alt': 'Kodi QR i PayPal për të dhuruar për LuxyOS'}, 'mk': {'qr_scan': 'Или скенирај со телефонот и донирај преку PayPal.', 'qr_alt': 'PayPal QR-код за донација за LuxyOS'}, 'tr': {'qr_scan': 'Ya da PayPal ile bağış yapmak için telefonunla tara.', 'qr_alt': 'LuxyOS’a bağış için PayPal QR kodu'}}
for _c, _x in QR.items():
    T[_c].update(_x)

# Button in the top bar that scrolls to the donation box.
HELP = {'en': 'Support us', 'nl': 'Steun ons', 'de': 'Unterstütze uns', 'fr': 'Soutenez-nous', 'es': 'Apóyanos', 'hr': 'Podrži nas', 'bs': 'Podrži nas', 'sr': 'Подржи нас', 'sq': 'Na mbështet', 'mk': 'Поддржи нѐ', 'tr': 'Bizi destekle'}
for _c, _x in HELP.items():
    T[_c]['help'] = _x

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
a, summary, button { -webkit-tap-highlight-color: transparent; }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
#doneren { scroll-margin-top: 20px; }
.help { display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; border-radius: 999px; background: var(--hemel); color: #ffffff; font-size: 14px; font-weight: 700; text-decoration: none; white-space: nowrap; }
.help svg { width: 16px; height: 16px; flex-shrink: 0; }
.help:hover { filter: brightness(1.08); }
.help:focus-visible { outline: 3px solid var(--zon); outline-offset: 2px; }
@media (prefers-color-scheme: dark) { .help { color: #0e1828; } }
body { margin: 0; background: var(--bg); color: var(--tekst); font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", Arial, sans-serif; line-height: 1.5; }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px; }
header .wrap { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-top: 22px; padding-bottom: 22px; }
.merk { display: flex; align-items: center; gap: 10px; min-height: 44px; text-decoration: none; color: var(--tekst); }
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
.hero .label { background: var(--kaart); border: 1px solid var(--rand); white-space: normal; max-width: 100%; line-height: 1.35; }
.hero .wrap { position: relative; z-index: 1; padding-top: 72px; padding-bottom: 200px; display: flex; flex-direction: column; align-items: flex-start; gap: 20px; }
h1 { margin: 0; font-size: clamp(34px, 6vw, 64px); line-height: 1.05; letter-spacing: -0.02em; font-weight: 800; max-width: 860px; overflow-wrap: break-word; }
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
.verhaal { display: grid; gap: 64px; margin-top: 8px; }
.rij { display: grid; grid-template-columns: minmax(0, 2fr) minmax(0, 3fr); gap: 40px; align-items: center; margin: 0; }
.rij:nth-child(even) { grid-template-columns: minmax(0, 3fr) minmax(0, 2fr); }
.rij:nth-child(even) .tekst { order: 2; }
.rij h3 { margin: 0 0 8px; font-size: clamp(20px, 2.4vw, 26px); letter-spacing: -0.01em; line-height: 1.2; }
.rij .tekst { margin: 0; font-size: inherit; color: inherit; }
.rij .tekst p { margin: 0; color: var(--tekst-zacht); font-size: 17px; }
@media (max-width: 760px) { .verhaal { gap: 44px; } .rij, .rij:nth-child(even) { grid-template-columns: 1fr; gap: 14px; } .rij:nth-child(even) .tekst { order: 0; } .rij .tekst p { font-size: 16px; } }
section.mee .wrap { padding-top: 56px; padding-bottom: 8px; }
.raster2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 18px; }
.mee .kaart { padding: 26px; gap: 12px; }
.mee .kaart .knop { align-self: flex-start; }
.vrijwillig { margin: 0; padding: 10px 12px; border-radius: 10px; background: var(--bg-zacht); font-size: 14px; font-weight: 600; color: var(--tekst); }
.klein { margin: 0; font-size: 13px; color: var(--tekst-zacht); }
.knop { display: inline-flex; align-items: center; gap: 10px; padding: 13px 20px; border-radius: 12px; background: var(--hemel); color: #ffffff; font-weight: 700; font-size: 16px; text-decoration: none; }
.knop.tweede { background: var(--nacht); }
.knop:hover { filter: brightness(1.08); }
.qr { display: none; margin: 4px 0 0; }
.qr img { display: block; width: 280px; height: 280px; border-radius: 12px; border: 1px solid var(--rand); background: #ffffff; }
.qr figcaption { margin-top: 8px; font-size: 14px; color: var(--tekst-zacht); }
@media (min-width: 761px) { .qr { display: block; } }
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
.gh { display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 999px; border: 1px solid var(--rand); color: var(--tekst); }
.gh svg { width: 18px; height: 18px; }
.gh:hover { background: var(--bg-zacht); }
.gh:focus-visible, footer a:focus-visible { outline: 3px solid var(--zon); outline-offset: 2px; }
section.supporters .wrap { padding-top: 40px; padding-bottom: 8px; }
.sup-blok { border: 1px solid var(--rand); border-radius: 16px; background: var(--kaart); padding: 26px; display: flex; flex-direction: column; gap: 12px; }
.sup-blok h2 { margin: 0; }
.sup-blok p { margin: 0; color: var(--tekst-zacht); max-width: 760px; }
.sup-lijst { list-style: none; margin: 6px 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: 10px; }
.sup-lijst li { padding: 8px 14px; border-radius: 999px; background: var(--bg-zacht); font-weight: 600; }
.sup-lijst li span { font-weight: 400; color: var(--tekst-zacht); margin-left: 6px; }
.sup-leeg { font-style: italic; }
.sup-blok h3 { margin: 6px 0 0; font-size: 14px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--tekst-zacht); }
.logos { display: flex; flex-wrap: wrap; gap: 14px; list-style: none; margin: 0; padding: 0; }
.logos li { display: grid; gap: 6px; justify-items: center; padding: 10px; border: 1px solid var(--rand); border-radius: 12px; background: #ffffff; }
.logos img { width: 160px; height: 64px; object-fit: contain; display: block; }
.logos span { font-size: 13px; color: #3d4b61; }
.betaald { margin: 0; padding: 10px 12px; border-radius: 10px; background: #e5f4e4; color: #14532d !important; font-size: 14px; font-weight: 600; }
.sup-blok a, .mee .klein a { color: var(--hemel); }
footer { border-top: 1px solid var(--rand); }
footer a { color: inherit; display: inline-flex; align-items: center; gap: 6px; padding: 12px 0; margin: -12px 0; }
footer a svg { width: 16px; height: 16px; }
footer .wrap { padding-top: 24px; padding-bottom: 32px; display: flex; flex-wrap: wrap; gap: 8px 24px; justify-content: space-between; color: var(--tekst-zacht); font-size: 14px; }
@media (max-width: 560px) {
  header .wrap { gap: 8px; }
  .merk { gap: 8px; }
  .merk svg { width: 34px; height: 34px; }
  .woordmerk { font-size: 20px; }
  .rechts { gap: 6px; }
  header .label { padding: 5px 10px; font-size: 13px; }
  .talen summary { padding: 5px 10px; font-size: 12px; }
  .talen ul { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; min-width: 0; width: min(300px, calc(100vw - 32px)); }
  .talen a { padding-left: 10px; padding-right: 10px; }
  .hero .wrap { padding-top: 48px; padding-bottom: 170px; }
  .zon { width: 80px; height: 80px; right: 8%; bottom: 90px; }
  .status-blok { padding: 24px; }
  .mee .kaart { padding: 22px; }
  .sup-blok { padding: 20px; }
  .rechts .gh { display: none; }
}
@media (max-width: 560px) { header .label { display: none; } .help { padding: 5px 12px; font-size: 13px; } }
@media (max-width: 380px) {
  h1 { font-size: 30px; }
  header .wrap { padding-left: 14px; padding-right: 14px; gap: 6px; }
  .merk { gap: 6px; }
  .merk svg { width: 28px; height: 28px; }
  .woordmerk { font-size: 17px; }
  .rechts { gap: 4px; }
  .help { padding: 5px 10px; font-size: 12.5px; }
  .help svg { display: none; }
  .talen summary { padding: 5px 8px; }
}
@media (max-width: 380px) and (pointer: coarse) { .help { padding: 0 10px; } .talen summary { padding: 0 9px; } }
/* Touch screens: every tap target at least 44 x 44 pixels */
@media (pointer: coarse) {
  .talen summary { min-height: 44px; padding: 0 14px; }
  .talen a { padding: 13px 12px; }
  .gh { width: 44px; height: 44px; }
  .help { min-height: 44px; }
}
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


SUPPORTERS_FILE = None  # set by --supporters
OUT_DIR = OUT  # set by --out


def load_supporters():
    """The real list lives in supporters.private.json, which is never committed
    (names in a public Git history cannot be erased). The public supporters.json
    stays empty and only documents the format."""
    private = os.path.join(HERE, "supporters.private.json")
    if SUPPORTERS_FILE:
        path = SUPPORTERS_FILE
    else:
        path = private if os.path.exists(private) else os.path.join(HERE, "supporters.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("anonymous", 0)
    data.setdefault("sponsors", [])
    data.setdefault("supporters", [])
    for sp in data["sponsors"]:
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*\.webp", sp.get("logo", "")):
            raise SystemExit(f"logo must be a WebP file name like name.webp: {sp!r}")
        datetime.date.fromisoformat(sp["until"])  # must be a valid date
    return data


def story_html(t, root, il):
    st = t["story"]
    rows = []
    for key, (h, p) in zip(STORY_KEYS, st["rows"]):
        big = f"{root}img/{key}-{il}-1440.webp"
        small = f"{root}img/{key}-{il}-720.webp"
        rows.append(
            f'<figure class="rij">\n<figcaption class="tekst"><h3>{e(h)}</h3><p>{e(p)}</p></figcaption>\n'
            f'<a href="{big}"><img src="{small}" srcset="{small} 720w, {big} 1440w" sizes="(max-width: 760px) 100vw, 620px" '
            f'width="1440" height="900" alt="{e(st["word"])}: {e(h)}" loading="lazy" decoding="async"></a>\n</figure>'
        )
    return '<div class="verhaal">\n' + "\n".join(rows) + "\n</div>"


def mail_link():
    return f'<a href="mailto:{CONTACT}">{e(CONTACT)}</a>'


def mail_line(t):
    if not CONTACT:
        return ""
    return '<p class="klein">' + e(t["spon_mail"]).replace("{email}", mail_link()) + "</p>"


def supporters_html(t, root, out):
    """The supporters block; empty until CONTACT is filled in."""
    if not CONTACT:
        return ""
    data = load_supporters()
    today = datetime.date.today()
    logos, names = [], []
    for sp in data["sponsors"]:
        if datetime.date.fromisoformat(sp["until"]) >= today:
            if not os.path.exists(os.path.join(out, "img", "sponsors", sp["logo"])):
                raise SystemExit(f"logo file missing: img/sponsors/{sp['logo']}")
            logos.append(sp)
        else:
            names.append(sp)  # after 12 months the logo goes, the name stays
    names = names + data["supporters"]

    def amount(p):
        return f'<span>{e(p["amount"])}</span>' if p.get("amount") else ""

    parts = []
    if logos:
        items = "\n".join(
            f'<li><img src="{root}img/sponsors/{sp["logo"]}" width="160" height="64" alt="{e(sp["name"])}" loading="lazy">'
            f'<span>{e(sp["name"])}{(" · " + e(sp["amount"])) if sp.get("amount") else ""}</span></li>'
            for sp in logos
        )
        parts.append(f'<h3>{e(t["sp_h"])}</h3>\n<ul class="logos">\n{items}\n</ul>')
    if names:
        items = "\n".join(f'<li>{e(p["name"])}{amount(p)}</li>' for p in names)
        parts.append(f'<h3>{e(t["su_h"])}</h3>\n<ul class="sup-lijst">\n{items}\n</ul>')
    if data["anonymous"]:
        parts.append(f'<p>{e(t["anon_count"]).replace("{n}", str(int(data["anonymous"])))}</p>')
    if not parts:
        parts.append(f'<p class="sup-leeg">{e(t["sup_empty"])}</p>')
    lijst = "\n".join(parts)
    mail = mail_link()
    remove = e(t["sup_remove"]).replace("{email}", mail)
    return f"""<section class="supporters" id="supporters">
<div class="wrap">
<div class="sup-blok">
<h2>{e(t["sup_h"])}</h2>
<p>{e(t["sup_p"])}</p>
{lijst}
<p class="betaald">{e(t["paid"])}</p>
<p>{e(t["logo_rule"])} {remove}</p>
</div>
</div>
</section>

"""


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
<a class="gh" href="{GITHUB}" rel="noopener" aria-label="{e(t["gh"])}" title="{e(t["gh"])}">{GH}</a>
<span class="label"><i aria-hidden="true"></i>{e(t["soon"])}</span>
<a class="help" href="#doneren">{HEART}{e(t["help"])}</a>
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
{story_html(t, root, il)}
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
<article class="kaart" id="doneren">
{icon("spon")}
<h3>{e(t["spon"][0])}</h3>
<p>{e(t["spon"][1])}</p>
<p class="vrijwillig">{e(t["vol"])}</p>
<a class="knop" href="{PAYPAL}" rel="noopener">{HEART}{e(t["spon"][2])}</a>
<figure class="qr"><img src="{root}img/paypal-qr.webp" width="280" height="280" alt="{e(t["qr_alt"])}" loading="lazy" decoding="async"><figcaption>{e(t["qr_scan"])}</figcaption></figure>
<p class="klein">{e(t["vol_small"])}</p>
{mail_line(t)}
</article>
</div>
</div>
</section>

{supporters_html(t, root, OUT_DIR)}<section class="status">
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
<span>© 2026 LuxyOS · <a href="{GITHUB}" rel="noopener">{GH}{e(t["gh"])}</a></span>
<span>{e(t["foot"])}</span>
</div>
</footer>

</body>
</html>
"""


def main():
    global SUPPORTERS_FILE
    ap = argparse.ArgumentParser(description="Build the luxyos.com pages.")
    ap.add_argument("--out", default=OUT, help="output folder (the webroot)")
    ap.add_argument("--supporters", help="JSON file with the supporters list")
    args = ap.parse_args()
    global OUT_DIR
    out = os.path.abspath(args.out)
    OUT_DIR = out
    if args.supporters:
        SUPPORTERS_FILE = os.path.abspath(args.supporters)
        load_supporters()  # fail early on a missing or broken file
    keys = set(T["en"])
    for code, _ in LANGS:
        missing = keys - set(T[code])
        assert not missing, (code, missing)
        path = os.path.join(out, "index.html") if code == "en" else os.path.join(out, code, "index.html")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(code))
        print("wrote", path)


if __name__ == "__main__":
    main()
