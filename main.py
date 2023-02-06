import helyzet
import minosites
import sorozat


minosites.beker()
minosites.ertekel()

v_szamok = sorozat.veletlen_szamok()
darab = sorozat.oszthatok_szama(v_szamok)
sorozat.veletlen_szamok()
sorozat.szamok_csillag(v_szamok)
sorozat.konzolra_ir(sorozat.oszthatok_szama(v_szamok))
sorozat.fajl_ir(darab)


gepek = helyzet.beolvas()
helyzet.beolvas()
helyzet.gepek_szama(gepek)
helyzet.atlag(gepek)
helyzet.legkisebb(gepek)
