# CMS pre štátne webstránky (ID-SK dizajn)

Toto CMS je navrhnuté špeciálne pre štátne webstránky, so zreteľom na ID-SK dizajn. Cieľom je nielen zabezpečiť jednotný dizajn pre všetky štátne webové stránky, ale aj zabezpečiť ich praktickú funkčnosť prostredníctvom online formulárov a UX dizajnu založeného na strome životných situácií občana.

## Hlavné vlastnosti:

- Založený na django 4.0.
- Využíva ID-SK a GOV-UK knižnice.
- Stránky sú navrhnuté tak, aby boli čo najviac dynamické.
- Orientácia na praktické využitie a životné situácie občana.

## Štruktura projektu:

Projekt nasleduje filozofiu Django, kde každá appka slúži jednému účelu. 

- **MainPage**: Uvodná obrazovka

  
- **CategoryPage**: Zobrazuje stránky podľa kategórie.
  
  
- **ArticlePage**: Zobrazenie článku.
 
  
- **LoginPage**: Prihlásenie do administrácie.
  
  
- **AdminPage**: Administrácia.


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

- Kategórie a hlavná stránka budú mať pevné rozloženie s možnosťou meniť len obsah jednotlivých modulov.
- Hlavným zámerom je vytvoriť jednoduché CMS pre správu štátnych webov ako alternatíva k WordPressu.

---

Ak máte akékoľvek otázky alebo pripomienky, prosím, neváhajte nás kontaktovať. Ďakujeme za využitie našeho CMS!
