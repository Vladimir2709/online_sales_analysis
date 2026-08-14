# Online Sales Analysis

Python projekat za analizu prodajnih podataka u online prodavnici, razvijen kao završni zadatak kursa "Rad sa GitHubom i Pythonom". Projekat demonstrira upravljanje verzijama kroz Git (grane, spajanje, rešavanje konflikata) i primenu OOP koncepata u Pythonu.

## Struktura projekta

- `product.py` – klasa `Product`
- `product_manager.py` – klasa `ProductManager`
- `cart.py` – klasa `Cart`
- `main.py` – glavna skripta koja povezuje sve klase
- `.gitignore` – izuzima poverljive podatke i snimke ekrana iz verzionisanja
- `config.json` – primer konfiguracionog fajla sa osetljivim podacima (ignorisan od strane Git-a)

## Klase

### Product (`product.py`)
Predstavlja pojedinačni proizvod u prodavnici.

- **Atributi:** `name`, `price`, `quantity`
- **Metodi:**
  - `display_info()` – prikazuje informacije o proizvodu
  - `update_quantity(new_quantity)` – ažurira količinu proizvoda na skladištu

### ProductManager (`product_manager.py`)
Upravlja kolekcijom svih dostupnih proizvoda.

- **Atributi:** `products` – lista svih proizvoda
- **Metodi:**
  - `add_product(product)` – dodaje proizvod u listu
  - `remove_product(name)` – uklanja proizvod na osnovu imena
  - `display_products()` – prikazuje sve dostupne proizvode
  - `total_inventory_value()` – računa ukupnu vrednost celog inventara

### Cart (`cart.py`)
Predstavlja korpu kupca.

- **Atributi:** `cart_items` – lista proizvoda u korpi
- **Metode:**
  - `add_item(product)` – dodaje proizvod u korpu
  - `calculate_total()` – računa ukupnu vrednost za naplatu
  - `display_cart()` – prikazuje sadržaj korpe

## Pokretanje projekta

```bash
python main.py
```

## Git workflow

Projekat je razvijan kroz sledeće grane:

1. `main` – osnovna funkcionalnost (Product, ProductManager)
2. `add-product-removal` – dodavanje metode za uklanjanje proizvoda
3. `add-cart-functionality` – dodavanje klase Cart i integracija u main.py

Grane su spojene u `main` uz ručno rešavanje konflikata nastalih paralelnim izmenama `main.py`.

## Sigurnost podataka

Fajl `config.json` sadrži osetljive podatke (API ključ, URL baze) i namerno je isključen iz verzionisanja putem `.gitignore`, zajedno sa svim snimcima ekrana korišćenim za dokumentovanje procesa rada.