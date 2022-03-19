# ENGETO - Prvni projekt - Textovy analyzator

Cilem tohoto projektu je analyzovat predpipravene texty na zaklade uzivatelske volby.

Program postupuje nasledovne:
* vyzada si od uzivatele prihlasovaci jmeno a heslo, 
* zjisti, jestli zadane udaje odpovidaji nekomu z registrovanych uzivatelu,
* pokud je registrovany, pozdravi a umozni analyzovat texty,
* pokud neni registrovany, upozorni a ukonci program.
* registrovanemu uzivateli je umozneno vybrat ze 3 textu
  * pokud uzivatel vybere text, ktery neni v nabidce, program jej upozorni a skonci
* pro vybrany text program spocita nasledujici statistiky:
  * pocet slov,
  * pocet slov zacinajicich velkym pismenem, 
  * pocet slov psanych velkymi pismeny,
  * pocet slov psanych malymi pismeny,
  * pocet cisel (ne cifer),
  * sumu vsech cisel (ne cifer) v textu.
* program zobrazi jednoduchy sloupcovy graf, ktery reprezentuje cetnost ruznych delek slov v textu.