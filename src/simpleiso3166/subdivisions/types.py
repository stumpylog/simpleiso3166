from typing import Literal

SubdivisionCodeType = Literal[
    # Principality of Andorra
    "AD-02",  # Canillo
    "AD-03",  # Encamp
    "AD-04",  # La Massana
    "AD-05",  # Ordino
    "AD-06",  # Sant Julià de Lòria
    "AD-07",  # Andorra la Vella
    "AD-08",  # Escaldes-Engordany
    # United Arab Emirates
    "AE-AJ",  # ‘Ajmān
    "AE-AZ",  # Abū Z̧aby
    "AE-DU",  # Dubayy
    "AE-FU",  # Al Fujayrah
    "AE-RK",  # Ra’s al Khaymah
    "AE-SH",  # Ash Shāriqah
    "AE-UQ",  # Umm al Qaywayn
    # Islamic Republic of Afghanistan
    "AF-BAL",  # Balkh
    "AF-BAM",  # Bāmyān
    "AF-BDG",  # Bādghīs
    "AF-BDS",  # Badakhshān
    "AF-BGL",  # Baghlān
    "AF-DAY",  # Dāykundī
    "AF-FRA",  # Farāh
    "AF-FYB",  # Fāryāb
    "AF-GHA",  # Ghaznī
    "AF-GHO",  # Ghōr
    "AF-HEL",  # Helmand
    "AF-HER",  # Herāt
    "AF-JOW",  # Jowzjān
    "AF-KAB",  # Kābul
    "AF-KAN",  # Kandahār
    "AF-KAP",  # Kāpīsā
    "AF-KDZ",  # Kunduz
    "AF-KHO",  # Khōst
    "AF-KNR",  # Kunaṟ
    "AF-LAG",  # Laghmān
    "AF-LOG",  # Lōgar
    "AF-NAN",  # Nangarhār
    "AF-NIM",  # Nīmrōz
    "AF-NUR",  # Nūristān
    "AF-PAN",  # Panjshayr
    "AF-PAR",  # Parwān
    "AF-PIA",  # Paktiyā
    "AF-PKA",  # Paktīkā
    "AF-SAM",  # Samangān
    "AF-SAR",  # Sar-e Pul
    "AF-TAK",  # Takhār
    "AF-URU",  # Uruzgān
    "AF-WAR",  # Wardak
    "AF-ZAB",  # Zābul
    # Antigua and Barbuda
    "AG-03",  # Saint George
    "AG-04",  # Saint John
    "AG-05",  # Saint Mary
    "AG-06",  # Saint Paul
    "AG-07",  # Saint Peter
    "AG-08",  # Saint Philip
    "AG-10",  # Barbuda
    "AG-11",  # Redonda
    # Anguilla
    # (no subdivisions)
    # Republic of Albania
    "AL-01",  # Berat
    "AL-02",  # Durrës
    "AL-03",  # Elbasan
    "AL-04",  # Fier
    "AL-05",  # Gjirokastër
    "AL-06",  # Korçë
    "AL-07",  # Kukës
    "AL-08",  # Lezhë
    "AL-09",  # Dibër
    "AL-10",  # Shkodër
    "AL-11",  # Tiranë
    "AL-12",  # Vlorë
    # Republic of Armenia
    "AM-AG",  # Aragac̣otn
    "AM-AR",  # Ararat
    "AM-AV",  # Armavir
    "AM-ER",  # Erevan
    "AM-GR",  # Geġark'unik'
    "AM-KT",  # Kotayk'
    "AM-LO",  # Loṙi
    "AM-SH",  # Širak
    "AM-SU",  # Syunik'
    "AM-TV",  # Tavuš
    "AM-VD",  # Vayoć Jor
    # Republic of Angola
    "AO-BGO",  # Bengo
    "AO-BGU",  # Benguela
    "AO-BIE",  # Bié
    "AO-CAB",  # Cabinda
    "AO-CCU",  # Cuando Cubango
    "AO-CNN",  # Cunene
    "AO-CNO",  # Cuanza-Norte
    "AO-CUS",  # Cuanza-Sul
    "AO-HUA",  # Huambo
    "AO-HUI",  # Huíla
    "AO-LNO",  # Lunda-Norte
    "AO-LSU",  # Lunda-Sul
    "AO-LUA",  # Luanda
    "AO-MAL",  # Malange
    "AO-MOX",  # Moxico
    "AO-NAM",  # Namibe
    "AO-UIG",  # Uíge
    "AO-ZAI",  # Zaire
    # Antarctica
    # (no subdivisions)
    # Argentine Republic
    "AR-A",  # Salta
    "AR-B",  # Buenos Aires
    "AR-C",  # Ciudad Autónoma de Buenos Aires
    "AR-D",  # San Luis
    "AR-E",  # Entre Ríos
    "AR-F",  # La Rioja
    "AR-G",  # Santiago del Estero
    "AR-H",  # Chaco
    "AR-J",  # San Juan
    "AR-K",  # Catamarca
    "AR-L",  # La Pampa
    "AR-M",  # Mendoza
    "AR-N",  # Misiones
    "AR-P",  # Formosa
    "AR-Q",  # Neuquén
    "AR-R",  # Río Negro
    "AR-S",  # Santa Fe
    "AR-T",  # Tucumán
    "AR-U",  # Chubut
    "AR-V",  # Tierra del Fuego
    "AR-W",  # Corrientes
    "AR-X",  # Córdoba
    "AR-Y",  # Jujuy
    "AR-Z",  # Santa Cruz
    # American Samoa
    # (no subdivisions)
    # Republic of Austria
    "AT-1",  # Burgenland
    "AT-2",  # Kärnten
    "AT-3",  # Niederösterreich
    "AT-4",  # Oberösterreich
    "AT-5",  # Salzburg
    "AT-6",  # Steiermark
    "AT-7",  # Tirol
    "AT-8",  # Vorarlberg
    "AT-9",  # Wien
    # Australia
    "AU-ACT",  # Australian Capital Territory
    "AU-NSW",  # New South Wales
    "AU-NT",  # Northern Territory
    "AU-QLD",  # Queensland
    "AU-SA",  # South Australia
    "AU-TAS",  # Tasmania
    "AU-VIC",  # Victoria
    "AU-WA",  # Western Australia
    # Aruba
    # (no subdivisions)
    # Åland Islands
    # (no subdivisions)
    # Republic of Azerbaijan
    "AZ-ABS",  # Abşeron
    "AZ-AGA",  # Ağstafa
    "AZ-AGC",  # Ağcabədi
    "AZ-AGM",  # Ağdam
    "AZ-AGS",  # Ağdaş
    "AZ-AGU",  # Ağsu
    "AZ-AST",  # Astara
    "AZ-BA",  # Bakı
    "AZ-BAB",  # Babək
    "AZ-BAL",  # Balakən
    "AZ-BAR",  # Bərdə
    "AZ-BEY",  # Beyləqan
    "AZ-BIL",  # Biləsuvar
    "AZ-CAB",  # Cəbrayıl
    "AZ-CAL",  # Cəlilabad
    "AZ-CUL",  # Culfa
    "AZ-DAS",  # Daşkəsən
    "AZ-FUZ",  # Füzuli
    "AZ-GA",  # Gəncə
    "AZ-GAD",  # Gədəbəy
    "AZ-GOR",  # Goranboy
    "AZ-GOY",  # Göyçay
    "AZ-GYG",  # Göygöl
    "AZ-HAC",  # Hacıqabul
    "AZ-IMI",  # İmişli
    "AZ-ISM",  # İsmayıllı
    "AZ-KAL",  # Kəlbəcər
    "AZ-KAN",  # Kǝngǝrli
    "AZ-KUR",  # Kürdəmir
    "AZ-LA",  # Lənkəran
    "AZ-LAC",  # Laçın
    "AZ-LAN",  # Lənkəran
    "AZ-LER",  # Lerik
    "AZ-MAS",  # Masallı
    "AZ-MI",  # Mingəçevir
    "AZ-NA",  # Naftalan
    "AZ-NEF",  # Neftçala
    "AZ-NV",  # Naxçıvan
    "AZ-NX",  # Naxçıvan
    "AZ-OGU",  # Oğuz
    "AZ-ORD",  # Ordubad
    "AZ-QAB",  # Qəbələ
    "AZ-QAX",  # Qax
    "AZ-QAZ",  # Qazax
    "AZ-QBA",  # Quba
    "AZ-QBI",  # Qubadlı
    "AZ-QOB",  # Qobustan
    "AZ-QUS",  # Qusar
    "AZ-SA",  # Şəki
    "AZ-SAB",  # Sabirabad
    "AZ-SAD",  # Sədərək
    "AZ-SAH",  # Şahbuz
    "AZ-SAK",  # Şəki
    "AZ-SAL",  # Salyan
    "AZ-SAR",  # Şərur
    "AZ-SAT",  # Saatlı
    "AZ-SBN",  # Şabran
    "AZ-SIY",  # Siyəzən
    "AZ-SKR",  # Şəmkir
    "AZ-SM",  # Sumqayıt
    "AZ-SMI",  # Şamaxı
    "AZ-SMX",  # Samux
    "AZ-SR",  # Şirvan
    "AZ-SUS",  # Şuşa
    "AZ-TAR",  # Tərtər
    "AZ-TOV",  # Tovuz
    "AZ-UCA",  # Ucar
    "AZ-XA",  # Xankəndi
    "AZ-XAC",  # Xaçmaz
    "AZ-XCI",  # Xocalı
    "AZ-XIZ",  # Xızı
    "AZ-XVD",  # Xocavənd
    "AZ-YAR",  # Yardımlı
    "AZ-YE",  # Yevlax
    "AZ-YEV",  # Yevlax
    "AZ-ZAN",  # Zəngilan
    "AZ-ZAQ",  # Zaqatala
    "AZ-ZAR",  # Zərdab
    # Republic of Bosnia and Herzegovina
    "BA-BIH",  # Federacija Bosne i Hercegovine
    "BA-BRC",  # Brčko distrikt
    "BA-SRP",  # Republika Srpska
    # Barbados
    "BB-01",  # Christ Church
    "BB-02",  # Saint Andrew
    "BB-03",  # Saint George
    "BB-04",  # Saint James
    "BB-05",  # Saint John
    "BB-06",  # Saint Joseph
    "BB-07",  # Saint Lucy
    "BB-08",  # Saint Michael
    "BB-09",  # Saint Peter
    "BB-10",  # Saint Philip
    "BB-11",  # Saint Thomas
    # People's Republic of Bangladesh
    "BD-01",  # Bandarban
    "BD-02",  # Barguna
    "BD-03",  # Bogura
    "BD-04",  # Brahmanbaria
    "BD-05",  # Bagerhat
    "BD-06",  # Barishal
    "BD-07",  # Bhola
    "BD-08",  # Cumilla
    "BD-09",  # Chandpur
    "BD-10",  # Chattogram
    "BD-11",  # Cox's Bazar
    "BD-12",  # Chuadanga
    "BD-13",  # Dhaka
    "BD-14",  # Dinajpur
    "BD-15",  # Faridpur
    "BD-16",  # Feni
    "BD-17",  # Gopalganj
    "BD-18",  # Gazipur
    "BD-19",  # Gaibandha
    "BD-20",  # Habiganj
    "BD-21",  # Jamalpur
    "BD-22",  # Jashore
    "BD-23",  # Jhenaidah
    "BD-24",  # Joypurhat
    "BD-25",  # Jhalakathi
    "BD-26",  # Kishoreganj
    "BD-27",  # Khulna
    "BD-28",  # Kurigram
    "BD-29",  # Khagrachhari
    "BD-30",  # Kushtia
    "BD-31",  # Lakshmipur
    "BD-32",  # Lalmonirhat
    "BD-33",  # Manikganj
    "BD-34",  # Mymensingh
    "BD-35",  # Munshiganj
    "BD-36",  # Madaripur
    "BD-37",  # Magura
    "BD-38",  # Moulvibazar
    "BD-39",  # Meherpur
    "BD-40",  # Narayanganj
    "BD-41",  # Netrakona
    "BD-42",  # Narsingdi
    "BD-43",  # Narail
    "BD-44",  # Natore
    "BD-45",  # Chapai Nawabganj
    "BD-46",  # Nilphamari
    "BD-47",  # Noakhali
    "BD-48",  # Naogaon
    "BD-49",  # Pabna
    "BD-50",  # Pirojpur
    "BD-51",  # Patuakhali
    "BD-52",  # Panchagarh
    "BD-53",  # Rajbari
    "BD-54",  # Rajshahi
    "BD-55",  # Rangpur
    "BD-56",  # Rangamati
    "BD-57",  # Sherpur
    "BD-58",  # Satkhira
    "BD-59",  # Sirajganj
    "BD-60",  # Sylhet
    "BD-61",  # Sunamganj
    "BD-62",  # Shariatpur
    "BD-63",  # Tangail
    "BD-64",  # Thakurgaon
    "BD-A",  # Barishal
    "BD-B",  # Chattogram
    "BD-C",  # Dhaka
    "BD-D",  # Khulna
    "BD-E",  # Rajshahi
    "BD-F",  # Rangpur
    "BD-G",  # Sylhet
    "BD-H",  # Mymensingh
    # Kingdom of Belgium
    "BE-BRU",  # Bruxelles-Capitale, Région de
    "BE-VAN",  # Antwerpen
    "BE-VBR",  # Vlaams-Brabant
    "BE-VLG",  # Vlaams Gewest
    "BE-VLI",  # Limburg
    "BE-VOV",  # Oost-Vlaanderen
    "BE-VWV",  # West-Vlaanderen
    "BE-WAL",  # wallonne, Région
    "BE-WBR",  # Brabant wallon
    "BE-WHT",  # Hainaut
    "BE-WLG",  # Liège
    "BE-WLX",  # Luxembourg
    "BE-WNA",  # Namur
    # Burkina Faso
    "BF-01",  # Boucle du Mouhoun
    "BF-02",  # Cascades
    "BF-03",  # Centre
    "BF-04",  # Centre-Est
    "BF-05",  # Centre-Nord
    "BF-06",  # Centre-Ouest
    "BF-07",  # Centre-Sud
    "BF-08",  # Est
    "BF-09",  # Hauts-Bassins
    "BF-10",  # Nord
    "BF-11",  # Plateau-Central
    "BF-12",  # Sahel
    "BF-13",  # Sud-Ouest
    "BF-BAL",  # Balé
    "BF-BAM",  # Bam
    "BF-BAN",  # Banwa
    "BF-BAZ",  # Bazèga
    "BF-BGR",  # Bougouriba
    "BF-BLG",  # Boulgou
    "BF-BLK",  # Boulkiemdé
    "BF-COM",  # Comoé
    "BF-GAN",  # Ganzourgou
    "BF-GNA",  # Gnagna
    "BF-GOU",  # Gourma
    "BF-HOU",  # Houet
    "BF-IOB",  # Ioba
    "BF-KAD",  # Kadiogo
    "BF-KEN",  # Kénédougou
    "BF-KMD",  # Komondjari
    "BF-KMP",  # Kompienga
    "BF-KOP",  # Koulpélogo
    "BF-KOS",  # Kossi
    "BF-KOT",  # Kouritenga
    "BF-KOW",  # Kourwéogo
    "BF-LER",  # Léraba
    "BF-LOR",  # Loroum
    "BF-MOU",  # Mouhoun
    "BF-NAM",  # Namentenga
    "BF-NAO",  # Nahouri
    "BF-NAY",  # Nayala
    "BF-NOU",  # Noumbiel
    "BF-OUB",  # Oubritenga
    "BF-OUD",  # Oudalan
    "BF-PAS",  # Passoré
    "BF-PON",  # Poni
    "BF-SEN",  # Séno
    "BF-SIS",  # Sissili
    "BF-SMT",  # Sanmatenga
    "BF-SNG",  # Sanguié
    "BF-SOM",  # Soum
    "BF-SOR",  # Sourou
    "BF-TAP",  # Tapoa
    "BF-TUI",  # Tuy
    "BF-YAG",  # Yagha
    "BF-YAT",  # Yatenga
    "BF-ZIR",  # Ziro
    "BF-ZON",  # Zondoma
    "BF-ZOU",  # Zoundwéogo
    # Republic of Bulgaria
    "BG-01",  # Blagoevgrad
    "BG-02",  # Burgas
    "BG-03",  # Varna
    "BG-04",  # Veliko Tarnovo
    "BG-05",  # Vidin
    "BG-06",  # Vratsa
    "BG-07",  # Gabrovo
    "BG-08",  # Dobrich
    "BG-09",  # Kardzhali
    "BG-10",  # Kyustendil
    "BG-11",  # Lovech
    "BG-12",  # Montana
    "BG-13",  # Pazardzhik
    "BG-14",  # Pernik
    "BG-15",  # Pleven
    "BG-16",  # Plovdiv
    "BG-17",  # Razgrad
    "BG-18",  # Ruse
    "BG-19",  # Silistra
    "BG-20",  # Sliven
    "BG-21",  # Smolyan
    "BG-22",  # Sofia (stolitsa)
    "BG-23",  # Sofia
    "BG-24",  # Stara Zagora
    "BG-25",  # Targovishte
    "BG-26",  # Haskovo
    "BG-27",  # Shumen
    "BG-28",  # Yambol
    # Kingdom of Bahrain
    "BH-13",  # Al ‘Āşimah
    "BH-14",  # Al Janūbīyah
    "BH-15",  # Al Muḩarraq
    "BH-17",  # Ash Shamālīyah
    # Republic of Burundi
    "BI-BB",  # Bubanza
    "BI-BL",  # Bujumbura Rural
    "BI-BM",  # Bujumbura Mairie
    "BI-BR",  # Bururi
    "BI-CA",  # Cankuzo
    "BI-CI",  # Cibitoke
    "BI-GI",  # Gitega
    "BI-KI",  # Kirundo
    "BI-KR",  # Karuzi
    "BI-KY",  # Kayanza
    "BI-MA",  # Makamba
    "BI-MU",  # Muramvya
    "BI-MW",  # Mwaro
    "BI-MY",  # Muyinga
    "BI-NG",  # Ngozi
    "BI-RM",  # Rumonge
    "BI-RT",  # Rutana
    "BI-RY",  # Ruyigi
    # Republic of Benin
    "BJ-AK",  # Atacora
    "BJ-AL",  # Alibori
    "BJ-AQ",  # Atlantique
    "BJ-BO",  # Borgou
    "BJ-CO",  # Collines
    "BJ-DO",  # Donga
    "BJ-KO",  # Couffo
    "BJ-LI",  # Littoral
    "BJ-MO",  # Mono
    "BJ-OU",  # Ouémé
    "BJ-PL",  # Plateau
    "BJ-ZO",  # Zou
    # Saint Barthélemy
    # (no subdivisions)
    # Bermuda
    # (no subdivisions)
    # Brunei Darussalam
    "BN-BE",  # Belait
    "BN-BM",  # Brunei-Muara
    "BN-TE",  # Temburong
    "BN-TU",  # Tutong
    # Plurinational State of Bolivia
    "BO-B",  # El Beni
    "BO-C",  # Cochabamba
    "BO-H",  # Chuquisaca
    "BO-L",  # La Paz
    "BO-N",  # Pando
    "BO-O",  # Oruro
    "BO-P",  # Potosí
    "BO-S",  # Santa Cruz
    "BO-T",  # Tarija
    # Bonaire, Sint Eustatius and Saba
    "BQ-BO",  # Bonaire
    "BQ-SA",  # Saba
    "BQ-SE",  # Sint Eustatius
    # Federative Republic of Brazil
    "BR-AC",  # Acre
    "BR-AL",  # Alagoas
    "BR-AM",  # Amazonas
    "BR-AP",  # Amapá
    "BR-BA",  # Bahia
    "BR-CE",  # Ceará
    "BR-DF",  # Distrito Federal
    "BR-ES",  # Espírito Santo
    "BR-GO",  # Goiás
    "BR-MA",  # Maranhão
    "BR-MG",  # Minas Gerais
    "BR-MS",  # Mato Grosso do Sul
    "BR-MT",  # Mato Grosso
    "BR-PA",  # Pará
    "BR-PB",  # Paraíba
    "BR-PE",  # Pernambuco
    "BR-PI",  # Piauí
    "BR-PR",  # Paraná
    "BR-RJ",  # Rio de Janeiro
    "BR-RN",  # Rio Grande do Norte
    "BR-RO",  # Rondônia
    "BR-RR",  # Roraima
    "BR-RS",  # Rio Grande do Sul
    "BR-SC",  # Santa Catarina
    "BR-SE",  # Sergipe
    "BR-SP",  # São Paulo
    "BR-TO",  # Tocantins
    # Commonwealth of the Bahamas
    "BS-AK",  # Acklins
    "BS-BI",  # Bimini
    "BS-BP",  # Black Point
    "BS-BY",  # Berry Islands
    "BS-CE",  # Central Eleuthera
    "BS-CI",  # Cat Island
    "BS-CK",  # Crooked Island and Long Cay
    "BS-CO",  # Central Abaco
    "BS-CS",  # Central Andros
    "BS-EG",  # East Grand Bahama
    "BS-EX",  # Exuma
    "BS-FP",  # City of Freeport
    "BS-GC",  # Grand Cay
    "BS-HI",  # Harbour Island
    "BS-HT",  # Hope Town
    "BS-IN",  # Inagua
    "BS-LI",  # Long Island
    "BS-MC",  # Mangrove Cay
    "BS-MG",  # Mayaguana
    "BS-MI",  # Moore's Island
    "BS-NE",  # North Eleuthera
    "BS-NO",  # North Abaco
    "BS-NP",  # New Providence
    "BS-NS",  # North Andros
    "BS-RC",  # Rum Cay
    "BS-RI",  # Ragged Island
    "BS-SA",  # South Andros
    "BS-SE",  # South Eleuthera
    "BS-SO",  # South Abaco
    "BS-SS",  # San Salvador
    "BS-SW",  # Spanish Wells
    "BS-WG",  # West Grand Bahama
    # Kingdom of Bhutan
    "BT-11",  # Paro
    "BT-12",  # Chhukha
    "BT-13",  # Haa
    "BT-14",  # Samtse
    "BT-15",  # Thimphu
    "BT-21",  # Tsirang
    "BT-22",  # Dagana
    "BT-23",  # Punakha
    "BT-24",  # Wangdue Phodrang
    "BT-31",  # Sarpang
    "BT-32",  # Trongsa
    "BT-33",  # Bumthang
    "BT-34",  # Zhemgang
    "BT-41",  # Trashigang
    "BT-42",  # Monggar
    "BT-43",  # Pema Gatshel
    "BT-44",  # Lhuentse
    "BT-45",  # Samdrup Jongkhar
    "BT-GA",  # Gasa
    "BT-TY",  # Trashi Yangtse
    # Bouvet Island
    # (no subdivisions)
    # Republic of Botswana
    "BW-CE",  # Central
    "BW-CH",  # Chobe
    "BW-FR",  # Francistown
    "BW-GA",  # Gaborone
    "BW-GH",  # Ghanzi
    "BW-JW",  # Jwaneng
    "BW-KG",  # Kgalagadi
    "BW-KL",  # Kgatleng
    "BW-KW",  # Kweneng
    "BW-LO",  # Lobatse
    "BW-NE",  # North East
    "BW-NW",  # North West
    "BW-SE",  # South East
    "BW-SO",  # Southern
    "BW-SP",  # Selibe Phikwe
    "BW-ST",  # Sowa Town
    # Republic of Belarus
    "BY-BR",  # Bresckaja voblasć
    "BY-HM",  # Gorod Minsk
    "BY-HO",  # Gomel'skaja oblast'
    "BY-HR",  # Grodnenskaja oblast'
    "BY-MA",  # Mahilioŭskaja voblasć
    "BY-MI",  # Minskaja oblast'
    "BY-VI",  # Viciebskaja voblasć
    # Belize
    "BZ-BZ",  # Belize
    "BZ-CY",  # Cayo
    "BZ-CZL",  # Corozal
    "BZ-OW",  # Orange Walk
    "BZ-SC",  # Stann Creek
    "BZ-TOL",  # Toledo
    # Canada
    "CA-AB",  # Alberta
    "CA-BC",  # British Columbia
    "CA-MB",  # Manitoba
    "CA-NB",  # New Brunswick
    "CA-NL",  # Newfoundland and Labrador
    "CA-NS",  # Nova Scotia
    "CA-NT",  # Northwest Territories
    "CA-NU",  # Nunavut
    "CA-ON",  # Ontario
    "CA-PE",  # Prince Edward Island
    "CA-QC",  # Quebec
    "CA-SK",  # Saskatchewan
    "CA-YT",  # Yukon
    # Cocos (Keeling) Islands
    # (no subdivisions)
    # Congo, The Democratic Republic of the
    "CD-BC",  # Kongo Central
    "CD-BU",  # Bas-Uélé
    "CD-EQ",  # Équateur
    "CD-HK",  # Haut-Katanga
    "CD-HL",  # Haut-Lomami
    "CD-HU",  # Haut-Uélé
    "CD-IT",  # Ituri
    "CD-KC",  # Kasaï Central
    "CD-KE",  # Kasaï Oriental
    "CD-KG",  # Kwango
    "CD-KL",  # Kwilu
    "CD-KN",  # Kinshasa
    "CD-KS",  # Kasaï
    "CD-LO",  # Lomami
    "CD-LU",  # Lualaba
    "CD-MA",  # Maniema
    "CD-MN",  # Mai-Ndombe
    "CD-MO",  # Mongala
    "CD-NK",  # Nord-Kivu
    "CD-NU",  # Nord-Ubangi
    "CD-SA",  # Sankuru
    "CD-SK",  # Sud-Kivu
    "CD-SU",  # Sud-Ubangi
    "CD-TA",  # Tanganyika
    "CD-TO",  # Tshopo
    "CD-TU",  # Tshuapa
    # Central African Republic
    "CF-AC",  # Ouham
    "CF-BB",  # Bamingui-Bangoran
    "CF-BGF",  # Bangui
    "CF-BK",  # Basse-Kotto
    "CF-HK",  # Haute-Kotto
    "CF-HM",  # Haut-Mbomou
    "CF-HS",  # Haute-Sangha / Mambéré-Kadéï
    "CF-KB",  # Gribingui
    "CF-KG",  # Kémo-Gribingui
    "CF-LB",  # Lobaye
    "CF-MB",  # Mbomou
    "CF-MP",  # Ombella-Mpoko
    "CF-NM",  # Nana-Mambéré
    "CF-OP",  # Ouham-Pendé
    "CF-SE",  # Sangha
    "CF-UK",  # Ouaka
    "CF-VK",  # Vakaga
    # Republic of the Congo
    "CG-11",  # Bouenza
    "CG-12",  # Pool
    "CG-13",  # Sangha
    "CG-14",  # Plateaux
    "CG-15",  # Cuvette-Ouest
    "CG-16",  # Pointe-Noire
    "CG-2",  # Lékoumou
    "CG-5",  # Kouilou
    "CG-7",  # Likouala
    "CG-8",  # Cuvette
    "CG-9",  # Niari
    "CG-BZV",  # Brazzaville
    # Swiss Confederation
    "CH-AG",  # Aargau
    "CH-AI",  # Appenzell Innerrhoden
    "CH-AR",  # Appenzell Ausserrhoden
    "CH-BE",  # Berne
    "CH-BL",  # Basel-Landschaft
    "CH-BS",  # Basel-Stadt
    "CH-FR",  # Fribourg
    "CH-GE",  # Genève
    "CH-GL",  # Glarus
    "CH-GR",  # Graubünden
    "CH-JU",  # Jura
    "CH-LU",  # Luzern
    "CH-NE",  # Neuchâtel
    "CH-NW",  # Nidwalden
    "CH-OW",  # Obwalden
    "CH-SG",  # Sankt Gallen
    "CH-SH",  # Schaffhausen
    "CH-SO",  # Solothurn
    "CH-SZ",  # Schwyz
    "CH-TG",  # Thurgau
    "CH-TI",  # Ticino
    "CH-UR",  # Uri
    "CH-VD",  # Vaud
    "CH-VS",  # Valais
    "CH-ZG",  # Zug
    "CH-ZH",  # Zürich
    # Republic of Côte d'Ivoire
    "CI-AB",  # Abidjan
    "CI-BS",  # Bas-Sassandra
    "CI-CM",  # Comoé
    "CI-DN",  # Denguélé
    "CI-GD",  # Gôh-Djiboua
    "CI-LC",  # Lacs
    "CI-LG",  # Lagunes
    "CI-MG",  # Montagnes
    "CI-SM",  # Sassandra-Marahoué
    "CI-SV",  # Savanes
    "CI-VB",  # Vallée du Bandama
    "CI-WR",  # Woroba
    "CI-YM",  # Yamoussoukro
    "CI-ZZ",  # Zanzan
    # Cook Islands
    # (no subdivisions)
    # Republic of Chile
    "CL-AI",  # Aisén del General Carlos Ibañez del Campo
    "CL-AN",  # Antofagasta
    "CL-AP",  # Arica y Parinacota
    "CL-AR",  # La Araucanía
    "CL-AT",  # Atacama
    "CL-BI",  # Biobío
    "CL-CO",  # Coquimbo
    "CL-LI",  # Libertador General Bernardo O'Higgins
    "CL-LL",  # Los Lagos
    "CL-LR",  # Los Ríos
    "CL-MA",  # Magallanes
    "CL-ML",  # Maule
    "CL-NB",  # Ñuble
    "CL-RM",  # Región Metropolitana de Santiago
    "CL-TA",  # Tarapacá
    "CL-VS",  # Valparaíso
    # Republic of Cameroon
    "CM-AD",  # Adamaoua
    "CM-CE",  # Centre
    "CM-EN",  # Far North
    "CM-ES",  # East
    "CM-LT",  # Littoral
    "CM-NO",  # North
    "CM-NW",  # North-West
    "CM-OU",  # West
    "CM-SU",  # South
    "CM-SW",  # South-West
    # People's Republic of China
    "CN-AH",  # Anhui Sheng
    "CN-BJ",  # Beijing Shi
    "CN-CQ",  # Chongqing Shi
    "CN-FJ",  # Fujian Sheng
    "CN-GD",  # Guangdong Sheng
    "CN-GS",  # Gansu Sheng
    "CN-GX",  # Guangxi Zhuangzu Zizhiqu
    "CN-GZ",  # Guizhou Sheng
    "CN-HA",  # Henan Sheng
    "CN-HB",  # Hubei Sheng
    "CN-HE",  # Hebei Sheng
    "CN-HI",  # Hainan Sheng
    "CN-HK",  # Hong Kong SAR
    "CN-HL",  # Heilongjiang Sheng
    "CN-HN",  # Hunan Sheng
    "CN-JL",  # Jilin Sheng
    "CN-JS",  # Jiangsu Sheng
    "CN-JX",  # Jiangxi Sheng
    "CN-LN",  # Liaoning Sheng
    "CN-MO",  # Macao SAR
    "CN-NM",  # Nei Mongol Zizhiqu
    "CN-NX",  # Ningxia Huizu Zizhiqu
    "CN-QH",  # Qinghai Sheng
    "CN-SC",  # Sichuan Sheng
    "CN-SD",  # Shandong Sheng
    "CN-SH",  # Shanghai Shi
    "CN-SN",  # Shaanxi Sheng
    "CN-SX",  # Shanxi Sheng
    "CN-TJ",  # Tianjin Shi
    "CN-TW",  # Taiwan Sheng
    "CN-XJ",  # Xinjiang Uygur Zizhiqu
    "CN-XZ",  # Xizang Zizhiqu
    "CN-YN",  # Yunnan Sheng
    "CN-ZJ",  # Zhejiang Sheng
    # Republic of Colombia
    "CO-AMA",  # Amazonas
    "CO-ANT",  # Antioquia
    "CO-ARA",  # Arauca
    "CO-ATL",  # Atlántico
    "CO-BOL",  # Bolívar
    "CO-BOY",  # Boyacá
    "CO-CAL",  # Caldas
    "CO-CAQ",  # Caquetá
    "CO-CAS",  # Casanare
    "CO-CAU",  # Cauca
    "CO-CES",  # Cesar
    "CO-CHO",  # Chocó
    "CO-COR",  # Córdoba
    "CO-CUN",  # Cundinamarca
    "CO-DC",  # Distrito Capital de Bogotá
    "CO-GUA",  # Guainía
    "CO-GUV",  # Guaviare
    "CO-HUI",  # Huila
    "CO-LAG",  # La Guajira
    "CO-MAG",  # Magdalena
    "CO-MET",  # Meta
    "CO-NAR",  # Nariño
    "CO-NSA",  # Norte de Santander
    "CO-PUT",  # Putumayo
    "CO-QUI",  # Quindío
    "CO-RIS",  # Risaralda
    "CO-SAN",  # Santander
    "CO-SAP",  # San Andrés, Providencia y Santa Catalina
    "CO-SUC",  # Sucre
    "CO-TOL",  # Tolima
    "CO-VAC",  # Valle del Cauca
    "CO-VAU",  # Vaupés
    "CO-VID",  # Vichada
    # Republic of Costa Rica
    "CR-A",  # Alajuela
    "CR-C",  # Cartago
    "CR-G",  # Guanacaste
    "CR-H",  # Heredia
    "CR-L",  # Limón
    "CR-P",  # Puntarenas
    "CR-SJ",  # San José
    # Republic of Cuba
    "CU-01",  # Pinar del Río
    "CU-03",  # La Habana
    "CU-04",  # Matanzas
    "CU-05",  # Villa Clara
    "CU-06",  # Cienfuegos
    "CU-07",  # Sancti Spíritus
    "CU-08",  # Ciego de Ávila
    "CU-09",  # Camagüey
    "CU-10",  # Las Tunas
    "CU-11",  # Holguín
    "CU-12",  # Granma
    "CU-13",  # Santiago de Cuba
    "CU-14",  # Guantánamo
    "CU-15",  # Artemisa
    "CU-16",  # Mayabeque
    "CU-99",  # Isla de la Juventud
    # Republic of Cabo Verde
    "CV-B",  # Ilhas de Barlavento
    "CV-BR",  # Brava
    "CV-BV",  # Boa Vista
    "CV-CA",  # Santa Catarina
    "CV-CF",  # Santa Catarina do Fogo
    "CV-CR",  # Santa Cruz
    "CV-MA",  # Maio
    "CV-MO",  # Mosteiros
    "CV-PA",  # Paul
    "CV-PN",  # Porto Novo
    "CV-PR",  # Praia
    "CV-RB",  # Ribeira Brava
    "CV-RG",  # Ribeira Grande
    "CV-RS",  # Ribeira Grande de Santiago
    "CV-S",  # Ilhas de Sotavento
    "CV-SD",  # São Domingos
    "CV-SF",  # São Filipe
    "CV-SL",  # Sal
    "CV-SM",  # São Miguel
    "CV-SO",  # São Lourenço dos Órgãos
    "CV-SS",  # São Salvador do Mundo
    "CV-SV",  # São Vicente
    "CV-TA",  # Tarrafal
    "CV-TS",  # Tarrafal de São Nicolau
    # Curaçao
    # (no subdivisions)
    # Christmas Island
    # (no subdivisions)
    # Republic of Cyprus
    "CY-01",  # Lefkosia
    "CY-02",  # Lemesos
    "CY-03",  # Larnaka
    "CY-04",  # Ammochostos
    "CY-05",  # Baf
    "CY-06",  # Girne
    # Czech Republic
    "CZ-10",  # Praha, Hlavní město
    "CZ-20",  # Středočeský kraj
    "CZ-201",  # Benešov
    "CZ-202",  # Beroun
    "CZ-203",  # Kladno
    "CZ-204",  # Kolín
    "CZ-205",  # Kutná Hora
    "CZ-206",  # Mělník
    "CZ-207",  # Mladá Boleslav
    "CZ-208",  # Nymburk
    "CZ-209",  # Praha-východ
    "CZ-20A",  # Praha-západ
    "CZ-20B",  # Příbram
    "CZ-20C",  # Rakovník
    "CZ-31",  # Jihočeský kraj
    "CZ-311",  # České Budějovice
    "CZ-312",  # Český Krumlov
    "CZ-313",  # Jindřichův Hradec
    "CZ-314",  # Písek
    "CZ-315",  # Prachatice
    "CZ-316",  # Strakonice
    "CZ-317",  # Tábor
    "CZ-32",  # Plzeňský kraj
    "CZ-321",  # Domažlice
    "CZ-322",  # Klatovy
    "CZ-323",  # Plzeň-město
    "CZ-324",  # Plzeň-jih
    "CZ-325",  # Plzeň-sever
    "CZ-326",  # Rokycany
    "CZ-327",  # Tachov
    "CZ-41",  # Karlovarský kraj
    "CZ-411",  # Cheb
    "CZ-412",  # Karlovy Vary
    "CZ-413",  # Sokolov
    "CZ-42",  # Ústecký kraj
    "CZ-421",  # Děčín
    "CZ-422",  # Chomutov
    "CZ-423",  # Litoměřice
    "CZ-424",  # Louny
    "CZ-425",  # Most
    "CZ-426",  # Teplice
    "CZ-427",  # Ústí nad Labem
    "CZ-51",  # Liberecký kraj
    "CZ-511",  # Česká Lípa
    "CZ-512",  # Jablonec nad Nisou
    "CZ-513",  # Liberec
    "CZ-514",  # Semily
    "CZ-52",  # Královéhradecký kraj
    "CZ-521",  # Hradec Králové
    "CZ-522",  # Jičín
    "CZ-523",  # Náchod
    "CZ-524",  # Rychnov nad Kněžnou
    "CZ-525",  # Trutnov
    "CZ-53",  # Pardubický kraj
    "CZ-531",  # Chrudim
    "CZ-532",  # Pardubice
    "CZ-533",  # Svitavy
    "CZ-534",  # Ústí nad Orlicí
    "CZ-63",  # Kraj Vysočina
    "CZ-631",  # Havlíčkův Brod
    "CZ-632",  # Jihlava
    "CZ-633",  # Pelhřimov
    "CZ-634",  # Třebíč
    "CZ-635",  # Žďár nad Sázavou
    "CZ-64",  # Jihomoravský kraj
    "CZ-641",  # Blansko
    "CZ-642",  # Brno-město
    "CZ-643",  # Brno-venkov
    "CZ-644",  # Břeclav
    "CZ-645",  # Hodonín
    "CZ-646",  # Vyškov
    "CZ-647",  # Znojmo
    "CZ-71",  # Olomoucký kraj
    "CZ-711",  # Jeseník
    "CZ-712",  # Olomouc
    "CZ-713",  # Prostějov
    "CZ-714",  # Přerov
    "CZ-715",  # Šumperk
    "CZ-72",  # Zlínský kraj
    "CZ-721",  # Kroměříž
    "CZ-722",  # Uherské Hradiště
    "CZ-723",  # Vsetín
    "CZ-724",  # Zlín
    "CZ-80",  # Moravskoslezský kraj
    "CZ-801",  # Bruntál
    "CZ-802",  # Frýdek-Místek
    "CZ-803",  # Karviná
    "CZ-804",  # Nový Jičín
    "CZ-805",  # Opava
    "CZ-806",  # Ostrava-město
    # Federal Republic of Germany
    "DE-BB",  # Brandenburg
    "DE-BE",  # Berlin
    "DE-BW",  # Baden-Württemberg
    "DE-BY",  # Bayern
    "DE-HB",  # Bremen
    "DE-HE",  # Hessen
    "DE-HH",  # Hamburg
    "DE-MV",  # Mecklenburg-Vorpommern
    "DE-NI",  # Niedersachsen
    "DE-NW",  # Nordrhein-Westfalen
    "DE-RP",  # Rheinland-Pfalz
    "DE-SH",  # Schleswig-Holstein
    "DE-SL",  # Saarland
    "DE-SN",  # Sachsen
    "DE-ST",  # Sachsen-Anhalt
    "DE-TH",  # Thüringen
    # Republic of Djibouti
    "DJ-AR",  # Arta
    "DJ-AS",  # Ali Sabieh
    "DJ-DI",  # Dikhil
    "DJ-DJ",  # Djibouti
    "DJ-OB",  # Obock
    "DJ-TA",  # Tadjourah
    # Kingdom of Denmark
    "DK-81",  # Nordjylland
    "DK-82",  # Midtjylland
    "DK-83",  # Syddanmark
    "DK-84",  # Hovedstaden
    "DK-85",  # Sjælland
    # Commonwealth of Dominica
    "DM-02",  # Saint Andrew
    "DM-03",  # Saint David
    "DM-04",  # Saint George
    "DM-05",  # Saint John
    "DM-06",  # Saint Joseph
    "DM-07",  # Saint Luke
    "DM-08",  # Saint Mark
    "DM-09",  # Saint Patrick
    "DM-10",  # Saint Paul
    "DM-11",  # Saint Peter
    # Dominican Republic
    "DO-01",  # Distrito Nacional (Santo Domingo)
    "DO-02",  # Azua
    "DO-03",  # Baoruco
    "DO-04",  # Barahona
    "DO-05",  # Dajabón
    "DO-06",  # Duarte
    "DO-07",  # Elías Piña
    "DO-08",  # El Seibo
    "DO-09",  # Espaillat
    "DO-10",  # Independencia
    "DO-11",  # La Altagracia
    "DO-12",  # La Romana
    "DO-13",  # La Vega
    "DO-14",  # María Trinidad Sánchez
    "DO-15",  # Monte Cristi
    "DO-16",  # Pedernales
    "DO-17",  # Peravia
    "DO-18",  # Puerto Plata
    "DO-19",  # Hermanas Mirabal
    "DO-20",  # Samaná
    "DO-21",  # San Cristóbal
    "DO-22",  # San Juan
    "DO-23",  # San Pedro de Macorís
    "DO-24",  # Sánchez Ramírez
    "DO-25",  # Santiago
    "DO-26",  # Santiago Rodríguez
    "DO-27",  # Valverde
    "DO-28",  # Monseñor Nouel
    "DO-29",  # Monte Plata
    "DO-30",  # Hato Mayor
    "DO-31",  # San José de Ocoa
    "DO-32",  # Santo Domingo
    "DO-33",  # Cibao Nordeste
    "DO-34",  # Cibao Noroeste
    "DO-35",  # Cibao Norte
    "DO-36",  # Cibao Sur
    "DO-37",  # El Valle
    "DO-38",  # Enriquillo
    "DO-39",  # Higuamo
    "DO-40",  # Ozama
    "DO-41",  # Valdesia
    "DO-42",  # Yuma
    # People's Democratic Republic of Algeria
    "DZ-01",  # Adrar
    "DZ-02",  # Chlef
    "DZ-03",  # Laghouat
    "DZ-04",  # Oum el Bouaghi
    "DZ-05",  # Batna
    "DZ-06",  # Béjaïa
    "DZ-07",  # Biskra
    "DZ-08",  # Béchar
    "DZ-09",  # Blida
    "DZ-10",  # Bouira
    "DZ-11",  # Tamanrasset
    "DZ-12",  # Tébessa
    "DZ-13",  # Tlemcen
    "DZ-14",  # Tiaret
    "DZ-15",  # Tizi Ouzou
    "DZ-16",  # Alger
    "DZ-17",  # Djelfa
    "DZ-18",  # Jijel
    "DZ-19",  # Sétif
    "DZ-20",  # Saïda
    "DZ-21",  # Skikda
    "DZ-22",  # Sidi Bel Abbès
    "DZ-23",  # Annaba
    "DZ-24",  # Guelma
    "DZ-25",  # Constantine
    "DZ-26",  # Médéa
    "DZ-27",  # Mostaganem
    "DZ-28",  # M'sila
    "DZ-29",  # Mascara
    "DZ-30",  # Ouargla
    "DZ-31",  # Oran
    "DZ-32",  # El Bayadh
    "DZ-33",  # Illizi
    "DZ-34",  # Bordj Bou Arréridj
    "DZ-35",  # Boumerdès
    "DZ-36",  # El Tarf
    "DZ-37",  # Tindouf
    "DZ-38",  # Tissemsilt
    "DZ-39",  # El Oued
    "DZ-40",  # Khenchela
    "DZ-41",  # Souk Ahras
    "DZ-42",  # Tipaza
    "DZ-43",  # Mila
    "DZ-44",  # Aïn Defla
    "DZ-45",  # Naama
    "DZ-46",  # Aïn Témouchent
    "DZ-47",  # Ghardaïa
    "DZ-48",  # Relizane
    "DZ-49",  # Timimoun
    "DZ-50",  # Bordj Badji Mokhtar
    "DZ-51",  # Ouled Djellal
    "DZ-52",  # Béni Abbès
    "DZ-53",  # In Salah
    "DZ-54",  # In Guezzam
    "DZ-55",  # Touggourt
    "DZ-56",  # Djanet
    "DZ-57",  # El Meghaier
    "DZ-58",  # El Meniaa
    # Republic of Ecuador
    "EC-A",  # Azuay
    "EC-B",  # Bolívar
    "EC-C",  # Carchi
    "EC-D",  # Orellana
    "EC-E",  # Esmeraldas
    "EC-F",  # Cañar
    "EC-G",  # Guayas
    "EC-H",  # Chimborazo
    "EC-I",  # Imbabura
    "EC-L",  # Loja
    "EC-M",  # Manabí
    "EC-N",  # Napo
    "EC-O",  # El Oro
    "EC-P",  # Pichincha
    "EC-R",  # Los Ríos
    "EC-S",  # Morona Santiago
    "EC-SD",  # Santo Domingo de los Tsáchilas
    "EC-SE",  # Santa Elena
    "EC-T",  # Tungurahua
    "EC-U",  # Sucumbíos
    "EC-W",  # Galápagos
    "EC-X",  # Cotopaxi
    "EC-Y",  # Pastaza
    "EC-Z",  # Zamora Chinchipe
    # Republic of Estonia
    "EE-130",  # Alutaguse
    "EE-141",  # Anija
    "EE-142",  # Antsla
    "EE-171",  # Elva
    "EE-184",  # Haapsalu
    "EE-191",  # Haljala
    "EE-198",  # Harku
    "EE-205",  # Hiiumaa
    "EE-214",  # Häädemeeste
    "EE-245",  # Jõelähtme
    "EE-247",  # Jõgeva
    "EE-251",  # Jõhvi
    "EE-255",  # Järva
    "EE-272",  # Kadrina
    "EE-283",  # Kambja
    "EE-284",  # Kanepi
    "EE-291",  # Kastre
    "EE-293",  # Kehtna
    "EE-296",  # Keila
    "EE-303",  # Kihnu
    "EE-305",  # Kiili
    "EE-317",  # Kohila
    "EE-321",  # Kohtla-Järve
    "EE-338",  # Kose
    "EE-353",  # Kuusalu
    "EE-37",  # Harjumaa
    "EE-39",  # Hiiumaa
    "EE-424",  # Loksa
    "EE-430",  # Lääneranna
    "EE-431",  # Lääne-Harju
    "EE-432",  # Luunja
    "EE-441",  # Lääne-Nigula
    "EE-442",  # Lüganuse
    "EE-446",  # Maardu
    "EE-45",  # Ida-Virumaa
    "EE-478",  # Muhu
    "EE-480",  # Mulgi
    "EE-486",  # Mustvee
    "EE-50",  # Jõgevamaa
    "EE-503",  # Märjamaa
    "EE-511",  # Narva
    "EE-514",  # Narva-Jõesuu
    "EE-52",  # Järvamaa
    "EE-528",  # Nõo
    "EE-557",  # Otepää
    "EE-56",  # Läänemaa
    "EE-567",  # Paide
    "EE-586",  # Peipsiääre
    "EE-60",  # Lääne-Virumaa
    "EE-615",  # Põhja-Sakala
    "EE-618",  # Põltsamaa
    "EE-622",  # Põlva
    "EE-624",  # Pärnu
    "EE-638",  # Põhja-Pärnumaa
    "EE-64",  # Põlvamaa
    "EE-651",  # Raasiku
    "EE-653",  # Rae
    "EE-661",  # Rakvere
    "EE-663",  # Rakvere
    "EE-668",  # Rapla
    "EE-68",  # Pärnumaa
    "EE-689",  # Ruhnu
    "EE-698",  # Rõuge
    "EE-708",  # Räpina
    "EE-71",  # Raplamaa
    "EE-712",  # Saarde
    "EE-714",  # Saaremaa
    "EE-719",  # Saku
    "EE-726",  # Saue
    "EE-732",  # Setomaa
    "EE-735",  # Sillamäe
    "EE-74",  # Saaremaa
    "EE-784",  # Tallinn
    "EE-79",  # Tartumaa
    "EE-792",  # Tapa
    "EE-793",  # Tartu
    "EE-796",  # Tartu
    "EE-803",  # Toila
    "EE-809",  # Tori
    "EE-81",  # Valgamaa
    "EE-824",  # Tõrva
    "EE-834",  # Türi
    "EE-84",  # Viljandimaa
    "EE-855",  # Valga
    "EE-87",  # Võrumaa
    "EE-890",  # Viimsi
    "EE-897",  # Viljandi
    "EE-899",  # Viljandi
    "EE-901",  # Vinni
    "EE-903",  # Viru-Nigula
    "EE-907",  # Vormsi
    "EE-917",  # Võru
    "EE-919",  # Võru
    "EE-928",  # Väike-Maarja
    # Arab Republic of Egypt
    "EG-ALX",  # Al Iskandarīyah
    "EG-ASN",  # Aswān
    "EG-AST",  # Asyūţ
    "EG-BA",  # Al Baḩr al Aḩmar
    "EG-BH",  # Al Buḩayrah
    "EG-BNS",  # Banī Suwayf
    "EG-C",  # Al Qāhirah
    "EG-DK",  # Ad Daqahlīyah
    "EG-DT",  # Dumyāţ
    "EG-FYM",  # Al Fayyūm
    "EG-GH",  # Al Gharbīyah
    "EG-GZ",  # Al Jīzah
    "EG-IS",  # Al Ismā'īlīyah
    "EG-JS",  # Janūb Sīnā'
    "EG-KB",  # Al Qalyūbīyah
    "EG-KFS",  # Kafr ash Shaykh
    "EG-KN",  # Qinā
    "EG-LX",  # Al Uqşur
    "EG-MN",  # Al Minyā
    "EG-MNF",  # Al Minūfīyah
    "EG-MT",  # Maţrūḩ
    "EG-PTS",  # Būr Sa‘īd
    "EG-SHG",  # Sūhāj
    "EG-SHR",  # Ash Sharqīyah
    "EG-SIN",  # Shamāl Sīnā'
    "EG-SUZ",  # As Suways
    "EG-WAD",  # Al Wādī al Jadīd
    # Western Sahara
    # (no subdivisions)
    # the State of Eritrea
    "ER-AN",  # Ansabā
    "ER-DK",  # Debubawi K’eyyĭḥ Baḥri
    "ER-DU",  # Al Janūbī
    "ER-GB",  # Gash-Barka
    "ER-MA",  # Al Awsaţ
    "ER-SK",  # Semienawi K’eyyĭḥ Baḥri
    # Kingdom of Spain
    "ES-A",  # Alacant*
    "ES-AB",  # Albacete
    "ES-AL",  # Almería
    "ES-AN",  # Andalucía
    "ES-AR",  # Aragón
    "ES-AS",  # Asturias, Principado de
    "ES-AV",  # Ávila
    "ES-B",  # Barcelona [Barcelona]
    "ES-BA",  # Badajoz
    "ES-BI",  # Bizkaia
    "ES-BU",  # Burgos
    "ES-C",  # A Coruña [La Coruña]
    "ES-CA",  # Cádiz
    "ES-CB",  # Cantabria
    "ES-CC",  # Cáceres
    "ES-CE",  # Ceuta
    "ES-CL",  # Castilla y León
    "ES-CM",  # Castilla-La Mancha
    "ES-CN",  # Canarias
    "ES-CO",  # Córdoba
    "ES-CR",  # Ciudad Real
    "ES-CS",  # Castelló*
    "ES-CT",  # Catalunya [Cataluña]
    "ES-CU",  # Cuenca
    "ES-EX",  # Extremadura
    "ES-GA",  # Galicia [Galicia]
    "ES-GC",  # Las Palmas
    "ES-GI",  # Girona [Gerona]
    "ES-GR",  # Granada
    "ES-GU",  # Guadalajara
    "ES-H",  # Huelva
    "ES-HU",  # Huesca
    "ES-IB",  # Illes Balears [Islas Baleares]
    "ES-J",  # Jaén
    "ES-L",  # Lleida [Lérida]
    "ES-LE",  # León
    "ES-LO",  # La Rioja
    "ES-LU",  # Lugo [Lugo]
    "ES-M",  # Madrid
    "ES-MA",  # Málaga
    "ES-MC",  # Murcia, Región de
    "ES-MD",  # Madrid, Comunidad de
    "ES-ML",  # Melilla
    "ES-MU",  # Murcia
    "ES-NA",  # Nafarroa*
    "ES-NC",  # Nafarroako Foru Komunitatea*
    "ES-O",  # Asturias
    "ES-OR",  # Ourense [Orense]
    "ES-P",  # Palencia
    "ES-PM",  # Illes Balears [Islas Baleares]
    "ES-PO",  # Pontevedra [Pontevedra]
    "ES-PV",  # Euskal Herria
    "ES-RI",  # La Rioja
    "ES-S",  # Cantabria
    "ES-SA",  # Salamanca
    "ES-SE",  # Sevilla
    "ES-SG",  # Segovia
    "ES-SO",  # Soria
    "ES-SS",  # Gipuzkoa
    "ES-T",  # Tarragona [Tarragona]
    "ES-TE",  # Teruel
    "ES-TF",  # Santa Cruz de Tenerife
    "ES-TO",  # Toledo
    "ES-V",  # Valencia
    "ES-VA",  # Valladolid
    "ES-VC",  # Valenciana, Comunidad
    "ES-VI",  # Araba*
    "ES-Z",  # Zaragoza
    "ES-ZA",  # Zamora
    # Federal Democratic Republic of Ethiopia
    "ET-AA",  # Addis Ababa
    "ET-AF",  # Afar
    "ET-AM",  # Amara
    "ET-BE",  # Benshangul-Gumaz
    "ET-DD",  # Dire Dawa
    "ET-GA",  # Gambela Peoples
    "ET-HA",  # Harari People
    "ET-OR",  # Oromia
    "ET-SI",  # Sidama
    "ET-SN",  # Southern Nations, Nationalities and Peoples
    "ET-SO",  # Somali
    "ET-SW",  # Southwest Ethiopia Peoples
    "ET-TI",  # Tigrai
    # Republic of Finland
    "FI-01",  # Landskapet Åland
    "FI-02",  # Etelä-Karjala
    "FI-03",  # Etelä-Pohjanmaa
    "FI-04",  # Etelä-Savo
    "FI-05",  # Kainuu
    "FI-06",  # Kanta-Häme
    "FI-07",  # Keski-Pohjanmaa
    "FI-08",  # Keski-Suomi
    "FI-09",  # Kymenlaakso
    "FI-10",  # Lappi
    "FI-11",  # Pirkanmaa
    "FI-12",  # Pohjanmaa
    "FI-13",  # Pohjois-Karjala
    "FI-14",  # Pohjois-Pohjanmaa
    "FI-15",  # Pohjois-Savo
    "FI-16",  # Päijät-Häme
    "FI-17",  # Satakunta
    "FI-18",  # Uusimaa
    "FI-19",  # Varsinais-Suomi
    # Republic of Fiji
    "FJ-01",  # Ba
    "FJ-02",  # Bua
    "FJ-03",  # Cakaudrove
    "FJ-04",  # Kadavu
    "FJ-05",  # Lau
    "FJ-06",  # Lomaiviti
    "FJ-07",  # Macuata
    "FJ-08",  # Nadroga and Navosa
    "FJ-09",  # Naitasiri
    "FJ-10",  # Namosi
    "FJ-11",  # Ra
    "FJ-12",  # Rewa
    "FJ-13",  # Serua
    "FJ-14",  # Tailevu
    "FJ-C",  # Central
    "FJ-E",  # Eastern
    "FJ-N",  # Northern
    "FJ-R",  # Rotuma
    "FJ-W",  # Western
    # Falkland Islands (Malvinas)
    # (no subdivisions)
    # Federated States of Micronesia
    "FM-KSA",  # Kosrae
    "FM-PNI",  # Pohnpei
    "FM-TRK",  # Chuuk
    "FM-YAP",  # Yap
    # Faroe Islands
    # (no subdivisions)
    # French Republic
    "FR-01",  # Ain
    "FR-02",  # Aisne
    "FR-03",  # Allier
    "FR-04",  # Alpes-de-Haute-Provence
    "FR-05",  # Hautes-Alpes
    "FR-06",  # Alpes-Maritimes
    "FR-07",  # Ardèche
    "FR-08",  # Ardennes
    "FR-09",  # Ariège
    "FR-10",  # Aube
    "FR-11",  # Aude
    "FR-12",  # Aveyron
    "FR-13",  # Bouches-du-Rhône
    "FR-14",  # Calvados
    "FR-15",  # Cantal
    "FR-16",  # Charente
    "FR-17",  # Charente-Maritime
    "FR-18",  # Cher
    "FR-19",  # Corrèze
    "FR-20R",  # Corse
    "FR-21",  # Côte-d'Or
    "FR-22",  # Côtes-d'Armor
    "FR-23",  # Creuse
    "FR-24",  # Dordogne
    "FR-25",  # Doubs
    "FR-26",  # Drôme
    "FR-27",  # Eure
    "FR-28",  # Eure-et-Loir
    "FR-29",  # Finistère
    "FR-2A",  # Corse-du-Sud
    "FR-2B",  # Haute-Corse
    "FR-30",  # Gard
    "FR-31",  # Haute-Garonne
    "FR-32",  # Gers
    "FR-33",  # Gironde
    "FR-34",  # Hérault
    "FR-35",  # Ille-et-Vilaine
    "FR-36",  # Indre
    "FR-37",  # Indre-et-Loire
    "FR-38",  # Isère
    "FR-39",  # Jura
    "FR-40",  # Landes
    "FR-41",  # Loir-et-Cher
    "FR-42",  # Loire
    "FR-43",  # Haute-Loire
    "FR-44",  # Loire-Atlantique
    "FR-45",  # Loiret
    "FR-46",  # Lot
    "FR-47",  # Lot-et-Garonne
    "FR-48",  # Lozère
    "FR-49",  # Maine-et-Loire
    "FR-50",  # Manche
    "FR-51",  # Marne
    "FR-52",  # Haute-Marne
    "FR-53",  # Mayenne
    "FR-54",  # Meurthe-et-Moselle
    "FR-55",  # Meuse
    "FR-56",  # Morbihan
    "FR-57",  # Moselle
    "FR-58",  # Nièvre
    "FR-59",  # Nord
    "FR-60",  # Oise
    "FR-61",  # Orne
    "FR-62",  # Pas-de-Calais
    "FR-63",  # Puy-de-Dôme
    "FR-64",  # Pyrénées-Atlantiques
    "FR-65",  # Hautes-Pyrénées
    "FR-66",  # Pyrénées-Orientales
    "FR-67",  # Bas-Rhin
    "FR-68",  # Haut-Rhin
    "FR-69",  # Rhône
    "FR-69M",  # Métropole de Lyon
    "FR-6AE",  # Alsace
    "FR-70",  # Haute-Saône
    "FR-71",  # Saône-et-Loire
    "FR-72",  # Sarthe
    "FR-73",  # Savoie
    "FR-74",  # Haute-Savoie
    "FR-75C",  # Paris
    "FR-76",  # Seine-Maritime
    "FR-77",  # Seine-et-Marne
    "FR-78",  # Yvelines
    "FR-79",  # Deux-Sèvres
    "FR-80",  # Somme
    "FR-81",  # Tarn
    "FR-82",  # Tarn-et-Garonne
    "FR-83",  # Var
    "FR-84",  # Vaucluse
    "FR-85",  # Vendée
    "FR-86",  # Vienne
    "FR-87",  # Haute-Vienne
    "FR-88",  # Vosges
    "FR-89",  # Yonne
    "FR-90",  # Territoire de Belfort
    "FR-91",  # Essonne
    "FR-92",  # Hauts-de-Seine
    "FR-93",  # Seine-Saint-Denis
    "FR-94",  # Val-de-Marne
    "FR-95",  # Val-d'Oise
    "FR-971",  # Guadeloupe
    "FR-972",  # Martinique
    "FR-973",  # Guyane (française)
    "FR-974",  # La Réunion
    "FR-976",  # Mayotte
    "FR-ARA",  # Auvergne-Rhône-Alpes
    "FR-BFC",  # Bourgogne-Franche-Comté
    "FR-BL",  # Saint-Barthélemy
    "FR-BRE",  # Bretagne
    "FR-CP",  # Clipperton
    "FR-CVL",  # Centre-Val de Loire
    "FR-GES",  # Grand-Est
    "FR-HDF",  # Hauts-de-France
    "FR-IDF",  # Île-de-France
    "FR-MF",  # Saint-Martin
    "FR-NAQ",  # Nouvelle-Aquitaine
    "FR-NC",  # Nouvelle-Calédonie
    "FR-NOR",  # Normandie
    "FR-OCC",  # Occitanie
    "FR-PAC",  # Provence-Alpes-Côte-d’Azur
    "FR-PDL",  # Pays-de-la-Loire
    "FR-PF",  # Polynésie française
    "FR-PM",  # Saint-Pierre-et-Miquelon
    "FR-TF",  # Terres australes françaises
    "FR-WF",  # Wallis-et-Futuna
    # Gabonese Republic
    "GA-1",  # Estuaire
    "GA-2",  # Haut-Ogooué
    "GA-3",  # Moyen-Ogooué
    "GA-4",  # Ngounié
    "GA-5",  # Nyanga
    "GA-6",  # Ogooué-Ivindo
    "GA-7",  # Ogooué-Lolo
    "GA-8",  # Ogooué-Maritime
    "GA-9",  # Woleu-Ntem
    # United Kingdom of Great Britain and Northern Ireland
    "GB-ABC",  # Armagh City, Banbridge and Craigavon
    "GB-ABD",  # Aberdeenshire
    "GB-ABE",  # Aberdeen City
    "GB-AGB",  # Argyll and Bute
    "GB-AGY",  # Isle of Anglesey [Sir Ynys Môn GB-YNM]
    "GB-AND",  # Ards and North Down
    "GB-ANN",  # Antrim and Newtownabbey
    "GB-ANS",  # Angus
    "GB-BAS",  # Bath and North East Somerset
    "GB-BBD",  # Blackburn with Darwen
    "GB-BCP",  # Bournemouth, Christchurch and Poole
    "GB-BDF",  # Bedford
    "GB-BDG",  # Barking and Dagenham
    "GB-BEN",  # Brent
    "GB-BEX",  # Bexley
    "GB-BFS",  # Belfast City
    "GB-BGE",  # Bridgend [Pen-y-bont ar Ogwr GB-POG]
    "GB-BGW",  # Blaenau Gwent
    "GB-BIR",  # Birmingham
    "GB-BKM",  # Buckinghamshire
    "GB-BNE",  # Barnet
    "GB-BNH",  # Brighton and Hove
    "GB-BNS",  # Barnsley
    "GB-BOL",  # Bolton
    "GB-BPL",  # Blackpool
    "GB-BRC",  # Bracknell Forest
    "GB-BRD",  # Bradford
    "GB-BRY",  # Bromley
    "GB-BST",  # Bristol, City of
    "GB-BUR",  # Bury
    "GB-CAM",  # Cambridgeshire
    "GB-CAY",  # Caerphilly [Caerffili GB-CAF]
    "GB-CBF",  # Central Bedfordshire
    "GB-CCG",  # Causeway Coast and Glens
    "GB-CGN",  # Ceredigion [Sir Ceredigion]
    "GB-CHE",  # Cheshire East
    "GB-CHW",  # Cheshire West and Chester
    "GB-CLD",  # Calderdale
    "GB-CLK",  # Clackmannanshire
    "GB-CMA",  # Cumbria
    "GB-CMD",  # Camden
    "GB-CMN",  # Carmarthenshire [Sir Gaerfyrddin GB-GFY]
    "GB-CON",  # Cornwall
    "GB-COV",  # Coventry
    "GB-CRF",  # Cardiff [Caerdydd GB-CRD]
    "GB-CRY",  # Croydon
    "GB-CWY",  # Conwy
    "GB-DAL",  # Darlington
    "GB-DBY",  # Derbyshire
    "GB-DEN",  # Denbighshire [Sir Ddinbych GB-DDB]
    "GB-DER",  # Derby
    "GB-DEV",  # Devon
    "GB-DGY",  # Dumfries and Galloway
    "GB-DNC",  # Doncaster
    "GB-DND",  # Dundee City
    "GB-DOR",  # Dorset
    "GB-DRS",  # Derry and Strabane
    "GB-DUD",  # Dudley
    "GB-DUR",  # Durham, County
    "GB-EAL",  # Ealing
    "GB-EAY",  # East Ayrshire
    "GB-EDH",  # Edinburgh, City of
    "GB-EDU",  # East Dunbartonshire
    "GB-ELN",  # East Lothian
    "GB-ELS",  # Eilean Siar
    "GB-ENF",  # Enfield
    "GB-ENG",  # England
    "GB-ERW",  # East Renfrewshire
    "GB-ERY",  # East Riding of Yorkshire
    "GB-ESS",  # Essex
    "GB-ESX",  # East Sussex
    "GB-FAL",  # Falkirk
    "GB-FIF",  # Fife
    "GB-FLN",  # Flintshire [Sir y Fflint GB-FFL]
    "GB-FMO",  # Fermanagh and Omagh
    "GB-GAT",  # Gateshead
    "GB-GLG",  # Glasgow City
    "GB-GLS",  # Gloucestershire
    "GB-GRE",  # Greenwich
    "GB-GWN",  # Gwynedd
    "GB-HAL",  # Halton
    "GB-HAM",  # Hampshire
    "GB-HAV",  # Havering
    "GB-HCK",  # Hackney
    "GB-HEF",  # Herefordshire
    "GB-HIL",  # Hillingdon
    "GB-HLD",  # Highland
    "GB-HMF",  # Hammersmith and Fulham
    "GB-HNS",  # Hounslow
    "GB-HPL",  # Hartlepool
    "GB-HRT",  # Hertfordshire
    "GB-HRW",  # Harrow
    "GB-HRY",  # Haringey
    "GB-IOS",  # Isles of Scilly
    "GB-IOW",  # Isle of Wight
    "GB-ISL",  # Islington
    "GB-IVC",  # Inverclyde
    "GB-KEC",  # Kensington and Chelsea
    "GB-KEN",  # Kent
    "GB-KHL",  # Kingston upon Hull
    "GB-KIR",  # Kirklees
    "GB-KTT",  # Kingston upon Thames
    "GB-KWL",  # Knowsley
    "GB-LAN",  # Lancashire
    "GB-LBC",  # Lisburn and Castlereagh
    "GB-LBH",  # Lambeth
    "GB-LCE",  # Leicester
    "GB-LDS",  # Leeds
    "GB-LEC",  # Leicestershire
    "GB-LEW",  # Lewisham
    "GB-LIN",  # Lincolnshire
    "GB-LIV",  # Liverpool
    "GB-LND",  # London, City of
    "GB-LUT",  # Luton
    "GB-MAN",  # Manchester
    "GB-MDB",  # Middlesbrough
    "GB-MDW",  # Medway
    "GB-MEA",  # Mid and East Antrim
    "GB-MIK",  # Milton Keynes
    "GB-MLN",  # Midlothian
    "GB-MON",  # Monmouthshire [Sir Fynwy GB-FYN]
    "GB-MRT",  # Merton
    "GB-MRY",  # Moray
    "GB-MTY",  # Merthyr Tydfil [Merthyr Tudful GB-MTU]
    "GB-MUL",  # Mid-Ulster
    "GB-NAY",  # North Ayrshire
    "GB-NBL",  # Northumberland
    "GB-NEL",  # North East Lincolnshire
    "GB-NET",  # Newcastle upon Tyne
    "GB-NFK",  # Norfolk
    "GB-NGM",  # Nottingham
    "GB-NIR",  # Northern Ireland
    "GB-NLK",  # North Lanarkshire
    "GB-NLN",  # North Lincolnshire
    "GB-NMD",  # Newry, Mourne and Down
    "GB-NNH",  # North Northamptonshire
    "GB-NSM",  # North Somerset
    "GB-NTL",  # Neath Port Talbot [Castell-nedd Port Talbot GB-CTL]
    "GB-NTT",  # Nottinghamshire
    "GB-NTY",  # North Tyneside
    "GB-NWM",  # Newham
    "GB-NWP",  # Newport [Casnewydd GB-CNW]
    "GB-NYK",  # North Yorkshire
    "GB-OLD",  # Oldham
    "GB-ORK",  # Orkney Islands
    "GB-OXF",  # Oxfordshire
    "GB-PEM",  # Pembrokeshire [Sir Benfro GB-BNF]
    "GB-PKN",  # Perth and Kinross
    "GB-PLY",  # Plymouth
    "GB-POR",  # Portsmouth
    "GB-POW",  # Powys
    "GB-PTE",  # Peterborough
    "GB-RCC",  # Redcar and Cleveland
    "GB-RCH",  # Rochdale
    "GB-RCT",  # Rhondda Cynon Taff [Rhondda CynonTaf]
    "GB-RDB",  # Redbridge
    "GB-RDG",  # Reading
    "GB-RFW",  # Renfrewshire
    "GB-RIC",  # Richmond upon Thames
    "GB-ROT",  # Rotherham
    "GB-RUT",  # Rutland
    "GB-SAW",  # Sandwell
    "GB-SAY",  # South Ayrshire
    "GB-SCB",  # Scottish Borders
    "GB-SCT",  # Scotland
    "GB-SFK",  # Suffolk
    "GB-SFT",  # Sefton
    "GB-SGC",  # South Gloucestershire
    "GB-SHF",  # Sheffield
    "GB-SHN",  # St. Helens
    "GB-SHR",  # Shropshire
    "GB-SKP",  # Stockport
    "GB-SLF",  # Salford
    "GB-SLG",  # Slough
    "GB-SLK",  # South Lanarkshire
    "GB-SND",  # Sunderland
    "GB-SOL",  # Solihull
    "GB-SOM",  # Somerset
    "GB-SOS",  # Southend-on-Sea
    "GB-SRY",  # Surrey
    "GB-STE",  # Stoke-on-Trent
    "GB-STG",  # Stirling
    "GB-STH",  # Southampton
    "GB-STN",  # Sutton
    "GB-STS",  # Staffordshire
    "GB-STT",  # Stockton-on-Tees
    "GB-STY",  # South Tyneside
    "GB-SWA",  # Swansea [Abertawe GB-ATA]
    "GB-SWD",  # Swindon
    "GB-SWK",  # Southwark
    "GB-TAM",  # Tameside
    "GB-TFW",  # Telford and Wrekin
    "GB-THR",  # Thurrock
    "GB-TOB",  # Torbay
    "GB-TOF",  # Torfaen [Tor-faen]
    "GB-TRF",  # Trafford
    "GB-TWH",  # Tower Hamlets
    "GB-VGL",  # Vale of Glamorgan, The [Bro Morgannwg GB-BMG]
    "GB-WAR",  # Warwickshire
    "GB-WBK",  # West Berkshire
    "GB-WDU",  # West Dunbartonshire
    "GB-WFT",  # Waltham Forest
    "GB-WGN",  # Wigan
    "GB-WIL",  # Wiltshire
    "GB-WKF",  # Wakefield
    "GB-WLL",  # Walsall
    "GB-WLN",  # West Lothian
    "GB-WLS",  # Wales [Cymru GB-CYM]
    "GB-WLV",  # Wolverhampton
    "GB-WND",  # Wandsworth
    "GB-WNH",  # West Northamptonshire
    "GB-WNM",  # Windsor and Maidenhead
    "GB-WOK",  # Wokingham
    "GB-WOR",  # Worcestershire
    "GB-WRL",  # Wirral
    "GB-WRT",  # Warrington
    "GB-WRX",  # Wrexham [Wrecsam GB-WRC]
    "GB-WSM",  # Westminster
    "GB-WSX",  # West Sussex
    "GB-YOR",  # York
    "GB-ZET",  # Shetland Islands
    # Grenada
    "GD-01",  # Saint Andrew
    "GD-02",  # Saint David
    "GD-03",  # Saint George
    "GD-04",  # Saint John
    "GD-05",  # Saint Mark
    "GD-06",  # Saint Patrick
    "GD-10",  # Southern Grenadine Islands
    # Georgia
    "GE-AB",  # Abkhazia
    "GE-AJ",  # Ajaria
    "GE-GU",  # Guria
    "GE-IM",  # Imereti
    "GE-KA",  # K'akheti
    "GE-KK",  # Kvemo Kartli
    "GE-MM",  # Mtskheta-Mtianeti
    "GE-RL",  # Rach'a-Lechkhumi-Kvemo Svaneti
    "GE-SJ",  # Samtskhe-Javakheti
    "GE-SK",  # Shida Kartli
    "GE-SZ",  # Samegrelo-Zemo Svaneti
    "GE-TB",  # Tbilisi
    # French Guiana
    # (no subdivisions)
    # Guernsey
    # (no subdivisions)
    # Republic of Ghana
    "GH-AA",  # Greater Accra
    "GH-AF",  # Ahafo
    "GH-AH",  # Ashanti
    "GH-BE",  # Bono East
    "GH-BO",  # Bono
    "GH-CP",  # Central
    "GH-EP",  # Eastern
    "GH-NE",  # North East
    "GH-NP",  # Northern
    "GH-OT",  # Oti
    "GH-SV",  # Savannah
    "GH-TV",  # Volta
    "GH-UE",  # Upper East
    "GH-UW",  # Upper West
    "GH-WN",  # Western North
    "GH-WP",  # Western
    # Gibraltar
    # (no subdivisions)
    # Greenland
    "GL-AV",  # Avannaata Kommunia
    "GL-KU",  # Kommune Kujalleq
    "GL-QE",  # Qeqqata Kommunia
    "GL-QT",  # Kommune Qeqertalik
    "GL-SM",  # Kommuneqarfik Sermersooq
    # Republic of the Gambia
    "GM-B",  # Banjul
    "GM-L",  # Lower River
    "GM-M",  # Central River
    "GM-N",  # North Bank
    "GM-U",  # Upper River
    "GM-W",  # Western
    # Republic of Guinea
    "GN-B",  # Boké
    "GN-BE",  # Beyla
    "GN-BF",  # Boffa
    "GN-BK",  # Boké
    "GN-C",  # Conakry
    "GN-CO",  # Coyah
    "GN-D",  # Kindia
    "GN-DB",  # Dabola
    "GN-DI",  # Dinguiraye
    "GN-DL",  # Dalaba
    "GN-DU",  # Dubréka
    "GN-F",  # Faranah
    "GN-FA",  # Faranah
    "GN-FO",  # Forécariah
    "GN-FR",  # Fria
    "GN-GA",  # Gaoual
    "GN-GU",  # Guékédou
    "GN-K",  # Kankan
    "GN-KA",  # Kankan
    "GN-KB",  # Koubia
    "GN-KD",  # Kindia
    "GN-KE",  # Kérouané
    "GN-KN",  # Koundara
    "GN-KO",  # Kouroussa
    "GN-KS",  # Kissidougou
    "GN-L",  # Labé
    "GN-LA",  # Labé
    "GN-LE",  # Lélouma
    "GN-LO",  # Lola
    "GN-M",  # Mamou
    "GN-MC",  # Macenta
    "GN-MD",  # Mandiana
    "GN-ML",  # Mali
    "GN-MM",  # Mamou
    "GN-N",  # Nzérékoré
    "GN-NZ",  # Nzérékoré
    "GN-PI",  # Pita
    "GN-SI",  # Siguiri
    "GN-TE",  # Télimélé
    "GN-TO",  # Tougué
    "GN-YO",  # Yomou
    # Guadeloupe
    # (no subdivisions)
    # Republic of Equatorial Guinea
    "GQ-AN",  # Annobon
    "GQ-BN",  # Bioko Nord
    "GQ-BS",  # Bioko Sud
    "GQ-C",  # Région Continentale
    "GQ-CS",  # Centro Sud
    "GQ-DJ",  # Djibloho
    "GQ-I",  # Région Insulaire
    "GQ-KN",  # Kié-Ntem
    "GQ-LI",  # Littoral
    "GQ-WN",  # Wele-Nzas
    # Hellenic Republic
    "GR-69",  # Ágion Óros
    "GR-A",  # Anatolikí Makedonía kai Thráki
    "GR-B",  # Kentrikí Makedonía
    "GR-C",  # Dytikí Makedonía
    "GR-D",  # Ípeiros
    "GR-E",  # Thessalía
    "GR-F",  # Ionía Nísia
    "GR-G",  # Dytikí Elláda
    "GR-H",  # Stereá Elláda
    "GR-I",  # Attikí
    "GR-J",  # Pelopónnisos
    "GR-K",  # Vóreio Aigaío
    "GR-L",  # Nótio Aigaío
    "GR-M",  # Kríti
    # South Georgia and the South Sandwich Islands
    # (no subdivisions)
    # Republic of Guatemala
    "GT-01",  # Guatemala
    "GT-02",  # El Progreso
    "GT-03",  # Sacatepéquez
    "GT-04",  # Chimaltenango
    "GT-05",  # Escuintla
    "GT-06",  # Santa Rosa
    "GT-07",  # Sololá
    "GT-08",  # Totonicapán
    "GT-09",  # Quetzaltenango
    "GT-10",  # Suchitepéquez
    "GT-11",  # Retalhuleu
    "GT-12",  # San Marcos
    "GT-13",  # Huehuetenango
    "GT-14",  # Quiché
    "GT-15",  # Baja Verapaz
    "GT-16",  # Alta Verapaz
    "GT-17",  # Petén
    "GT-18",  # Izabal
    "GT-19",  # Zacapa
    "GT-20",  # Chiquimula
    "GT-21",  # Jalapa
    "GT-22",  # Jutiapa
    # Guam
    # (no subdivisions)
    # Republic of Guinea-Bissau
    "GW-BA",  # Bafatá
    "GW-BL",  # Bolama / Bijagós
    "GW-BM",  # Biombo
    "GW-BS",  # Bissau
    "GW-CA",  # Cacheu
    "GW-GA",  # Gabú
    "GW-L",  # Leste
    "GW-N",  # Norte
    "GW-OI",  # Oio
    "GW-QU",  # Quinara
    "GW-S",  # Sul
    "GW-TO",  # Tombali
    # Republic of Guyana
    "GY-BA",  # Barima-Waini
    "GY-CU",  # Cuyuni-Mazaruni
    "GY-DE",  # Demerara-Mahaica
    "GY-EB",  # East Berbice-Corentyne
    "GY-ES",  # Essequibo Islands-West Demerara
    "GY-MA",  # Mahaica-Berbice
    "GY-PM",  # Pomeroon-Supenaam
    "GY-PT",  # Potaro-Siparuni
    "GY-UD",  # Upper Demerara-Berbice
    "GY-UT",  # Upper Takutu-Upper Essequibo
    # Hong Kong Special Administrative Region of China
    # (no subdivisions)
    # Heard Island and McDonald Islands
    # (no subdivisions)
    # Republic of Honduras
    "HN-AT",  # Atlántida
    "HN-CH",  # Choluteca
    "HN-CL",  # Colón
    "HN-CM",  # Comayagua
    "HN-CP",  # Copán
    "HN-CR",  # Cortés
    "HN-EP",  # El Paraíso
    "HN-FM",  # Francisco Morazán
    "HN-GD",  # Gracias a Dios
    "HN-IB",  # Islas de la Bahía
    "HN-IN",  # Intibucá
    "HN-LE",  # Lempira
    "HN-LP",  # La Paz
    "HN-OC",  # Ocotepeque
    "HN-OL",  # Olancho
    "HN-SB",  # Santa Bárbara
    "HN-VA",  # Valle
    "HN-YO",  # Yoro
    # Republic of Croatia
    "HR-01",  # Zagrebačka županija
    "HR-02",  # Krapinsko-zagorska županija
    "HR-03",  # Sisačko-moslavačka županija
    "HR-04",  # Karlovačka županija
    "HR-05",  # Varaždinska županija
    "HR-06",  # Koprivničko-križevačka županija
    "HR-07",  # Bjelovarsko-bilogorska županija
    "HR-08",  # Primorsko-goranska županija
    "HR-09",  # Ličko-senjska županija
    "HR-10",  # Virovitičko-podravska županija
    "HR-11",  # Požeško-slavonska županija
    "HR-12",  # Brodsko-posavska županija
    "HR-13",  # Zadarska županija
    "HR-14",  # Osječko-baranjska županija
    "HR-15",  # Šibensko-kninska županija
    "HR-16",  # Vukovarsko-srijemska županija
    "HR-17",  # Splitsko-dalmatinska županija
    "HR-18",  # Istarska županija
    "HR-19",  # Dubrovačko-neretvanska županija
    "HR-20",  # Međimurska županija
    "HR-21",  # Grad Zagreb
    # Republic of Haiti
    "HT-AR",  # Artibonite
    "HT-CE",  # Centre
    "HT-GA",  # Grande’Anse
    "HT-ND",  # Nord
    "HT-NE",  # Nord-Est
    "HT-NI",  # Nippes
    "HT-NO",  # Nord-Ouest
    "HT-OU",  # Ouest
    "HT-SD",  # Sud
    "HT-SE",  # Sud-Est
    # Hungary
    "HU-BA",  # Baranya
    "HU-BC",  # Békéscsaba
    "HU-BE",  # Békés
    "HU-BK",  # Bács-Kiskun
    "HU-BU",  # Budapest
    "HU-BZ",  # Borsod-Abaúj-Zemplén
    "HU-CS",  # Csongrád-Csanád
    "HU-DE",  # Debrecen
    "HU-DU",  # Dunaújváros
    "HU-EG",  # Eger
    "HU-ER",  # Érd
    "HU-FE",  # Fejér
    "HU-GS",  # Győr-Moson-Sopron
    "HU-GY",  # Győr
    "HU-HB",  # Hajdú-Bihar
    "HU-HE",  # Heves
    "HU-HV",  # Hódmezővásárhely
    "HU-JN",  # Jász-Nagykun-Szolnok
    "HU-KE",  # Komárom-Esztergom
    "HU-KM",  # Kecskemét
    "HU-KV",  # Kaposvár
    "HU-MI",  # Miskolc
    "HU-NK",  # Nagykanizsa
    "HU-NO",  # Nógrád
    "HU-NY",  # Nyíregyháza
    "HU-PE",  # Pest
    "HU-PS",  # Pécs
    "HU-SD",  # Szeged
    "HU-SF",  # Székesfehérvár
    "HU-SH",  # Szombathely
    "HU-SK",  # Szolnok
    "HU-SN",  # Sopron
    "HU-SO",  # Somogy
    "HU-SS",  # Szekszárd
    "HU-ST",  # Salgótarján
    "HU-SZ",  # Szabolcs-Szatmár-Bereg
    "HU-TB",  # Tatabánya
    "HU-TO",  # Tolna
    "HU-VA",  # Vas
    "HU-VE",  # Veszprém
    "HU-VM",  # Veszprém
    "HU-ZA",  # Zala
    "HU-ZE",  # Zalaegerszeg
    # Republic of Indonesia
    "ID-AC",  # Aceh
    "ID-BA",  # Bali
    "ID-BB",  # Kepulauan Bangka Belitung
    "ID-BE",  # Bengkulu
    "ID-BT",  # Banten
    "ID-GO",  # Gorontalo
    "ID-JA",  # Jambi
    "ID-JB",  # Jawa Barat
    "ID-JI",  # Jawa Timur
    "ID-JK",  # Jakarta Raya
    "ID-JT",  # Jawa Tengah
    "ID-JW",  # Jawa
    "ID-KA",  # Kalimantan
    "ID-KB",  # Kalimantan Barat
    "ID-KI",  # Kalimantan Timur
    "ID-KR",  # Kepulauan Riau
    "ID-KS",  # Kalimantan Selatan
    "ID-KT",  # Kalimantan Tengah
    "ID-KU",  # Kalimantan Utara
    "ID-LA",  # Lampung
    "ID-MA",  # Maluku
    "ID-ML",  # Maluku
    "ID-MU",  # Maluku Utara
    "ID-NB",  # Nusa Tenggara Barat
    "ID-NT",  # Nusa Tenggara Timur
    "ID-NU",  # Nusa Tenggara
    "ID-PA",  # Papua
    "ID-PB",  # Papua Barat
    "ID-PD",  # Papua Barat Daya
    "ID-PE",  # Papua Pengunungan
    "ID-PP",  # Papua
    "ID-PS",  # Papua Selatan
    "ID-PT",  # Papua Tengah
    "ID-RI",  # Riau
    "ID-SA",  # Sulawesi Utara
    "ID-SB",  # Sumatera Barat
    "ID-SG",  # Sulawesi Tenggara
    "ID-SL",  # Sulawesi
    "ID-SM",  # Sumatera
    "ID-SN",  # Sulawesi Selatan
    "ID-SR",  # Sulawesi Barat
    "ID-SS",  # Sumatera Selatan
    "ID-ST",  # Sulawesi Tengah
    "ID-SU",  # Sumatera Utara
    "ID-YO",  # Yogyakarta
    # Ireland
    "IE-C",  # Connaught
    "IE-CE",  # Clare
    "IE-CN",  # Cavan
    "IE-CO",  # Cork
    "IE-CW",  # Carlow
    "IE-D",  # Dublin
    "IE-DL",  # Donegal
    "IE-G",  # Galway
    "IE-KE",  # Kildare
    "IE-KK",  # Kilkenny
    "IE-KY",  # Kerry
    "IE-L",  # Leinster
    "IE-LD",  # Longford
    "IE-LH",  # Louth
    "IE-LK",  # Limerick
    "IE-LM",  # Leitrim
    "IE-LS",  # Laois
    "IE-M",  # Munster
    "IE-MH",  # Meath
    "IE-MN",  # Monaghan
    "IE-MO",  # Mayo
    "IE-OY",  # Offaly
    "IE-RN",  # Roscommon
    "IE-SO",  # Sligo
    "IE-TA",  # Tipperary
    "IE-U",  # Ulster
    "IE-WD",  # Waterford
    "IE-WH",  # Westmeath
    "IE-WW",  # Wicklow
    "IE-WX",  # Wexford
    # State of Israel
    "IL-D",  # Al Janūbī
    "IL-HA",  # H̱efa
    "IL-JM",  # Al Quds
    "IL-M",  # Al Awsaţ
    "IL-TA",  # Tall Abīb
    "IL-Z",  # Ash Shamālī
    # Isle of Man
    # (no subdivisions)
    # Republic of India
    "IN-AN",  # Andaman and Nicobar Islands
    "IN-AP",  # Andhra Pradesh
    "IN-AR",  # Arunāchal Pradesh
    "IN-AS",  # Assam
    "IN-BR",  # Bihār
    "IN-CG",  # Chhattīsgarh
    "IN-CH",  # Chandīgarh
    "IN-DH",  # Dādra and Nagar Haveli and Damān and Diu
    "IN-DL",  # Delhi
    "IN-GA",  # Goa
    "IN-GJ",  # Gujarāt
    "IN-HP",  # Himāchal Pradesh
    "IN-HR",  # Haryāna
    "IN-JH",  # Jhārkhand
    "IN-JK",  # Jammu and Kashmīr
    "IN-KA",  # Karnātaka
    "IN-KL",  # Kerala
    "IN-LA",  # Ladākh
    "IN-LD",  # Lakshadweep
    "IN-MH",  # Mahārāshtra
    "IN-ML",  # Meghālaya
    "IN-MN",  # Manipur
    "IN-MP",  # Madhya Pradesh
    "IN-MZ",  # Mizoram
    "IN-NL",  # Nāgāland
    "IN-OD",  # Odisha
    "IN-PB",  # Punjab
    "IN-PY",  # Puducherry
    "IN-RJ",  # Rājasthān
    "IN-SK",  # Sikkim
    "IN-TN",  # Tamil Nādu
    "IN-TR",  # Tripura
    "IN-TS",  # Telangāna
    "IN-UK",  # Uttarākhand
    "IN-UP",  # Uttar Pradesh
    "IN-WB",  # West Bengal
    # British Indian Ocean Territory
    # (no subdivisions)
    # Republic of Iraq
    "IQ-AN",  # Al Anbār
    "IQ-AR",  # Arbīl
    "IQ-BA",  # Al Başrah
    "IQ-BB",  # Bābil
    "IQ-BG",  # Baghdād
    "IQ-DA",  # Dahūk
    "IQ-DI",  # Diyālá
    "IQ-DQ",  # Dhī Qār
    "IQ-KA",  # Karbalā’
    "IQ-KI",  # Kirkūk
    "IQ-KR",  # Herêm-î Kurdistan
    "IQ-MA",  # Maysān
    "IQ-MU",  # Al Muthanná
    "IQ-NA",  # An Najaf
    "IQ-NI",  # Nīnawá
    "IQ-QA",  # Al Qādisīyah
    "IQ-SD",  # Şalāḩ ad Dīn
    "IQ-SU",  # As Sulaymānīyah
    "IQ-WA",  # Wāsiţ
    # Islamic Republic of Iran
    "IR-00",  # Markazī
    "IR-01",  # Gīlān
    "IR-02",  # Māzandarān
    "IR-03",  # Āz̄ārbāyjān-e Shārqī
    "IR-04",  # Āz̄ārbāyjān-e Ghārbī
    "IR-05",  # Kermānshāh
    "IR-06",  # Khūzestān
    "IR-07",  # Fārs
    "IR-08",  # Kermān
    "IR-09",  # Khorāsān-e Raẕavī
    "IR-10",  # Eşfahān
    "IR-11",  # Sīstān va Balūchestān
    "IR-12",  # Kordestān
    "IR-13",  # Hamadān
    "IR-14",  # Chahār Maḩāl va Bakhtīārī
    "IR-15",  # Lorestān
    "IR-16",  # Īlām
    "IR-17",  # Kohgīlūyeh va Bowyer Aḩmad
    "IR-18",  # Būshehr
    "IR-19",  # Zanjān
    "IR-20",  # Semnān
    "IR-21",  # Yazd
    "IR-22",  # Hormozgān
    "IR-23",  # Tehrān
    "IR-24",  # Ardabīl
    "IR-25",  # Qom
    "IR-26",  # Qazvīn
    "IR-27",  # Golestān
    "IR-28",  # Khorāsān-e Shomālī
    "IR-29",  # Khorāsān-e Jonūbī
    "IR-30",  # Alborz
    # Republic of Iceland
    "IS-1",  # Höfuðborgarsvæði
    "IS-2",  # Suðurnes
    "IS-3",  # Vesturland
    "IS-4",  # Vestfirðir
    "IS-5",  # Norðurland vestra
    "IS-6",  # Norðurland eystra
    "IS-7",  # Austurland
    "IS-8",  # Suðurland
    "IS-AKN",  # Akraneskaupstaður
    "IS-AKU",  # Akureyrarbær
    "IS-ARN",  # Árneshreppur
    "IS-ASA",  # Ásahreppur
    "IS-BLA",  # Bláskógabyggð
    "IS-BOG",  # Borgarbyggð
    "IS-BOL",  # Bolungarvíkurkaupstaður
    "IS-DAB",  # Dalabyggð
    "IS-DAV",  # Dalvíkurbyggð
    "IS-EOM",  # Eyja- og Miklaholtshreppur
    "IS-EYF",  # Eyjafjarðarsveit
    "IS-FJD",  # Fjarðabyggð
    "IS-FJL",  # Fjallabyggð
    "IS-FLA",  # Flóahreppur
    "IS-FLR",  # Fljótsdalshreppur
    "IS-GAR",  # Garðabær
    "IS-GOG",  # Grímsnes- og Grafningshreppur
    "IS-GRN",  # Grindavíkurbær
    "IS-GRU",  # Grundarfjarðarbær
    "IS-GRY",  # Grýtubakkahreppur
    "IS-HAF",  # Hafnarfjarðarkaupstaður
    "IS-HRG",  # Hörgársveit
    "IS-HRU",  # Hrunamannahreppur
    "IS-HUG",  # Húnabyggð
    "IS-HUV",  # Húnaþing vestra
    "IS-HVA",  # Hvalfjarðarsveit
    "IS-HVE",  # Hveragerðisbær
    "IS-ISA",  # Ísafjarðarbær
    "IS-KAL",  # Kaldrananeshreppur
    "IS-KJO",  # Kjósarhreppur
    "IS-KOP",  # Kópavogsbær
    "IS-LAN",  # Langanesbyggð
    "IS-MOS",  # Mosfellsbær
    "IS-MUL",  # Múlaþing
    "IS-MYR",  # Mýrdalshreppur
    "IS-NOR",  # Norðurþing
    "IS-RGE",  # Rangárþing eystra
    "IS-RGY",  # Rangárþing ytra
    "IS-RHH",  # Reykhólahreppur
    "IS-RKN",  # Reykjanesbær
    "IS-RKV",  # Reykjavíkurborg
    "IS-SBT",  # Svalbarðsstrandarhreppur
    "IS-SDN",  # Suðurnesjabær
    "IS-SDV",  # Súðavíkurhreppur
    "IS-SEL",  # Seltjarnarnesbær
    "IS-SFA",  # Sveitarfélagið Árborg
    "IS-SHF",  # Sveitarfélagið Hornafjörður
    "IS-SKF",  # Skaftárhreppur
    "IS-SKG",  # Skagabyggð
    "IS-SKO",  # Skorradalshreppur
    "IS-SKR",  # Skagafjörður
    "IS-SNF",  # Snæfellsbær
    "IS-SOG",  # Skeiða- og Gnúpverjahreppur
    "IS-SOL",  # Sveitarfélagið Ölfus
    "IS-SSS",  # Sveitarfélagið Skagaströnd
    "IS-STR",  # Strandabyggð
    "IS-STY",  # Stykkishólmsbær
    "IS-SVG",  # Sveitarfélagið Vogar
    "IS-TAL",  # Tálknafjarðarhreppur
    "IS-THG",  # Þingeyjarsveit
    "IS-TJO",  # Tjörneshreppur
    "IS-VEM",  # Vestmannaeyjabær
    "IS-VER",  # Vesturbyggð
    "IS-VOP",  # Vopnafjarðarhreppur
    # Italian Republic
    "IT-21",  # Piemonte
    "IT-23",  # Val d'Aoste
    "IT-25",  # Lombardia
    "IT-32",  # Trentino-Alto Adige
    "IT-34",  # Veneto
    "IT-36",  # Friuli Venezia Giulia
    "IT-42",  # Liguria
    "IT-45",  # Emilia-Romagna
    "IT-52",  # Toscana
    "IT-55",  # Umbria
    "IT-57",  # Marche
    "IT-62",  # Lazio
    "IT-65",  # Abruzzo
    "IT-67",  # Molise
    "IT-72",  # Campania
    "IT-75",  # Puglia
    "IT-77",  # Basilicata
    "IT-78",  # Calabria
    "IT-82",  # Sicilia
    "IT-88",  # Sardegna
    "IT-AG",  # Agrigento
    "IT-AL",  # Alessandria
    "IT-AN",  # Ancona
    "IT-AP",  # Ascoli Piceno
    "IT-AQ",  # L'Aquila
    "IT-AR",  # Arezzo
    "IT-AT",  # Asti
    "IT-AV",  # Avellino
    "IT-BA",  # Bari
    "IT-BG",  # Bergamo
    "IT-BI",  # Biella
    "IT-BL",  # Belluno
    "IT-BN",  # Benevento
    "IT-BO",  # Bologna
    "IT-BR",  # Brindisi
    "IT-BS",  # Brescia
    "IT-BT",  # Barletta-Andria-Trani
    "IT-BZ",  # Bolzano
    "IT-CA",  # Cagliari
    "IT-CB",  # Campobasso
    "IT-CE",  # Caserta
    "IT-CH",  # Chieti
    "IT-CL",  # Caltanissetta
    "IT-CN",  # Cuneo
    "IT-CO",  # Como
    "IT-CR",  # Cremona
    "IT-CS",  # Cosenza
    "IT-CT",  # Catania
    "IT-CZ",  # Catanzaro
    "IT-EN",  # Enna
    "IT-FC",  # Forlì-Cesena
    "IT-FE",  # Ferrara
    "IT-FG",  # Foggia
    "IT-FI",  # Firenze
    "IT-FM",  # Fermo
    "IT-FR",  # Frosinone
    "IT-GE",  # Genova
    "IT-GO",  # Gorizia
    "IT-GR",  # Grosseto
    "IT-IM",  # Imperia
    "IT-IS",  # Isernia
    "IT-KR",  # Crotone
    "IT-LC",  # Lecco
    "IT-LE",  # Lecce
    "IT-LI",  # Livorno
    "IT-LO",  # Lodi
    "IT-LT",  # Latina
    "IT-LU",  # Lucca
    "IT-MB",  # Monza e Brianza
    "IT-MC",  # Macerata
    "IT-ME",  # Messina
    "IT-MI",  # Milano
    "IT-MN",  # Mantova
    "IT-MO",  # Modena
    "IT-MS",  # Massa-Carrara
    "IT-MT",  # Matera
    "IT-NA",  # Napoli
    "IT-NO",  # Novara
    "IT-NU",  # Nuoro
    "IT-OR",  # Oristano
    "IT-PA",  # Palermo
    "IT-PC",  # Piacenza
    "IT-PD",  # Padova
    "IT-PE",  # Pescara
    "IT-PG",  # Perugia
    "IT-PI",  # Pisa
    "IT-PN",  # Pordenone
    "IT-PO",  # Prato
    "IT-PR",  # Parma
    "IT-PT",  # Pistoia
    "IT-PU",  # Pesaro e Urbino
    "IT-PV",  # Pavia
    "IT-PZ",  # Potenza
    "IT-RA",  # Ravenna
    "IT-RC",  # Reggio Calabria
    "IT-RE",  # Reggio Emilia
    "IT-RG",  # Ragusa
    "IT-RI",  # Rieti
    "IT-RM",  # Roma
    "IT-RN",  # Rimini
    "IT-RO",  # Rovigo
    "IT-SA",  # Salerno
    "IT-SI",  # Siena
    "IT-SO",  # Sondrio
    "IT-SP",  # La Spezia
    "IT-SR",  # Siracusa
    "IT-SS",  # Sassari
    "IT-SU",  # Sud Sardegna
    "IT-SV",  # Savona
    "IT-TA",  # Taranto
    "IT-TE",  # Teramo
    "IT-TN",  # Trento
    "IT-TO",  # Torino
    "IT-TP",  # Trapani
    "IT-TR",  # Terni
    "IT-TS",  # Trieste
    "IT-TV",  # Treviso
    "IT-UD",  # Udine
    "IT-VA",  # Varese
    "IT-VB",  # Verbano-Cusio-Ossola
    "IT-VC",  # Vercelli
    "IT-VE",  # Venezia
    "IT-VI",  # Vicenza
    "IT-VR",  # Verona
    "IT-VT",  # Viterbo
    "IT-VV",  # Vibo Valentia
    # Jersey
    # (no subdivisions)
    # Jamaica
    "JM-01",  # Kingston
    "JM-02",  # Saint Andrew
    "JM-03",  # Saint Thomas
    "JM-04",  # Portland
    "JM-05",  # Saint Mary
    "JM-06",  # Saint Ann
    "JM-07",  # Trelawny
    "JM-08",  # Saint James
    "JM-09",  # Hanover
    "JM-10",  # Westmoreland
    "JM-11",  # Saint Elizabeth
    "JM-12",  # Manchester
    "JM-13",  # Clarendon
    "JM-14",  # Saint Catherine
    # Hashemite Kingdom of Jordan
    "JO-AJ",  # ‘Ajlūn
    "JO-AM",  # Al ‘A̅şimah
    "JO-AQ",  # Al ‘Aqabah
    "JO-AT",  # Aţ Ţafīlah
    "JO-AZ",  # Az Zarqā’
    "JO-BA",  # Al Balqā’
    "JO-IR",  # Irbid
    "JO-JA",  # Jarash
    "JO-KA",  # Al Karak
    "JO-MA",  # Al Mafraq
    "JO-MD",  # Mādabā
    "JO-MN",  # Ma‘ān
    # Japan
    "JP-01",  # Hokkaido
    "JP-02",  # Aomori
    "JP-03",  # Iwate
    "JP-04",  # Miyagi
    "JP-05",  # Akita
    "JP-06",  # Yamagata
    "JP-07",  # Fukushima
    "JP-08",  # Ibaraki
    "JP-09",  # Tochigi
    "JP-10",  # Gunma
    "JP-11",  # Saitama
    "JP-12",  # Chiba
    "JP-13",  # Tokyo
    "JP-14",  # Kanagawa
    "JP-15",  # Niigata
    "JP-16",  # Toyama
    "JP-17",  # Ishikawa
    "JP-18",  # Fukui
    "JP-19",  # Yamanashi
    "JP-20",  # Nagano
    "JP-21",  # Gifu
    "JP-22",  # Shizuoka
    "JP-23",  # Aichi
    "JP-24",  # Mie
    "JP-25",  # Shiga
    "JP-26",  # Kyoto
    "JP-27",  # Osaka
    "JP-28",  # Hyogo
    "JP-29",  # Nara
    "JP-30",  # Wakayama
    "JP-31",  # Tottori
    "JP-32",  # Shimane
    "JP-33",  # Okayama
    "JP-34",  # Hiroshima
    "JP-35",  # Yamaguchi
    "JP-36",  # Tokushima
    "JP-37",  # Kagawa
    "JP-38",  # Ehime
    "JP-39",  # Kochi
    "JP-40",  # Fukuoka
    "JP-41",  # Saga
    "JP-42",  # Nagasaki
    "JP-43",  # Kumamoto
    "JP-44",  # Oita
    "JP-45",  # Miyazaki
    "JP-46",  # Kagoshima
    "JP-47",  # Okinawa
    # Republic of Kenya
    "KE-01",  # Baringo
    "KE-02",  # Bomet
    "KE-03",  # Bungoma
    "KE-04",  # Busia
    "KE-05",  # Elgeyo/Marakwet
    "KE-06",  # Embu
    "KE-07",  # Garissa
    "KE-08",  # Homa Bay
    "KE-09",  # Isiolo
    "KE-10",  # Kajiado
    "KE-11",  # Kakamega
    "KE-12",  # Kericho
    "KE-13",  # Kiambu
    "KE-14",  # Kilifi
    "KE-15",  # Kirinyaga
    "KE-16",  # Kisii
    "KE-17",  # Kisumu
    "KE-18",  # Kitui
    "KE-19",  # Kwale
    "KE-20",  # Laikipia
    "KE-21",  # Lamu
    "KE-22",  # Machakos
    "KE-23",  # Makueni
    "KE-24",  # Mandera
    "KE-25",  # Marsabit
    "KE-26",  # Meru
    "KE-27",  # Migori
    "KE-28",  # Mombasa
    "KE-29",  # Murang'a
    "KE-30",  # Nairobi City
    "KE-31",  # Nakuru
    "KE-32",  # Nandi
    "KE-33",  # Narok
    "KE-34",  # Nyamira
    "KE-35",  # Nyandarua
    "KE-36",  # Nyeri
    "KE-37",  # Samburu
    "KE-38",  # Siaya
    "KE-39",  # Taita/Taveta
    "KE-40",  # Tana River
    "KE-41",  # Tharaka-Nithi
    "KE-42",  # Trans Nzoia
    "KE-43",  # Turkana
    "KE-44",  # Uasin Gishu
    "KE-45",  # Vihiga
    "KE-46",  # Wajir
    "KE-47",  # West Pokot
    # Kyrgyz Republic
    "KG-B",  # Batken
    "KG-C",  # Chuyskaya oblast'
    "KG-GB",  # Bishkek Shaary
    "KG-GO",  # Gorod Osh
    "KG-J",  # Dzhalal-Abadskaya oblast'
    "KG-N",  # Naryn
    "KG-O",  # Osh
    "KG-T",  # Talas
    "KG-Y",  # Issyk-Kul'skaja oblast'
    # Kingdom of Cambodia
    "KH-1",  # Banteay Mean Choăy
    "KH-10",  # Kracheh
    "KH-11",  # Mondol Kiri
    "KH-12",  # Phnom Penh
    "KH-13",  # Preah Vihear
    "KH-14",  # Prey Veaeng
    "KH-15",  # Pousaat
    "KH-16",  # Rotanak Kiri
    "KH-17",  # Siem Reab
    "KH-18",  # Preah Sihanouk
    "KH-19",  # Stoĕng Trêng
    "KH-2",  # Baat Dambang
    "KH-20",  # Svaay Rieng
    "KH-21",  # Taakaev
    "KH-22",  # Otdar Mean Chey
    "KH-23",  # Kaeb
    "KH-24",  # Pailin
    "KH-25",  # Tbong Khmum
    "KH-3",  # Kampong Chaam
    "KH-4",  # Kampong Chhnang
    "KH-5",  # Kampong Spueu
    "KH-6",  # Kampong Thum
    "KH-7",  # Kampot
    "KH-8",  # Kandaal
    "KH-9",  # Kaoh Kong
    # Republic of Kiribati
    "KI-G",  # Gilbert Islands
    "KI-L",  # Line Islands
    "KI-P",  # Phoenix Islands
    # Union of the Comoros
    "KM-A",  # Anjouan
    "KM-G",  # Grande Comore
    "KM-M",  # Mohéli
    # Saint Kitts and Nevis
    "KN-01",  # Christ Church Nichola Town
    "KN-02",  # Saint Anne Sandy Point
    "KN-03",  # Saint George Basseterre
    "KN-04",  # Saint George Gingerland
    "KN-05",  # Saint James Windward
    "KN-06",  # Saint John Capisterre
    "KN-07",  # Saint John Figtree
    "KN-08",  # Saint Mary Cayon
    "KN-09",  # Saint Paul Capisterre
    "KN-10",  # Saint Paul Charlestown
    "KN-11",  # Saint Peter Basseterre
    "KN-12",  # Saint Thomas Lowland
    "KN-13",  # Saint Thomas Middle Island
    "KN-15",  # Trinity Palmetto Point
    "KN-K",  # Saint Kitts
    "KN-N",  # Nevis
    # Democratic People's Republic of Korea
    "KP-01",  # P'yǒngyang
    "KP-02",  # P'yǒngan-namdo
    "KP-03",  # P'yǒngan-bukto
    "KP-04",  # Chagang-do
    "KP-05",  # Hwanghae-namdo
    "KP-06",  # Hwanghae-bukto
    "KP-07",  # Kangweonto
    "KP-08",  # Hamgyǒng-namdo
    "KP-09",  # Hamgyǒng-bukto
    "KP-10",  # Ryanggang-do
    "KP-13",  # Raseon
    "KP-14",  # Nampho
    "KP-15",  # Kaeseong
    # Republic of Korea
    "KR-11",  # Seoul-teukbyeolsi
    "KR-26",  # Busan-gwangyeoksi
    "KR-27",  # Daegu-gwangyeoksi
    "KR-28",  # Incheon-gwangyeoksi
    "KR-29",  # Gwangju-gwangyeoksi
    "KR-30",  # Daejeon-gwangyeoksi
    "KR-31",  # Ulsan-gwangyeoksi
    "KR-41",  # Gyeonggi-do
    "KR-42",  # Gangwon-teukbyeoljachido
    "KR-43",  # Chungcheongbuk-do
    "KR-44",  # Chungcheongnam-do
    "KR-45",  # Jeollabuk-do
    "KR-46",  # Jeollanam-do
    "KR-47",  # Gyeongsangbuk-do
    "KR-48",  # Gyeongsangnam-do
    "KR-49",  # Jeju-teukbyeoljachido
    "KR-50",  # Sejong
    # State of Kuwait
    "KW-AH",  # Al Aḩmadī
    "KW-FA",  # Al Farwānīyah
    "KW-HA",  # Ḩawallī
    "KW-JA",  # Al Jahrā’
    "KW-KU",  # Al ‘Āşimah
    "KW-MU",  # Mubārak al Kabīr
    # Cayman Islands
    # (no subdivisions)
    # Republic of Kazakhstan
    "KZ-10",  # Abajskaja oblast’
    "KZ-11",  # Akmolinskaja oblast'
    "KZ-15",  # Aktjubinskaja oblast'
    "KZ-19",  # Almatinskaja oblast'
    "KZ-23",  # Atyrauskaja oblast'
    "KZ-27",  # Batys Qazaqstan oblysy
    "KZ-31",  # Zhambyl oblysy
    "KZ-33",  # Zhetisū oblysy
    "KZ-35",  # Karagandinskaja oblast'
    "KZ-39",  # Kostanajskaja oblast'
    "KZ-43",  # Kyzylordinskaja oblast'
    "KZ-47",  # Mangghystaū oblysy
    "KZ-55",  # Pavlodar oblysy
    "KZ-59",  # Severo-Kazahstanskaja oblast'
    "KZ-61",  # Turkestankaya oblast'
    "KZ-62",  # Ulytauskaja oblast’
    "KZ-63",  # Shyghys Qazaqstan oblysy
    "KZ-71",  # Astana
    "KZ-75",  # Almaty
    "KZ-79",  # Shymkent
    # Lao People's Democratic Republic
    "LA-AT",  # Attapu
    "LA-BK",  # Bokèo
    "LA-BL",  # Bolikhamxai
    "LA-CH",  # Champasak
    "LA-HO",  # Houaphan
    "LA-KH",  # Khammouan
    "LA-LM",  # Louang Namtha
    "LA-LP",  # Louangphabang
    "LA-OU",  # Oudômxai
    "LA-PH",  # Phôngsali
    "LA-SL",  # Salavan
    "LA-SV",  # Savannakhét
    "LA-VI",  # Viangchan
    "LA-VT",  # Viangchan
    "LA-XA",  # Xaignabouli
    "LA-XE",  # Xékong
    "LA-XI",  # Xiangkhouang
    "LA-XS",  # Xaisômboun
    # Lebanese Republic
    "LB-AK",  # Aakkâr
    "LB-AS",  # Ash Shimāl
    "LB-BA",  # Bayrūt
    "LB-BH",  # Baalbek-Hermel
    "LB-BI",  # Al Biqā‘
    "LB-JA",  # Al Janūb
    "LB-JL",  # Jabal Lubnān
    "LB-NA",  # An Nabaţīyah
    # Saint Lucia
    "LC-01",  # Anse la Raye
    "LC-02",  # Castries
    "LC-03",  # Choiseul
    "LC-05",  # Dennery
    "LC-06",  # Gros Islet
    "LC-07",  # Laborie
    "LC-08",  # Micoud
    "LC-10",  # Soufrière
    "LC-11",  # Vieux Fort
    "LC-12",  # Canaries
    # Principality of Liechtenstein
    "LI-01",  # Balzers
    "LI-02",  # Eschen
    "LI-03",  # Gamprin
    "LI-04",  # Mauren
    "LI-05",  # Planken
    "LI-06",  # Ruggell
    "LI-07",  # Schaan
    "LI-08",  # Schellenberg
    "LI-09",  # Triesen
    "LI-10",  # Triesenberg
    "LI-11",  # Vaduz
    # Democratic Socialist Republic of Sri Lanka
    "LK-1",  # Western Province
    "LK-11",  # Colombo
    "LK-12",  # Gampaha
    "LK-13",  # Kalutara
    "LK-2",  # Central Province
    "LK-21",  # Kandy
    "LK-22",  # Matale
    "LK-23",  # Nuwara Eliya
    "LK-3",  # Southern Province
    "LK-31",  # Galle
    "LK-32",  # Matara
    "LK-33",  # Hambantota
    "LK-4",  # Northern Province
    "LK-41",  # Jaffna
    "LK-42",  # Kilinochchi
    "LK-43",  # Mannar
    "LK-44",  # Vavuniya
    "LK-45",  # Mullaittivu
    "LK-5",  # Eastern Province
    "LK-51",  # Batticaloa
    "LK-52",  # Ampara
    "LK-53",  # Trincomalee
    "LK-6",  # North Western Province
    "LK-61",  # Kurunegala
    "LK-62",  # Puttalam
    "LK-7",  # North Central Province
    "LK-71",  # Anuradhapura
    "LK-72",  # Polonnaruwa
    "LK-8",  # Uva Province
    "LK-81",  # Badulla
    "LK-82",  # Monaragala
    "LK-9",  # Sabaragamuwa Province
    "LK-91",  # Ratnapura
    "LK-92",  # Kegalla
    # Republic of Liberia
    "LR-BG",  # Bong
    "LR-BM",  # Bomi
    "LR-CM",  # Grand Cape Mount
    "LR-GB",  # Grand Bassa
    "LR-GG",  # Grand Gedeh
    "LR-GK",  # Grand Kru
    "LR-GP",  # Gbarpolu
    "LR-LO",  # Lofa
    "LR-MG",  # Margibi
    "LR-MO",  # Montserrado
    "LR-MY",  # Maryland
    "LR-NI",  # Nimba
    "LR-RG",  # River Gee
    "LR-RI",  # River Cess
    "LR-SI",  # Sinoe
    # Kingdom of Lesotho
    "LS-A",  # Maseru
    "LS-B",  # Botha-Bothe
    "LS-C",  # Leribe
    "LS-D",  # Berea
    "LS-E",  # Mafeteng
    "LS-F",  # Mohale's Hoek
    "LS-G",  # Quthing
    "LS-H",  # Qacha's Nek
    "LS-J",  # Mokhotlong
    "LS-K",  # Thaba-Tseka
    # Republic of Lithuania
    "LT-01",  # Akmenė
    "LT-02",  # Alytaus miestas
    "LT-03",  # Alytus
    "LT-04",  # Anykščiai
    "LT-05",  # Birštonas
    "LT-06",  # Biržai
    "LT-07",  # Druskininkai
    "LT-08",  # Elektrėnai
    "LT-09",  # Ignalina
    "LT-10",  # Jonava
    "LT-11",  # Joniškis
    "LT-12",  # Jurbarkas
    "LT-13",  # Kaišiadorys
    "LT-14",  # Kalvarija
    "LT-15",  # Kauno miestas
    "LT-16",  # Kaunas
    "LT-17",  # Kazlų Rūdos
    "LT-18",  # Kėdainiai
    "LT-19",  # Kelmė
    "LT-20",  # Klaipėdos miestas
    "LT-21",  # Klaipėda
    "LT-22",  # Kretinga
    "LT-23",  # Kupiškis
    "LT-24",  # Lazdijai
    "LT-25",  # Marijampolė
    "LT-26",  # Mažeikiai
    "LT-27",  # Molėtai
    "LT-28",  # Neringa
    "LT-29",  # Pagėgiai
    "LT-30",  # Pakruojis
    "LT-31",  # Palangos miestas
    "LT-32",  # Panevėžio miestas
    "LT-33",  # Panevėžys
    "LT-34",  # Pasvalys
    "LT-35",  # Plungė
    "LT-36",  # Prienai
    "LT-37",  # Radviliškis
    "LT-38",  # Raseiniai
    "LT-39",  # Rietavas
    "LT-40",  # Rokiškis
    "LT-41",  # Šakiai
    "LT-42",  # Šalčininkai
    "LT-43",  # Šiaulių miestas
    "LT-44",  # Šiauliai
    "LT-45",  # Šilalė
    "LT-46",  # Šilutė
    "LT-47",  # Širvintos
    "LT-48",  # Skuodas
    "LT-49",  # Švenčionys
    "LT-50",  # Tauragė
    "LT-51",  # Telšiai
    "LT-52",  # Trakai
    "LT-53",  # Ukmergė
    "LT-54",  # Utena
    "LT-55",  # Varėna
    "LT-56",  # Vilkaviškis
    "LT-57",  # Vilniaus miestas
    "LT-58",  # Vilnius
    "LT-59",  # Visaginas
    "LT-60",  # Zarasai
    "LT-AL",  # Alytaus apskritis
    "LT-KL",  # Klaipėdos apskritis
    "LT-KU",  # Kauno apskritis
    "LT-MR",  # Marijampolės apskritis
    "LT-PN",  # Panevėžio apskritis
    "LT-SA",  # Šiaulių apskritis
    "LT-TA",  # Tauragės apskritis
    "LT-TE",  # Telšių apskritis
    "LT-UT",  # Utenos apskritis
    "LT-VL",  # Vilniaus apskritis
    # Grand Duchy of Luxembourg
    "LU-CA",  # Capellen
    "LU-CL",  # Clervaux
    "LU-DI",  # Diekirch
    "LU-EC",  # Echternach
    "LU-ES",  # Esch-sur-Alzette
    "LU-GR",  # Grevenmacher
    "LU-LU",  # Luxembourg
    "LU-ME",  # Mersch
    "LU-RD",  # Redange
    "LU-RM",  # Remich
    "LU-VD",  # Vianden
    "LU-WI",  # Wiltz
    # Republic of Latvia
    "LV-002",  # Aizkraukles novads
    "LV-007",  # Alūksnes novads
    "LV-011",  # Ādažu novads
    "LV-015",  # Balvu novads
    "LV-016",  # Bauskas novads
    "LV-022",  # Cēsu novads
    "LV-026",  # Dobeles novads
    "LV-033",  # Gulbenes novads
    "LV-041",  # Jelgavas novads
    "LV-042",  # Jēkabpils novads
    "LV-047",  # Krāslavas novads
    "LV-050",  # Kuldīgas novads
    "LV-052",  # Ķekavas novads
    "LV-054",  # Limbažu novads
    "LV-056",  # Līvānu novads
    "LV-058",  # Ludzas novads
    "LV-059",  # Madonas novads
    "LV-062",  # Mārupes novads
    "LV-067",  # Ogres novads
    "LV-068",  # Olaines novads
    "LV-073",  # Preiļu novads
    "LV-077",  # Rēzeknes novads
    "LV-080",  # Ropažu novads
    "LV-087",  # Salaspils novads
    "LV-088",  # Saldus novads
    "LV-089",  # Saulkrastu novads
    "LV-091",  # Siguldas novads
    "LV-094",  # Smiltenes novads
    "LV-097",  # Talsu novads
    "LV-099",  # Tukuma novads
    "LV-101",  # Valkas novads
    "LV-102",  # Varakļānu novads
    "LV-106",  # Ventspils novads
    "LV-111",  # Augšdaugavas novads
    "LV-112",  # Dienvidkurzemes Novads
    "LV-113",  # Valmieras Novads
    "LV-DGV",  # Daugavpils
    "LV-JEL",  # Jelgava
    "LV-JUR",  # Jūrmala
    "LV-LPX",  # Liepāja
    "LV-REZ",  # Rēzekne
    "LV-RIX",  # Rīga
    "LV-VEN",  # Ventspils
    # Libya
    "LY-BA",  # Banghāzī
    "LY-BU",  # Al Buţnān
    "LY-DR",  # Darnah
    "LY-GT",  # Ghāt
    "LY-JA",  # Al Jabal al Akhḑar
    "LY-JG",  # Al Jabal al Gharbī
    "LY-JI",  # Al Jafārah
    "LY-JU",  # Al Jufrah
    "LY-KF",  # Al Kufrah
    "LY-MB",  # Al Marqab
    "LY-MI",  # Mişrātah
    "LY-MJ",  # Al Marj
    "LY-MQ",  # Murzuq
    "LY-NL",  # Nālūt
    "LY-NQ",  # An Nuqāţ al Khams
    "LY-SB",  # Sabhā
    "LY-SR",  # Surt
    "LY-TB",  # Ţarābulus
    "LY-WA",  # Al Wāḩāt
    "LY-WD",  # Wādī al Ḩayāt
    "LY-WS",  # Wādī ash Shāţi’
    "LY-ZA",  # Az Zāwiyah
    # Kingdom of Morocco
    "MA-01",  # Tanger-Tétouan-Al Hoceïma
    "MA-02",  # L'Oriental
    "MA-03",  # Fès-Meknès
    "MA-04",  # Rabat-Salé-Kénitra
    "MA-05",  # Béni Mellal-Khénifra
    "MA-06",  # Casablanca-Settat
    "MA-07",  # Marrakech-Safi
    "MA-08",  # Drâa-Tafilalet
    "MA-09",  # Souss-Massa
    "MA-10",  # Guelmim-Oued Noun (EH-partial)
    "MA-11",  # Laâyoune-Sakia El Hamra (EH-partial)
    "MA-12",  # Dakhla-Oued Ed-Dahab (EH)
    "MA-AGD",  # Agadir-Ida-Ou-Tanane
    "MA-AOU",  # Aousserd (EH)
    "MA-ASZ",  # Assa-Zag (EH-partial)
    "MA-AZI",  # Azilal
    "MA-BEM",  # Béni Mellal
    "MA-BER",  # Berkane
    "MA-BES",  # Benslimane
    "MA-BOD",  # Boujdour (EH)
    "MA-BOM",  # Boulemane
    "MA-BRR",  # Berrechid
    "MA-CAS",  # Casablanca
    "MA-CHE",  # Chefchaouen
    "MA-CHI",  # Chichaoua
    "MA-CHT",  # Chtouka-Ait Baha
    "MA-DRI",  # Driouch
    "MA-ERR",  # Errachidia
    "MA-ESI",  # Essaouira
    "MA-ESM",  # Es-Semara (EH-partial)
    "MA-FAH",  # Fahs-Anjra
    "MA-FES",  # Fès
    "MA-FIG",  # Figuig
    "MA-FQH",  # Fquih Ben Salah
    "MA-GUE",  # Guelmim
    "MA-GUF",  # Guercif
    "MA-HAJ",  # El Hajeb
    "MA-HAO",  # Al Haouz
    "MA-HOC",  # Al Hoceïma
    "MA-IFR",  # Ifrane
    "MA-INE",  # Inezgane-Ait Melloul
    "MA-JDI",  # El Jadida
    "MA-JRA",  # Jerada
    "MA-KEN",  # Kénitra
    "MA-KES",  # El Kelâa des Sraghna
    "MA-KHE",  # Khémisset
    "MA-KHN",  # Khénifra
    "MA-KHO",  # Khouribga
    "MA-LAA",  # Laâyoune (EH)
    "MA-LAR",  # Larache
    "MA-MAR",  # Marrakech
    "MA-MDF",  # M’diq-Fnideq
    "MA-MED",  # Médiouna
    "MA-MEK",  # Meknès
    "MA-MID",  # Midelt
    "MA-MOH",  # Mohammadia
    "MA-MOU",  # Moulay Yacoub
    "MA-NAD",  # Nador
    "MA-NOU",  # Nouaceur
    "MA-OUA",  # Ouarzazate
    "MA-OUD",  # Oued Ed-Dahab (EH)
    "MA-OUJ",  # Oujda-Angad
    "MA-OUZ",  # Ouezzane
    "MA-RAB",  # Rabat
    "MA-REH",  # Rehamna
    "MA-SAF",  # Safi
    "MA-SAL",  # Salé
    "MA-SEF",  # Sefrou
    "MA-SET",  # Settat
    "MA-SIB",  # Sidi Bennour
    "MA-SIF",  # Sidi Ifni
    "MA-SIK",  # Sidi Kacem
    "MA-SIL",  # Sidi Slimane
    "MA-SKH",  # Skhirate-Témara
    "MA-TAF",  # Tarfaya (EH-partial)
    "MA-TAI",  # Taourirt
    "MA-TAO",  # Taounate
    "MA-TAR",  # Taroudannt
    "MA-TAT",  # Tata
    "MA-TAZ",  # Taza
    "MA-TET",  # Tétouan
    "MA-TIN",  # Tinghir
    "MA-TIZ",  # Tiznit
    "MA-TNG",  # Tanger-Assilah
    "MA-TNT",  # Tan-Tan (EH-partial)
    "MA-YUS",  # Youssoufia
    "MA-ZAG",  # Zagora
    # Principality of Monaco
    "MC-CL",  # La Colle
    "MC-CO",  # La Condamine
    "MC-FO",  # Fontvieille
    "MC-GA",  # La Gare
    "MC-JE",  # Jardin Exotique
    "MC-LA",  # Larvotto
    "MC-MA",  # Malbousquet
    "MC-MC",  # Monte-Carlo
    "MC-MG",  # Moneghetti
    "MC-MO",  # Monaco-Ville
    "MC-MU",  # Moulins
    "MC-PH",  # Port-Hercule
    "MC-SD",  # Sainte-Dévote
    "MC-SO",  # La Source
    "MC-SP",  # Spélugues
    "MC-SR",  # Saint-Roman
    "MC-VR",  # Vallon de la Rousse
    # Republic of Moldova
    "MD-AN",  # Anenii Noi
    "MD-BA",  # Bălți
    "MD-BD",  # Bender [Tighina]
    "MD-BR",  # Briceni
    "MD-BS",  # Basarabeasca
    "MD-CA",  # Cahul
    "MD-CL",  # Călărași
    "MD-CM",  # Cimișlia
    "MD-CR",  # Criuleni
    "MD-CS",  # Căușeni
    "MD-CT",  # Cantemir
    "MD-CU",  # Chișinău
    "MD-DO",  # Dondușeni
    "MD-DR",  # Drochia
    "MD-DU",  # Dubăsari
    "MD-ED",  # Edineț
    "MD-FA",  # Fălești
    "MD-FL",  # Florești
    "MD-GA",  # Găgăuzia, Unitatea teritorială autonomă (UTAG)
    "MD-GL",  # Glodeni
    "MD-HI",  # Hîncești
    "MD-IA",  # Ialoveni
    "MD-LE",  # Leova
    "MD-NI",  # Nisporeni
    "MD-OC",  # Ocnița
    "MD-OR",  # Orhei
    "MD-RE",  # Rezina
    "MD-RI",  # Rîșcani
    "MD-SD",  # Șoldănești
    "MD-SI",  # Sîngerei
    "MD-SN",  # Stînga Nistrului, unitatea teritorială din
    "MD-SO",  # Soroca
    "MD-ST",  # Strășeni
    "MD-SV",  # Ștefan Vodă
    "MD-TA",  # Taraclia
    "MD-TE",  # Telenești
    "MD-UN",  # Ungheni
    # Montenegro
    "ME-01",  # Andrijevica
    "ME-02",  # Bar
    "ME-03",  # Berane
    "ME-04",  # Bijelo Polje
    "ME-05",  # Budva
    "ME-06",  # Cetinje
    "ME-07",  # Danilovgrad
    "ME-08",  # Herceg-Novi
    "ME-09",  # Kolašin
    "ME-10",  # Kotor
    "ME-11",  # Mojkovac
    "ME-12",  # Nikšić
    "ME-13",  # Plav
    "ME-14",  # Pljevlja
    "ME-15",  # Plužine
    "ME-16",  # Podgorica
    "ME-17",  # Rožaje
    "ME-18",  # Šavnik
    "ME-19",  # Tivat
    "ME-20",  # Ulcinj
    "ME-21",  # Žabljak
    "ME-22",  # Gusinje
    "ME-23",  # Petnjica
    "ME-24",  # Tuzi
    "ME-25",  # Zeta
    # Saint Martin (French part)
    # (no subdivisions)
    # Republic of Madagascar
    "MG-A",  # Toamasina
    "MG-D",  # Antsiranana
    "MG-F",  # Fianarantsoa
    "MG-M",  # Mahajanga
    "MG-T",  # Antananarivo
    "MG-U",  # Toliara
    # Republic of the Marshall Islands
    "MH-ALK",  # Ailuk
    "MH-ALL",  # Ailinglaplap
    "MH-ARN",  # Arno
    "MH-AUR",  # Aur
    "MH-EBO",  # Ebon
    "MH-ENI",  # Enewetak & Ujelang
    "MH-JAB",  # Jabat
    "MH-JAL",  # Jaluit
    "MH-KIL",  # Bikini & Kili
    "MH-KWA",  # Kwajalein
    "MH-L",  # Ralik chain
    "MH-LAE",  # Lae
    "MH-LIB",  # Lib
    "MH-LIK",  # Likiep
    "MH-MAJ",  # Majuro
    "MH-MAL",  # Maloelap
    "MH-MEJ",  # Mejit
    "MH-MIL",  # Mili
    "MH-NMK",  # Namdrik
    "MH-NMU",  # Namu
    "MH-RON",  # Rongelap
    "MH-T",  # Ratak chain
    "MH-UJA",  # Ujae
    "MH-UTI",  # Utrik
    "MH-WTH",  # Wotho
    "MH-WTJ",  # Wotje
    # Republic of North Macedonia
    "MK-101",  # Veles
    "MK-102",  # Gradsko
    "MK-103",  # Demir Kapija
    "MK-104",  # Kavadarci
    "MK-105",  # Lozovo
    "MK-106",  # Negotino
    "MK-107",  # Rosoman
    "MK-108",  # Sveti Nikole
    "MK-109",  # Čaška
    "MK-201",  # Berovo
    "MK-202",  # Vinica
    "MK-203",  # Delčevo
    "MK-204",  # Zrnovci
    "MK-205",  # Karbinci
    "MK-206",  # Kočani
    "MK-207",  # Makedonska Kamenica
    "MK-208",  # Pehčevo
    "MK-209",  # Probištip
    "MK-210",  # Češinovo-Obleševo
    "MK-211",  # Štip
    "MK-301",  # Vevčani
    "MK-303",  # Debar
    "MK-304",  # Debrca
    "MK-307",  # Kičevo
    "MK-308",  # Makedonski Brod
    "MK-310",  # Ohrid
    "MK-311",  # Plasnica
    "MK-312",  # Struga
    "MK-313",  # Centar Župa
    "MK-401",  # Bogdanci
    "MK-402",  # Bosilovo
    "MK-403",  # Valandovo
    "MK-404",  # Vasilevo
    "MK-405",  # Gevgelija
    "MK-406",  # Dojran
    "MK-407",  # Konče
    "MK-408",  # Novo Selo
    "MK-409",  # Radoviš
    "MK-410",  # Strumica
    "MK-501",  # Bitola
    "MK-502",  # Demir Hisar
    "MK-503",  # Dolneni
    "MK-504",  # Krivogaštani
    "MK-505",  # Kruševo
    "MK-506",  # Mogila
    "MK-507",  # Novaci
    "MK-508",  # Prilep
    "MK-509",  # Resen
    "MK-601",  # Bogovinje
    "MK-602",  # Brvenica
    "MK-603",  # Vrapčište
    "MK-604",  # Gostivar
    "MK-605",  # Želino
    "MK-606",  # Jegunovce
    "MK-607",  # Mavrovo i Rostuše
    "MK-608",  # Tearce
    "MK-609",  # Tetovo
    "MK-701",  # Kratovo
    "MK-702",  # Kriva Palanka
    "MK-703",  # Kumanovo
    "MK-704",  # Lipkovo
    "MK-705",  # Rankovce
    "MK-706",  # Staro Nagoričane
    "MK-801",  # Aerodrom †
    "MK-802",  # Aračinovo
    "MK-803",  # Butel †
    "MK-804",  # Gazi Baba †
    "MK-805",  # Gjorče Petrov †
    "MK-806",  # Zelenikovo
    "MK-807",  # Ilinden
    "MK-808",  # Karpoš †
    "MK-809",  # Kisela Voda †
    "MK-810",  # Petrovec
    "MK-811",  # Saraj †
    "MK-812",  # Sopište
    "MK-813",  # Studeničani
    "MK-814",  # Centar †
    "MK-815",  # Čair †
    "MK-816",  # Čučer-Sandevo
    "MK-817",  # Šuto Orizari †
    # Republic of Mali
    "ML-1",  # Kayes
    "ML-10",  # Taoudénit
    "ML-2",  # Koulikoro
    "ML-3",  # Sikasso
    "ML-4",  # Ségou
    "ML-5",  # Mopti
    "ML-6",  # Tombouctou
    "ML-7",  # Gao
    "ML-8",  # Kidal
    "ML-9",  # Ménaka
    "ML-BKO",  # Bamako
    # Republic of Myanmar
    "MM-01",  # Sagaing
    "MM-02",  # Bago
    "MM-03",  # Magway
    "MM-04",  # Mandalay
    "MM-05",  # Tanintharyi
    "MM-06",  # Yangon
    "MM-07",  # Ayeyarwady
    "MM-11",  # Kachin
    "MM-12",  # Kayah
    "MM-13",  # Kayin
    "MM-14",  # Chin
    "MM-15",  # Mon
    "MM-16",  # Rakhine
    "MM-17",  # Shan
    "MM-18",  # Nay Pyi Taw
    # Mongolia
    "MN-035",  # Orhon
    "MN-037",  # Darhan uul
    "MN-039",  # Hentiy
    "MN-041",  # Hövsgöl
    "MN-043",  # Hovd
    "MN-046",  # Uvs
    "MN-047",  # Töv
    "MN-049",  # Selenge
    "MN-051",  # Sühbaatar
    "MN-053",  # Ömnögovĭ
    "MN-055",  # Övörhangay
    "MN-057",  # Dzavhan
    "MN-059",  # Dundgovĭ
    "MN-061",  # Dornod
    "MN-063",  # Dornogovĭ
    "MN-064",  # Govĭ-Sümber
    "MN-065",  # Govĭ-Altay
    "MN-067",  # Bulgan
    "MN-069",  # Bayanhongor
    "MN-071",  # Bayan-Ölgiy
    "MN-073",  # Arhangay
    "MN-1",  # Ulaanbaatar
    # Macao Special Administrative Region of China
    # (no subdivisions)
    # Commonwealth of the Northern Mariana Islands
    # (no subdivisions)
    # Martinique
    # (no subdivisions)
    # Islamic Republic of Mauritania
    "MR-01",  # Hodh ech Chargui
    "MR-02",  # Hodh el Gharbi
    "MR-03",  # Assaba
    "MR-04",  # Gorgol
    "MR-05",  # Brakna
    "MR-06",  # Trarza
    "MR-07",  # Adrar
    "MR-08",  # Dakhlet Nouâdhibou
    "MR-09",  # Tagant
    "MR-10",  # Guidimaka
    "MR-11",  # Tiris Zemmour
    "MR-12",  # Inchiri
    "MR-13",  # Nouakchott Ouest
    "MR-14",  # Nouakchott Nord
    "MR-15",  # Nouakchott Sud
    # Montserrat
    # (no subdivisions)
    # Republic of Malta
    "MT-01",  # Attard
    "MT-02",  # Balzan
    "MT-03",  # Birgu
    "MT-04",  # Birkirkara
    "MT-05",  # Birżebbuġa
    "MT-06",  # Bormla
    "MT-07",  # Dingli
    "MT-08",  # Fgura
    "MT-09",  # Floriana
    "MT-10",  # Fontana
    "MT-11",  # Gudja
    "MT-12",  # Gżira
    "MT-13",  # Għajnsielem
    "MT-14",  # Għarb
    "MT-15",  # Għargħur
    "MT-16",  # Għasri
    "MT-17",  # Għaxaq
    "MT-18",  # Ħamrun
    "MT-19",  # Iklin
    "MT-20",  # Isla
    "MT-21",  # Kalkara
    "MT-22",  # Kerċem
    "MT-23",  # Kirkop
    "MT-24",  # Lija
    "MT-25",  # Luqa
    "MT-26",  # Marsa
    "MT-27",  # Marsaskala
    "MT-28",  # Marsaxlokk
    "MT-29",  # Mdina
    "MT-30",  # Mellieħa
    "MT-31",  # Mġarr
    "MT-32",  # Mosta
    "MT-33",  # Mqabba
    "MT-34",  # Msida
    "MT-35",  # Mtarfa
    "MT-36",  # Munxar
    "MT-37",  # Nadur
    "MT-38",  # Naxxar
    "MT-39",  # Paola
    "MT-40",  # Pembroke
    "MT-41",  # Pietà
    "MT-42",  # Qala
    "MT-43",  # Qormi
    "MT-44",  # Qrendi
    "MT-45",  # Rabat Gozo
    "MT-46",  # Rabat Malta
    "MT-47",  # Safi
    "MT-48",  # Saint Julian's
    "MT-49",  # Saint John
    "MT-50",  # Saint Lawrence
    "MT-51",  # Saint Paul's Bay
    "MT-52",  # Sannat
    "MT-53",  # Saint Lucia's
    "MT-54",  # Santa Venera
    "MT-55",  # Siġġiewi
    "MT-56",  # Sliema
    "MT-57",  # Swieqi
    "MT-58",  # Ta' Xbiex
    "MT-59",  # Tarxien
    "MT-60",  # Valletta
    "MT-61",  # Xagħra
    "MT-62",  # Xewkija
    "MT-63",  # Xgħajra
    "MT-64",  # Żabbar
    "MT-65",  # Żebbuġ Gozo
    "MT-66",  # Żebbuġ Malta
    "MT-67",  # Żejtun
    "MT-68",  # Żurrieq
    # Republic of Mauritius
    "MU-AG",  # Agalega Islands
    "MU-BL",  # Black River
    "MU-CC",  # Cargados Carajos Shoals
    "MU-FL",  # Flacq
    "MU-GP",  # Grand Port
    "MU-MO",  # Moka
    "MU-PA",  # Pamplemousses
    "MU-PL",  # Port Louis
    "MU-PW",  # Plaines Wilhems
    "MU-RO",  # Rodrigues Island
    "MU-RR",  # Rivière du Rempart
    "MU-SA",  # Savanne
    # Republic of Maldives
    "MV-00",  # South Ari Atoll
    "MV-01",  # Addu City
    "MV-02",  # North Ari Atoll
    "MV-03",  # Faadhippolhu
    "MV-04",  # Felidhu Atoll
    "MV-05",  # Hahdhunmathi
    "MV-07",  # North Thiladhunmathi
    "MV-08",  # Kolhumadulu
    "MV-12",  # Mulaku Atoll
    "MV-13",  # North Maalhosmadulu
    "MV-14",  # North Nilandhe Atoll
    "MV-17",  # South Nilandhe Atoll
    "MV-20",  # South Maalhosmadulu
    "MV-23",  # South Thiladhunmathi
    "MV-24",  # North Miladhunmadulu
    "MV-25",  # South Miladhunmadulu
    "MV-26",  # Male Atoll
    "MV-27",  # North Huvadhu Atoll
    "MV-28",  # South Huvadhu Atoll
    "MV-29",  # Fuvammulah
    "MV-MLE",  # Male
    # Republic of Malawi
    "MW-BA",  # Balaka
    "MW-BL",  # Blantyre
    "MW-C",  # Central Region
    "MW-CK",  # Chikwawa
    "MW-CR",  # Chiradzulu
    "MW-CT",  # Chitipa
    "MW-DE",  # Dedza
    "MW-DO",  # Dowa
    "MW-KR",  # Karonga
    "MW-KS",  # Kasungu
    "MW-LI",  # Lilongwe
    "MW-LK",  # Likoma
    "MW-MC",  # Mchinji
    "MW-MG",  # Mangochi
    "MW-MH",  # Machinga
    "MW-MU",  # Mulanje
    "MW-MW",  # Mwanza
    "MW-MZ",  # Mzimba
    "MW-N",  # Northern Region
    "MW-NB",  # Nkhata Bay
    "MW-NE",  # Neno
    "MW-NI",  # Ntchisi
    "MW-NK",  # Nkhotakota
    "MW-NS",  # Nsanje
    "MW-NU",  # Ntcheu
    "MW-PH",  # Phalombe
    "MW-RU",  # Rumphi
    "MW-S",  # Southern Region
    "MW-SA",  # Salima
    "MW-TH",  # Thyolo
    "MW-ZO",  # Zomba
    # United Mexican States
    "MX-AGU",  # Aguascalientes
    "MX-BCN",  # Baja California
    "MX-BCS",  # Baja California Sur
    "MX-CAM",  # Campeche
    "MX-CHH",  # Chihuahua
    "MX-CHP",  # Chiapas
    "MX-CMX",  # Ciudad de México
    "MX-COA",  # Coahuila de Zaragoza
    "MX-COL",  # Colima
    "MX-DUR",  # Durango
    "MX-GRO",  # Guerrero
    "MX-GUA",  # Guanajuato
    "MX-HID",  # Hidalgo
    "MX-JAL",  # Jalisco
    "MX-MEX",  # México
    "MX-MIC",  # Michoacán de Ocampo
    "MX-MOR",  # Morelos
    "MX-NAY",  # Nayarit
    "MX-NLE",  # Nuevo León
    "MX-OAX",  # Oaxaca
    "MX-PUE",  # Puebla
    "MX-QUE",  # Querétaro
    "MX-ROO",  # Quintana Roo
    "MX-SIN",  # Sinaloa
    "MX-SLP",  # San Luis Potosí
    "MX-SON",  # Sonora
    "MX-TAB",  # Tabasco
    "MX-TAM",  # Tamaulipas
    "MX-TLA",  # Tlaxcala
    "MX-VER",  # Veracruz de Ignacio de la Llave
    "MX-YUC",  # Yucatán
    "MX-ZAC",  # Zacatecas
    # Malaysia
    "MY-01",  # Johor
    "MY-02",  # Kedah
    "MY-03",  # Kelantan
    "MY-04",  # Melaka
    "MY-05",  # Negeri Sembilan
    "MY-06",  # Pahang
    "MY-07",  # Pulau Pinang
    "MY-08",  # Perak
    "MY-09",  # Perlis
    "MY-10",  # Selangor
    "MY-11",  # Terengganu
    "MY-12",  # Sabah
    "MY-13",  # Sarawak
    "MY-14",  # Wilayah Persekutuan Kuala Lumpur
    "MY-15",  # Wilayah Persekutuan Labuan
    "MY-16",  # Wilayah Persekutuan Putrajaya
    # Republic of Mozambique
    "MZ-A",  # Niassa
    "MZ-B",  # Manica
    "MZ-G",  # Gaza
    "MZ-I",  # Inhambane
    "MZ-L",  # Maputo
    "MZ-MPM",  # Maputo
    "MZ-N",  # Nampula
    "MZ-P",  # Cabo Delgado
    "MZ-Q",  # Zambézia
    "MZ-S",  # Sofala
    "MZ-T",  # Tete
    # Republic of Namibia
    "NA-CA",  # Zambezi
    "NA-ER",  # Erongo
    "NA-HA",  # Hardap
    "NA-KA",  # //Karas
    "NA-KE",  # Kavango East
    "NA-KH",  # Khomas
    "NA-KU",  # Kunene
    "NA-KW",  # Kavango West
    "NA-OD",  # Otjozondjupa
    "NA-OH",  # Omaheke
    "NA-ON",  # Oshana
    "NA-OS",  # Omusati
    "NA-OT",  # Oshikoto
    "NA-OW",  # Ohangwena
    # New Caledonia
    # (no subdivisions)
    # Republic of the Niger
    "NE-1",  # Agadez
    "NE-2",  # Diffa
    "NE-3",  # Dosso
    "NE-4",  # Maradi
    "NE-5",  # Tahoua
    "NE-6",  # Tillabéri
    "NE-7",  # Zinder
    "NE-8",  # Niamey
    # Norfolk Island
    # (no subdivisions)
    # Federal Republic of Nigeria
    "NG-AB",  # Abia
    "NG-AD",  # Adamawa
    "NG-AK",  # Akwa Ibom
    "NG-AN",  # Anambra
    "NG-BA",  # Bauchi
    "NG-BE",  # Benue
    "NG-BO",  # Borno
    "NG-BY",  # Bayelsa
    "NG-CR",  # Cross River
    "NG-DE",  # Delta
    "NG-EB",  # Ebonyi
    "NG-ED",  # Edo
    "NG-EK",  # Ekiti
    "NG-EN",  # Enugu
    "NG-FC",  # Abuja Federal Capital Territory
    "NG-GO",  # Gombe
    "NG-IM",  # Imo
    "NG-JI",  # Jigawa
    "NG-KD",  # Kaduna
    "NG-KE",  # Kebbi
    "NG-KN",  # Kano
    "NG-KO",  # Kogi
    "NG-KT",  # Katsina
    "NG-KW",  # Kwara
    "NG-LA",  # Lagos
    "NG-NA",  # Nasarawa
    "NG-NI",  # Niger
    "NG-OG",  # Ogun
    "NG-ON",  # Ondo
    "NG-OS",  # Osun
    "NG-OY",  # Oyo
    "NG-PL",  # Plateau
    "NG-RI",  # Rivers
    "NG-SO",  # Sokoto
    "NG-TA",  # Taraba
    "NG-YO",  # Yobe
    "NG-ZA",  # Zamfara
    # Republic of Nicaragua
    "NI-AN",  # Costa Caribe Norte
    "NI-AS",  # Costa Caribe Sur
    "NI-BO",  # Boaco
    "NI-CA",  # Carazo
    "NI-CI",  # Chinandega
    "NI-CO",  # Chontales
    "NI-ES",  # Estelí
    "NI-GR",  # Granada
    "NI-JI",  # Jinotega
    "NI-LE",  # León
    "NI-MD",  # Madriz
    "NI-MN",  # Managua
    "NI-MS",  # Masaya
    "NI-MT",  # Matagalpa
    "NI-NS",  # Nueva Segovia
    "NI-RI",  # Rivas
    "NI-SJ",  # Río San Juan
    # Kingdom of the Netherlands
    "NL-AW",  # Aruba
    "NL-BQ1",  # Bonaire
    "NL-BQ2",  # Saba
    "NL-BQ3",  # Sint Eustatius
    "NL-CW",  # Curaçao
    "NL-DR",  # Drenthe
    "NL-FL",  # Flevoland
    "NL-FR",  # Fryslân
    "NL-GE",  # Gelderland
    "NL-GR",  # Groningen
    "NL-LI",  # Limburg
    "NL-NB",  # Noord-Brabant
    "NL-NH",  # Noord-Holland
    "NL-OV",  # Overijssel
    "NL-SX",  # Sint Maarten
    "NL-UT",  # Utrecht
    "NL-ZE",  # Zeeland
    "NL-ZH",  # Zuid-Holland
    # Kingdom of Norway
    "NO-03",  # Oslo
    "NO-11",  # Rogaland
    "NO-15",  # Møre og Romsdal
    "NO-18",  # Nordland
    "NO-21",  # Svalbard (Arctic Region)
    "NO-22",  # Jan Mayen (Arctic Region)
    "NO-30",  # Viken
    "NO-34",  # Innlandet
    "NO-38",  # Vestfold og Telemark
    "NO-42",  # Agder
    "NO-46",  # Vestland
    "NO-50",  # Trööndelage
    "NO-54",  # Romssa ja Finnmárkku
    # Federal Democratic Republic of Nepal
    "NP-P1",  # Koshi
    "NP-P2",  # Madhesh
    "NP-P3",  # Bagmati
    "NP-P4",  # Gandaki
    "NP-P5",  # Lumbini
    "NP-P6",  # Karnali
    "NP-P7",  # Sudurpashchim
    # Republic of Nauru
    "NR-01",  # Aiwo
    "NR-02",  # Anabar
    "NR-03",  # Anetan
    "NR-04",  # Anibare
    "NR-05",  # Baitsi
    "NR-06",  # Boe
    "NR-07",  # Buada
    "NR-08",  # Denigomodu
    "NR-09",  # Ewa
    "NR-10",  # Ijuw
    "NR-11",  # Meneng
    "NR-12",  # Nibok
    "NR-13",  # Uaboe
    "NR-14",  # Yaren
    # Niue
    # (no subdivisions)
    # New Zealand
    "NZ-AUK",  # Auckland
    "NZ-BOP",  # Bay of Plenty
    "NZ-CAN",  # Canterbury
    "NZ-CIT",  # Chatham Islands Territory
    "NZ-GIS",  # Gisborne
    "NZ-HKB",  # Hawke's Bay
    "NZ-MBH",  # Marlborough
    "NZ-MWT",  # Manawatū-Whanganui
    "NZ-NSN",  # Nelson
    "NZ-NTL",  # Northland
    "NZ-OTA",  # Otago
    "NZ-STL",  # Southland
    "NZ-TAS",  # Tasman
    "NZ-TKI",  # Taranaki
    "NZ-WGN",  # Greater Wellington
    "NZ-WKO",  # Waikato
    "NZ-WTC",  # West Coast
    # Sultanate of Oman
    "OM-BJ",  # Janūb al Bāţinah
    "OM-BS",  # Shamāl al Bāţinah
    "OM-BU",  # Al Buraymī
    "OM-DA",  # Ad Dākhilīyah
    "OM-MA",  # Masqaţ
    "OM-MU",  # Musandam
    "OM-SJ",  # Janūb ash Sharqīyah
    "OM-SS",  # Shamāl ash Sharqīyah
    "OM-WU",  # Al Wusţá
    "OM-ZA",  # Az̧ Z̧āhirah
    "OM-ZU",  # Z̧ufār
    # Republic of Panama
    "PA-1",  # Bocas del Toro
    "PA-10",  # Panamá Oeste
    "PA-2",  # Coclé
    "PA-3",  # Colón
    "PA-4",  # Chiriquí
    "PA-5",  # Darién
    "PA-6",  # Herrera
    "PA-7",  # Los Santos
    "PA-8",  # Panamá
    "PA-9",  # Veraguas
    "PA-EM",  # Emberá
    "PA-KY",  # Guna Yala
    "PA-NB",  # Ngäbe-Buglé
    "PA-NT",  # Naso Tjër Di
    # Republic of Peru
    "PE-AMA",  # Amarumayu
    "PE-ANC",  # Ancash
    "PE-APU",  # Apurimaq
    "PE-ARE",  # Arequipa
    "PE-AYA",  # Ayacucho
    "PE-CAJ",  # Cajamarca
    "PE-CAL",  # El Callao
    "PE-CUS",  # Cusco
    "PE-HUC",  # Huánuco
    "PE-HUV",  # Huancavelica
    "PE-ICA",  # Ica
    "PE-JUN",  # Hunin
    "PE-LAL",  # La Libertad
    "PE-LAM",  # Lambayeque
    "PE-LIM",  # Lima
    "PE-LMA",  # Lima hatun llaqta
    "PE-LOR",  # Loreto
    "PE-MDD",  # Madre de Dios
    "PE-MOQ",  # Moquegua
    "PE-PAS",  # Pasco
    "PE-PIU",  # Piura
    "PE-PUN",  # Puno
    "PE-SAM",  # San Martin
    "PE-TAC",  # Tacna
    "PE-TUM",  # Tumbes
    "PE-UCA",  # Ucayali
    # French Polynesia
    # (no subdivisions)
    # Independent State of Papua New Guinea
    "PG-CPK",  # Chimbu
    "PG-CPM",  # Central
    "PG-EBR",  # East New Britain
    "PG-EHG",  # Eastern Highlands
    "PG-EPW",  # Enga
    "PG-ESW",  # East Sepik
    "PG-GPK",  # Gulf
    "PG-HLA",  # Hela
    "PG-JWK",  # Jiwaka
    "PG-MBA",  # Milne Bay
    "PG-MPL",  # Morobe
    "PG-MPM",  # Madang
    "PG-MRL",  # Manus
    "PG-NCD",  # National Capital District (Port Moresby)
    "PG-NIK",  # New Ireland
    "PG-NPP",  # Northern
    "PG-NSB",  # Bougainville
    "PG-SAN",  # West Sepik
    "PG-SHM",  # Southern Highlands
    "PG-WBK",  # West New Britain
    "PG-WHM",  # Western Highlands
    "PG-WPD",  # Western
    # Republic of the Philippines
    "PH-00",  # National Capital Region
    "PH-01",  # Ilocos (Region I)
    "PH-02",  # Cagayan Valley (Region II)
    "PH-03",  # Central Luzon (Region III)
    "PH-05",  # Bicol (Region V)
    "PH-06",  # Western Visayas (Region VI)
    "PH-07",  # Central Visayas (Region VII)
    "PH-08",  # Eastern Visayas (Region VIII)
    "PH-09",  # Zamboanga Peninsula (Region IX)
    "PH-10",  # Northern Mindanao (Region X)
    "PH-11",  # Davao (Region XI)
    "PH-12",  # Soccsksargen (Region XII)
    "PH-13",  # Caraga (Region XIII)
    "PH-14",  # Autonomous Region in Muslim Mindanao (ARMM)
    "PH-15",  # Cordillera Administrative Region (CAR)
    "PH-40",  # Calabarzon (Region IV-A)
    "PH-41",  # Mimaropa (Region IV-B)
    "PH-ABR",  # Abra
    "PH-AGN",  # Agusan del Norte
    "PH-AGS",  # Agusan del Sur
    "PH-AKL",  # Aklan
    "PH-ALB",  # Albay
    "PH-ANT",  # Antique
    "PH-APA",  # Apayao
    "PH-AUR",  # Aurora
    "PH-BAN",  # Bataan
    "PH-BAS",  # Basilan
    "PH-BEN",  # Benguet
    "PH-BIL",  # Biliran
    "PH-BOH",  # Bohol
    "PH-BTG",  # Batangas
    "PH-BTN",  # Batanes
    "PH-BUK",  # Bukidnon
    "PH-BUL",  # Bulacan
    "PH-CAG",  # Cagayan
    "PH-CAM",  # Camiguin
    "PH-CAN",  # Camarines Norte
    "PH-CAP",  # Capiz
    "PH-CAS",  # Camarines Sur
    "PH-CAT",  # Catanduanes
    "PH-CAV",  # Cavite
    "PH-CEB",  # Cebu
    "PH-COM",  # Davao de Oro
    "PH-DAO",  # Davao Oriental
    "PH-DAS",  # Davao del Sur
    "PH-DAV",  # Davao del Norte
    "PH-DIN",  # Dinagat Islands
    "PH-DVO",  # Davao Occidental
    "PH-EAS",  # Eastern Samar
    "PH-GUI",  # Guimaras
    "PH-IFU",  # Ifugao
    "PH-ILI",  # Iloilo
    "PH-ILN",  # Ilocos Norte
    "PH-ILS",  # Ilocos Sur
    "PH-ISA",  # Isabela
    "PH-KAL",  # Kalinga
    "PH-LAG",  # Laguna
    "PH-LAN",  # Lanao del Norte
    "PH-LAS",  # Lanao del Sur
    "PH-LEY",  # Leyte
    "PH-LUN",  # La Union
    "PH-MAD",  # Marinduque
    "PH-MAS",  # Masbate
    "PH-MDC",  # Mindoro Occidental
    "PH-MDR",  # Mindoro Oriental
    "PH-MGN",  # Maguindanao del Norte
    "PH-MGS",  # Maguindanao del Sur
    "PH-MOU",  # Mountain Province
    "PH-MSC",  # Misamis Occidental
    "PH-MSR",  # Misamis Oriental
    "PH-NCO",  # Cotabato
    "PH-NEC",  # Negros Occidental
    "PH-NER",  # Negros Oriental
    "PH-NSA",  # Northern Samar
    "PH-NUE",  # Nueva Ecija
    "PH-NUV",  # Nueva Vizcaya
    "PH-PAM",  # Pampanga
    "PH-PAN",  # Pangasinan
    "PH-PLW",  # Palawan
    "PH-QUE",  # Quezon
    "PH-QUI",  # Quirino
    "PH-RIZ",  # Rizal
    "PH-ROM",  # Romblon
    "PH-SAR",  # Sarangani
    "PH-SCO",  # South Cotabato
    "PH-SIG",  # Siquijor
    "PH-SLE",  # Southern Leyte
    "PH-SLU",  # Sulu
    "PH-SOR",  # Sorsogon
    "PH-SUK",  # Sultan Kudarat
    "PH-SUN",  # Surigao del Norte
    "PH-SUR",  # Surigao del Sur
    "PH-TAR",  # Tarlac
    "PH-TAW",  # Tawi-Tawi
    "PH-WSA",  # Samar
    "PH-ZAN",  # Zamboanga del Norte
    "PH-ZAS",  # Zamboanga del Sur
    "PH-ZMB",  # Zambales
    "PH-ZSI",  # Zamboanga Sibugay
    # Islamic Republic of Pakistan
    "PK-BA",  # Balochistan
    "PK-GB",  # Gilgit-Baltistan
    "PK-IS",  # Islamabad
    "PK-JK",  # Azad Jammu and Kashmir
    "PK-KP",  # Khyber Pakhtunkhwa
    "PK-PB",  # Punjab
    "PK-SD",  # Sindh
    # Republic of Poland
    "PL-02",  # Dolnośląskie
    "PL-04",  # Kujawsko-Pomorskie
    "PL-06",  # Lubelskie
    "PL-08",  # Lubuskie
    "PL-10",  # Łódzkie
    "PL-12",  # Małopolskie
    "PL-14",  # Mazowieckie
    "PL-16",  # Opolskie
    "PL-18",  # Podkarpackie
    "PL-20",  # Podlaskie
    "PL-22",  # Pomorskie
    "PL-24",  # Śląskie
    "PL-26",  # Świętokrzyskie
    "PL-28",  # Warmińsko-Mazurskie
    "PL-30",  # Wielkopolskie
    "PL-32",  # Zachodniopomorskie
    # Saint Pierre and Miquelon
    # (no subdivisions)
    # Pitcairn
    # (no subdivisions)
    # Puerto Rico
    # (no subdivisions)
    # the State of Palestine
    "PS-BTH",  # Bethlehem
    "PS-DEB",  # Deir El Balah
    "PS-GZA",  # Gaza
    "PS-HBN",  # Hebron
    "PS-JEM",  # Jerusalem
    "PS-JEN",  # Jenin
    "PS-JRH",  # Jericho and Al Aghwar
    "PS-KYS",  # Khan Yunis
    "PS-NBS",  # Nablus
    "PS-NGZ",  # North Gaza
    "PS-QQA",  # Qalqilya
    "PS-RBH",  # Ramallah
    "PS-RFH",  # Rafah
    "PS-SLT",  # Salfit
    "PS-TBS",  # Tubas
    "PS-TKM",  # Tulkarm
    # Portuguese Republic
    "PT-01",  # Aveiro
    "PT-02",  # Beja
    "PT-03",  # Braga
    "PT-04",  # Bragança
    "PT-05",  # Castelo Branco
    "PT-06",  # Coimbra
    "PT-07",  # Évora
    "PT-08",  # Faro
    "PT-09",  # Guarda
    "PT-10",  # Leiria
    "PT-11",  # Lisboa
    "PT-12",  # Portalegre
    "PT-13",  # Porto
    "PT-14",  # Santarém
    "PT-15",  # Setúbal
    "PT-16",  # Viana do Castelo
    "PT-17",  # Vila Real
    "PT-18",  # Viseu
    "PT-20",  # Região Autónoma dos Açores
    "PT-30",  # Região Autónoma da Madeira
    # Republic of Palau
    "PW-002",  # Aimeliik
    "PW-004",  # Airai
    "PW-010",  # Angaur
    "PW-050",  # Hatohobei
    "PW-100",  # Kayangel
    "PW-150",  # Koror
    "PW-212",  # Melekeok
    "PW-214",  # Ngaraard
    "PW-218",  # Ngarchelong
    "PW-222",  # Ngardmau
    "PW-224",  # Ngatpang
    "PW-226",  # Ngchesar
    "PW-227",  # Ngeremlengui
    "PW-228",  # Ngiwal
    "PW-350",  # Peleliu
    "PW-370",  # Sonsorol
    # Republic of Paraguay
    "PY-1",  # Concepción
    "PY-10",  # Alto Paraná
    "PY-11",  # Central
    "PY-12",  # Ñeembucú
    "PY-13",  # Amambay
    "PY-14",  # Canindeyú
    "PY-15",  # Presidente Hayes
    "PY-16",  # Alto Paraguay
    "PY-19",  # Boquerón
    "PY-2",  # San Pedro
    "PY-3",  # Cordillera
    "PY-4",  # Guairá
    "PY-5",  # Caaguazú
    "PY-6",  # Caazapá
    "PY-7",  # Itapúa
    "PY-8",  # Misiones
    "PY-9",  # Paraguarí
    "PY-ASU",  # Asunción
    # State of Qatar
    "QA-DA",  # Ad Dawḩah
    "QA-KH",  # Al Khawr wa adh Dhakhīrah
    "QA-MS",  # Ash Shamāl
    "QA-RA",  # Ar Rayyān
    "QA-SH",  # Ash Shīḩānīyah
    "QA-US",  # Umm Şalāl
    "QA-WA",  # Al Wakrah
    "QA-ZA",  # Az̧ Z̧a‘āyin
    # Réunion
    # (no subdivisions)
    # Romania
    "RO-AB",  # Alba
    "RO-AG",  # Argeș
    "RO-AR",  # Arad
    "RO-B",  # București
    "RO-BC",  # Bacău
    "RO-BH",  # Bihor
    "RO-BN",  # Bistrița-Năsăud
    "RO-BR",  # Brăila
    "RO-BT",  # Botoșani
    "RO-BV",  # Brașov
    "RO-BZ",  # Buzău
    "RO-CJ",  # Cluj
    "RO-CL",  # Călărași
    "RO-CS",  # Caraș-Severin
    "RO-CT",  # Constanța
    "RO-CV",  # Covasna
    "RO-DB",  # Dâmbovița
    "RO-DJ",  # Dolj
    "RO-GJ",  # Gorj
    "RO-GL",  # Galați
    "RO-GR",  # Giurgiu
    "RO-HD",  # Hunedoara
    "RO-HR",  # Harghita
    "RO-IF",  # Ilfov
    "RO-IL",  # Ialomița
    "RO-IS",  # Iași
    "RO-MH",  # Mehedinți
    "RO-MM",  # Maramureș
    "RO-MS",  # Mureș
    "RO-NT",  # Neamț
    "RO-OT",  # Olt
    "RO-PH",  # Prahova
    "RO-SB",  # Sibiu
    "RO-SJ",  # Sălaj
    "RO-SM",  # Satu Mare
    "RO-SV",  # Suceava
    "RO-TL",  # Tulcea
    "RO-TM",  # Timiș
    "RO-TR",  # Teleorman
    "RO-VL",  # Vâlcea
    "RO-VN",  # Vrancea
    "RO-VS",  # Vaslui
    # Republic of Serbia
    "RS-00",  # Beograd
    "RS-01",  # Severnobački okrug
    "RS-02",  # Srednjebanatski okrug
    "RS-03",  # Severnobanatski okrug
    "RS-04",  # Južnobanatski okrug
    "RS-05",  # Zapadnobački okrug
    "RS-06",  # Južnobački okrug
    "RS-07",  # Sremski okrug
    "RS-08",  # Mačvanski okrug
    "RS-09",  # Kolubarski okrug
    "RS-10",  # Podunavski okrug
    "RS-11",  # Braničevski okrug
    "RS-12",  # Šumadijski okrug
    "RS-13",  # Pomoravski okrug
    "RS-14",  # Borski okrug
    "RS-15",  # Zaječarski okrug
    "RS-16",  # Zlatiborski okrug
    "RS-17",  # Moravički okrug
    "RS-18",  # Raški okrug
    "RS-19",  # Rasinski okrug
    "RS-20",  # Nišavski okrug
    "RS-21",  # Toplički okrug
    "RS-22",  # Pirotski okrug
    "RS-23",  # Jablanički okrug
    "RS-24",  # Pčinjski okrug
    "RS-25",  # Kosovski okrug
    "RS-26",  # Pećki okrug
    "RS-27",  # Prizrenski okrug
    "RS-28",  # Kosovsko-Mitrovački okrug
    "RS-29",  # Kosovsko-Pomoravski okrug
    "RS-KM",  # Kosovo-Metohija
    "RS-VO",  # Vojvodina
    # Russian Federation
    "RU-AD",  # Adygeja, Respublika
    "RU-AL",  # Altaj, Respublika
    "RU-ALT",  # Altajskij kraj
    "RU-AMU",  # Amurskaja oblast'
    "RU-ARK",  # Arhangel'skaja oblast'
    "RU-AST",  # Astrahanskaja oblast'
    "RU-BA",  # Bashkortostan, Respublika
    "RU-BEL",  # Belgorodskaja oblast'
    "RU-BRY",  # Brjanskaja oblast'
    "RU-BU",  # Burjatija, Respublika
    "RU-CE",  # Chechenskaya Respublika
    "RU-CHE",  # Chelyabinskaya oblast'
    "RU-CHU",  # Chukotskiy avtonomnyy okrug
    "RU-CU",  # Chuvashskaya Respublika
    "RU-DA",  # Dagestan, Respublika
    "RU-IN",  # Ingushetiya, Respublika
    "RU-IRK",  # Irkutskaja oblast'
    "RU-IVA",  # Ivanovskaja oblast'
    "RU-KAM",  # Kamchatskiy kray
    "RU-KB",  # Kabardino-Balkarskaja Respublika
    "RU-KC",  # Karachayevo-Cherkesskaya Respublika
    "RU-KDA",  # Krasnodarskij kraj
    "RU-KEM",  # Kemerovskaja oblast'
    "RU-KGD",  # Kaliningradskaja oblast'
    "RU-KGN",  # Kurganskaja oblast'
    "RU-KHA",  # Habarovskij kraj
    "RU-KHM",  # Hanty-Mansijskij avtonomnyj okrug
    "RU-KIR",  # Kirovskaja oblast'
    "RU-KK",  # Hakasija, Respublika
    "RU-KL",  # Kalmykija, Respublika
    "RU-KLU",  # Kaluzhskaya oblast'
    "RU-KO",  # Komi, Respublika
    "RU-KOS",  # Kostromskaja oblast'
    "RU-KR",  # Karelija, Respublika
    "RU-KRS",  # Kurskaja oblast'
    "RU-KYA",  # Krasnojarskij kraj
    "RU-LEN",  # Leningradskaja oblast'
    "RU-LIP",  # Lipeckaja oblast'
    "RU-MAG",  # Magadanskaja oblast'
    "RU-ME",  # Marij Èl, Respublika
    "RU-MO",  # Mordovija, Respublika
    "RU-MOS",  # Moskovskaja oblast'
    "RU-MOW",  # Moskva
    "RU-MUR",  # Murmanskaja oblast'
    "RU-NEN",  # Neneckij avtonomnyj okrug
    "RU-NGR",  # Novgorodskaja oblast'
    "RU-NIZ",  # Nizhegorodskaya oblast'
    "RU-NVS",  # Novosibirskaja oblast'
    "RU-OMS",  # Omskaja oblast'
    "RU-ORE",  # Orenburgskaja oblast'
    "RU-ORL",  # Orlovskaja oblast'
    "RU-PER",  # Permskij kraj
    "RU-PNZ",  # Penzenskaja oblast'
    "RU-PRI",  # Primorskij kraj
    "RU-PSK",  # Pskovskaja oblast'
    "RU-ROS",  # Rostovskaja oblast'
    "RU-RYA",  # Rjazanskaja oblast'
    "RU-SA",  # Saha, Respublika
    "RU-SAK",  # Sahalinskaja oblast'
    "RU-SAM",  # Samarskaja oblast'
    "RU-SAR",  # Saratovskaja oblast'
    "RU-SE",  # Severnaja Osetija, Respublika
    "RU-SMO",  # Smolenskaja oblast'
    "RU-SPE",  # Sankt-Peterburg
    "RU-STA",  # Stavropol'skij kraj
    "RU-SVE",  # Sverdlovskaja oblast'
    "RU-TA",  # Tatarstan, Respublika
    "RU-TAM",  # Tambovskaja oblast'
    "RU-TOM",  # Tomskaja oblast'
    "RU-TUL",  # Tul'skaja oblast'
    "RU-TVE",  # Tverskaja oblast'
    "RU-TY",  # Tyva, Respublika
    "RU-TYU",  # Tjumenskaja oblast'
    "RU-UD",  # Udmurtskaja Respublika
    "RU-ULY",  # Ul'janovskaja oblast'
    "RU-VGG",  # Volgogradskaja oblast'
    "RU-VLA",  # Vladimirskaja oblast'
    "RU-VLG",  # Vologodskaja oblast'
    "RU-VOR",  # Voronezhskaya oblast'
    "RU-YAN",  # Jamalo-Neneckij avtonomnyj okrug
    "RU-YAR",  # Jaroslavskaja oblast'
    "RU-YEV",  # Evrejskaja avtonomnaja oblast'
    "RU-ZAB",  # Zabajkal'skij kraj
    # Rwandese Republic
    "RW-01",  # City of Kigali
    "RW-02",  # Eastern
    "RW-03",  # Northern
    "RW-04",  # Western
    "RW-05",  # Southern
    # Kingdom of Saudi Arabia
    "SA-01",  # Ar Riyāḑ
    "SA-02",  # Makkah al Mukarramah
    "SA-03",  # Al Madīnah al Munawwarah
    "SA-04",  # Ash Sharqīyah
    "SA-05",  # Al Qaşīm
    "SA-06",  # Ḩā'il
    "SA-07",  # Tabūk
    "SA-08",  # Al Ḩudūd ash Shamālīyah
    "SA-09",  # Jāzān
    "SA-10",  # Najrān
    "SA-11",  # Al Bāḩah
    "SA-12",  # Al Jawf
    "SA-14",  # 'Asīr
    # Solomon Islands
    "SB-CE",  # Central
    "SB-CH",  # Choiseul
    "SB-CT",  # Capital Territory (Honiara)
    "SB-GU",  # Guadalcanal
    "SB-IS",  # Isabel
    "SB-MK",  # Makira-Ulawa
    "SB-ML",  # Malaita
    "SB-RB",  # Rennell and Bellona
    "SB-TE",  # Temotu
    "SB-WE",  # Western
    # Republic of Seychelles
    "SC-01",  # Anse aux Pins
    "SC-02",  # Anse Boileau
    "SC-03",  # Anse Etoile
    "SC-04",  # Au Cap
    "SC-05",  # Anse Royale
    "SC-06",  # Baie Lazare
    "SC-07",  # Baie Sainte Anne
    "SC-08",  # Beau Vallon
    "SC-09",  # Bel Air
    "SC-10",  # Bel Ombre
    "SC-11",  # Cascade
    "SC-12",  # Glacis
    "SC-13",  # Grand Anse Mahe
    "SC-14",  # Grand Anse Praslin
    "SC-15",  # La Digue
    "SC-16",  # English River
    "SC-17",  # Mont Buxton
    "SC-18",  # Mont Fleuri
    "SC-19",  # Plaisance
    "SC-20",  # Pointe Larue
    "SC-21",  # Port Glaud
    "SC-22",  # Saint Louis
    "SC-23",  # Takamaka
    "SC-24",  # Les Mamelles
    "SC-25",  # Roche Caiman
    "SC-26",  # Ile Perseverance I
    "SC-27",  # Ile Perseverance II
    # Republic of the Sudan
    "SD-DC",  # Central Darfur
    "SD-DE",  # East Darfur
    "SD-DN",  # North Darfur
    "SD-DS",  # South Darfur
    "SD-DW",  # West Darfur
    "SD-GD",  # Gedaref
    "SD-GK",  # West Kordofan
    "SD-GZ",  # Gezira
    "SD-KA",  # Kassala
    "SD-KH",  # Khartoum
    "SD-KN",  # North Kordofan
    "SD-KS",  # South Kordofan
    "SD-NB",  # Blue Nile
    "SD-NO",  # Northern
    "SD-NR",  # River Nile
    "SD-NW",  # White Nile
    "SD-RS",  # Red Sea
    "SD-SI",  # Sennar
    # Kingdom of Sweden
    "SE-AB",  # Stockholms län [SE-01]
    "SE-AC",  # Västerbottens län [SE-24]
    "SE-BD",  # Norrbottens län [SE-25]
    "SE-C",  # Uppsala län [SE-03]
    "SE-D",  # Södermanlands län [SE-04]
    "SE-E",  # Östergötlands län [SE-05]
    "SE-F",  # Jönköpings län [SE-06]
    "SE-G",  # Kronobergs län [SE-07]
    "SE-H",  # Kalmar län [SE-08]
    "SE-I",  # Gotlands län [SE-09]
    "SE-K",  # Blekinge län [SE-10]
    "SE-M",  # Skåne län [SE-12]
    "SE-N",  # Hallands län [SE-13]
    "SE-O",  # Västra Götalands län [SE-14]
    "SE-S",  # Värmlands län [SE-17]
    "SE-T",  # Örebro län [SE-18]
    "SE-U",  # Västmanlands län [SE-19]
    "SE-W",  # Dalarnas län [SE-20]
    "SE-X",  # Gävleborgs län [SE-21]
    "SE-Y",  # Västernorrlands län [SE-22]
    "SE-Z",  # Jämtlands län [SE-23]
    # Republic of Singapore
    "SG-01",  # Central Singapore
    "SG-02",  # North East
    "SG-03",  # North West
    "SG-04",  # South East
    "SG-05",  # South West
    # Saint Helena, Ascension and Tristan da Cunha
    "SH-AC",  # Ascension
    "SH-HL",  # Saint Helena
    "SH-TA",  # Tristan da Cunha
    # Republic of Slovenia
    "SI-001",  # Ajdovščina
    "SI-002",  # Beltinci
    "SI-003",  # Bled
    "SI-004",  # Bohinj
    "SI-005",  # Borovnica
    "SI-006",  # Bovec
    "SI-007",  # Brda
    "SI-008",  # Brezovica
    "SI-009",  # Brežice
    "SI-010",  # Tišina
    "SI-011",  # Celje
    "SI-012",  # Cerklje na Gorenjskem
    "SI-013",  # Cerknica
    "SI-014",  # Cerkno
    "SI-015",  # Črenšovci
    "SI-016",  # Črna na Koroškem
    "SI-017",  # Črnomelj
    "SI-018",  # Destrnik
    "SI-019",  # Divača
    "SI-020",  # Dobrepolje
    "SI-021",  # Dobrova-Polhov Gradec
    "SI-022",  # Dol pri Ljubljani
    "SI-023",  # Domžale
    "SI-024",  # Dornava
    "SI-025",  # Dravograd
    "SI-026",  # Duplek
    "SI-027",  # Gorenja vas-Poljane
    "SI-028",  # Gorišnica
    "SI-029",  # Gornja Radgona
    "SI-030",  # Gornji Grad
    "SI-031",  # Gornji Petrovci
    "SI-032",  # Grosuplje
    "SI-033",  # Šalovci
    "SI-034",  # Hrastnik
    "SI-035",  # Hrpelje-Kozina
    "SI-036",  # Idrija
    "SI-037",  # Ig
    "SI-038",  # Ilirska Bistrica
    "SI-039",  # Ivančna Gorica
    "SI-040",  # Izola
    "SI-041",  # Jesenice
    "SI-042",  # Juršinci
    "SI-043",  # Kamnik
    "SI-044",  # Kanal ob Soči
    "SI-045",  # Kidričevo
    "SI-046",  # Kobarid
    "SI-047",  # Kobilje
    "SI-048",  # Kočevje
    "SI-049",  # Komen
    "SI-050",  # Koper
    "SI-051",  # Kozje
    "SI-052",  # Kranj
    "SI-053",  # Kranjska Gora
    "SI-054",  # Krško
    "SI-055",  # Kungota
    "SI-056",  # Kuzma
    "SI-057",  # Laško
    "SI-058",  # Lenart
    "SI-059",  # Lendava
    "SI-060",  # Litija
    "SI-061",  # Ljubljana
    "SI-062",  # Ljubno
    "SI-063",  # Ljutomer
    "SI-064",  # Logatec
    "SI-065",  # Loška dolina
    "SI-066",  # Loški Potok
    "SI-067",  # Luče
    "SI-068",  # Lukovica
    "SI-069",  # Majšperk
    "SI-070",  # Maribor
    "SI-071",  # Medvode
    "SI-072",  # Mengeš
    "SI-073",  # Metlika
    "SI-074",  # Mežica
    "SI-075",  # Miren-Kostanjevica
    "SI-076",  # Mislinja
    "SI-077",  # Moravče
    "SI-078",  # Moravske Toplice
    "SI-079",  # Mozirje
    "SI-080",  # Murska Sobota
    "SI-081",  # Muta
    "SI-082",  # Naklo
    "SI-083",  # Nazarje
    "SI-084",  # Nova Gorica
    "SI-085",  # Novo Mesto
    "SI-086",  # Odranci
    "SI-087",  # Ormož
    "SI-088",  # Osilnica
    "SI-089",  # Pesnica
    "SI-090",  # Piran
    "SI-091",  # Pivka
    "SI-092",  # Podčetrtek
    "SI-093",  # Podvelka
    "SI-094",  # Postojna
    "SI-095",  # Preddvor
    "SI-096",  # Ptuj
    "SI-097",  # Puconci
    "SI-098",  # Rače-Fram
    "SI-099",  # Radeče
    "SI-100",  # Radenci
    "SI-101",  # Radlje ob Dravi
    "SI-102",  # Radovljica
    "SI-103",  # Ravne na Koroškem
    "SI-104",  # Ribnica
    "SI-105",  # Rogašovci
    "SI-106",  # Rogaška Slatina
    "SI-107",  # Rogatec
    "SI-108",  # Ruše
    "SI-109",  # Semič
    "SI-110",  # Sevnica
    "SI-111",  # Sežana
    "SI-112",  # Slovenj Gradec
    "SI-113",  # Slovenska Bistrica
    "SI-114",  # Slovenske Konjice
    "SI-115",  # Starše
    "SI-116",  # Sveti Jurij ob Ščavnici
    "SI-117",  # Šenčur
    "SI-118",  # Šentilj
    "SI-119",  # Šentjernej
    "SI-120",  # Šentjur
    "SI-121",  # Škocjan
    "SI-122",  # Škofja Loka
    "SI-123",  # Škofljica
    "SI-124",  # Šmarje pri Jelšah
    "SI-125",  # Šmartno ob Paki
    "SI-126",  # Šoštanj
    "SI-127",  # Štore
    "SI-128",  # Tolmin
    "SI-129",  # Trbovlje
    "SI-130",  # Trebnje
    "SI-131",  # Tržič
    "SI-132",  # Turnišče
    "SI-133",  # Velenje
    "SI-134",  # Velike Lašče
    "SI-135",  # Videm
    "SI-136",  # Vipava
    "SI-137",  # Vitanje
    "SI-138",  # Vodice
    "SI-139",  # Vojnik
    "SI-140",  # Vrhnika
    "SI-141",  # Vuzenica
    "SI-142",  # Zagorje ob Savi
    "SI-143",  # Zavrč
    "SI-144",  # Zreče
    "SI-146",  # Železniki
    "SI-147",  # Žiri
    "SI-148",  # Benedikt
    "SI-149",  # Bistrica ob Sotli
    "SI-150",  # Bloke
    "SI-151",  # Braslovče
    "SI-152",  # Cankova
    "SI-153",  # Cerkvenjak
    "SI-154",  # Dobje
    "SI-155",  # Dobrna
    "SI-156",  # Dobrovnik
    "SI-157",  # Dolenjske Toplice
    "SI-158",  # Grad
    "SI-159",  # Hajdina
    "SI-160",  # Hoče-Slivnica
    "SI-161",  # Hodoš
    "SI-162",  # Horjul
    "SI-163",  # Jezersko
    "SI-164",  # Komenda
    "SI-165",  # Kostel
    "SI-166",  # Križevci
    "SI-167",  # Lovrenc na Pohorju
    "SI-168",  # Markovci
    "SI-169",  # Miklavž na Dravskem polju
    "SI-170",  # Mirna Peč
    "SI-171",  # Oplotnica
    "SI-172",  # Podlehnik
    "SI-173",  # Polzela
    "SI-174",  # Prebold
    "SI-175",  # Prevalje
    "SI-176",  # Razkrižje
    "SI-177",  # Ribnica na Pohorju
    "SI-178",  # Selnica ob Dravi
    "SI-179",  # Sodražica
    "SI-180",  # Solčava
    "SI-181",  # Sveta Ana
    "SI-182",  # Sveti Andraž v Slovenskih goricah
    "SI-183",  # Šempeter-Vrtojba
    "SI-184",  # Tabor
    "SI-185",  # Trnovska Vas
    "SI-186",  # Trzin
    "SI-187",  # Velika Polana
    "SI-188",  # Veržej
    "SI-189",  # Vransko
    "SI-190",  # Žalec
    "SI-191",  # Žetale
    "SI-192",  # Žirovnica
    "SI-193",  # Žužemberk
    "SI-194",  # Šmartno pri Litiji
    "SI-195",  # Apače
    "SI-196",  # Cirkulane
    "SI-197",  # Kostanjevica na Krki
    "SI-198",  # Makole
    "SI-199",  # Mokronog-Trebelno
    "SI-200",  # Poljčane
    "SI-201",  # Renče-Vogrsko
    "SI-202",  # Središče ob Dravi
    "SI-203",  # Straža
    "SI-204",  # Sveta Trojica v Slovenskih goricah
    "SI-205",  # Sveti Tomaž
    "SI-206",  # Šmarješke Toplice
    "SI-207",  # Gorje
    "SI-208",  # Log-Dragomer
    "SI-209",  # Rečica ob Savinji
    "SI-210",  # Sveti Jurij v Slovenskih goricah
    "SI-211",  # Šentrupert
    "SI-212",  # Mirna
    "SI-213",  # Ankaran
    # Svalbard and Jan Mayen
    # (no subdivisions)
    # Slovak Republic
    "SK-BC",  # Banskobystrický kraj
    "SK-BL",  # Bratislavský kraj
    "SK-KI",  # Košický kraj
    "SK-NI",  # Nitriansky kraj
    "SK-PV",  # Prešovský kraj
    "SK-TA",  # Trnavský kraj
    "SK-TC",  # Trenčiansky kraj
    "SK-ZI",  # Žilinský kraj
    # Republic of Sierra Leone
    "SL-E",  # Eastern
    "SL-N",  # Northern
    "SL-NW",  # North Western
    "SL-S",  # Southern
    "SL-W",  # Western Area (Freetown)
    # Republic of San Marino
    "SM-01",  # Acquaviva
    "SM-02",  # Chiesanuova
    "SM-03",  # Domagnano
    "SM-04",  # Faetano
    "SM-05",  # Fiorentino
    "SM-06",  # Borgo Maggiore
    "SM-07",  # Città di San Marino
    "SM-08",  # Montegiardino
    "SM-09",  # Serravalle
    # Republic of Senegal
    "SN-DB",  # Diourbel
    "SN-DK",  # Dakar
    "SN-FK",  # Fatick
    "SN-KA",  # Kaffrine
    "SN-KD",  # Kolda
    "SN-KE",  # Kédougou
    "SN-KL",  # Kaolack
    "SN-LG",  # Louga
    "SN-MT",  # Matam
    "SN-SE",  # Sédhiou
    "SN-SL",  # Saint-Louis
    "SN-TC",  # Tambacounda
    "SN-TH",  # Thiès
    "SN-ZG",  # Ziguinchor
    # Federal Republic of Somalia
    "SO-AW",  # Awdal
    "SO-BK",  # Bakool
    "SO-BN",  # Banaadir
    "SO-BR",  # Bari
    "SO-BY",  # Bay
    "SO-GA",  # Galguduud
    "SO-GE",  # Gedo
    "SO-HI",  # Hiiraan
    "SO-JD",  # Jubbada Dhexe
    "SO-JH",  # Jubbada Hoose
    "SO-MU",  # Mudug
    "SO-NU",  # Nugaal
    "SO-SA",  # Sanaag
    "SO-SD",  # Shabeellaha Dhexe
    "SO-SH",  # Shabeellaha Hoose
    "SO-SO",  # Sool
    "SO-TO",  # Togdheer
    "SO-WO",  # Woqooyi Galbeed
    # Republic of Suriname
    "SR-BR",  # Brokopondo
    "SR-CM",  # Commewijne
    "SR-CR",  # Coronie
    "SR-MA",  # Marowijne
    "SR-NI",  # Nickerie
    "SR-PM",  # Paramaribo
    "SR-PR",  # Para
    "SR-SA",  # Saramacca
    "SR-SI",  # Sipaliwini
    "SR-WA",  # Wanica
    # Republic of South Sudan
    "SS-BN",  # Northern Bahr el Ghazal
    "SS-BW",  # Western Bahr el Ghazal
    "SS-EC",  # Central Equatoria
    "SS-EE",  # Eastern Equatoria
    "SS-EW",  # Western Equatoria
    "SS-JG",  # Jonglei
    "SS-LK",  # Lakes
    "SS-NU",  # Upper Nile
    "SS-UY",  # Unity
    "SS-WR",  # Warrap
    # Democratic Republic of Sao Tome and Principe
    "ST-01",  # Água Grande
    "ST-02",  # Cantagalo
    "ST-03",  # Caué
    "ST-04",  # Lembá
    "ST-05",  # Lobata
    "ST-06",  # Mé-Zóchi
    "ST-P",  # Príncipe
    # Republic of El Salvador
    "SV-AH",  # Ahuachapán
    "SV-CA",  # Cabañas
    "SV-CH",  # Chalatenango
    "SV-CU",  # Cuscatlán
    "SV-LI",  # La Libertad
    "SV-MO",  # Morazán
    "SV-PA",  # La Paz
    "SV-SA",  # Santa Ana
    "SV-SM",  # San Miguel
    "SV-SO",  # Sonsonate
    "SV-SS",  # San Salvador
    "SV-SV",  # San Vicente
    "SV-UN",  # La Unión
    "SV-US",  # Usulután
    # Sint Maarten (Dutch part)
    # (no subdivisions)
    # Syrian Arab Republic
    "SY-DI",  # Dimashq
    "SY-DR",  # Dar'ā
    "SY-DY",  # Dayr az Zawr
    "SY-HA",  # Al Ḩasakah
    "SY-HI",  # Ḩimş
    "SY-HL",  # Ḩalab
    "SY-HM",  # Ḩamāh
    "SY-ID",  # Idlib
    "SY-LA",  # Al Lādhiqīyah
    "SY-QU",  # Al Qunayţirah
    "SY-RA",  # Ar Raqqah
    "SY-RD",  # Rīf Dimashq
    "SY-SU",  # As Suwaydā'
    "SY-TA",  # Ţarţūs
    # Kingdom of Eswatini
    "SZ-HH",  # Hhohho
    "SZ-LU",  # Lubombo
    "SZ-MA",  # Manzini
    "SZ-SH",  # Shiselweni
    # Turks and Caicos Islands
    # (no subdivisions)
    # Republic of Chad
    "TD-BA",  # Batha
    "TD-BG",  # Bahr el Ghazal
    "TD-BO",  # Borkou
    "TD-CB",  # Chari-Baguirmi
    "TD-EE",  # Ennedi-Est
    "TD-EO",  # Ennedi-Ouest
    "TD-GR",  # Guéra
    "TD-HL",  # Hadjer Lamis
    "TD-KA",  # Kanem
    "TD-LC",  # Lac
    "TD-LO",  # Logone-Occidental
    "TD-LR",  # Logone-Oriental
    "TD-MA",  # Mandoul
    "TD-MC",  # Moyen-Chari
    "TD-ME",  # Mayo-Kebbi-Est
    "TD-MO",  # Mayo-Kebbi-Ouest
    "TD-ND",  # Ville de Ndjamena
    "TD-OD",  # Ouaddaï
    "TD-SA",  # Salamat
    "TD-SI",  # Sila
    "TD-TA",  # Tandjilé
    "TD-TI",  # Tibesti
    "TD-WF",  # Wadi Fira
    # French Southern Territories
    # (no subdivisions)
    # Togolese Republic
    "TG-C",  # Centrale
    "TG-K",  # Kara
    "TG-M",  # Maritime (Région)
    "TG-P",  # Plateaux
    "TG-S",  # Savanes
    # Kingdom of Thailand
    "TH-10",  # Krung Thep Maha Nakhon
    "TH-11",  # Samut Prakan
    "TH-12",  # Nonthaburi
    "TH-13",  # Pathum Thani
    "TH-14",  # Phra Nakhon Si Ayutthaya
    "TH-15",  # Ang Thong
    "TH-16",  # Lop Buri
    "TH-17",  # Sing Buri
    "TH-18",  # Chai Nat
    "TH-19",  # Saraburi
    "TH-20",  # Chon Buri
    "TH-21",  # Rayong
    "TH-22",  # Chanthaburi
    "TH-23",  # Trat
    "TH-24",  # Chachoengsao
    "TH-25",  # Prachin Buri
    "TH-26",  # Nakhon Nayok
    "TH-27",  # Sa Kaeo
    "TH-30",  # Nakhon Ratchasima
    "TH-31",  # Buri Ram
    "TH-32",  # Surin
    "TH-33",  # Si Sa Ket
    "TH-34",  # Ubon Ratchathani
    "TH-35",  # Yasothon
    "TH-36",  # Chaiyaphum
    "TH-37",  # Amnat Charoen
    "TH-38",  # Bueng Kan
    "TH-39",  # Nong Bua Lam Phu
    "TH-40",  # Khon Kaen
    "TH-41",  # Udon Thani
    "TH-42",  # Loei
    "TH-43",  # Nong Khai
    "TH-44",  # Maha Sarakham
    "TH-45",  # Roi Et
    "TH-46",  # Kalasin
    "TH-47",  # Sakon Nakhon
    "TH-48",  # Nakhon Phanom
    "TH-49",  # Mukdahan
    "TH-50",  # Chiang Mai
    "TH-51",  # Lamphun
    "TH-52",  # Lampang
    "TH-53",  # Uttaradit
    "TH-54",  # Phrae
    "TH-55",  # Nan
    "TH-56",  # Phayao
    "TH-57",  # Chiang Rai
    "TH-58",  # Mae Hong Son
    "TH-60",  # Nakhon Sawan
    "TH-61",  # Uthai Thani
    "TH-62",  # Kamphaeng Phet
    "TH-63",  # Tak
    "TH-64",  # Sukhothai
    "TH-65",  # Phitsanulok
    "TH-66",  # Phichit
    "TH-67",  # Phetchabun
    "TH-70",  # Ratchaburi
    "TH-71",  # Kanchanaburi
    "TH-72",  # Suphan Buri
    "TH-73",  # Nakhon Pathom
    "TH-74",  # Samut Sakhon
    "TH-75",  # Samut Songkhram
    "TH-76",  # Phetchaburi
    "TH-77",  # Prachuap Khiri Khan
    "TH-80",  # Nakhon Si Thammarat
    "TH-81",  # Krabi
    "TH-82",  # Phangnga
    "TH-83",  # Phuket
    "TH-84",  # Surat Thani
    "TH-85",  # Ranong
    "TH-86",  # Chumphon
    "TH-90",  # Songkhla
    "TH-91",  # Satun
    "TH-92",  # Trang
    "TH-93",  # Phatthalung
    "TH-94",  # Pattani
    "TH-95",  # Yala
    "TH-96",  # Narathiwat
    "TH-S",  # Phatthaya
    # Republic of Tajikistan
    "TJ-DU",  # Dushanbe
    "TJ-GB",  # Kŭhistoni Badakhshon
    "TJ-KT",  # Khatlon
    "TJ-RA",  # nohiyahoi tobei jumhurí
    "TJ-SU",  # Sughd
    # Tokelau
    # (no subdivisions)
    # Democratic Republic of Timor-Leste
    "TL-AL",  # Aileu
    "TL-AN",  # Ainaro
    "TL-BA",  # Baucau
    "TL-BO",  # Bobonaro
    "TL-CO",  # Cova Lima
    "TL-DI",  # Díli
    "TL-ER",  # Ermera
    "TL-LA",  # Lautein
    "TL-LI",  # Likisá
    "TL-MF",  # Manufahi
    "TL-MT",  # Manatuto
    "TL-OE",  # Oekusi-Ambenu
    "TL-VI",  # Vikeke
    # Turkmenistan
    "TM-A",  # Ahal
    "TM-B",  # Balkan
    "TM-D",  # Daşoguz
    "TM-L",  # Lebap
    "TM-M",  # Mary
    "TM-S",  # Aşgabat
    # Republic of Tunisia
    "TN-11",  # Tunis
    "TN-12",  # L'Ariana
    "TN-13",  # Ben Arous
    "TN-14",  # La Manouba
    "TN-21",  # Nabeul
    "TN-22",  # Zaghouan
    "TN-23",  # Bizerte
    "TN-31",  # Béja
    "TN-32",  # Jendouba
    "TN-33",  # Le Kef
    "TN-34",  # Siliana
    "TN-41",  # Kairouan
    "TN-42",  # Kasserine
    "TN-43",  # Sidi Bouzid
    "TN-51",  # Sousse
    "TN-52",  # Monastir
    "TN-53",  # Mahdia
    "TN-61",  # Sfax
    "TN-71",  # Gafsa
    "TN-72",  # Tozeur
    "TN-73",  # Kébili
    "TN-81",  # Gabès
    "TN-82",  # Médenine
    "TN-83",  # Tataouine
    # Kingdom of Tonga
    "TO-01",  # 'Eua
    "TO-02",  # Ha'apai
    "TO-03",  # Niuas
    "TO-04",  # Tongatapu
    "TO-05",  # Vava'u
    # Republic of Türkiye
    "TR-01",  # Adana
    "TR-02",  # Adıyaman
    "TR-03",  # Afyonkarahisar
    "TR-04",  # Ağrı
    "TR-05",  # Amasya
    "TR-06",  # Ankara
    "TR-07",  # Antalya
    "TR-08",  # Artvin
    "TR-09",  # Aydın
    "TR-10",  # Balıkesir
    "TR-11",  # Bilecik
    "TR-12",  # Bingöl
    "TR-13",  # Bitlis
    "TR-14",  # Bolu
    "TR-15",  # Burdur
    "TR-16",  # Bursa
    "TR-17",  # Çanakkale
    "TR-18",  # Çankırı
    "TR-19",  # Çorum
    "TR-20",  # Denizli
    "TR-21",  # Diyarbakır
    "TR-22",  # Edirne
    "TR-23",  # Elazığ
    "TR-24",  # Erzincan
    "TR-25",  # Erzurum
    "TR-26",  # Eskişehir
    "TR-27",  # Gaziantep
    "TR-28",  # Giresun
    "TR-29",  # Gümüşhane
    "TR-30",  # Hakkâri
    "TR-31",  # Hatay
    "TR-32",  # Isparta
    "TR-33",  # Mersin
    "TR-34",  # İstanbul
    "TR-35",  # İzmir
    "TR-36",  # Kars
    "TR-37",  # Kastamonu
    "TR-38",  # Kayseri
    "TR-39",  # Kırklareli
    "TR-40",  # Kırşehir
    "TR-41",  # Kocaeli
    "TR-42",  # Konya
    "TR-43",  # Kütahya
    "TR-44",  # Malatya
    "TR-45",  # Manisa
    "TR-46",  # Kahramanmaraş
    "TR-47",  # Mardin
    "TR-48",  # Muğla
    "TR-49",  # Muş
    "TR-50",  # Nevşehir
    "TR-51",  # Niğde
    "TR-52",  # Ordu
    "TR-53",  # Rize
    "TR-54",  # Sakarya
    "TR-55",  # Samsun
    "TR-56",  # Siirt
    "TR-57",  # Sinop
    "TR-58",  # Sivas
    "TR-59",  # Tekirdağ
    "TR-60",  # Tokat
    "TR-61",  # Trabzon
    "TR-62",  # Tunceli
    "TR-63",  # Şanlıurfa
    "TR-64",  # Uşak
    "TR-65",  # Van
    "TR-66",  # Yozgat
    "TR-67",  # Zonguldak
    "TR-68",  # Aksaray
    "TR-69",  # Bayburt
    "TR-70",  # Karaman
    "TR-71",  # Kırıkkale
    "TR-72",  # Batman
    "TR-73",  # Şırnak
    "TR-74",  # Bartın
    "TR-75",  # Ardahan
    "TR-76",  # Iğdır
    "TR-77",  # Yalova
    "TR-78",  # Karabük
    "TR-79",  # Kilis
    "TR-80",  # Osmaniye
    "TR-81",  # Düzce
    # Republic of Trinidad and Tobago
    "TT-ARI",  # Arima
    "TT-CHA",  # Chaguanas
    "TT-CTT",  # Couva-Tabaquite-Talparo
    "TT-DMN",  # Diego Martin
    "TT-MRC",  # Mayaro-Rio Claro
    "TT-PED",  # Penal-Debe
    "TT-POS",  # Port of Spain
    "TT-PRT",  # Princes Town
    "TT-PTF",  # Point Fortin
    "TT-SFO",  # San Fernando
    "TT-SGE",  # Sangre Grande
    "TT-SIP",  # Siparia
    "TT-SJL",  # San Juan-Laventille
    "TT-TOB",  # Tobago
    "TT-TUP",  # Tunapuna-Piarco
    # Tuvalu
    "TV-FUN",  # Funafuti
    "TV-NIT",  # Niutao
    "TV-NKF",  # Nukufetau
    "TV-NKL",  # Nukulaelae
    "TV-NMA",  # Nanumea
    "TV-NMG",  # Nanumaga
    "TV-NUI",  # Nui
    "TV-VAI",  # Vaitupu
    # Taiwan, Province of China
    "TW-CHA",  # Changhua
    "TW-CYI",  # Chiayi
    "TW-CYQ",  # Chiayi
    "TW-HSQ",  # Hsinchu
    "TW-HSZ",  # Hsinchu
    "TW-HUA",  # Hualien
    "TW-ILA",  # Yilan
    "TW-KEE",  # Keelung
    "TW-KHH",  # Kaohsiung
    "TW-KIN",  # Kinmen
    "TW-LIE",  # Lienchiang
    "TW-MIA",  # Miaoli
    "TW-NAN",  # Nantou
    "TW-NWT",  # New Taipei
    "TW-PEN",  # Penghu
    "TW-PIF",  # Pingtung
    "TW-TAO",  # Taoyuan
    "TW-TNN",  # Tainan
    "TW-TPE",  # Taipei
    "TW-TTT",  # Taitung
    "TW-TXG",  # Taichung
    "TW-YUN",  # Yunlin
    # United Republic of Tanzania
    "TZ-01",  # Arusha
    "TZ-02",  # Dar es Salaam
    "TZ-03",  # Dodoma
    "TZ-04",  # Iringa
    "TZ-05",  # Kagera
    "TZ-06",  # Pemba North
    "TZ-07",  # Zanzibar North
    "TZ-08",  # Kigoma
    "TZ-09",  # Kilimanjaro
    "TZ-10",  # Pemba South
    "TZ-11",  # Zanzibar South
    "TZ-12",  # Lindi
    "TZ-13",  # Mara
    "TZ-14",  # Mbeya
    "TZ-15",  # Zanzibar West
    "TZ-16",  # Morogoro
    "TZ-17",  # Mtwara
    "TZ-18",  # Mwanza
    "TZ-19",  # Coast
    "TZ-20",  # Rukwa
    "TZ-21",  # Ruvuma
    "TZ-22",  # Shinyanga
    "TZ-23",  # Singida
    "TZ-24",  # Tabora
    "TZ-25",  # Tanga
    "TZ-26",  # Manyara
    "TZ-27",  # Geita
    "TZ-28",  # Katavi
    "TZ-29",  # Njombe
    "TZ-30",  # Simiyu
    "TZ-31",  # Songwe
    # Ukraine
    "UA-05",  # Vinnytska oblast
    "UA-07",  # Volynska oblast
    "UA-09",  # Luhanska oblast
    "UA-12",  # Dnipropetrovska oblast
    "UA-14",  # Donetska oblast
    "UA-18",  # Zhytomyrska oblast
    "UA-21",  # Zakarpatska oblast
    "UA-23",  # Zaporizka oblast
    "UA-26",  # Ivano-Frankivska oblast
    "UA-30",  # Kyiv
    "UA-32",  # Kyivska oblast
    "UA-35",  # Kirovohradska oblast
    "UA-40",  # Sevastopol
    "UA-43",  # Avtonomna Respublika Krym
    "UA-46",  # Lvivska oblast
    "UA-48",  # Mykolaivska oblast
    "UA-51",  # Odeska oblast
    "UA-53",  # Poltavska oblast
    "UA-56",  # Rivnenska oblast
    "UA-59",  # Sumska oblast
    "UA-61",  # Ternopilska oblast
    "UA-63",  # Kharkivska oblast
    "UA-65",  # Khersonska oblast
    "UA-68",  # Khmelnytska oblast
    "UA-71",  # Cherkaska oblast
    "UA-74",  # Chernihivska oblast
    "UA-77",  # Chernivetska oblast
    # Republic of Uganda
    "UG-101",  # Kalangala
    "UG-102",  # Kampala
    "UG-103",  # Kiboga
    "UG-104",  # Luwero
    "UG-105",  # Masaka
    "UG-106",  # Mpigi
    "UG-107",  # Mubende
    "UG-108",  # Mukono
    "UG-109",  # Nakasongola
    "UG-110",  # Rakai
    "UG-111",  # Sembabule
    "UG-112",  # Kayunga
    "UG-113",  # Wakiso
    "UG-114",  # Lyantonde
    "UG-115",  # Mityana
    "UG-116",  # Nakaseke
    "UG-117",  # Buikwe
    "UG-118",  # Bukomansibi
    "UG-119",  # Butambala
    "UG-120",  # Buvuma
    "UG-121",  # Gomba
    "UG-122",  # Kalungu
    "UG-123",  # Kyankwanzi
    "UG-124",  # Lwengo
    "UG-125",  # Kyotera
    "UG-126",  # Kasanda
    "UG-201",  # Bugiri
    "UG-202",  # Busia
    "UG-203",  # Iganga
    "UG-204",  # Jinja
    "UG-205",  # Kamuli
    "UG-206",  # Kapchorwa
    "UG-207",  # Katakwi
    "UG-208",  # Kumi
    "UG-209",  # Mbale
    "UG-210",  # Pallisa
    "UG-211",  # Soroti
    "UG-212",  # Tororo
    "UG-213",  # Kaberamaido
    "UG-214",  # Mayuge
    "UG-215",  # Sironko
    "UG-216",  # Amuria
    "UG-217",  # Budaka
    "UG-218",  # Bududa
    "UG-219",  # Bukedea
    "UG-220",  # Bukwo
    "UG-221",  # Butaleja
    "UG-222",  # Kaliro
    "UG-223",  # Manafwa
    "UG-224",  # Namutumba
    "UG-225",  # Bulambuli
    "UG-226",  # Buyende
    "UG-227",  # Kibuku
    "UG-228",  # Kween
    "UG-229",  # Luuka
    "UG-230",  # Namayingo
    "UG-231",  # Ngora
    "UG-232",  # Serere
    "UG-233",  # Butebo
    "UG-234",  # Namisindwa
    "UG-235",  # Bugweri
    "UG-236",  # Kapelebyong
    "UG-237",  # Kalaki
    "UG-301",  # Adjumani
    "UG-302",  # Apac
    "UG-303",  # Arua
    "UG-304",  # Gulu
    "UG-305",  # Kitgum
    "UG-306",  # Kotido
    "UG-307",  # Lira
    "UG-308",  # Moroto
    "UG-309",  # Moyo
    "UG-310",  # Nebbi
    "UG-311",  # Nakapiripirit
    "UG-312",  # Pader
    "UG-313",  # Yumbe
    "UG-314",  # Abim
    "UG-315",  # Amolatar
    "UG-316",  # Amuru
    "UG-317",  # Dokolo
    "UG-318",  # Kaabong
    "UG-319",  # Koboko
    "UG-320",  # Maracha
    "UG-321",  # Oyam
    "UG-322",  # Agago
    "UG-323",  # Alebtong
    "UG-324",  # Amudat
    "UG-325",  # Kole
    "UG-326",  # Lamwo
    "UG-327",  # Napak
    "UG-328",  # Nwoya
    "UG-329",  # Otuke
    "UG-330",  # Zombo
    "UG-331",  # Omoro
    "UG-332",  # Pakwach
    "UG-333",  # Kwania
    "UG-334",  # Nabilatuk
    "UG-335",  # Karenga
    "UG-336",  # Madi-Okollo
    "UG-337",  # Obongi
    "UG-401",  # Bundibugyo
    "UG-402",  # Bushenyi
    "UG-403",  # Hoima
    "UG-404",  # Kabale
    "UG-405",  # Kabarole
    "UG-406",  # Kasese
    "UG-407",  # Kibaale
    "UG-408",  # Kisoro
    "UG-409",  # Masindi
    "UG-410",  # Mbarara
    "UG-411",  # Ntungamo
    "UG-412",  # Rukungiri
    "UG-413",  # Kamwenge
    "UG-414",  # Kanungu
    "UG-415",  # Kyenjojo
    "UG-416",  # Buliisa
    "UG-417",  # Ibanda
    "UG-418",  # Isingiro
    "UG-419",  # Kiruhura
    "UG-420",  # Buhweju
    "UG-421",  # Kiryandongo
    "UG-422",  # Kyegegwa
    "UG-423",  # Mitooma
    "UG-424",  # Ntoroko
    "UG-425",  # Rubirizi
    "UG-426",  # Sheema
    "UG-427",  # Kagadi
    "UG-428",  # Kakumiro
    "UG-429",  # Rubanda
    "UG-430",  # Bunyangabu
    "UG-431",  # Rukiga
    "UG-432",  # Kikuube
    "UG-433",  # Kazo
    "UG-434",  # Kitagwenda
    "UG-435",  # Rwampara
    "UG-C",  # Central
    "UG-E",  # Eastern
    "UG-N",  # Northern
    "UG-W",  # Western
    # United States Minor Outlying Islands
    "UM-67",  # Johnston Atoll
    "UM-71",  # Midway Islands
    "UM-76",  # Navassa Island
    "UM-79",  # Wake Island
    "UM-81",  # Baker Island
    "UM-84",  # Howland Island
    "UM-86",  # Jarvis Island
    "UM-89",  # Kingman Reef
    "UM-95",  # Palmyra Atoll
    # United States of America
    "US-AK",  # Alaska
    "US-AL",  # Alabama
    "US-AR",  # Arkansas
    "US-AS",  # American Samoa
    "US-AZ",  # Arizona
    "US-CA",  # California
    "US-CO",  # Colorado
    "US-CT",  # Connecticut
    "US-DC",  # District of Columbia
    "US-DE",  # Delaware
    "US-FL",  # Florida
    "US-GA",  # Georgia
    "US-GU",  # Guam
    "US-HI",  # Hawaii
    "US-IA",  # Iowa
    "US-ID",  # Idaho
    "US-IL",  # Illinois
    "US-IN",  # Indiana
    "US-KS",  # Kansas
    "US-KY",  # Kentucky
    "US-LA",  # Louisiana
    "US-MA",  # Massachusetts
    "US-MD",  # Maryland
    "US-ME",  # Maine
    "US-MI",  # Michigan
    "US-MN",  # Minnesota
    "US-MO",  # Missouri
    "US-MP",  # Northern Mariana Islands
    "US-MS",  # Mississippi
    "US-MT",  # Montana
    "US-NC",  # North Carolina
    "US-ND",  # North Dakota
    "US-NE",  # Nebraska
    "US-NH",  # New Hampshire
    "US-NJ",  # New Jersey
    "US-NM",  # New Mexico
    "US-NV",  # Nevada
    "US-NY",  # New York
    "US-OH",  # Ohio
    "US-OK",  # Oklahoma
    "US-OR",  # Oregon
    "US-PA",  # Pennsylvania
    "US-PR",  # Puerto Rico
    "US-RI",  # Rhode Island
    "US-SC",  # South Carolina
    "US-SD",  # South Dakota
    "US-TN",  # Tennessee
    "US-TX",  # Texas
    "US-UM",  # United States Minor Outlying Islands
    "US-UT",  # Utah
    "US-VA",  # Virginia
    "US-VI",  # Virgin Islands, U.S.
    "US-VT",  # Vermont
    "US-WA",  # Washington
    "US-WI",  # Wisconsin
    "US-WV",  # West Virginia
    "US-WY",  # Wyoming
    # Eastern Republic of Uruguay
    "UY-AR",  # Artigas
    "UY-CA",  # Canelones
    "UY-CL",  # Cerro Largo
    "UY-CO",  # Colonia
    "UY-DU",  # Durazno
    "UY-FD",  # Florida
    "UY-FS",  # Flores
    "UY-LA",  # Lavalleja
    "UY-MA",  # Maldonado
    "UY-MO",  # Montevideo
    "UY-PA",  # Paysandú
    "UY-RN",  # Río Negro
    "UY-RO",  # Rocha
    "UY-RV",  # Rivera
    "UY-SA",  # Salto
    "UY-SJ",  # San José
    "UY-SO",  # Soriano
    "UY-TA",  # Tacuarembó
    "UY-TT",  # Treinta y Tres
    # Republic of Uzbekistan
    "UZ-AN",  # Andijon
    "UZ-BU",  # Buxoro
    "UZ-FA",  # Farg‘ona
    "UZ-JI",  # Jizzax
    "UZ-NG",  # Namangan
    "UZ-NW",  # Navoiy
    "UZ-QA",  # Qashqadaryo
    "UZ-QR",  # Qoraqalpog‘iston Respublikasi
    "UZ-SA",  # Samarqand
    "UZ-SI",  # Sirdaryo
    "UZ-SU",  # Surxondaryo
    "UZ-TK",  # Toshkent
    "UZ-TO",  # Toshkent
    "UZ-XO",  # Xorazm
    # Holy See (Vatican City State)
    # (no subdivisions)
    # Saint Vincent and the Grenadines
    "VC-01",  # Charlotte
    "VC-02",  # Saint Andrew
    "VC-03",  # Saint David
    "VC-04",  # Saint George
    "VC-05",  # Saint Patrick
    "VC-06",  # Grenadines
    # Bolivarian Republic of Venezuela
    "VE-A",  # Distrito Capital
    "VE-B",  # Anzoátegui
    "VE-C",  # Apure
    "VE-D",  # Aragua
    "VE-E",  # Barinas
    "VE-F",  # Bolívar
    "VE-G",  # Carabobo
    "VE-H",  # Cojedes
    "VE-I",  # Falcón
    "VE-J",  # Guárico
    "VE-K",  # Lara
    "VE-L",  # Mérida
    "VE-M",  # Miranda
    "VE-N",  # Monagas
    "VE-O",  # Nueva Esparta
    "VE-P",  # Portuguesa
    "VE-R",  # Sucre
    "VE-S",  # Táchira
    "VE-T",  # Trujillo
    "VE-U",  # Yaracuy
    "VE-V",  # Zulia
    "VE-W",  # Dependencias Federales
    "VE-X",  # La Guaira
    "VE-Y",  # Delta Amacuro
    "VE-Z",  # Amazonas
    # British Virgin Islands
    # (no subdivisions)
    # Virgin Islands of the United States
    # (no subdivisions)
    # Socialist Republic of Viet Nam
    "VN-01",  # Lai Châu
    "VN-02",  # Lào Cai
    "VN-03",  # Hà Giang
    "VN-04",  # Cao Bằng
    "VN-05",  # Sơn La
    "VN-06",  # Yên Bái
    "VN-07",  # Tuyên Quang
    "VN-09",  # Lạng Sơn
    "VN-13",  # Quảng Ninh
    "VN-14",  # Hòa Bình
    "VN-18",  # Ninh Bình
    "VN-20",  # Thái Bình
    "VN-21",  # Thanh Hóa
    "VN-22",  # Nghệ An
    "VN-23",  # Hà Tĩnh
    "VN-24",  # Quảng Bình
    "VN-25",  # Quảng Trị
    "VN-26",  # Thừa Thiên-Huế
    "VN-27",  # Quảng Nam
    "VN-28",  # Kon Tum
    "VN-29",  # Quảng Ngãi
    "VN-30",  # Gia Lai
    "VN-31",  # Bình Định
    "VN-32",  # Phú Yên
    "VN-33",  # Đắk Lắk
    "VN-34",  # Khánh Hòa
    "VN-35",  # Lâm Đồng
    "VN-36",  # Ninh Thuận
    "VN-37",  # Tây Ninh
    "VN-39",  # Đồng Nai
    "VN-40",  # Bình Thuận
    "VN-41",  # Long An
    "VN-43",  # Bà Rịa - Vũng Tàu
    "VN-44",  # An Giang
    "VN-45",  # Đồng Tháp
    "VN-46",  # Tiền Giang
    "VN-47",  # Kiến Giang
    "VN-49",  # Vĩnh Long
    "VN-50",  # Bến Tre
    "VN-51",  # Trà Vinh
    "VN-52",  # Sóc Trăng
    "VN-53",  # Bắc Kạn
    "VN-54",  # Bắc Giang
    "VN-55",  # Bạc Liêu
    "VN-56",  # Bắc Ninh
    "VN-57",  # Bình Dương
    "VN-58",  # Bình Phước
    "VN-59",  # Cà Mau
    "VN-61",  # Hải Dương
    "VN-63",  # Hà Nam
    "VN-66",  # Hưng Yên
    "VN-67",  # Nam Định
    "VN-68",  # Phú Thọ
    "VN-69",  # Thái Nguyên
    "VN-70",  # Vĩnh Phúc
    "VN-71",  # Điện Biên
    "VN-72",  # Đắk Nông
    "VN-73",  # Hậu Giang
    "VN-CT",  # Cần Thơ
    "VN-DN",  # Đà Nẵng
    "VN-HN",  # Hà Nội
    "VN-HP",  # Hải Phòng
    "VN-SG",  # Hồ Chí Minh
    # Republic of Vanuatu
    "VU-MAP",  # Malampa
    "VU-PAM",  # Pénama
    "VU-SAM",  # Sanma
    "VU-SEE",  # Shéfa
    "VU-TAE",  # Taféa
    "VU-TOB",  # Torba
    # Wallis and Futuna
    "WF-AL",  # Alo
    "WF-SG",  # Sigave
    "WF-UV",  # Uvea
    # Independent State of Samoa
    "WS-AA",  # A'ana
    "WS-AL",  # Aiga-i-le-Tai
    "WS-AT",  # Atua
    "WS-FA",  # Fa'asaleleaga
    "WS-GE",  # Gaga'emauga
    "WS-GI",  # Gagaifomauga
    "WS-PA",  # Palauli
    "WS-SA",  # Satupa'itea
    "WS-TU",  # Tuamasaga
    "WS-VF",  # Va'a-o-Fonoti
    "WS-VS",  # Vaisigano
    # Republic of Yemen
    "YE-AB",  # Abyan
    "YE-AD",  # ‘Adan
    "YE-AM",  # ‘Amrān
    "YE-BA",  # Al Bayḑā’
    "YE-DA",  # Aḑ Ḑāli‘
    "YE-DH",  # Dhamār
    "YE-HD",  # Ḩaḑramawt
    "YE-HJ",  # Ḩajjah
    "YE-HU",  # Al Ḩudaydah
    "YE-IB",  # Ibb
    "YE-JA",  # Al Jawf
    "YE-LA",  # Laḩij
    "YE-MA",  # Ma’rib
    "YE-MR",  # Al Mahrah
    "YE-MW",  # Al Maḩwīt
    "YE-RA",  # Raymah
    "YE-SA",  # Amānat al ‘Āşimah [city]
    "YE-SD",  # Şāʻdah
    "YE-SH",  # Shabwah
    "YE-SN",  # Şanʻā’
    "YE-SU",  # Arkhabīl Suquţrá
    "YE-TA",  # Tāʻizz
    # Mayotte
    # (no subdivisions)
    # Republic of South Africa
    "ZA-EC",  # Eastern Cape
    "ZA-FS",  # Free State
    "ZA-GP",  # Gauteng
    "ZA-KZN",  # Kwazulu-Natal
    "ZA-LP",  # Limpopo
    "ZA-MP",  # Mpumalanga
    "ZA-NC",  # Northern Cape
    "ZA-NW",  # North-West
    "ZA-WC",  # Western Cape
    # Republic of Zambia
    "ZM-01",  # Western
    "ZM-02",  # Central
    "ZM-03",  # Eastern
    "ZM-04",  # Luapula
    "ZM-05",  # Northern
    "ZM-06",  # North-Western
    "ZM-07",  # Southern
    "ZM-08",  # Copperbelt
    "ZM-09",  # Lusaka
    "ZM-10",  # Muchinga
    # Republic of Zimbabwe
    "ZW-BU",  # Bulawayo
    "ZW-HA",  # Harare
    "ZW-MA",  # Manicaland
    "ZW-MC",  # Mashonaland Central
    "ZW-ME",  # Mashonaland East
    "ZW-MI",  # Midlands
    "ZW-MN",  # Matabeleland North
    "ZW-MS",  # Matabeleland South
    "ZW-MV",  # Masvingo
    "ZW-MW",  # Mashonaland West
]
