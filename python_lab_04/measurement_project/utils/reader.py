def prochitat_chisla(put_k_faylu):
    spisok_chisel = []
    with open(put_k_faylu, "r", encoding="utf-8") as fayl:
        for stroka in fayl:
            chislo = float(stroka.strip())
            spisok_chisel.append(chislo)
    return spisok_chisel