import sqlite3
import os

class Evidence:
    def __init__(self, ):
        self.conn = sqlite3.connect('databaze.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.vytvor_tabulku()

    def vytvor_tabulku(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS klienti (
                klient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                jméno TEXT, 
                příjmení TEXT, 
                věk INTEGER, 
                email TEXT, 
                telefon INTEGER, 
                ulice_ČP TEXT, 
                město TEXT, 
                PSČ TEXT)""")
        
    def vypis_operace(self):
        operace = ["Přidat nového pojištěného", "Vypsat seznam pojištěných", "Vyhledat pojištěného a zobrazit podrobnosti",
                   "Editovat pojištěnce", "Ukončit program"]
        for i in range(len(operace)):
            print(f"{i+1} - {operace[i]}")
        
    def pridej(self, jmeno, prijmeni, vek, email, telefon, ulice, mesto, psc):
        novy_klient = (jmeno, prijmeni, vek, email, telefon, ulice, mesto, psc)
        self.c.execute("""INSERT OR IGNORE INTO klienti (
                'jméno', 'příjmení', 'věk', 'email', 'telefon', 'ulice_ČP','město', 'PSČ') 
                VALUES(?,?,?,?,?,?,?,?)""", novy_klient)
        self.conn.commit()
    
    def vypis_klienty(self):
        self.c.execute("SELECT klient_id, jméno, příjmení, věk FROM klienti LIMIT 50")
        klienti = self.c.fetchall()
        return klienti

    def vyhledej(self, jmeno, prijmeni):
        self.c.execute("SELECT * FROM klienti WHERE jméno=(?) AND příjmení=(?)", (jmeno, prijmeni))
        return (self.c.fetchall())
        
    def edituj(self, jmeno, prijmeni, udaj, hodnota):
        self.c.execute("UPDATE klienti SET {}=? WHERE jméno=? AND příjmení=?".format(udaj), (hodnota, jmeno, prijmeni))
        self.conn.commit()

evidence = Evidence()