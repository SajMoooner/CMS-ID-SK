# Vlastné CMS pre štátne webstránky (ID-SK dizajn)

Toto CMS je navrhnuté špeciálne pre štátne webstránky, so zreteľom na ID-SK dizajn. Cieľom je nielen zabezpečiť jednotný dizajn pre všetky štátne webové stránky, ale aj zabezpečiť ich praktickú funkčnosť prostredníctvom online formulárov a UX dizajnu založeného na strome životných situácií občana.

## Demo

Celý projekt môžete otestovať na [mesto.slovakosoft.sk](https://mesto.slovakosoft.sk/).
Admin časť sa nachádza na [mesto.slovakosoft.sk/uvod](https://mesto.slovakosoft.sk/uvod).

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
  
- **AdminPage**: Slúži pre CRUD operácie 
- Pridanie/Uprava/Odstranenie kategórií
- Pridanie/Uprava/Odstranenie článkov

### Priečinky a súbory:

- `templates`: Obsahuje HTML súbory.
- `static`: Obsahuje CSS a JS súbory.
- `staticfiles`: Slúži pre spracovanie statických súborov nginxom.
- `models.py`: Definuje databázu.
- `urls.py`: Routing.
- `views`: Pohlady.
- `mestoSlovakoSoft`: Manažér apiek a centrálne miesto pre správu všetkých modulov/aplikácií.


## Dostupnosť:

- Hlavná stránka: [mesto.slovakosoft.sk](https://mesto.slovakosoft.sk/)
- Dynamická stránka pre kategórie: [mesto.slovakosoft.sk/kategoria/](https://mesto.slovakosoft.sk/kategoria/)
- Dynamická stránka pre články: [mesto.slovakosoft.sk/clanok/](https://mesto.slovakosoft.sk/clanok/)
- Stránka pre prihlásenie: [mesto.slovakosoft.sk/prihlasenie/](https://mesto.slovakosoft.sk/prihlasenie/)
- Administrátorské prostredie: [mesto.slovakosoft.sk/uvod/](https://mesto.slovakosoft.sk/uvod/)

## Poznámky:

- Projekt obsahuje aj varovania, ale netreba sa ich báť, pretože zákony sú vymyslené.
- Hlavným zámerom je vytvoriť jednoduché CMS pre správu štátnych webov ako alternatíva k WordPressu.
- Tento CMS systém nie je určený ako centrálny systém. Bol navrhnutý a vyvinutý v súlade s požiadavkami UVO pre vývoj softvéru.


## Systém v praxi:

# MainPage

<img width="823" alt="image" src="https://github.com/SajMoooner/CMS-ID-SK/assets/70257823/a1df576b-9217-42c8-8569-c5fcbd43f932">

# CategoryPage

<img width="595" alt="image" src="https://github.com/SajMoooner/CMS-ID-SK/assets/70257823/6a1df68d-9f59-4313-a7d1-cba81551c7ae">

# ArticlePage

<img width="781" alt="image" src="https://github.com/SajMoooner/CMS-ID-SK/assets/70257823/511c27fe-b51d-4930-bc1b-fcaacb33b234">

# LoginPage

<img width="715" alt="image" src="https://github.com/SajMoooner/CMS-ID-SK/assets/70257823/d3cf425f-9e8f-4869-8ab2-aab054bfc408">

# AdminPage

<img width="674" alt="image" src="https://github.com/SajMoooner/CMS-ID-SK/assets/70257823/48fd37c3-b7cf-43d0-8eef-490dffeebe5f">


