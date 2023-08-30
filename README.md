---
author:
    Lars G Johnsen
organization:
    Nasjonalbiblioteket
date:
    juni 2014
---

Tokenisator for ngramleser (evt. parsing).
-------------------------------------------


Tokenisatorens oppgave er å danne token eller ord fra en sekvens med tegn.
I utgangspunktet fungerer skilletegn og mellomrom som ordgrenser,
men det er unntak, se listen nedenfor. Skilletegn danner som oftest egne token,
men spesielt punktum og komma brukes på flere måter, noe det må tas høyde for.

Noen ord (token) har bestanddeler i form av skilletegn, som forkortelser, tall,
i tillegg kan ordene selv være bundet sammen med bindestrek:

p-pille (bindestrek)
3.3 (punktum i seksjonsnummerering)
etc. (forkortelser)
10 000 (token over mellomrom)
3,14 (desimaltall med komma)
co2 (bokstaver og tall i kjemiske formler)
co2-forurensning (bokstaver tall pluss bindestrek)
17. (ordenstall som i 17. mai)
P. A. Munch (punktum i initialer)
... tre eller flere  punktum
Når punktum følger tall vil tokenisatoren la punktum tilhøre tallet
med mindre punktumet følges av mellomrom og stor bokstav.

Punktum tilhører alle forkortelser som tar punktum uavhenging av kontekst.
Den kan imidlertid gjøres følsom for påfølgende stor bokstav,
men det er altså ikke gjort her.
Punktum tillates inne i ord og deler ikke opp ord med punktum i seg.

Alle skilletegn ellers utgjør egne token, bortsett fra § som kan sekvensieres,
så § og §§ vil være egne tokener;
de benyttes en hel del i lovtekster for entall og flertall.

Tall skrevet med mellomrom blir ett token om de er på formen xx xxx, altså 1
eller 3 siffer etterfulgt av grupper på tre siffer skilt med ett mellomrom.
Så 3 1995 vil være to tokener, mens 3 995 blir ett token,
4000 398 blir igjen to token. (Mulig det er endret)

Tall som følger etter § (adskilt med maks ett mellomrom)
vil aldri tiltrekke seg punktum.

Øvrige tegn som ikke passer inn med mønstrene over behandles som separate token.
