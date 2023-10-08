# ANATOMY-for-dummies
Opetussovellus anatomiasta

Sovelluksen on tarkoitus olla matalan kynnyksen opetussovellus parempaan anatomiatuntemukseen.
Sen on myös tarkoitus auttaa oppilasta innostumaan kehonhuollosta ja antamaan
sitä varten neuvoja ja vinkkejä. Sovelluksesta löytyy myös kursseista fun fact -teemaisia tietoiskuja.
Mikäli lopussa jää aikaa niin aion tehdä kurssialustalle keskustelupalstan, jossa kurssin opiskelijat voivat keskustella kurssin aiheista tai pyytää apua.

Sovelluksen idea:
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

(08.09.2023)
Tämän hetken tilanne sovelluksen testauksessa:
- Käyttäjä voi kirjautua sisään tai tehdä käyttäjätunnuksen.
- Sovelluksen html tiedostot ja layout ovat käytännössä valmiit.
- Sovellukseen on lisätty uusia tauluja tietokantaan.
- Sovellukseen on tehty pohjat tuleville metodeille.
- Kokonaisuus alkaa olla kunnossa, mutta hion vielä eri objektien välistä toiminnalisuutta, jonka vuoksi sovellusta ei voi tällä hetkellä sen enempää testata.
- Viimeisin git push oli tehty kaikki tiedostot yhdessä, koska en ollut saanut sitä aikaisemmin toimimaan (ongelma personal tokenin luonnissa). Jatkossa teen git pushin jokaisen muutoksen jälkeen.

Sovelluksen taulut:
1. Users
2. Courses
3. Lessons
4. Enrollments
5. Choices
6. Answers
7. Reviews

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
