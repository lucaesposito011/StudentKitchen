from pymongo import MongoClient

def popolamento_db():
    client = MongoClient("mongodb://mongo:27017")
    db = client["studentkitchen"]
    ricette = db["ricette"]

    if ricette.count_documents({}) > 0:
        return

    listaricette = [
            {
                "nome": "Pasta al Pomodoro",
                "listaingredienti": ["pasta", "pomodoro", "olio", "sale", "aglio", "basilico", "parmigiano"],
                "istruzioni": "Porta a ebollizione una pentola d'acqua salata e cuoci la pasta. Nel frattempo scalda in padella un filo d’olio e fai dorare uno spicchio d’aglio. Aggiungi la passata di pomodoro, un pizzico di sale e lascia cuocere per 10 minuti mescolando ogni tanto. Scola la pasta al dente, trasferiscila nella padella e mescola bene per amalgamare tutto. Aggiungi parmigiano grattugiato e basilico fresco prima di servire.",
                "foto": "https://www.cucchiaio.it/content/cucchiaio/it/ricette/2019/12/spaghetti-al-pomodoro/jcr:content/header-par/image-single.img.jpg/1576681061599.jpg",
                "tempo_preparazione": 20,
                "calorie": 520,
                "recensioni": []
            },
            {
                "nome": "Riso al Tonno",
                "listaingredienti": ["riso", "tonno", "olio", "sale", "pepe"],
                "istruzioni": "Cuoci il riso in acqua salata seguendo i tempi indicati sulla confezione. Scola bene e trasferisci in una ciotola. Aggiungi il tonno sgocciolato, un filo d’olio e una spolverata di pepe. Mescola con delicatezza per distribuire il condimento. Puoi aggiungere anche mais o olive se desideri arricchirlo.",
                "foto": "https://wips.plug.it/cips/buonissimo.org/cms/2011/11/riso-tonnato.jpg",
                "tempo_preparazione": 15,
                "calorie": 430,
                "recensioni": []
            },
            {
                "nome": "Uova Strapazzate",
                "listaingredienti": ["uova", "olio", "sale", "pepe"],
                "istruzioni": "Rompi le uova in una ciotola e sbattile con sale e pepe. Scalda un filo d’olio in padella e versa le uova. Cuoci mescolando continuamente a fuoco basso fino a ottenere una consistenza morbida e cremosa. Spegni poco prima che siano completamente asciutte.",
                "foto": "https://media-assets.lacucinaitaliana.it/photos/61fd3361f1485d0b9a0d116f/3:2/w_1500,h_1000,c_limit/UOVA-STRAPAZZATE.jpg",
                "tempo_preparazione": 8,
                "calorie": 220,
                "recensioni": []
            },
            {
                "nome": "Bruschetta al Pomodoro",
                "listaingredienti": ["pane", "pomodorini", "olio", "sale", "aglio", "erbe_aromatiche"],
                "istruzioni": "Taglia il pane a fette e tostalo in padella o in forno. Strofina uno spicchio d’aglio sulla superficie calda. In una ciotola mescola pomodorini tagliati a cubetti, sale, olio e basilico fresco. Distribuisci il composto sul pane tostato e servi subito.",
                "foto": "https://www.cucchiaio.it/content/cucchiaio/it/ricette/2009/11/ricetta-bruschetta-pomodoro/jcr:content/imagePreview.img10.jpg/1596697514993.jpg",
                "tempo_preparazione": 10,
                "calorie": 180,
                "recensioni": []
            },
            {
                "nome": "Pancake Veloci",
                "listaingredienti": ["farina", "latte", "uova", "zucchero", "burro"],
                "istruzioni": "In una ciotola mescola farina e zucchero. Aggiungi le uova e il latte mescolando con una frusta fino a ottenere un impasto liscio. Sciogli un po’ di burro in padella e versa un mestolo di impasto. Cuoci finché compaiono bolle, poi gira il pancake. Servi con miele o marmellata.",
                "foto": "https://blog.giallozafferano.it/graziaintavola/wp-content/uploads/2021/03/IMG_0738rid-320x213.jpg",
                "tempo_preparazione": 15,
                "calorie": 310,
                "recensioni": []
            },
            {
                "nome": "Pollo al Limone",
                "listaingredienti": ["pollo", "limone", "olio", "sale", "pepe"],
                "istruzioni": "Taglia il petto di pollo a strisce e fallo rosolare in padella con un filo d’olio. Quando è dorato, aggiungi sale, pepe e il succo di mezzo limone. Cuoci altri 5 minuti finché il pollo risulta morbido e il fondo leggermente cremoso.",
                "foto": "https://www.cucchiaio.it/content/dam/cucchiaio/it/ricette/2022/02/petto-di-pollo-al-limone/polloorizzontale.jpg",
                "tempo_preparazione": 20,
                "calorie": 280,
                "recensioni": []
            },
            {
                "nome": "Purè di Patate",
                "listaingredienti": ["patate", "latte", "burro", "sale"],
                "istruzioni": "Sbuccia e taglia le patate a cubetti, poi lessale in acqua salata finché diventano morbide. Schiacciale con uno schiacciapatate, aggiungi burro e latte caldo. Mescola fino a ottenere una consistenza cremosa e uniforme.",
                "foto": "https://d2sj0xby2hzqoy.cloudfront.net/kenwood_italy/attachments/data/000/007/287/medium/pure-di-patate.jpg",
                "tempo_preparazione": 30,
                "calorie": 210,
                "recensioni": []
            },
            {
                "nome": "Frittata di Zucchine",
                "listaingredienti": ["uova", "zucchine", "olio", "sale", "pepe"],
                "istruzioni": "Taglia le zucchine a rondelle sottili e falle rosolare con un filo d’olio per 5 minuti. In una ciotola sbatti le uova con sale e pepe. Versa il composto in padella e cuoci a fuoco medio finché la frittata si compatta. Gira con un piatto per dorare anche l’altro lato.",
                "foto": "https://www.cucchiaio.it/content/cucchiaio/it/ricette/2009/11/ricetta-frittata-zucchine/jcr:content/header-par/image_single.img.jpg/1458118529152.jpg",
                "tempo_preparazione": 15,
                "calorie": 260,
                "recensioni": []
            },
            {
                "nome": "Polpette di Carne",
                "listaingredienti": ["carne_macinata", "pangrattato", "uova", "sale", "pepe", "aglio", "erbe_aromatiche"],
                "istruzioni": "Mescola in una ciotola la carne macinata con pangrattato, uova, sale, pepe, aglio tritato e prezzemolo. Forma delle palline e falle rosolare in padella con poco olio. Cuoci finché risultano dorate e ben cotte internamente.",
                "foto": "https://www.giallozafferano.it/images/242-24200/Polpette-di-carne_450x300.jpg",
                "tempo_preparazione": 25,
                "calorie": 340,
                "recensioni": []
            },
            {
                "nome": "Pasta Tonno e Piselli",
                "listaingredienti": ["pasta", "tonno", "piselli", "olio", "sale", "cipolla"],
                "istruzioni": "Fai soffriggere un po’ di cipolla tritata in padella con un filo d’olio. Aggiungi i piselli e cuoci per 5 minuti, poi unisci il tonno sgocciolato. Cuoci la pasta, scolala e mescola tutto direttamente in padella. Aggiusta di sale e servi.",
                "foto": "https://www.giallozafferano.it/images/184-18455/Pasta-tonno-e-piselli_780x520_wm.jpg",
                "tempo_preparazione": 20,
                "calorie": 520,
                "recensioni": []
            },
            {
                "nome": "Frittata di Patate",
                "listaingredienti": ["uova", "patate", "olio", "sale", "pepe"],
                "istruzioni": "Sbuccia le patate e tagliale a cubetti piccoli. Falle rosolare in padella con un filo d’olio finché diventano morbide. Sbatti le uova in una ciotola con sale e pepe, aggiungi le patate e mescola. Versa tutto in padella e cuoci a fuoco medio, girando la frittata quando si compatta.",
                "foto": "https://www.lacucinaimperfetta.com/wp-content/uploads/2012/10/Frittata-di-patate.jpg",
                "tempo_preparazione": 20,
                "calorie": 300,
                "recensioni": []
            },
            {
                "nome": "Pasta Aglio Olio e Peperoncino",
                "listaingredienti": ["pasta", "olio", "aglio", "sale", "pepe"],
                "istruzioni": "Cuoci la pasta in acqua salata. In padella scalda l’olio con aglio schiacciato e peperoncino (opzionale). Lascia insaporire senza bruciare l’aglio. Scola la pasta e saltala nella padella per un minuto. Aggiungi un po’ d’acqua di cottura per creare una leggera cremina.",
                "foto": "https://farchioni1780.com/cdn/shop/articles/spaghetti-aglio-olio-e-peperoncino_435ddae9-d252-4e47-b296-3d292d5c47d8.jpg?v=1748598647",
                "tempo_preparazione": 12,
                "calorie": 480,
                "recensioni": []
            },
            {
                "nome": "Insalata di Tonno e Mais",
                "listaingredienti": ["tonno", "mais", "cipolla", "olio", "sale"],
                "istruzioni": "Sgocciola il tonno e scolalo bene. Mescola in una ciotola tonno, mais e cipolla tagliata molto sottile. Condisci con olio, sale e un pizzico di pepe. Lascia riposare 5 minuti prima di servire.",
                "foto": "https://blog.giallozafferano.it/cucinafacileconelena/wp-content/uploads/2021/07/insalata-tonno-e-mais.jpeg",
                "tempo_preparazione": 5,
                "calorie": 250,
                "recensioni": []
            },
            {
                "nome": "Toast Prosciutto e Formaggio",
                "listaingredienti": ["pane", "prosciutto_cotto", "mozzarella", "burro"],
                "istruzioni": "Spalma un velo di burro all’esterno delle due fette di pane. Farcisci con prosciutto e mozzarella. Cuoci in padella o tostapane finché il formaggio si scioglie e il pane diventa dorato e croccante.",
                "foto": "https://media-assets.lacucinaitaliana.it/photos/61fae954a3e5752964f94951/4:3/w_644,h_483,c_limit/271a77ff-34c4-4849-bd04-57faa2336eaf.jpg",
                "tempo_preparazione": 8,
                "calorie": 340,
                "recensioni": []
            },
            {
                "nome": "Riso con Verdure",
                "listaingredienti": ["riso", "carote", "piselli", "olio", "sale"],
                "istruzioni": "Cuoci il riso in acqua salata. A parte rosola carote tagliate a cubetti e piselli in padella con olio. Unisci il riso cotto e salta tutto insieme per 2 minuti per amalgamare i sapori.",
                "foto": "https://www.giallozafferano.it/images/9-999/Risotto-alle-verdure_780x520_wm.jpg",
                "tempo_preparazione": 20,
                "calorie": 380,
                "recensioni": []
            },
            {
                "nome": "Zucchine Gratinate",
                "listaingredienti": ["zucchine", "pangrattato", "olio", "sale", "parmigiano"],
                "istruzioni": "Taglia le zucchine a rondelle e disponile su una teglia. Condisci con sale, olio, pangrattato e parmigiano. Cuoci in forno a 200°C per 20 minuti finché diventano dorate.",
                "foto": "https://www.casapappagallo.it/storage/19290/zucchine-gratinate.JPG",
                "tempo_preparazione": 25,
                "calorie": 190,
                "recensioni": []
            },
            {
                "nome": "Pasta al Burro e Parmigiano",
                "listaingredienti": ["pasta", "burro", "parmigiano", "sale"],
                "istruzioni": "Cuoci la pasta in acqua salata. Scolala e condiscila con abbondante burro e parmigiano grattugiato. Mescola fino a ottenere una crema omogenea.",
                "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBS1z7Xj5g4MfarCLYLvttKQZ0GL_CbDM7lQ&s",
                "tempo_preparazione": 12,
                "calorie": 520,
                "recensioni": []
            },
            {
                "nome": "Patate al Forno",
                "listaingredienti": ["patate", "olio", "sale", "pepe", "erbe_aromatiche"],
                "istruzioni": "Taglia le patate a cubetti o spicchi. Condisci con olio, sale, pepe e rosmarino o prezzemolo. Cuoci in forno a 200°C per 35-40 minuti finché risultano croccanti.",
                "foto": "https://www.cucchiaio.it/content/cucchiaio/it/ricette/2015/04/patate-al-forno/jcr:content/imagePreview.img10.jpg/1582270791908.jpg",
                "tempo_preparazione": 45,
                "calorie": 330,
                "recensioni": []
            },
            {
                "nome": "Frittata di Cipolle",
                "listaingredienti": ["uova", "cipolla", "olio", "sale", "pepe"],
                "istruzioni": "Affetta la cipolla e falla appassire in padella con un filo d’olio. Sbatti le uova con sale e pepe, versale sulla cipolla e cuoci finché la frittata si compatta. Gira con attenzione e completa la cottura.",
                "foto": "https://www.fattoincasadabenedetta.it/wp-content/uploads/2020/11/FRITTTATA-DI-CIPOLLE-ROSSE-sito2.jpg",
                "tempo_preparazione": 20,
                "calorie": 270,
                "recensioni": []
            },
            {
                "nome": "Caffè Latte Freddo",
                "listaingredienti": ["latte", "caffe", "zucchero"],
                "istruzioni": "Prepara il caffè e lascialo raffreddare completamente. Mescola latte freddo, caffè e zucchero in un bicchiere. Aggiungi ghiaccio se desideri una bevanda più fresca.",
                "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT35OKkdfNHVvtsyHFBZtoMgVj7YK0Pa2Z3Ug&s",
                "tempo_preparazione": 5,
                "calorie": 90,
                "recensioni": []
            },
            {
                "nome": "Pasta con Panna e Prosciutto",
                "listaingredienti": ["pasta", "panna", "prosciutto_cotto", "sale", "cipolla", "olio"],
                "istruzioni": "Rosola cipolla tritata in padella con un po’ d’olio. Aggiungi prosciutto tagliato a pezzetti e la panna. Cuoci la pasta e mescola tutto insieme creando una salsa cremosa.",
                "foto": "https://staticcookist.akamaized.net/wp-content/uploads/sites/21/2025/05/pasta-panna-e-prosciutto-still-life.jpeg",
                "tempo_preparazione": 15,
                "calorie": 650,
                "recensioni": []
            },
            {
                "nome": "Uova all’Occhio di Bue",
                "listaingredienti": ["uova", "olio", "sale"],
                "istruzioni": "Scalda un filo d’olio in padella. Rompi le uova e cuoci finché l’albume si compatta lasciando il tuorlo morbido. Aggiungi un pizzico di sale e servi.",
                "foto": "https://static.planeat.eco/media/planeat_it_mi/item_pics/uova-occhio-di-bue-600x400.jpg",
                "tempo_preparazione": 5,
                "calorie": 170,
                "recensioni": []
            },
            {
                "nome": "Cipolle Caramellate",
                "listaingredienti": ["cipolla", "zucchero", "olio", "sale"],
                "istruzioni": "Affetta sottilmente le cipolle e cuocile in padella con olio finché diventano morbide. Aggiungi un cucchiaino di zucchero e mescola finché diventano dorate e caramellate.",
                "foto": "https://www.cucchiaio.it/content/dam/cucchiaio/it/ricette/2022/03/cipolle-rosse-caramellate/cipolle-rosse-caramellate-finale.jpg",
                "tempo_preparazione": 30,
                "calorie": 150,
                "recensioni": []
            },
            {
                "nome": "Pane Bruschettato all’Aglio",
                "listaingredienti": ["pane", "aglio", "olio", "sale"],
                "istruzioni": "Tosta il pane e strofina uno spicchio d’aglio sulla superficie calda. Condisci con olio e un pizzico di sale. Perfetto come antipasto o accompagnamento.",
                "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9F9cmY_h6a1RoYYzNqoC6cv1kIwMIit1YQQ&s",
                "tempo_preparazione": 7,
                "calorie": 140,
                "recensioni": []
            },
            {
                "nome": "Piselli in Padella",
                "listaingredienti": ["piselli", "cipolla", "olio", "sale"],
                "istruzioni": "Taglia la cipolla e falla soffriggere. Aggiungi i piselli e un po’ d’acqua. Cuoci 10-12 minuti finché risultano morbidi. Regola di sale.",
                "foto": "https://media-assets.lacucinaitaliana.it/photos/6824ae814895109b56d079d8/16:9/w_2560%2Cc_limit/1427554700",
                "tempo_preparazione": 15,
                "calorie": 120,
                "recensioni": []
            },
            {
                "nome": "Pasta con Zucchine",
                "listaingredienti": ["pasta", "zucchine", "olio", "sale", "cipolla"],
                "istruzioni": "Rosola cipolla tritata, aggiungi zucchine tagliate a rondelle e cuoci per 10 minuti. Unisci la pasta cotta e salta tutto insieme.",
                "foto": "https://www.giallozafferano.it/images/166-16633/Pasta-e-zucchine_650x433_wm.jpg",
                "tempo_preparazione": 18,
                "calorie": 480,
                "recensioni": []
            },
            {
                "nome": "Tonno e Fagioli",
                "listaingredienti": ["tonno", "fagioli", "olio", "sale", "pepe"],
                "istruzioni": "Scola per bene i fagioli e mescolali con il tonno sgocciolato. Aggiungi olio, sale e pepe. Mescola delicatamente e servi fresco.",
                "foto": "https://blog.giallozafferano.it/dulcisinforno/wp-content/uploads/2023/08/Insalata-tonno-e-fagioli-4467.jpg",
                "tempo_preparazione": 7,
                "calorie": 320,
                "recensioni": []
            },
            {
                "nome": "Carote in Padella",
                "listaingredienti": ["carote", "olio", "sale", "pepe"],
                "istruzioni": "Taglia le carote a rondelle sottili e cuocile in padella con olio, sale e pepe per 10-12 minuti, finché diventano morbide ma non sfatte.",
                "foto": "https://www.mangiabevigodi.it/wp-content/uploads/2025/02/carote-in-padella-al-rosmarino-2.jpg",
                "tempo_preparazione": 15,
                "calorie": 90,
                "recensioni": []
            },
            {
                "nome": "Zuppa di Verdure Semplice",
                "listaingredienti": ["carote", "patate", "cipolla", "olio", "sale"],
                "istruzioni": "Taglia tutte le verdure a cubetti e cuocile in acqua salata per 30 minuti. Aggiungi un filo d’olio a fine cottura. Puoi frullarla per una crema liscia.",
                "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7KeUfwb0D_T1jdB_fOPQ-YtnpGXKzDdf2vg&s",
                "tempo_preparazione": 35,
                "calorie": 160,
                "recensioni": []
            },
            {
                "nome": "Pasta in Bianco",
                "listaingredienti": ["pasta", "olio", "sale", "parmigiano"],
                "istruzioni": "Cuoci la pasta, scolala e condiscila con olio e parmigiano. Variante semplice e veloce per quando hai pochi ingredienti.",
                "foto": "https://www.giallozafferano.it/images/contents/3643/Pasta_bianca-750x500.jpg",
                "tempo_preparazione": 10,
                "calorie": 450,
                "recensioni": []
            },
            {
                "nome": "Pasta Olive e Pomodoro",
                "listaingredienti": ["pasta", "olive", "pomodoro", "olio", "sale", "aglio"],
                "istruzioni": "Cuoci la pasta in acqua salata. In una padella scalda un filo d'olio e fai soffriggere uno spicchio d'aglio. Aggiungi la passata di pomodoro e cuoci per 10 minuti. Unisci le olive tagliate a rondelle e mescola. Scola la pasta e falle assorbire il sugo per un paio di minuti. Servi con un filo d’olio a crudo.",
                "foto": "https://www.fattoincasadabenedetta.it/wp-content/uploads/2022/03/sito-24-Pasta-pomodoro-e-olive.jpg",
                "tempo_preparazione": 20,
                "calorie": 480,
                "recensioni": []
            },
            {
                "nome": "Melanzane alla Piastra",
                "listaingredienti": ["melanzane", "olio", "sale", "pepe", "erbe_aromatiche"],
                "istruzioni": "Taglia le melanzane a fette spesse mezzo centimetro. Ungile leggermente con olio e scaldale su una piastra ben calda per 3-4 minuti per lato. Condisci con sale, pepe e prezzemolo o basilico tritato. Servile calde o tiepide come contorno leggero.",
                "foto": "https://www.cucchiaio.it/content/cucchiaio/it/ricette/2020/09/melanzane-grigliate/jcr:content/header-par/image-single.img.jpg/1600157023919.jpg",
                "tempo_preparazione": 15,
                "calorie": 120,
                "recensioni": []
            },
            {
                "nome": "Salsa allo Yogurt",
                "listaingredienti": ["yogurt", "olio", "sale", "limone", "erbe_aromatiche"],
                "istruzioni": "Versa lo yogurt in una ciotolina. Aggiungi un cucchiaio di olio, un pizzico di sale e alcune gocce di limone. Mescola bene e aggiungi prezzemolo o erba cipollina tritata. Ottima come salsa fresca per verdure, carne o insalate.",
                "foto": "https://thinkmilkbesmart.eu/wp-content/uploads/2021/11/Salsa-allo-yogurt-1-shutterstock_773045590.jpeg",
                "tempo_preparazione": 5,
                "calorie": 70,
                "recensioni": []
            },
            {
                "nome": "Pasta Pancetta e Piselli",
                "listaingredienti": ["pasta", "pancetta", "piselli", "cipolla", "olio", "sale"],
                "istruzioni": "Trita la cipolla e falle appassire in padella con un filo d’olio. Aggiungi la pancetta a cubetti e falla rosolare. Unisci i piselli e cuoci per qualche minuto. Cuoci la pasta, scolala e mescola tutto insieme in padella. Aggiusta di sale e servi caldo.",
                "foto": "https://www.silviaerosmarino.it/wp-content/uploads/elementor/thumbs/26A1F23A-EA48-4FDE-A68D-2E46A73DDA35-olco428vtazlsazv3kneq5ya5fcvcwiou4ftbl79qo.jpeg",
                "tempo_preparazione": 20,
                "calorie": 560,
                "recensioni": []
            },
            {
                "nome": "Wurstel in Padella",
                "listaingredienti": ["wurstel", "olio", "pepe"],
                "istruzioni": "Taglia i wurstel a metà o a rondelle. Scalda una padella antiaderente con un filo d’olio e cuoci i wurstel a fuoco medio finché risultano dorati. Aggiungi una spolverata di pepe e servi con pane o contorni a piacere.",
                "foto": "https://www.ilcuoreinpentola.it/wp-content/uploads/2012/09/wurstel-in-padella-1.jpeg",
                "tempo_preparazione": 8,
                "calorie": 300,
                "recensioni": []
            }
    ]

    ricette.insert_many(listaricette)

if __name__ == "__main__":
    popolamento_db()
