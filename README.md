Juomamaailma-Scrape
===================

This utility scrapes the Juomamaailma.fi site for product information, making it ostensibly easier to order beverages
for your office or organization.

Usage of Juomamaailma.fi is governed by [their terms of use](https://www.juomamaailma.fi/media/wysiwyg/kayttoehdot.pdf).
In particular, one should note that copying, editing and use of any material, including text as downloaded by this tool,
requires express permission from Hartwall:

> Palvelun sisältö on suojattu tekijänoikeuksilla sekä mahdollisesti myös muilla immateriaalioikeuksilla. 
> Kaikenlainen Palvelussa olevan materiaalin (kuten tekstit ja valokuvat) kopioiminen, muokkaaminen, käyttö, 
> tallentaminen ja jakelu on kielletty, ellei sivustolla nimenomaisesti toisin mainita. Hartwall pidättää itsellään 
> kaikki oikeudet, joita ei nimenomaisesti ole tässä myönnetty.

One can argue that this means use of the site at all is implicitly forbidden too, since one's user agent needs to download
(copy and save) images and text from the site.

Usage
-----

* Create a Python 3.6+ virtualenv.
* Install requirements, e.g. `pip install -r requirements.txt`
* Run `make`
* Enjoy `doc.tsv`