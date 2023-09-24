# ANATOMY-for-dummies
Opetussovellus anatomiasta

Sovelluksen on tarkoitus olla matalan kynnyksen opetussovellus parempaan anatomiatuntemukseen.
Sen on myös tarkoitus auttaa oppilasta innostumaan kehonhuollosta ja antamaan
sitä varten neuvoja ja vinkkejä. Sovelluksesta löytyy myös kursseista fun fact -teemaisia tietoiskuja.

Sovelluksen käyttäjä toimii opiskelijan roolissa.
Opiskelija tekee oman käyttäjätunnuksen, jossa hän luo käyttäjänimen ja antaa salasanan.
Sen jälkeen opiskelija pääsee kurssialustalle, josta löytyy eri pienkursseja eri lihasryhmistä ja muuhun anatomiaan liittyvästä.
Opiskelija valitsee kurssin. Jokaisen kurssin alussa on lyhyt teoriaosuus kyseisestä lihasryhmästä. 
Sen jälkeen on monivalintatehtäviä ja kun opiskelija osaa jo tarpeeksi, niin väliin tulee myös
kirjallisia tehtäviä. Täytyy esimerkiksi kirjoittaa lihaksen nimi.
Sovelluksessa on myös mahdolliesti kuvat kyseisistä lihaksista helpottaakseen opetusta.
Lopuksi, kun opiskelija on päässyt kurssista läpi, näkee hän pienen ohjeen miten tehdä lyhyt
taukojumppa kyseiselle lihasryhmälle työ-/koulupäivän aikana.
Opiskelija pystyy seuraamaan edistymistä sovelluksen tilastoista.
Jokainen kurssi vaatii tietyn minimi määrän, jotta sen voi päästä läpi.

Sovelluksen opettaja pystyy tekemään/poistamaan kursseja tai lisäämään tietoja jo olemassa oleviin kursseihin.
Opettajalla on omat käyttäjätunnukset, jotka mahdollistavat laajemmat muutokset.
Opettaja pystyy näkemään kurssin osallistujat ja heidän tilastot.

(24.09.2023)
Sovelluksen ominaisuudet:
1. Käyttäjä voi kirjautua sisään tai tehdä käyttäjätunnuksen (Toimii)
2. Käyttäjä voi osallistua kurssialustalla eri kursseille
3. Kursseilla on monivalinta-, sekä yksisanaisia kirjoitustehtäviä
4. Kurssin edetessä käyttäjälle näkyy nippelitietoja anatomiasta
5. Käyttäjän päästessä kurssista läpi, ilmestyy hänelle lyhyt kehonhuolto ohje tai vinkki
6. Käyttäjä voi seurata etenemistään tilastojen avulla
7. Pääkäyttäjä voi kirjautua kurssialustalle
8. Pääkäyttäjä näkee muiden käyttäjien etenemisen kursseilla
9. Pääkäyttäjä voi lisätä tai poistaa kurssin käyttäjiä

- Sovelluksen ominaisuudet kirjautuminen ja käyttäjätunnuksen tekeminen löytyvät koodista. Myös tietokantayhteys on saatu toimimaan. Tällä hetkellä "login" tai "register" aiheuttaa virheen nimeltä Bad request. Kyseessä on todennäköisesti jokin virhe "POST" komennossa, jota en nyt löydä. Seuraavaksi on tarkoitus korjata kyseinen virhe, lisätä uusia tauluja ja rakentaa kurssialustan pohja. Tarvittavien toiminnallisuuksien jälkeen alan muokkaamaan sovelluksen visuaalista ilmettä. Sovellus on vasta alussa, mutta sille on tehty hyvä pohja jatkolle.

Sovelluksen taulut:
1. Users
2. (Muut ovat vielä tulossa)
3. Muun muassa: reviews, answers, options ja niin edelleen.

Sovelluksen asentamisen ohjeet paikallisesti:
1. Tallenna tästä sovelluksesta löytyvät tiedostot samaan kansioon. (Huomaa tiedoston requirement.txt vaadittavat paketit ja lataa ne)
2. Luo .env tiedosto kyseiseen kansioon ja lisää siihen seuraavat tiedot:
 - DATABASE_URL=<database-local-address> (postgresql:///user)
 - SECRET_KEY=<your_secret_key>
3. Avaa terminaali, aktivoi virtuaaliympäristö ja aja seuraavat käskyt:
 - $ python3 -m venv venv
 - $ source venv/bin/activate
 - $ pip install -r ./requirements.txt
4. Luo tietokanta psql:ssä:
 - $ psql < schema.sql
5. Käynnistä sovellus:
 - $ flask run
