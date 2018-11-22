# Tests for inflecting Finnish words
#
# Copyright (c) 2018 Tatu Ylonen.  See LICENSE and https://ylonen.org

import unittest
import wiktfinnish

testcases = [
    ["fi-decl-valo", {"1": "val", "2": "", "3": "", "4": "o", "5": "a"},
     ["nom-sg", "valo"],
     ["ine-pl", "valoissa"],
     [("", "", "tra-pl", "1s", "kO"), "valoikseniko"]],
    ["fi-decl-valo", {"1": "lä", "2": "mp", "3": "mm", "4": "ö", "5": "ä"},
     [("", "", "tra-sg", "3x", "hAn"), "lämmöksensähän"]],
    ["fi-decl-valo", {"1": "liu", "2": "k", "3": "'", "4": "u", "5": "a"},
     ["gen-sg", "liu'un"]],
    ["fi-decl-palvelu", {"1": "palvelu", "2": "a"},
     ["gen-pl", "palvelujen"],
     ["gen-pl", "palveluitten"],
     ["ill-sg", "palveluun"]],
    ["fi-decl-palvelu", {"1": "yhtälö", "2": "ä"},
     ["ptv-sg", "yhtälöä"]],
    ["fi-decl-valtio", {"1": "valtio", "2": "a"},
     ["nom-pl", "valtiot"],
     ["cmt", "valtioineen"]],
    ["fi-decl-laatikko",
     {"1": "laati", "2": "kk", "3": "k", "4": "o", "5": "a"},
     ["ade-sg", "laatikolla"],
     ["ill-sg", "laatikkoon"]],
    ["fi-decl-risti", {"1": "rist", "4": "ä"},
     ["ptv-pl", "ristejä"]],
    ["fi-decl-risti", {"1": "vah", "2": "t", "3": "d", "4": "a"},
     ["nom-pl", "vahdit"],
     ["ela-pl", "vahdeista"]],
    ["fi-decl-risti", {"1": "het", "4": "ä", "i": "0"},
     ["nom-sg", "het"],
     ["ade-sg", "hetillä"]],
    ["fi-decl-paperi", {"1": "paper", "2": "a"},
     ["ptv-pl", "papereita"]],
    ["fi-decl-ovi", {"1": "ov", "4": "a"},
     ["abe-sg", "ovetta"]],
    ["fi-decl-nalle", {"1": "nall", "4": "a"},
     ["nom-sg", "nalle"],
     ["gen-pl", "nallejen"]],
    ["fi-decl-nalle", {"1": "olkinu", "2": "kk", "3": "k", "4": "a"},
     ["abl-pl", "olkinukeilta"]],
    ["fi-decl-kala", {"1": "kal", "4": "a"},
     ["nom-pl", "kalat"],
     ["ptv-pl", "kaloja"]],
    ["fi-decl-kala", {"1": "böön", "4": "a"},
     ["nom-sg", "bööna"]],
    ["fi-decl-kala", {"1": "ekstr", "4": "a"},
     ["all-pl", "ekstroille"]],
    ["fi-decl-kala", {"1": "helky", "2": "nt", "3": "nn", "4": "ä"},
     ["nom-pl", "helkynnät"]],
    ["fi-decl-kala", {"1": "ha", "2": "k", "3": "", "4": "a"},
     ["gen-sg", "haan"]],
    ["fi-decl-koira", {"1": "koir", "4": "a"},
     ["nom-sg", "koira"],
     ["abe-pl", "koiritta"]],
    ["fi-decl-koira", {"1": "ku", "2": "nt", "3": "nn", "4": "a"},
     ["ine-pl", "kunnissa"],
     ["ptv-sg", "kuntaa"]],
    ["fi-decl-omena", {"1": "omen", "2": "a"},
     ["ine-pl", "omenoissa"],
     ["ine-pl", "omenissa"]],
    ["fi-decl-kulkija", {"1": "kulkij", "2": "a"},
     ["ine-pl", "kulkijoissa"],
     ["ill-pl", "kulkijoihin"]],
    ["fi-decl-katiska", {"1": "katisk", "2": "a"},
     ["ptv-pl", "katiskoja"]],
    ["fi-decl-solakka", {"1": "sila", "2": "kk", "3": "k", "4": "a"},
     ["ptv-pl", "silakoita"],
     ["ill-sg", "silakkaan"]],
    ["fi-decl-solakka", {"1": "känny", "2": "kk", "3": "k", "4": "ä"},
     ["ptv-sg", "kännykkää"],
     ["ade-pl", "kännyköillä"]],
    ["fi-decl-korkea", {"1": "korke", "2": "a", "pos": "adj"},
     ["ess-pl", "korkeina"]],
    ["fi-decl-vanhempi", {"1": "vanhe", "2": "a", "pos": "adj"},
     ["ine-sg", "vanhemmassa"]],
    ["fi-decl-vapaa", {"1": "vapa", "2": "a", "pos": "adj"},
     ["cmt", "vapaine"]],
    ["fi-decl-vapaa", {"1": "taku", "2": "a"},
     ["nom-pl", "takuut"],
     ["nom-sg", "takuu"],
     ["abe-pl", "takuitta"],
     ["tra-pl", "takuiksi"]],
    ["fi-decl-maa", {"1": "maa", "2": "a"},
     ["gen-pl", "maiden"]],
    ["fi-decl-suo", {"1": "suo", "2": "a"},
     ["gen-pl", "soiden"]],
    ["fi-decl-suo", {"1": "työ", "2": "ä"},
     ["ine-pl", "töissä"]],
    ["fi-decl-filee", {"1": "filee", "2": "ä"},
     ["nom-pl", "fileet"],
     ["tra-pl", "fileiksi"]],
    ["fi-decl-rosé", {"1": "rosé", "2": "a", "ill_sg_vowel": "e"},
     ["ill-sg", "roséhen"]],
    ["fi-decl-parfait", {"1": "parfait", "2": "a", "ill_sg_vowel": "e"},
     ["ill-sg", "parfait'hen"]],
    ["fi-decl-tiili", {"1": "tiil", "2": "ä"},
     ["ptv-sg", "tiiltä"]],
    ["fi-decl-uni", {"1": "un", "2": "a"},
     ["gen-sg", "unen"],
     ["ill-pl", "uniin"],
     ["ptv-sg", "unta"]],
    ["fi-decl-uni", {"1": "mer", "2": "ä", "par_sg_a": "a"},
     ["ine-sg", "meressä"],
     ["ptv-sg", "merta"]],
    ["fi-decl-toimi", {"1": "toi", "2": "a"},
     ["ine-sg", "toimessa"]],
    ["fi-decl-pieni", {"1": "pien", "2": "ä", "pos": "adj"},
     ["nom-sg", "pieni"],
     ["ptv-sg", "pientä"],
     ["ill-sg", "pieneen"]],
    ["fi-decl-pieni", {"1": "ver", "2": "ä", "par_sg_a": "a"},
     ["ine-sg", "veressä"],
     ["ptv-sg", "verta"]],
    ["fi-decl-käsi", {"1": "kä", "2": "ä"},
     ["abe-sg", "kädettä"],
     ["abe-pl", "käsittä"]],
    ["fi-decl-kynsi", {"1": "kyn", "2": "ä"},
     ["gen-sg", "kynnen"],
     ["ptv-sg", "kynttä"],
     ["nom-sg", "kynsi"]],
    ["fi-decl-kynsi", {"1": "kan", "2": "a"},
     ["gen-sg", "kannen"],
     ["ptv-sg", "kantta"],
     ["ess-sg", "kantena"],
     ["nom-sg", "kansi"]],
    ["fi-decl-lapsi", {"1": "lap", "2": "a"},
     ["ptv-sg", "lasta"],
     ["gen-sg", "lapsen"]],
    ["fi-decl-veitsi", {"1": "vei", "2": "ä"},
     ["ptv-sg", "veistä"],
     ["all-sg", "veitselle"]],
    ["fi-decl-kaksi", {"1": "ka", "2": "a"},
     ["nom-sg", "kaksi"],
     ["ptv-sg", "kahta"],
     ["tra-sg", "kahdeksi"]],
    ["fi-decl-sisar", {"1": "sis", "4": "ar", "5": "a"},
     ["ptv-sg", "sisarta"]],
    ["fi-decl-sisar", {"1": "kauno", "2": "t", "3": "tt", "4": "ar", "5": "a"},
     ["ptv-pl", "kaunottaria"],
     ["gen-pl", "kaunotarten"]],
    ["fi-decl-sisar", {"1": "säv", "4": "el", "5": "ä"},
     ["ine-sg", "sävelessä"]],
    ["fi-decl-kytkin", {"1": "kytk", "4": "i", "5": "ä"},
     ["ptv-sg", "kytkintä"],
     ["ins-pl", "kytkimin"]],
    ["fi-decl-kytkin", {"1": "juo", "2": "t", "3": "tt", "4": "i", "5": "a"},
     ["ade-sg", "juottimella"]],
    ["fi-decl-kytkin", {"1": "aske", "2": "ll", "3": "lt", "4": "i", "5": "a"},
     ["ade-pl", "askeltimilla"]],
    ["fi-decl-onneton", {"1": "onne", "2": "a", "pos": "adj"},
     ["nom-pl", "onnettomat"]],
    ["fi-decl-onneton", {"1": "hävy", "2": "ä", "pos": "adj"},
     ["ine-sg", "hävyttömässä"]],
    ["fi-decl-lämmin", {"pos": "adj"},
     ["nom-pl", "lämpimät"]],
    ["fi-decl-sisin", {"1": "sis", "2": "ä", "pos": "adj"},
     ["ine-sg", "sisimmässä"],
     ["ess-pl", "sisimpinä"]],
    ["fi-decl-vasen", {"pos": "adj"},
     ["nom-sg", "vasen"],
     ["ptv-pl", "vasempia"]],
    ["fi-decl-nainen", {"1": "nai", "2": "a"},
     ["nom-sg", "nainen"],
     ["nom-pl", "naiset"],
     ["abl-pl", "naisilta"]],
    ["fi-decl-vastaus", {"1": "vastau", "2": "a"},
     ["gen-sg", "vastauksen"]],
    ["fi-decl-kalleus", {"1": "kalleu", "2": "a"},
     ["ptv-sg", "kalleutta"]],
    ["fi-decl-vieras", {"1": "vier", "4": "a", "5": "a"},
     ["ptv-sg", "vierasta"],
     ["gen-sg", "vieraan"],
     ["ill-sg", "vieraaseen"]],
    ["fi-decl-vieras", {"1": "rai", "2": "k", "3": "kk", "4": "a", "5": "a",
                        "pos": "adj"},
     ["ade-pl", "raikkailla"],
     ["ela-sg", "raikkaasta"],
     ["ptv-sg", "raikasta"]],
    ["fi-decl-mies", {},
     ["nom-sg", "mies"],
     ["nom-pl", "miehet"],
     ["abl-pl", "miehiltä"]],
    ["fi-decl-ohut", {"1": "oh", "4": "u", "5": "a"},
     ["ptv-sg", "ohutta"]],
    ["fi-decl-ohut", {"1": "i", "2": "mm", "3": "mp", "4": "y", "5": "ä"},
     ["nom-sg", "immyt"],
     ["gen-sg", "impyen"]],
    ["fi-decl-kevät", {"1": "kevä", "2": "ä"},
     ["gen-pl", "keväiden"]],
    ["fi-decl-kahdeksas", {"1": "kahdeksa", "2": "a"},
     ["gen-sg", "kahdeksannen"]],
    ["fi-decl-tuhat", {"1": "tuha", "2": "a", "pos": "adj"},
     ["nom-sg", "tuhat"],
     ["gen-pl", "tuhansien"]],
    ["fi-decl-kuollut", {"1": "kuoll", "2": "a", "pos": "adj"},
     ["ine-pl", "kuolleissa"],
     ["gen-sg", "kuolleen"]],
    ["fi-decl-hame", {"1": "ham", "4": "a"},
     ["gen-sg", "hameen"]],
    ["fi-decl-hame", {"1": "mu", "2": "rr", "3": "rt", "4": "a"},
     ["gen-pl", "murteiden"]],
    ["fi-decl-maa-dot", {"1": "DNA", "2": "a", "3": "a"},
     [("", "", "nom-sg", "", "kO"), "DNA:ko"],
     ["gen-sg", "DNA:n"]],
    ["fi-decl", {
        "nom_sg": "nuoripari",
        "gen_sg": "nuorenparin",
        "par_sg": "nuortaparia",
        "ine_sg": "nuoressaparissa",
        "ela_sg": "nuorestaparista",
        "ill_sg": "nuoreenpariin",
        "ade_sg": "nuorellaparilla",
        "abl_sg": "nuoreltaparilta",
        "all_sg": "nuorelleparille",
        "ess_sg": "nuorenaparina",
        "tra_sg": "nuoreksipariksi",
        "abe_sg": "nuorettaparitta",
        "nom_pl": "nuoretparit",
        "gen_pl": "nuortenparien",
        "gen_pl2": "nuorienparien",
        "par_pl": "nuoriapareja",
        "ine_pl": "nuorissapareissa",
        "ela_pl": "nuoristapareista",
        "ill_pl": "nuoriinpareihin",
        "ade_pl": "nuorillapareilla",
        "abl_pl": "nuoriltapareilta",
        "all_pl": "nuorillepareille",
        "ess_pl": "nuorinapareina",
        "tra_pl": "nuoriksipareiksi",
        "ins_pl": "nuorinparein",
        "abe_pl": "nuorittapareitta",
        "com_pl": "nuorinepareineen",
    },
     ["nom-sg", "nuoripari"],
     ["gen-sg", "nuorenparin"],
     ["ptv-sg", "nuortaparia"],
     ["ine-sg", "nuoressaparissa"],
     ["ela-sg", "nuorestaparista"],
     ["ill-sg", "nuoreenpariin"],
     ["ade-sg", "nuorellaparilla"],
     ["abl-sg", "nuoreltaparilta"],
     ["all-sg", "nuorelleparille"],
     ["ess-sg", "nuorenaparina"],
     ["tra-sg", "nuoreksipariksi"],
     ["abe-sg", "nuorettaparitta"],
     ["nom-pl", "nuoretparit"],
     ["gen-pl", "nuortenparien"],
     ["gen-pl", "nuorienparien"],
     ["ptv-pl", "nuoriapareja"],
     ["ine-pl", "nuorissapareissa"],
     ["ela-pl", "nuoristapareista"],
     ["ill-pl", "nuoriinpareihin"],
     ["ade-pl", "nuorillapareilla"],
     ["abl-pl", "nuoriltapareilta"],
     ["all-pl", "nuorillepareille"],
     ["ess-pl", "nuorinapareina"],
     ["tra-pl", "nuoriksipareiksi"],
     ["ins-pl", "nuorinparein"],
     ["abe-pl", "nuorittapareitta"],
     ["cmt", "nuorinepareineen"],
     [("", "", "tra-sg", "3x", ""), "nuoreksipariksensa"],
     [("", "", "gen-sg", "1s", ""), "nuorenparini"],
     [("", "", "gen-sg", "", "kO"), "nuorenparinko"],
     [("", "", "tra-pl", "", "kO"), "nuoriksipareiksiko"],
    ],
    ["fi-decl-pron", {"type": "koira", "1s": "'''seitsem\u00e4n''' (*)", "2s": "'''seitsem\u00e4n'''", "3s": "[[seitsem\u00e4\u00e4]]", "4s": "'''seitsem\u00e4n'''", "5s": "[[seitsem\u00e4ss\u00e4]]", "6s": "[[seitsem\u00e4st\u00e4]]", "7s": "[[seitsem\u00e4\u00e4n]]", "8s": "[[seitsem\u00e4ll\u00e4]]", "9s": "[[seitsem\u00e4lt\u00e4]]", "10s": "[[seitsem\u00e4lle]]", "11s": "[[seitsem\u00e4n\u00e4]]", "12s": "[[seitsem\u00e4ksi]]", "14s": "[[seitsem\u00e4tt\u00e4]]", "1p": "[[seitsem\u00e4t]]", "2p": "[[seitsemien]]", "3p": "[[seitsemi\u00e4]]", "4p": "[[seitsem\u00e4t]]", "5p": "[[seitsemiss\u00e4]]", "6p": "[[seitsemist\u00e4]]", "7p": "[[seitsemiin]]", "8p": "[[seitsemill\u00e4]]", "9p": "[[seitsemilt\u00e4]]", "10p": "[[seitsemille]]", "11p": "[[seitsemin\u00e4]]", "12p": "[[seitsemiksi]]", "13p": "[[seitsemin]]", "14p": "[[seitsemitt\u00e4]]", "15p": "[[seitsemine]]", "a7s": "[[seitsem\u00e4sti]]", "template_name": "fi-decl-pron", "pos": "num"},
     ["nom-sg", "seitsemän"],
     ["gen-sg", "seitsemän"],
     ["ptv-sg", "seitsemää"],
     ["ine-sg", "seitsemässä"],
     ["ela-sg", "seitsemästä"],
     ["ill-sg", "seitsemään"],
     ["ade-sg", "seitsemällä"],
     ["abl-sg", "seitsemältä"],
     ["all-sg", "seitsemälle"],
     ["ess-sg", "seitsemänä"],
     ["tra-sg", "seitsemäksi"],
     ["nom-pl", "seitsemät"],
     ["gen-pl", "seitsemien"],
     ["ptv-pl", "seitsemiä"],
     ["ine-pl", "seitsemissä"],
     ["ela-pl", "seitsemistä"],
     ["ill-pl", "seitsemiin"],
     ["ade-pl", "seitsemillä"],
     ["abl-pl", "seitsemiltä"],
     ["all-pl", "seitsemille"],
     ["ess-pl", "seitseminä"],
     ["tra-pl", "seitsemiksi"],
     ["ins-pl", "seitsemin"],
     ["abe-pl", "seitsemittä"],
     ["cmt", "seitsemine"],
     [("", "", "gen-sg", "2s", ""), "seitsemäsi"],
     [("", "", "gen-sg", "", "kin"), "seitsemänkin"]],

    ["fi-decl-pron", {"1s": "[[se]]", "2s": "[[sen#Finnish|sen]]", "3s": "[[sit\u00e4]]", "4s": "[[se]], [[sen#Finnish|sen]]", "5s": "[[siin\u00e4]]", "6s": "[[siit\u00e4]]", "7s": "[[siihen]]", "8s": "[[sill\u00e4]]", "9s": "[[silt\u00e4]]", "10s": "[[sille]]", "11s": "[[sin\u00e4]]", "12s": "[[siksi]]", "1p": "[[ne]]", "2p": "[[niiden]], [[niitten]]", "3p": "[[niit\u00e4]]", "4p": "[[ne]]", "5p": "[[niiss\u00e4]]", "6p": "[[niist\u00e4]]", "7p": "[[niihin]]", "8p": "[[niill\u00e4]]", "9p": "[[niilt\u00e4]]", "10p": "[[niille]]", "11p": "[[niin\u00e4]]", "12p": "[[niiksi]]", "13p": "([[niin]])", "14p": "([[niitt\u00e4]])", "15p": "[[niine]]", "a1s": "[[siell\u00e4]]", "a2s": "[[sielt\u00e4]]", "a3s": "[[sinne]]", "a4s": "[[siis]]", "a5s": "[[silloin]]", "a6s": "[[siten]]", "template_name": "fi-decl-pron", "pos": "pron"},
     ["nom-sg", "se"],
     ["gen-sg", "sen"],
     ["ptv-sg", "sitä"],
     ["acc-sg", "se"],
     ["acc-sg", "sen"],
     ["ine-sg", "siinä"],
     ["ela-sg", "siitä"],
     ["ill-sg", "siihen"],
     ["ade-sg", "sillä"],
     ["abl-sg", "siltä"],
     ["all-sg", "sille"],
     ["ess-sg", "sinä"],
     ["tra-sg", "siksi"],
     ["nom-pl", "ne"],
     ["gen-pl", "niiden"],
     ["ptv-pl", "niitä"],
     ["acc-pl", "ne"],
     ["ine-pl", "niissä"],
     ["ela-pl", "niistä"],
     ["ill-pl", "niihin"],
     ["ade-pl", "niillä"],
     ["abl-pl", "niiltä"],
     ["all-pl", "niille"],
     ["ess-pl", "niinä"],
     ["tra-pl", "niiksi"],
     ["ins-pl", "niin"],
     ["abe-pl", "niittä"],
     ["cmt", "niine"],
    ],
    ["fi-decl-käsi-kulkija", {1: 'Uu', 2: 'a', 'space': '-', 3: 'Kaledoni', 4: 'a', 'nopl': '1', 'name': 'fi-decl-käsi-kulkija'},
     ["gen-sg", "Uuden-Kaledonian"]],
    ["fi-decl-käsi-maa", {'nopl': '1', 1: 'Uu', 2: 'a', 3: 'kaarlep', 4: 'y', 5: 'y', 6: 'ä', 'space': '', 'name': 'fi-decl-käsi-maa'},
     ["ine-sg", "Uudessakaarlepyyssä"]],
    ["fi-decl-käsi-risti", {1: 'Uu', 2: 'a', 3: 'Seela', 4: 'nt', 5: 'nn', 6: 'a', 'space': '-', 'name': 'fi-decl-käsi-risti'},
     ["ela-sg", "Uudesta-Seelannista"]],
    ["fi-decl-käsi-risti", {'nopl': '1', 1: 'Uu', 2: 'a', 3: 'kaupu', 4: 'nk', 5: 'ng', 6: 'a', 'space': '', 'name': 'fi-decl-käsi-risti'},
     [("", "", "gen-sg", "", "kO"), "Uudenkaupunginko"]],
    ["fi-decl-koira-kala", {1: 'nelj', 2: '', 3: '', 4: 'ä', 5: 'sa', 6: 't', 7: 'd', 'word': 'neljäsataa', 'space': '', 'name': 'fi-decl-koira-kala'},
     ["gen-sg", "neljänsadan"]],
    ["fi-decl-pieni-uni", {1: 'Tyyn', 2: 'ä', 'space': '', 3: 'mer', 4: 'ä', 'par_sg_a': 'a', 'nopl': '1', 'name': 'fi-decl-pieni-uni'},
     ["ptv-sg", "Tyyntämerta"]],
    ["fi-decl-valo-koira", {1: 'Is', 2: '', 3: '', 4: 'o', 5: 'a', 'space': '-', 6: 'Britanni', 7: '', 8: '', 9: 'a', 'nopl': '1', 'name': 'fi-decl-valo-koira'},
     ["ine-sg", "Isossa-Britanniassa"]],
    ["fi-conj-sanoa", {"1": "luu", "2": "t", "3": "d", "4": "u", "5": "a"},
     [("pres-part", "comp", "gen-sg", "", "kin"), "luutuvammankin"]],
    ["fi-conj-muistaa", {"1": "astu", "2": "tt", "3": "t", "4": "a"},
     [("past-3sg", "", "", "", ""), "astutti"],
     [("inf4-nom", "", "", "", ""), "astuttaminen"]],
    ["fi-conj-huutaa", {"1": "huu", "2": "a"},
     [("past-2sg", "", "", "", ""), "huusit"]],
    ["fi-conj-soutaa", {"1": "sou", "2": "a"},
     [("pres-1sg", "", "", "", ""), "soudan"]],
    ["fi-conj-soutaa", {"1": "kyn", "2": "ä"},
     [("inf2-pass-ine", "", "", "", ""), "kynnettäessä"]],
    ["fi-conj-kaivaa", {"1": "ah", "2": "t", "3": "d", "4": "a"},
     [("inf1", "", "", "", ""), "ahtaa"],
     [("pres-pass", "", "", "", ""), "ahdetaan"]],
    ["fi-conj-saartaa", {"1": "saar", "2": "a"},
     [("pres-1sg", "", "", "", ""), "saarran"],
     [("past-1sg", "", "", "", ""), "saarroin"],
     [("past-1sg", "", "", "", ""), "saarsin"]],
    ["fi-conj-laskea", {"1": "ry", "2": "p", "3": "v", "4": "ä"},
     [("potn-1sg", "", "", "", ""), "rypenen"],
     [("cond-pass", "", "", "", ""), "ryvettäisiin"]],
    ["fi-conj-tuntea", {"1": "tun", "2": "a"},
     [("past-1pl", "", "", "", ""), "tunsimme"]],
    ["fi-conj-lähteä", {"1": "lä", "2": "ä"},
     [("past-2pl", "", "", "", ""), "lähditte"]],
    ["fi-conj-sallia", {"1": "vaa", "2": "t", "3": "d", "4": "a"},
     [("past-part", "", "", "", ""), "vaatinut"],
     [("past-pass-part", "", "", "", ""), "vaadittu"]],
    ["fi-conj-voida", {"1": "voi", "2": "a"},
     [("pres-3pl", "", "", "", ""), "voivat"],
     [("inf2-pass-ine", "", "", "", ""), "voitaessa"]],
    ["fi-conj-saada", {"1": "my", "2": "ä"},
     [("impr-pass-neg", "", "", "", ""), "myytäkö"]],
    ["fi-conj-saada", {"1": "sa", "2": "a"},
     [("impr-pass-neg", "", "", "", ""), "saatako"]],
    ["fi-conj-juoda", {"1": "juo", "2": "a"},
     [("past-1sg", "", "", "", ""), "join"]],
    ["fi-conj-käydä", {"1": "käy", "2": "ä"},
     [("past-1sg", "", "", "", ""), "kävin"]],
    ["fi-conj-rohkaista", {"1": "va", "2": "v", "3": "p", "4": "i", "5": "a"},
     [("pres-1sg", "", "", "", ""), "vapisen"],
     [("inf1-long", "", "", "", ""), "vavistakseen"]],
    ["fi-conj-rohkaista", {"1": "öl", "2": "", "3": "", "4": "i", "5": "ä"},
     [("inf1", "", "", "", ""), "ölistä"],
     [("pres-neg", "", "", "", ""), "ölise"]],
    ["fi-conj-tulla", {"1": "est", "2": "", "3": "", "4": "el", "5": "ä"},
     [("potn-3sg", "", "", "", ""), "estellee"]],
    ["fi-conj-tulla", {"1": "p", "2": "", "3": "", "4": "ur", "5": "a"},
     [("inf1", "", "", "", ""), "purra"],
     [("pres-part", "", "", "", ""), "pureva"],
     [("pres-pass-part", "", "", "", ""), "purtava"]],
    ["fi-conj-tulla", {"1": "kaljoi", "2": "t", "3": "tt", "4": "el",
                       "5": "a"},
     [("past-1pl", "", "", "", ""), "kaljoittelimme"]],
    ["fi-conj-tulla", {"1": "p", "2": "", "3": "", "4": "an", "5": "a"},
     [("inf1", "", "", "", ""), "panna"],
     [("past-2sg", "", "", "", "kO"), "panitko"]],
    ["fi-conj-tupakoida", {"1": "tupakoi", "2": "a"},
     [("cond-1sg", "", "", "", ""), "tupakoisin"],
     [("cond-1sg", "", "", "", ""), "tupakoitsisin"]],
    ["fi-conj-valita", {"1": "vali", "2": "a"},
     [("cond-3sg-or-neg", "", "", "", ""), "valitsisi"]],
    ["fi-conj-juosta", {"1": "juo", "2": "a"},
     [("inf1", "", "", "", ""), "juosta"],
     [("pres-1sg", "", "", "", ""), "juoksen"]],
    ["fi-conj-nähdä", {"1": "nä", "2": "ä"}],
    ["fi-conj-vanheta", {"1": "su", "2": "p", "3": "pp", "4": "e", "5": "a"},
     [("pres-3sg", "", "", "", ""), "suppenee"]],
    ["fi-conj-salata", {"1": "ha", "2": "k", "3": "kk", "4": "a"},
     [("inf4-nom", "", "", "2s", "kAAn"), "hakkaamisesikaan"]],
    ["fi-conj-katketa", {"1": "ka", "2": "d", "3": "t", "4": "o", "5": "a"},
     [("past-1sg", "", "", "", ""), "katosin"]],
    ["fi-conj-selvitä", {"1": "aa", "2": "ll", "3": "lt", "4": "o", "5": "a"},
     [("pres-3sg", "", "", "", ""), "aaltoaa"],
     [("inf2-ine", "", "", "", ""), "aallotessa"]],
    ["fi-conj-taitaa", {"1": "tai", "2": "a"},
     [("past-pass", "", "", "", ""), "taidettiin"]],
    ["fi-conj-taitaa", {"1": "tie", "2": "ä"},
     [("pres-1sg", "", "", "", ""), "tiedän"],
     [("past-1sg", "", "", "", ""), "tiesin"]],
    ["fi-conj-kaikaa", {"1": "paukk", "2": "a"},
     [("cond-3sg-or-neg", "", "", "", ""), "paukkaisi"],
     [("pres-3pl", "", "", "", ""), "paukkaavat"]],
    ["fi-conj-kumajaa", {"1": "kum"},
     [("inf1", "", "", "", ""), "kumajaa"],
     [("past-3pl", "", "", "", ""), "kumajivat"]],
    ["fi-conj-kumajaa", {"1": "hel", "2": "ä", "3": "y", "4": "ö"},
     [("inf1", "", "", "", ""), "heläjää"],
     [("past-pass", "", "", "", ""), "heläjättiin"]],
    ["fi-conj-kumajaa", {"1": "vip"},
     [("impr-2sg", "", "", "", ""), "vipaja"]],
    ["fi-conj-olla", {},
     [("inf1", "", "", "", ""), "olla"],
     [("pres-1sg", "", "", "", ""), "olen"],
     [("pres-2sg", "", "", "", ""), "olet"],
     [("pres-3sg", "", "", "", ""), "on"],
     [("pres-1pl", "", "", "", ""), "olemme"],
     [("pres-2pl", "", "", "", ""), "olette"],
     [("pres-3pl", "", "", "", ""), "ovat"],
     [("pres-pass", "", "", "", ""), "ollaan"],
     [("pres-neg", "", "", "", ""), "ole"],
     [("past-1sg", "", "", "", ""), "olin"],
     [("past-2sg", "", "", "", ""), "olit"],
     [("past-3sg", "", "", "", ""), "oli"],
     [("past-1pl", "", "", "", ""), "olimme"],
     [("past-2pl", "", "", "", ""), "olitte"],
     [("past-3pl", "", "", "", ""), "olivat"],
     [("past-pass", "", "", "", ""), "oltiin"],
     [("past-1sg-neg", "", "", "", ""), "ollut"],
     [("pres-part", "", "", "", ""), "oleva"],
     ],
    ["fi-conj-ei", {},
     [("pres-1sg", "", "", "", ""), "en"],
     [("pres-2sg", "", "", "", ""), "et"],
     [("pres-3sg", "", "", "", ""), "ei"],
     [("pres-1pl", "", "", "", ""), "emme"],
     [("pres-2pl", "", "", "", ""), "ette"],
     [("pres-3pl", "", "", "", ""), "eivät"],
     [("impr-2sg", "", "", "", ""), "älä"],
     [("impr-3sg", "", "", "", ""), "älköön"],
     [("impr-1pl", "", "", "", ""), "älkäämme"],
     [("impr-2pl", "", "", "", ""), "älkää"],
     [("impr-3pl", "", "", "", ""), "älkööt"],
     ],
    ["fi-conj-table", {"title": "t\u00e4yty\u00e4", "nav": "1", "pres_1sg": "[[minun]] [[t\u00e4ytyy]]", "pres_2sg": "[[sinun]] t\u00e4ytyy", "pres_3sg": "[[h\u00e4nen]] t\u00e4ytyy", "pres_1pl": "[[meid\u00e4n]] t\u00e4ytyy", "pres_2pl": "[[teid\u00e4n]] t\u00e4ytyy", "pres_3pl": "[[heid\u00e4n]] t\u00e4ytyy", "pres_pass": "t\u00e4ytyy", "pres_1sg_neg": "minun ei [[t\u00e4ydy]]", "pres_2sg_neg": "sinun ei t\u00e4ydy", "pres_3sg_neg": "h\u00e4nen ei t\u00e4ydy", "pres_1pl_neg": "meid\u00e4n ei t\u00e4ydy", "pres_2pl_neg": "teid\u00e4n ei t\u00e4ydy", "pres_3pl_neg": "heid\u00e4n ei t\u00e4ydy", "pres_pass_neg": "ei t\u00e4ydy", "pres_perf_1sg": "minun [[on]] [[t\u00e4ytynyt]]", "pres_perf_2sg": "sinun on t\u00e4ytynyt", "pres_perf_3sg": "h\u00e4nen on t\u00e4ytynyt", "pres_perf_1pl": "meid\u00e4n on t\u00e4ytynyt", "pres_perf_2pl": "teid\u00e4n on t\u00e4ytynyt", "pres_perf_3pl": "heid\u00e4n on t\u00e4ytynyt", "pres_perf_pass": "on t\u00e4ytynyt", "pres_perf_1sg_neg": "minun ei [[ole]] t\u00e4ytynyt", "pres_perf_2sg_neg": "sinun ei ole t\u00e4ytynyt", "pres_perf_3sg_neg": "h\u00e4nen ei ole t\u00e4ytynyt", "pres_perf_1pl_neg": "meid\u00e4n ei ole t\u00e4ytynyt", "pres_perf_2pl_neg": "teid\u00e4n ei ole t\u00e4ytynyt", "pres_perf_3pl_neg": "heid\u00e4n ei ole t\u00e4ytynyt", "pres_perf_pass_neg": "ei ole t\u00e4ytynyt", "past_1sg": "minun [[t\u00e4ytyi]]", "past_2sg": "sinun t\u00e4ytyi", "past_3sg": "h\u00e4nen t\u00e4ytyi", "past_1pl": "meid\u00e4n t\u00e4ytyi", "past_2pl": "teid\u00e4n t\u00e4ytyi", "past_3pl": "heid\u00e4n t\u00e4ytyi", "past_pass": "t\u00e4ytyi", "past_1sg_neg": "minun ei [[t\u00e4ytynyt]]", "past_2sg_neg": "sinun ei t\u00e4ytynyt", "past_3sg_neg": "h\u00e4nen ei t\u00e4ytynyt", "past_1pl_neg": "meid\u00e4n ei t\u00e4ytynyt", "past_2pl_neg": "teid\u00e4n ei t\u00e4ytynyt", "past_3pl_neg": "heid\u00e4n ei t\u00e4ytynyt", "past_pass_neg": "ei t\u00e4ytynyt", "past_perf_1sg": "minun [[oli]] [[t\u00e4ytynyt]]", "past_perf_2sg": "sinun oli t\u00e4ytynyt", "past_perf_3sg": "h\u00e4nen oli t\u00e4ytynyt", "past_perf_1pl": "meid\u00e4n oli t\u00e4ytynyt", "past_perf_2pl": "teid\u00e4n oli t\u00e4ytynyt", "past_perf_3pl": "heid\u00e4n oli t\u00e4ytynyt", "past_perf_pass": "oli t\u00e4ytynyt", "past_perf_1sg_neg": "minun ei [[ollut]] t\u00e4ytynyt", "past_perf_2sg_neg": "sinun ei ollut t\u00e4ytynyt", "past_perf_3sg_neg": "h\u00e4nen ei ollut t\u00e4ytynyt", "past_perf_1pl_neg": "meid\u00e4n ei ollut t\u00e4ytynyt", "past_perf_2pl_neg": "teid\u00e4n ei ollut t\u00e4ytynyt", "past_perf_3pl_neg": "heid\u00e4n ei ollut t\u00e4ytynyt", "past_perf_pass_neg": "ei ollut t\u00e4ytynyt", "cond_1sg": "minun [[t\u00e4ytyisi]]", "cond_2sg": "sinun t\u00e4ytyisi", "cond_3sg": "h\u00e4nen t\u00e4ytyisi", "cond_1pl": "meid\u00e4n t\u00e4ytyisi", "cond_2pl": "teid\u00e4n t\u00e4ytyisi", "cond_3pl": "heid\u00e4n t\u00e4ytyisi", "cond_pass": "t\u00e4ytyisi", "cond_1sg_neg": "minun ei t\u00e4ytyisi", "cond_2sg_neg": "sinun ei t\u00e4ytyisi", "cond_3sg_neg": "h\u00e4nen ei t\u00e4ytyisi", "cond_1pl_neg": "meid\u00e4n ei t\u00e4ytyisi", "cond_2pl_neg": "teid\u00e4n ei t\u00e4ytyisi", "cond_3pl_neg": "heid\u00e4n ei t\u00e4ytyisi", "cond_pass_neg": "ei t\u00e4ytyisi", "cond_perf_1sg": "minun [[olisi]] [[t\u00e4ytynyt]]", "cond_perf_2sg": "sinun olisi t\u00e4ytynyt", "cond_perf_3sg": "h\u00e4nen olisi t\u00e4ytynyt", "cond_perf_1pl": "meid\u00e4n olisi t\u00e4ytynyt", "cond_perf_2pl": "teid\u00e4n olisi t\u00e4ytynyt", "cond_perf_3pl": "heid\u00e4n olisi t\u00e4ytynyt", "cond_perf_pass": "sinun olisi t\u00e4ytynyt", "cond_perf_1sg_neg": "minun ei olisi t\u00e4ytynyt", "cond_perf_2sg_neg": "sinun ei olisi t\u00e4ytynyt", "cond_perf_3sg_neg": "h\u00e4nen ei olisi t\u00e4ytynyt", "cond_perf_1pl_neg": "meid\u00e4n ei olisi t\u00e4ytynyt", "cond_perf_2pl_neg": "teid\u00e4n ei olisi t\u00e4ytynyt", "cond_perf_3pl_neg": "heid\u00e4n ei olisi t\u00e4ytynyt", "cond_perf_pass_neg": "ei olisi t\u00e4ytynyt", "impr_2sg": "[[t\u00e4ytyk\u00f6\u00f6n]] sinun", "impr_3sg": "t\u00e4ytyk\u00f6\u00f6n h\u00e4nen", "impr_1pl": "t\u00e4ytyk\u00f6\u00f6n meid\u00e4n", "impr_2pl": "t\u00e4ytyk\u00f6\u00f6n teid\u00e4n", "impr_3pl": "t\u00e4ytyk\u00f6\u00f6n heid\u00e4n", "impr_pass": "t\u00e4ytyk\u00f6\u00f6n", "impr_2sg_neg": "[[\u00e4lk\u00f6\u00f6n]] sinun [[t\u00e4ytyk\u00f6]]", "impr_3sg_neg": "\u00e4lk\u00f6\u00f6n h\u00e4nen t\u00e4ytyk\u00f6", "impr_1pl_neg": "\u00e4lk\u00f6\u00f6n meid\u00e4n t\u00e4ytyk\u00f6", "impr_2pl_neg": "\u00e4lk\u00f6\u00f6n teid\u00e4n t\u00e4ytyk\u00f6", "impr_3pl_neg": "\u00e4lk\u00f6\u00f6n heid\u00e4n t\u00e4ytyk\u00f6", "impr_pass_neg": "\u00e4lk\u00f6\u00f6n t\u00e4ytyk\u00f6", "impr_perf_2sg": "-", "impr_perf_3sg": "-", "impr_perf_1pl": "-", "impr_perf_2pl": "-", "impr_perf_3pl": "-", "impr_perf_pass": "-", "impr_perf_2sg_neg": "-", "impr_perf_3sg_neg": "-", "impr_perf_1pl_neg": "-", "impr_perf_2pl_neg": "-", "impr_perf_3pl_neg": "-", "impr_perf_pass_neg": "-", "potn_1sg": "minun [[t\u00e4ytynee]]", "potn_2sg": "sinun t\u00e4ytynee", "potn_3sg": "h\u00e4nen t\u00e4ytynee", "potn_1pl": "meid\u00e4n t\u00e4ytynee", "potn_2pl": "teid\u00e4n t\u00e4ytynee", "potn_3pl": "heid\u00e4n t\u00e4ytynee", "potn_pass": "t\u00e4ytynee", "potn_1sg_neg": "minun ei [[t\u00e4ytyne]]", "potn_2sg_neg": "sinun ei t\u00e4ytyne", "potn_3sg_neg": "h\u00e4nen ei t\u00e4ytyne", "potn_1pl_neg": "meid\u00e4n ei t\u00e4ytyne", "potn_2pl_neg": "teid\u00e4n ei t\u00e4ytyne", "potn_3pl_neg": "heid\u00e4n ei t\u00e4ytyne", "potn_pass_neg": "ei t\u00e4ytyne", "potn_perf_1sg": "-", "potn_perf_2sg": "-", "potn_perf_3sg": "-", "potn_perf_1pl": "-", "potn_perf_2pl": "-", "potn_perf_3pl": "-", "potn_perf_pass": "-", "potn_perf_1sg_neg": "-", "potn_perf_2sg_neg": "-", "potn_perf_3sg_neg": "-", "potn_perf_1pl_neg": "-", "potn_perf_2pl_neg": "-", "potn_perf_3pl_neg": "-", "potn_perf_pass_neg": "-", "inf1": "t\u00e4yty\u00e4", "inf1_long": "-<sup>2</sup>", "inf2_ine": "-<sup>1</sup>", "inf2_pass_ine": "-", "inf2_ins": "-", "inf3_ine": "-", "inf3_ela": "-", "inf3_ill": "-", "inf3_ade": "-", "inf3_abe": "-", "inf3_ins": "-", "inf3_pass_ins": "-", "inf4_nom": "[[t\u00e4ytyminen]]", "inf4_par": "[[t\u00e4ytymist\u00e4]]", "inf5": "-<sup>2</sup>", "pres_part": "-", "pres_pass_part": "-", "past_part": "-", "past_pass_part": "-", "agnt_part": "-<sup>1,&nbsp;3</sup>", "nega_part": "-", "template_name": "fi-conj-table"},
     [("inf1", "", "", "", ""), "täytyä"],
     [("pres-1sg", "", "", "", ""), "täytyy"],
     [("pres-neg", "", "", "", ""), "täydy"],
     [("past-2sg", "", "", "", ""), "täytyi"],
     [("cond-3sg-or-neg", "", "", "", ""), "täytyisi"],
     [("potn-1pl", "", "", "", ""), "täytynee"],
     ],

    ["fi-conj", {'type': 'selvitä', 'nav': '1', 'pres_1sg': 'kutian', 'pres_2sg': 'kutiat', 'pres_3sg': 'kutiaa', 'pres_1pl': 'kutiamme', 'pres_2pl': 'kutiatte', 'pres_3pl': 'kutiavat', 'pres_pass': 'kutistaan', 'pres_conn': 'kutia', 'pres_pass_conn': 'kutista', 'past_1sg': 'kutisin', 'past_2sg': 'kutisit', 'past_3sg': 'kutisi', 'past_1pl': 'kutisimme', 'past_2pl': 'kutisitte', 'past_3pl': 'kutisivat', 'past_pass': 'kutistiin', 'cond_1sg': 'kutiaisin', 'cond_2sg': 'kutiaisit', 'cond_1pl': 'kutiaisimme', 'cond_2pl': 'kutiaisitte', 'cond_3pl': 'kutiaisivat', 'cond_pass': 'kutistaisiin', 'cond_conn': 'kutiaisi', 'cond_pass_conn': 'kutistaisi', 'impr_3sg': 'kutiskoon', 'impr_1pl': 'kutiskaamme', 'impr_2pl': 'kutiskaa', 'impr_3pl': 'kutiskoot', 'impr_pass': 'kutistakoon', 'impr_conn': 'kutisko', 'impr_pass_conn': 'kutistako', 'potn_1sg': 'kutissen', 'potn_2sg': 'kutisset', 'potn_3sg': 'kutissee', 'potn_1pl': 'kutissemme', 'potn_2pl': 'kutissette', 'potn_3pl': 'kutissevat', 'potn_pass': 'kutistaneen', 'potn_conn': 'kutisse', 'potn_pass_conn': 'kutistane', 'inf1_longa': 'kutistakseen', 'inf2_ines': 'kutistessa', 'inf2_pass_ines': '–', 'inf2_inst': 'kutisten', 'inf3_ines': 'kutiamassa', 'inf3_elat': 'kutiamasta', 'inf3_illa': 'kutiamaan', 'inf3_ades': 'kutiamalla', 'inf3_abes': 'kutiamatta', 'inf3_inst': 'kutiaman', 'inf3_pass_inst': 'kutistaman', 'inf4_nomi': 'kutiaminen', 'inf4_part': 'kutiamista', 'inf5': 'kutiamaisillaan', 'pres_part': 'kutiava', 'pres_pass_part': 'kutistava', 'past_part': 'kutissut', 'past_part_pl': 'kutisseet', 'past_pass_part': 'kutistu', 'agnt_part': '–', 'nega_part': 'kutiamaton', 'name': 'fi-conj'},
     [("pres-neg", "", "", "", ""), "kutia"]],
    ["fi-conj-seistä", {},
     [("inf1", "", "", "", ""), "seistä"],
     [("pres-3sg", "", "", "", ""), "seisoo"],
     [("pres-pass", "", "", "", ""), "seistään"]],
    ["fi-conj-virkkaa", {},
     [("pres-1sg", "", "", "", ""), "virkan"],
     [("past-3sg", "", "", "", ""), "virkkoi"]],
]

class InflectTests(unittest.TestCase):

    def test_forms(self):
        for lst in testcases:
            name = lst[0]
            args = lst[1]
            for form, result in lst[2:]:
                if isinstance(form, str):
                    form = ("", "", form, "", "")
                ret = wiktfinnish.inflect(name, args, form)
                if result not in ret:
                    print(name, args, form)
                    print(form, result, "GOT UNEXPECTED RESULT:", ret)
                    assert result in ret
