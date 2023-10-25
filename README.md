# CMS pre štátne webstránky (ID-SK dizajn)

Toto CMS je navrhnuté špeciálne pre štátne webstránky, so zreteľom na ID-SK dizajn. Cieľom je nielen zabezpečiť jednotný dizajn pre všetky štátne webové stránky, ale aj zabezpečiť ich praktickú funkčnosť prostredníctvom online formulárov a UX dizajnu založeného na strome životných situácií občana.

## Demo

Celý projekt môžete otestovať na [mesto.slovakosoft.sk](https://mesto.slovakosoft.sk/).

## Hlavné vlastnosti:

- Založený na django 4.0.
- Využíva ID-SK a GOV-UK knižnice.
- Stránky sú navrhnuté tak, aby boli čo najviac dynamické.
- Orientácia na praktické využitie a životné situácie občana.
- Vytvorené v súlade so štátnym predpísaným dizajnom.

## Štruktura projektu:

Projekt nasleduje filozofiu Django, kde každá appka slúži jednému účelu. 

- **MainPage**: Appka v Djangou, ktorá slúži ako domovská stránka. Rozloženie je pevne stanovené, a meniť sa bude môcť len obsah jednotlivých modulov.
  
- **CategoryPage**: Appka pre kategórie. Kategórie sa budú môcť pridať, avšak každá kategória má pevne stanovené rozloženie a bude sa meniť len obsah.
  
- **ArticlePage**: Základný stavebný prvok projektu. Článok obsahuje text, obrázok, navigáciu a vždy patrí do nejakej kategórie. Rozloženie je volné.
  
- **LoginPage**: Stránka, ktorá umožňuje prístup do AdminPage. Slúži ako login s kódom mesta, aby bolo jasné, ktorému používateľovi sa čo zobrazuje.
  
- **AdminPage**: Slúži pre CRUD operácie a nič iné.

### Priečinky a súbory:

- `templates`: Obsahuje HTML súbory.
- `static`: Obsahuje CSS a JS súbory.
- `models.py`: Definuje databázu.
- `urls.py`: Routing.
- `views`: Pohlady.

## Dostupnosť:

- Hlavná stránka: [mesto.slovakosoft.sk](https://mesto.slovakosoft.sk/)
- Dynamická stránka pre kategórie: [mesto.slovakosoft.sk/kategoria/](https://mesto.slovakosoft.sk/kategoria/)
- Dynamická stránka pre články: [mesto.slovakosoft.sk/clanok/](https://mesto.slovakosoft.sk/clanok/)
- Stránka pre prihlásenie: [mesto.slovakosoft.sk/prihlasenie/](https://mesto.slovakosoft.sk/prihlasenie/)
- Administrátorské prostredie: [mesto.slovakosoft.sk/uvod/](https://mesto.slovakosoft.sk/uvod/)

## Poznámky:

- Projekt obsahuje aj varovania, ale netreba sa ich báť, pretože zákony sú vymyslené.
- Hlavným zámerom je vytvoriť jednoduché CMS pre správu štátnych webov ako alternatíva k WordPressu.

## Systém v praxi:

![MainPage Image](obrazok_mainpage.png)
![CategoryPage Image](obrazok_categorypage.png)
![ArticlePage Image](obrazok_articlepage.png)
![LoginPage Image](obrazok_loginpage.png)
![AdminPage Image](obrazok_adminpage.png)

---

Ak máte akékoľvek otázky alebo pripomienky, prosím, neváhajte nás kontaktovať. Ďakujeme za využitie našeho CMS!
