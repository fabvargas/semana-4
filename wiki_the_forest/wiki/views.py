from django.shortcuts import render

# Create your views here.

def lugares(request):
    pueblos = [
    {
    "nombre": "Pueblo",
    "descripcion": "Construidos por mutantes, son cabañas pequeñas con techo de paja y es una base para los mutantes, frecuentemente es ocupado de 2 a 7 mutantes en el día y la noche. Se pueden encontrar 2 tipos de cabañas triangulares y estilo de casa larga.",
    "flora": [],
    "fauna": [],
    "objetos": [],
    "imagen": "img_lugares_wiki/pueblotf_1.jpg"
    },
    {
    "nombre": "Pueblo Central",
    "descripcion": "Ubicado en el centro del mapa con ligera desviación al sur, una de las aldeas más peligrosas del juego debido a la alta cantidad de rutas de patrulla en el sector. Objetos que se pueden encontrar: Bidón de gasolina x2, cuerda x2, laptop, efigies de caníbales. Flora: achicoria, mora, arándano, hongos. Fauna: conejos y lagartos.",
    "flora": ["achicoria", "mora", "arándano", "hongos"],
    "fauna": ["conejos", "lagartos"],
    "objetos": ["Bidón de gasolina x2", "cuerda x2", "laptop", "efigies de caníbales"],
    "imagen": "img_lugares_wiki/pueblocentraltf.jpg"
    },
    {
    "nombre": "Pueblo Cabañas De Playa",
    "descripcion": "Construidos por caníbales, es una serie de cabañas repartidas a lo largo de toda la playa, patrullada por enemigos, con alta presencia de tiburones muertos. Puedes encontrar latas de combustible, maletas, calaveras, laptop, refrescos, bocadillos, laca y bebida alcohólica. Flora: twinberry. Fauna: tiburones muertos, gaviotas.",
    "flora": ["twinberry"],
    "fauna": ["tiburones muertos", "gaviotas"],
    "objetos": ["latas de combustible", "maletas", "calaveras", "laptop", "refrescos", "bocadillos", "laca", "bebida alcohólica"],
    "imagen": "img_lugares_wiki/pueblodecabañasplaya_1.jpg"
    },
    {
    "nombre": "Pueblo Junto al Lago",
    "descripcion": "Ubicado al lado del gran lago, en el se puede encontrar cuerda x2, atuendo, pernos de ballesta, maletas, olp-pot, hoguera caníbal, jaulas de madera, efigies caníbales. Flora: baya de nieve, hierbas, montones de nieves, árboles de palo. Fauna: peces, lagartos, conejos, gansos.",
    "flora": ["baya de nieve", "hierbas", "montones de nieves", "árboles de palo"],
    "fauna": ["peces", "lagartos", "conejos", "gansos"],
    "objetos": ["cuerda x2", "atuendo", "pernos de ballesta", "maletas", "olp-pot", "hoguera caníbal", "jaulas de madera", "efigies caníbales"],
    "imagen": "img_lugares_wiki/pueblojuntoallago_1.jpg"
    },
    {
    "nombre": "Pueblo de la Cascada",
    "descripcion": "La aldea de la cascada es una aldea mutante que los mutantes suelen utilizar como intercambio para sus patrullas. Es uno de los pueblos más valiosos para asaltar, ya que tiene muchos elementos diferentes y alcanza la flora y la fauna. Flora: Aloe vera, Hongos. Fauna: Conejos, Lagartos, Jabalíes, Ciervos, Ardillas.",
    "flora": ["Aloe vera", "Hongos"],
    "fauna": ["Conejos", "Lagartos", "Jabalíes", "Ciervos", "Ardillas"],
    "objetos": [],
    "imagen": "img_lugares_wiki/pueblodelacascada_1.jpg"
    },
    {
    "nombre": "Aldea de Cabañas de Cocodrilos",
    "descripcion": "Este pueblo está ubicado entre el río y la zona de nieve. Es posible que los caníbales lo hayan abandonado debido a la gran cantidad de cocodrilos. Las rutas de patrullas pasan por aquí con bastante frecuencia. Puedes encontrar pintura roja, lanza mejorada, cuerda, maletas. Flora: Arándano, Blackberry, Twinberry, Snowberry. Fauna: Cocodrilos, Lagartos, Conejos.",
    "flora": ["Arándano", "Blackberry", "Twinberry", "Snowberry"],
    "fauna": ["Cocodrilos", "Lagartos", "Conejos"],
    "objetos": ["pintura roja", "lanza mejorada", "cuerda", "maletas"],
    "imagen": "img_lugares_wiki/pueblodecocodrilos_1.jpg"
    },
    {
    "nombre": "Pueblo Ribereño",
    "descripcion": "Es pequeño y carece de objetos. Hay algunas tiendas de campaña de lona al otro lado del río y una Cueva 3 - Entradas a la Cueva Húmeda en las cercanías. Puedes encontrar elementos: atuendo. Flora: Hierbas, Arándano, Twinberry, Snowberry. Fauna: Lagartos, Conejos, Ciervos, Peces.",
    "flora": ["Hierbas", "Arándano", "Twinberry", "Snowberry"],
    "fauna": ["Lagartos", "Conejos", "Ciervos", "Peces"],
    "objetos": ["atuendo", "efigies caníbales x2"],
    "imagen": "img_lugares_wiki/puebloribereño_1.jpg"
    },
    {
    "nombre": "Pueblo Costero",
    "descripcion": "Se ubica junto al mar, contiene dos cabañas y suele estar patrullada por caníbales. No tiene muchos artículos de valor. Elementos: 2x Cuerda (colgadas en una de las cabañas). Flora: Twinberry, Árboles, Árboles de palo. Fauna: Conejos, Lagartos.",
    "flora": ["Twinberry", "Árboles", "Árboles de palo"],
    "fauna": ["Conejos", "Lagartos"],
    "objetos": ["Cuerda x2", "Efigies caníbales x3", "Cabañas caníbales", "Fuego inservible", "Carpas naranjas", "Cadáveres quemados"],
    "imagen": "img_lugares_wiki/pueblocostero_1.jpg"
    },
    {
    "nombre": "Pueblo Principal",
    "descripcion": "Es la aldea más grande que han construido los caníbales, a menudo patrullada por caníbales y es un lugar peligroso para construir o holgazanear. Puedes encontrar elementos como maletas de refrescos, tela de cuerda, lata de combustible, cajas de placa de circuito, bengalas, pelotas de tenis de dinamita, Timmy Drawing 10, pintura roja. Flora: Hierbas, Hongos, Árboles, Arbustos y árboles jóvenes. Fauna: Conejos, Lagartos, Ciervos.",
    "flora": ["Hierbas", "Hongos", "Árboles", "Arbustos", "Árboles jóvenes"],
    "fauna": ["Conejos", "Lagartos", "Ciervos"],
    "objetos": ["maletas de refrescos", "tela de cuerda", "lata de combustible", "cajas de placa de circuito", "bengalas", "pelotas de tenis de dinamita", "Timmy Drawing 10", "pintura roja"],
    "imagen": "img_lugares_wiki/puebloprincipal_1.jpg"
    }
    ]
    
    especiales =[
        
  {
    "nombre": "Tumba junto a la playa",
    "descripcion": "Se puede encontrar en la playa en la bahía de yates. Cassette 5 y varias fotos de yates se pueden encontrar encima. La imagen apoyada en la cruz se puede agregar a las notas. Se pueden encontrar varias maletas en las inmediaciones de la tumba.",
    "flora": [],
    "fauna": [],
    "objetos": ["Maletas", "Cassette 5", "Fotos de yates"],
    "imagen": "img_lugares_wiki/tumbadelaplaya_1.jpg"
  },
  {
    "nombre": "Cabina",
    "descripcion": "Es el frente faltante del avión estrellado en el que reapareces. Ubicado cerca de la cabina, el copiloto estaba sentado en una silla y hay una pistola de bengalas detrás de él en un asiento.",
    "flora": [],
    "fauna": ["Ciervo", "Conejos blancos", "Jabalí"],
    "objetos": ["Pistola de bengalas"],
    "imagen": "img_lugares_wiki/cabina_1.png"
  },
  {
    "nombre": "Lago de los Gansos",
    "descripcion": "Es un lugar dentro del bosque donde se pueden encontrar una multitud de gansos. El lago se asoma a un acantilado y es un lugar base popular debido a su naturaleza memorable, la protección natural del acantilado y la abundancia de comida cercana (gansos).",
    "flora": [],
    "fauna": ["Gansos"],
    "objetos": [],
    "imagen": "img_lugares_wiki/lagodelosgansos_1.png"
  },
  {
    "nombre": "Helicóptero",
    "descripcion": "Se encuentra en el fondo del sumidero. Es un avión pequeño, pero parece haber dejado algunos rasguños y marcas de quemaduras en el fondo del foso cuando se estrelló. Una de las ventanas delanteras ha sido rota.",
    "flora": [],
    "fauna": [],
    "objetos": ["Maleta", "Machete"],
    "imagen": "img_lugares_wiki/helicoptero_1.png"
  },
  {
    "nombre": "Contenedores de envío",
    "descripcion": "Solía encontrarse en la playa junto con otros dos contenedores, varios paquetes y algunos artículos dispersos. Había una cinta de casete, que se puede reproducir con el reproductor de casetes, pegada en la cuenca del ojo de la decoración de calavera de animal en la pared.",
    "flora": [],
    "fauna": [],
    "objetos": ["Cinta eléctrica", "Cajas de placas de circuitos", "Bebidas alcohólicas", "Medicamentos", "Monedas", "Manifiesto de carga"],
    "imagen": "img_lugares_wiki/contenedores de envio_1.png"
  },
  {
    "nombre": "Cuarto de alijo oculto",
    "descripcion": "Es una sala secreta que contiene montones de elementos y algunos elementos de la historia. Hay múltiples entradas para acceder a la habitación. El más cercano está cerca de Lakeside Village, hay un camino que conduce desde el pueblo hasta la entrada de la cueva.",
    "flora": ["Plantas marinas en el océano"],
    "fauna": ["Pez", "Tortuga", "Tiburón"],
    "objetos": ["Hacha moderna", "Informe de autopsia", "Cinta eléctrica", "Flecha moderna", "Dinamita", "Refrescos", "Medicamentos", "Tablero de circuitos", "Niños perdidos", "Caja de explosivos", "Pintura roja", "Traje de pincel"],
    "imagen": "img_lugares_wiki/cuartodealijo_1.jpg"
  },
  {
    "nombre": "Laboratorio Sahára",
    "descripcion": "Propiedad de Sahara Therapeutics, es un área subterránea profunda en la península. Para acceder al laboratorio, el jugador debe atravesar la puerta de la bóveda, ubicada al final de la cueva HC en el fondo del sumidero.",
    "flora": [],
    "fauna": ["Bebés mutantes", "Ejército", "Caníbales flacos", "End Boss", "Megan (víctima del obelisco)"],
    "objetos": [],
    "imagen": "img_lugares_wiki/labsahara_1.png"
  },
  {
    "nombre": "Obelisco",
    "descripcion": "Se dividen en 3 obeliscos: Obelisco de Res, Obelisco de Poder y Obelisco de la Muerte. Los dos primeros son artefactos sobrenaturales con diferentes efectos. El Obelisco de la Resurrección revive a los muertos, mientras que el Obelisco de Poder puede derribar aviones.",
    "flora": [],
    "fauna": [],
    "objetos": [],
    "imagen": "img_lugares_wiki/obelisco_1.png"
  },
  {
    "nombre": "Puerta de la Bóveda",
    "descripcion": "Al abrir la puerta de la bóveda, la historia avanza y proporciona acceso al Laboratorio Sahara. Se encuentra al final de la Cueva HC (Cueva del Infierno). La tarjeta de seguridad del empleado que se encuentra en la Cueva 6 es necesaria para abrir la puerta.",
    "flora": [],
    "fauna": [],
    "objetos": [],
    "imagen": "img_lugares_wiki/puertadeboveda_1.jpg"
  },
  {
    "nombre": "Sumidero",
    "descripcion": "Hay varias formas de llegar al fondo del sumidero. Para llegar al fondo puedes: pasar por la Cueva 7 o saltar desde el acantilado más alto directamente al estanque en el centro del sumidero.",
    "flora": [],
    "fauna": [],
    "objetos": ["Tarjeta de acceso", "Hacha de escalada", "Rebreather"],
    "imagen": "img_lugares_wiki/sumidero_1.png"
  },
  {
    "nombre": "Lago de nieve",
    "descripcion": "Es un lago grande y es un lugar popular para que los jugadores construyan una vez que hayan adquirido un traje de abrigo. Hay un caché cerca con Gun Part 7 en él.",
    "flora": ["Árboles de palo", "Hongos"],
    "fauna": ["Ciervo", "Conejos blancos"],
    "objetos": ["Caché con Gun Part 7"],
    "imagen": "img_lugares_wiki/lagodenieve_1.jpg"
  }
]

    variados=[
  {
    "nombre": "Islas",
    "descripcion": "Estas áreas del juego que están en el mar y no están conectadas por ningún tipo de puente terrestre, son los lugares más seguros para construir en el juego, ya que los mutantes y los mutantes espeluznantes no pueden nadar ni cruzar el agua.",
    "flora": [],
    "fauna": [],
    "objetos": [],
    "imagen": "img_lugares_wiki/islastf.jpg"
  },
  {
    "nombre": "Río",
    "descripcion": "Es el principal cuerpo de agua que discurre por el centro de la península. Los peces abundan en el río. Es muy grande con múltiples ramas y requiere en la mayoría de los lugares que el jugador nade para cruzarlo. En varios puntos existen zonas de paso poco profundas, normalmente marcadas por la presencia de varias rocas. Estas áreas de cruce son utilizadas frecuentemente por los caníbales.",
    "flora": [],
    "fauna": ["Cocodrilos", "tortugas", "conejos", "lagartos"],
    "objetos": [],
    "imagen": "img_lugares_wiki/riotf.png"
  },
  {
    "nombre": "Área de Montaña",
    "descripcion": "Es la parte norte de la península que está cubierta de nieve. No es escalable, pero un ascensor en el laboratorio Sahara llevará al jugador al observatorio en la cima de las montañas.",
    "flora": ["Setas (principalmente al sur del lago y en la parte occidental de la zona montañosa)"],
    "fauna": ["Ciervos", "ardillas", "pájaros", "conejos de las nieves", "jabalíes (en los bordes exteriores)", "Caníbales presentes"],
    "objetos": [],
    "imagen": "img_lugares_wiki/areademontaña_1.jpg"
  },
  {
    "nombre": "Puesto de Vigilancia",
    "descripcion": "Son estructuras que parecen haber sido creadas por los caníbales, aunque nunca se les ve usando los puestos. Son largos y altos, hechos de la misma madera flotante que los campamentos caníbales ubicados cerca del agua.",
    "flora": [],
    "fauna": [],
    "objetos": ["Ballesta"],
    "imagen": "img_lugares_wiki/puestodevigilancia_1.png"
  },
  {
    "nombre": "Árboles Sagrados",
    "descripcion": "Son árboles caducifolios gigantes, pálidos, parecidos a los robles, esparcidos por la parte sur de la península. Estos árboles no se pueden talar ni volar.",
    "flora": [],
    "fauna": ["Caníbales (pueden saltar lo suficiente como para alcanzar al jugador)"],
    "objetos": [],
    "imagen": "img_lugares_wiki/arbolessagrados_1.jpg"
  },
  {
    "nombre": "Campamento Abandonado",
    "descripcion": "Hay varios campings abandonados repartidos por la península y en las cuevas. En los campamentos abandonados, el jugador puede encontrar varios artículos como pastillas, bebidas alcohólicas, dinero en efectivo, monedas, bengalas, flechas modernas, ollas viejas, maletas y artículos de la historia.",
    "flora": [],
    "fauna": [],
    "objetos": ["Pastillas", "bebidas alcohólicas", "dinero en efectivo", "monedas", "bengalas", "flechas modernas", "ollas viejas", "maletas", "artículos de la historia"],
    "imagen": "img_lugares_wiki/campamentoabandonado_1.png"
  },
  {
    "nombre": "Playas",
    "descripcion": "Son lugares de arena en la mayoría de los bordes de la península. Las tortugas y las gaviotas son las principales fuentes de alimento para desovar, aunque los peces también pueden desovar en el agua. Se pueden encontrar esparcidos por varias playas, a veces con tiendas de campaña de campamentos abandonados cercanos.",
    "flora": [],
    "fauna": ["Tortugas", "gaviotas", "caníbales"],
    "objetos": [],
    "imagen": "img_lugares_wiki/playastf.png"
  },
  {
    "nombre": "Estanque de Pesca",
    "descripcion": "Son lugares de agua repartidos por toda la península. A veces se encuentran junto a pueblos caníbales, y también a veces tienen equipaje esparcido aparentemente desde el avión. Cuando están cerca de las aldeas, a menudo tienen altas torres de exploración en el agua o cerca.",
    "flora": [],
    "fauna": [],
    "objetos": ["Lanzas (para atrapar peces)"],
    "imagen": "img_lugares_wiki/estanquedepesca_1.jpg"
  }
]   
    return render(request, 'Lugarestf.html' , {'pueblos': pueblos, 'especiales': especiales, 'variados': variados})


def historia(request):
    return render(request, 'historia.html')
  
  
  
def flora(request):
  flores = [
    {
      "id": 1,
      "nombre": "Moras",
      "imagen": "imagenes/Flora/f1.png",
      "tipo": "Curativas(Sed/Hambre)",
      "descripcion": "Las moras se pueden encontrar por toda la península. Son uno de los alimentos más útiles, ya que proporcionan hidratación, saciedad y energía, al igual que los arándanos. Solo aportan 1 caloría cada uno. No se estropean, lo que los hace útiles para explorar las profundidades de las cuevas. Crecen en un arbusto con pocas hojas que se asemeja a una colección de enredaderas colgantes de color marrón espinoso. No se pueden utilizar en guisos. No hay semillas para las moras, por lo tanto, no se pueden cultivar en un jardín o en una maceta de pared."
    },
    {
      "id": 2,
      "nombre": "Arándanos",
      "imagen": "imagenes/Flora/f2.png",
      "tipo": "Curativas",
      "descripcion": "Los arándanos se pueden recolectar de los arbustos de arándanos, que se pueden encontrar por toda la isla. Son uno de los alimentos más útiles, ya que proporcionan hidratación, saciedad y energía. Solo aportan 1 caloría cada uno. No se estropean, lo que los hace útiles para explorar las profundidades de las cuevas. Después de recolectar o comer arándanos, el jugador tiene la posibilidad de recibir semillas de arándanos, que se pueden plantar en un jardín."
    },
    {
      "id": 3,
      "nombre": "Bayas de Nieve",
      "imagen": "imagenes/Flora/f3.png",
      "tipo": "Venenosas",
      "descripcion": "Las bayas de nieve se pueden encontrar en los arbustos de bayas de nieve. Son venenosas y dañarán la salud de los jugadores cuando se consuman, no proporcionan hidratación y no se pueden colocar en guisos. En modo normal y pacífico, este daño es solo 1 punto de salud. Aunque en el modo difícil y especialmente en el modo de supervivencia difícil, este daño puede ser letal. Los arbustos de bayas de nieve tienen el mismo aspecto que los arbustos de arándanos, aunque tienen bayas de color blanco en lugar de bayas de color azul."
    },
    {
      "id": 4,
      "nombre": "Twinberries",
      "imagen": "imagenes/Flora/f4.png",
      "tipo": "Venenosas",
      "descripcion": "Twinberries aparecen como dos bayas oscuras redondas rodeadas por una flor en forma de estrella de color naranja rojizo y se pueden encontrar en los arbustos de twinberries. Son venenosas y dañarán la salud de los jugadores cuando se consuman, no proporcionan hidratación y no se pueden colocar en guisos."
    },
    {
      "id": 5,
      "nombre": "Aloe",
      "imagen": "imagenes/Flora/f5.png",
      "tipo": "Curativas",
      "descripcion": "El aloe no tiene tallo, con solo hojas gruesas y carnosas. Se puede utilizar para elaborar hierbas medicinales, meds+ y energy mix+. Se encuentra más comúnmente desovando en grupos en el suelo del bosque. Las hojas se pueden comer solas para curar infecciones y enfermedades de la sangre, y para restaurar una pequeña cantidad de hambre. Cuando se reúnen, el jugador tiene una pequeña posibilidad de recolectar semillas de aloe, que se pueden plantar en un pequeño jardín o en una jardinera de pared."
    },
    {
      "id": 6,
      "nombre": "Achicoria",
      "imagen": "imagenes/Flora/f6.png",
      "tipo": "Curativas",
      "descripcion": "La achicoria se puede reconocer por sus flores de color azul claro. Al igual que el aloe, la equinácea y la caléndula, la achicoria a menudo se genera en grupos en el suelo del bosque. Se puede fabricar con equinácea para hacer una mezcla energética, o con equinácea y aloe para hacer una mezcla energética +. Si se come sola, la achicoria repondrá una pequeña cantidad de energía. El jugador solo puede llevar 10 achicorias en su inventario a la vez."
    },
    {
      "id": 7,
      "nombre": "Equinácea",
      "imagen": "imagenes/Flora/f7.png",
      "tipo": "Curativas",
      "descripcion": "La equinácea es una flor alta, en forma de cono, reconocible por sus pétalos blancos con un centro anaranjado. Se puede usar para elaborar mezclas energéticas, mezclas energéticas + y hierbas medicinales+. Se puede comer para restaurar una pequeña cantidad de salud. Cuando se recolectan, el jugador tiene una pequeña posibilidad de recolectar semillas de equinácea, que se puede plantar en un pequeño jardín o en una jardinera de pared. El jugador solo puede llevar 10 equináceas en su inventario a la vez."
    },
    {
      "id": 8,
      "nombre": "Caléndula",
      "imagen": "imagenes/Flora/f8.png",
      "tipo": "Curativas",
      "descripcion": "La caléndula se puede reconocer fácilmente por sus flores naranjas brillantes y redondas. La caléndula se puede encontrar por toda la península, a excepción de las zonas de nieve. (Consejo adicional: un engendro muy grande de caléndula está en el árbol de la vida/árbol sagrado cerca del yate.) Se puede usar para elaborar hierbas medicinales y hierbas medicinales+. La caléndula se puede comer sola para reponer una pequeña cantidad de hambre. El jugador solo puede llevar 10 caléndulas en su inventario a la vez."
    },
    {
      "id": 9,
      "nombre": "Hongo Amanita",
      "imagen": "imagenes/Flora/f9.png",
      "tipo": "Curativas",
      "descripcion": "Se pueden comer directamente para restaurar una pequeña cantidad de hambre y energía, o se pueden recolectar con la bolsa. Al igual que las bayas, las setas recolectadas no se echan a perder y se pueden comer más tarde, usar para hacer manualidades o plantar en un jardín. El jugador solo puede cultivar hongos en cuevas; sin embargo, no se reproducen allí de forma natural y deben traerse del exterior. A partir de la v0.66, no se pueden cultivar en maceteros de pared. Usando la bolsa, puedes recolectar hasta 10 hongos Amanita."
    },
    {
      "id": 10,
      "nombre": "Hongo Rebozuelo",
      "imagen": "imagenes/Flora/f10.png",
      "tipo": "Curativas",
      "descripcion": "Se pueden comer directamente para restaurar una pequeña cantidad de hambre y energía, o se pueden recolectar con la bolsa. Al igual que las bayas, las setas recolectadas no se echan a perder y se pueden comer más tarde, usar para hacer manualidades o plantar en un jardín. El jugador solo puede cultivar hongos en cuevas; sin embargo, no se reproducen allí de forma natural y deben traerse del exterior. A partir de la v0.66, no se pueden cultivar en maceteros de pared. Usando la bolsa, puedes recolectar hasta 10 hongos rebozuelos."
    },
    {
      "id": 11,
      "nombre": "Hongo Ciervo",
      "imagen": "imagenes/Flora/f11.png",
      "tipo": "Curativas",
      "descripcion": "Se pueden comer directamente para restaurar una pequeña cantidad de hambre y energía, o se pueden recolectar con la bolsa. Al igual que las bayas, las setas recolectadas no se echan a perder y se pueden comer más tarde, usar para hacer manualidades o plantar en un jardín. El jugador solo puede cultivar hongos en cuevas; sin embargo, no se reproducen allí de forma natural y deben traerse del exterior. A partir de la v0.66, no se pueden cultivar en maceteros de pared. Usando la bolsa, puedes recolectar hasta 10 hongos ciervos."
    },
    {
      "id": 12,
      "nombre": "Hongo Jack",
      "imagen": "imagenes/Flora/f12.png",
      "tipo": "Curativas",
      "descripcion": "Se pueden comer directamente para restaurar una pequeña cantidad de hambre y energía, o se pueden recolectar con la bolsa. Al igual que las bayas, las setas recolectadas no se echan a perder y se pueden comer más tarde, usar para hacer manualidades o plantar en un jardín. El jugador solo puede cultivar hongos en cuevas; sin embargo, no se reproducen allí de forma natural y deben traerse del exterior. A partir de la v0.66, no se pueden cultivar en maceteros de pared. Usando la bolsa, puedes recolectar hasta 10 Jack Mushrooms."
    },
    {
      "id": 13,
      "nombre": "Hongo Hojaldrado",
      "imagen": "imagenes/Flora/f13.png",
      "tipo": "Curativas",
      "descripcion": "Se pueden comer directamente para restaurar una pequeña cantidad de hambre y energía, o se pueden recolectar con la bolsa. Al igual que las bayas, las setas recolectadas no se echan a perder y se pueden comer más tarde, usar para hacer manualidades o plantar en un jardín. El jugador solo puede cultivar hongos en cuevas; sin embargo, no se reproducen allí de forma natural y deben traerse del exterior. A partir de la v0.66, no se pueden cultivar en maceteros de pared. Usando la bolsa, puedes recolectar hasta 10 hongos hojaldrados."
    }
  ]

  return render(request, 'Flora.html', {'flores': flores})


def enemigos(request):
  
  enemigos= [
    {
      "nombre": "Canibales delgados",
      "tipo": "Canibal",
      "descripcion": "Estos canibales son de los primeros que te encuentras en la isla aunque son de los mas debiles de toda la variedad que existen ya que tienen poca vida y poco daño, al momento de enfrentarlos no suponen ningun peligro a menos que esten grupo.",
      "imagen": "imagenes/Enemigos/SkinnyCannibals.webp"
    },
    {
      "nombre": "Canibales normales",
      "tipo": "Canibal",
      "descripcion": "Los canibales normales son el primer enemigo que encuentras en el juego, los cuales siempre van en manada de un lider y 2 a 4 mujeres, al principio te costara un poco matarlos por su vida intermedia y su daño intermedio, pero a medida que avances encontraras la mejor forma de enfrentarlos.",
      "imagen": "imagenes/Enemigos/RegularCannibals.webp"
    },
    {
      "nombre": "Canibales palidos",
      "tipo": "Canibal",
      "descripcion": "Los canibales palidos son un enemigo de dificultad intermedia ya que su vida y su daño es del doble que el del canibal delgado, se caracterizan, por como dice su nombre, ser palidos.",
      "imagen": "imagenes/Enemigos/PaleCannibal.webp"
    },
    {
      "nombre": "Canibales palidos y delgados",
      "tipo": "Canibal",
      "descripcion": "Los canibales palidos y delgados son iguales a los canibales delgados pero los palidos pegan aun menos resultando asi mas faciles.",
      "imagen": "imagenes/Enemigos/PaleSkinnyCannibal.webp"
    },
    {
      "nombre": "Canibales pintados",
      "tipo": "Canibal",
      "descripcion": "Estos son los canibales mas fuertes del juego ya que tienen mucha vida y un daño elevado, ademas estos van en manada de hasta 5 con un lider el cual es el mas peligroso, aparte de que estan todos pintados con una pintura roja, el lider se diferencia del resto por llevar un palo con una calavera arriba de la cabeza.",
      "imagen": "imagenes/Enemigos/PaintedCannibals.webp"
    },
    {
      "nombre": "Canibales de fuego",
      "tipo": "Canibal",
      "descripcion": "Los canibales de fuego tienen vida y daño bajo, aunque ellos siempre llevan una antorcha con la cual pegan, ten cuidado con su ataque ya que te aplica quemado.",
      "imagen": "imagenes/Enemigos/Firemen.webp"
    },
    {
      "nombre": "Canibales enmascarados",
      "tipo": "Canibal",
      "descripcion": "Estos canibales se diferencian del resto por ser altos y llevar una mascara hecha de pieles de sus victimas, su cantidad de vida es intermedia pero su daño es medio-elevado.",
      "imagen": "imagenes/Enemigos/MaskedCannibal.webp"
    },
    {
      "nombre": "Canibales enmascarados y delgados",
      "tipo": "Canibal",
      "descripcion": "Esta es la variante del canibal enmascarado pero es mas debil, teniendo el doble de vida menos y el triple de daño menos.",
      "imagen": "imagenes/Enemigos/MaskedSkinnyCannibal.webp"
    },
    {
      "nombre": "Canibales dinamita",
      "tipo": "Canibal",
      "descripcion": "Estos canibales van en grupos de 2-4, son faciles de diferenciar ya que son amarillos y usan un cinturon con dinamita, ademas su arma es un palo con fuego, su daño no es mucho y su vida es poca, pero ten cuidado ya que estos en algun momento de la pelea explotaran lo mas cerca tuyo.",
      "imagen": "imagenes/Enemigos/DynamiteCannibal.webp"
    },
    {
      "nombre": "Armsy",
      "tipo": "Mutante",
      "descripcion": "Este mutante se caracteriza por no tener cabeza y tener muchos brazos en la zona del torso, su vida es elevada y su daño es intermedio, pero este mutante pega con cada brazo cada vez que te ataca, acumulando su daño.",
      "imagen": "imagenes/Enemigos/Armsy.webp"
    },
    {
      "nombre": "Virginia",
      "tipo": "Mutante",
      "descripcion": "Virginia es un mutante con muchas patas y tiene unos brazos muy cortos, su vida es elevada y su daño es intermedio, este tiene varios ataques desde una embestida con sus atas delanteras hasta un salto que termina impactando en ti.",
      "imagen": "imagenes/Enemigos/Virginia.webp"
    },
    {
      "nombre": "Cowman",
      "tipo": "Mutante",
      "descripcion": "Este mutante de nombre 'Cowman' es un enemigo con brazos cortos pero su demas cuerpo es ancho, su vida es elevada y su daño bajo, pero ten cuidado ya que tiene ataques y una embestida que es capaz de derribarte por unos segundos dejandote muy vulnerable.",
      "imagen": "imagenes/Enemigos/Cowman.webp"
    },
    {
      "nombre": "Bebe mutante",
      "tipo": "Mutante",
      "descripcion": "Este mutante es el enemigo con menos vida del juego y su daño es intermedio, como dice su nombre, es un bebe mutante muy pequeño, estos siempre los encuentras en un grupo de muchos bebes, ten cuidado con su ataque de salto ya que saltan todos a la vez y cuando todos los bebes mutantes salten hacia a ti pueden provocar una insta-muerte.",
      "imagen": "imagenes/Enemigos/BabyMutant.webp"
    },
    {
      "nombre": "Armsy gris",
      "tipo": "Mutante",
      "descripcion": "Este es una variante del Armsy normal pero tiene mas vida y mas daño, a comparacion de su variante normal, este logra ser una enemigo fuerte.",
      "imagen": "imagenes/Enemigos/GreyArmsy.webp"
    },
    {
      "nombre": "Virginia gris",
      "tipo": "Mutante",
      "descripcion": "Este es una variante del mutante 'Virginia' pero con mas vida y mas daño logrando ser uno de los enemigos mas formidables del juego.",
      "imagen": "imagenes/Enemigos/GreyVirginia.webp"
    },
    {
      "nombre": "Gusano",
      "tipo": "Mutante",
      "descripcion": "Este mutante tiene forma de gusano con poca vida y daño bajo, cuando se acumulan muchos de estos en un lugar, existe la posibilidad de que se junten formen una especie de ave en la cual puden volar por muy pocos segundos.",
      "imagen": "imagenes/Enemigos/Worm.webp"
    },
    {
      "nombre": "Niña",
      "tipo": "Mutante",
      "descripcion": "Este mutante aparece despues de completar el juego una vez, es una variante del jefe final pero mas debil.",
      "imagen": "imagenes/Enemigos/Girl.webp"
    },
    {
      "nombre": "Jefe final",
      "tipo": "Mutante",
      "descripcion": "Este enemigo es unico en el juego ya que es el jefe final de este, su vida es elevadisima y su daño es intermedio, pero sus ataques te desestabilizan y tienen mucho rango, haciendolo de los enemigos mas dificiles.",
      "imagen": "imagenes/Enemigos/EndBoss.webp"
    }
  ]

  
  return render(request, 'Enemigos.html', {'enemigos':enemigos})



def animales (request):
  animales = [
    
    {
    "animal": "Murcielago",
    "tipo": "Pasivo",
    "descripcion": "Realmente no se puede interactuar con ellos y solo sirven para propósitos de inmersión. Es posible matar murciélagos golpeándolos con el arma que elijas, pero no dejan caer nada.",
    "imagen":"imagenes/Animales/1.png" 
  },
  {
    "animal": "Aves",
    "tipo": "Pasivo",
    "descripcion": "Las aves se refieren a una variedad de animales emplumados que se encuentran en el aire y se encuentran en casi todos los lugares sobre el suelo en The Forest. Proporcionan plumas, que son cruciales para fabricar flechas, y se pueden matar para obtener carne pequeña o, en el caso de la gaviota, cabezas de animales.",
    "imagen": "imagenes/Animales/2.png"
  },
  {
    "animal": "Ciervo",
    "tipo": "Pasivo",
    "descripcion": "Los ciervos se pueden encontrar en las zonas boscosas, aunque también en campos abiertos, como las Tierras Fértiles. Cuando los matan, pueden ser desollados por una piel de ciervo, luego sacrificados por cuatro carnes y finalmente dejar caer una cabeza de ciervo.",
    "imagen": "imagenes/Animales/3.png"
  },
  {
    "animal": "Peces",
    "tipo": "Pasivo",
    "descripcion": "Los peces son un grupo de animales pasivos que se pueden encontrar en el océano, río, estanques o en el agua de cuevas. Cuando se matan, los peces caen como un artículo de colección, el pescado crudo, que luego se puede cocinar o colgar en una rejilla de secado.",
    "imagen": "imagenes/Animales/4.png"
  },
  {
    "animal": "Gansos",
    "tipo": "Pasivo",
    "descripcion": "El ganso es un animal volador y emplumado que se encuentra cerca de los lagos. Es el único pájaro que se posa en el agua, y el mismo nombre del lago de los gansos, al suroeste de Sinkhole.",
    "imagen": "imagenes/Animales/5.png"
  },
  {
    "animal": "Lagarto",
    "tipo": "Pasivo",
    "descripcion": "Las lagartijas se pueden encontrar en casi toda la superficie de la península, excepto en las costas y las regiones nevadas profundas. Cuando muere, el jugador puede obtener una piel de lagarto y un lagarto crudo, así como una cabeza de lagarto.",
    "imagen": "imagenes/Animales/6.png"
  },
  {
    "animal": "Conejo",
    "tipo": "Pasivo",
    "descripcion": "El conejo se puede recolectar para obtener una piel de conejo, una carne de conejo cruda y una cabeza de conejo. La carne cosechada se puede cocinar al fuego o secar en una rejilla de secado y comer.",
    "imagen": "imagenes/Animales/8.png"
  },
  {
    "animal": "Mapache",
    "tipo": "Pasivo",
    "descripcion": "Los mapaches son algunos de los animales más raros del juego. Cuando los matan y los despellejan, dejan caer 2 carnes, 1 piel de mapache y 1 cabeza de mapache. A diferencia de la mayoría de los animales pequeños en The Forest, los mapaches solo se pueden matar con dos golpes de cualquier arma.",
    "imagen": "imagenes/Animales/9.png"
  },
  {
    "animal": "Gaviota",
    "tipo": "Pasivo",
    "descripcion": "Las aves se refieren a una variedad de animales emplumados que se encuentran en el aire y se encuentran en casi todos los lugares sobre el suelo en The Forest. Proporcionan plumas, que son cruciales para fabricar flechas, y se pueden matar para obtener carne pequeña o, en el caso de la gaviota, cabezas de animales.",
    "imagen": "imagenes/Animales/10.png"
  },
  {
    "animal": "Ardilla",
    "tipo": "Pasivo",
    "descripcion": "Las ardillas le dan al jugador una carne pequeña y una cabeza de ardilla. Al igual que con la mayoría de los animales pequeños, las ardillas se pueden matar con un solo golpe de cualquier arma en el juego.",
    "imagen": "imagenes/Animales/11.png"
  },
  {
    "animal": "Tortuga de tierra",
    "tipo": "Pasivo",
    "descripcion": "Las tortugas son animales pasivos que desovan en áreas específicas alrededor del agua, especialmente en las tierras pantanosas. Se mueven muy lentamente y se esconderán dentro de su caparazón si intentas atacarlos. Al igual que las tortugas, la tortuga dejará caer un caparazón de tortuga y dos piezas de carne después de la muerte.",
    "imagen": "imagenes/Animales/12.png"
  },
  {
    "animal": "Tortuga de mar",
    "tipo": "Pasivo",
    "descripcion": "Dejan caer un caparazón de tortuga, que se puede usar para fabricar el colector de agua, o como un trineo a partir de la v0.67, y dos carnes, que se pueden cocinar o secar y comer.",
    "imagen": "imagenes/Animales/13.png"
  },
  {
    "animal": "Jabali",
    "tipo": "Agresivo",
    "descripcion": "Similar al cocodrilo, el jabalí es un animal agresivo capaz de atacar y dañar al jugador. Si el jugador permanece cerca de un jabalí durante demasiado tiempo, emitirá un chillido y comenzará a cargar hacia el jugador. Si el jabalí golpea al jugador con su carga, inflige 15 puntos de daño al jugador sin armadura, al morir suelta 2 de carne y piel.",
    "imagen": "imagenes/Animales/Boar.webp"
  },
  {
    "animal": "Tiburón",
    "tipo": "Agresivo",
    "descripcion": "Los cocodrilos se pueden encontrar esparcidos por la parte norte del río que atraviesa la península, aunque casi nunca se encuentran en el agua. Dejan caer 4 pieles de lagarto y 4 carnes si se matan, junto con su cabeza que se puede usar como decoración.",
    "imagen": "imagenes/Animales/Shark.webp"
  },
  {
    "animal": "Cocodrilo",
    "tipo": "Agresivo",
    "descripcion": "Los tiburones son animales hostiles que se pueden encontrar nadando en áreas particulares del océano donde el agua es demasiado profunda para pararse. Si el jugador se acerca demasiado, un tiburón cargará hacia él y lo atacará mordiéndolo, al morir solo sueltan 1 de carne y la cabeza.",
    "imagen": "imagenes/Animales/Crocodile.webp"
  }
]

  
  return render(request, 'Animales.html', {'animales':animales})

def armas(request):
  
  armas = [
    
  {
    "id": 1,
    "imagen": "imagenes/Armas/PlaneAxe.webp",
    "nombre": "Hacha de avion",
    "tipo": "Melee",
    "descripcion": "El hacha de avion es el primer arma que te encuentras en el juego ya que la encontraras al salir del avion, el personaje tomara el arma si o si. El hacha de avion sirve para varias actividades como talar arboles, cazar hasta incluso matar."
  },
  {
    "id": 2,
    "imagen": "imagenes/Armas/CraftedAxe.webp",
    "nombre": "Hacha artesanal",
    "tipo": "Melee",
    "descripcion": "El hacha artesanal es la más lenta de todas las hachas, así como una de las armas más lentas del juego en términos de velocidad aunque hace mas daño que el hacha de avion. Sin embargo, como los elementos requeridos son muy comunes, puede ser útil fabricar esta arma muy pronto en el juego."
  },
  {
    "id": 3,
    "imagen": "imagenes/Armas/RustyAxe.webp",
    "nombre": "Hacha oxidada",
    "tipo": "Melee",
    "descripcion": "Esta hacha es más lenta y causa menos daño que el hacha moderna, pero tiene un mayor poder de derribo y el nivel de bloqueo más alto para un arma, similar al garrote y el caparazón de tortuga."
  },
  {
    "id": 4,
    "imagen": "imagenes/Armas/ModernAxe.webp",
    "nombre": "Hacha moderna",
    "tipo": "Melee",
    "descripcion": "La hacha moderna es la mejor hacha disponible para cortar árboles en el juego. Cuando se usa como arma, inflige cinco barras de daño. El hacha moderna se balancea más lento que el hacha de avion, pero derriba a los caníbales con más frecuencia que sus contrapartes más débiles."
  },
  {
    "id": 5,
    "imagen": "imagenes/Armas/ClimbingAxe.webp",
    "nombre": "Pico de escalada",
    "tipo": "Melee",
    "descripcion": "Se puede utilizar para escalar varios acantilados rocosos de la península y paredes específicas de las cuevas. Como arma, el hacha trepadora causa menos daño que el hacha de avion, pero se balancea rápido como la Katana."
  },
  {
    "id": 6,
    "imagen": "imagenes/Armas/Machete.webp",
    "nombre": "Machete",
    "tipo": "Melee",
    "descripcion": "El machete puede cortar palos de árboles, arbustos, arbustos de un solo golpe. Esto permite una recolección rápida de palos. Como arma el machete tiene un alcance muy corto y un daño intermedio. Casi todas las demás armas cuerpo a cuerpo del juego tienen un alcance mayor que el machete."
  },
  {
    "id": 7,
    "imagen": "imagenes/Armas/Katana.webp",
    "nombre": "Katana",
    "tipo": "Melee",
    "descripcion": "La Katana es un arma cuerpo a cuerpo de balanceo muy rápido. Su velocidad le permite al jugador golpear continuamente a un objetivo, evitando que el enemigo tome represalias. Sin embargo, la katana tiene un daño limitado en comparación con otras armas."
  },
  {
    "id": 8,
    "imagen": "imagenes/Armas/WeakSpear.webp",
    "nombre": "Lanza debil",
    "tipo": "Melee, Distancia",
    "descripcion": "La lanza debil es muy util para cazar ya que tiene un golpe terrestre que le permite cazar con mas facilidad a lagartos, peces, etc. Como arma, esta se puede lanzar pero su velocidad no es la mejor y su daño es intermedio, aunque esta es muy facil de crear ya que se necesitan solo 2 palos."
  },
  {
    "id": 9,
    "imagen": "imagenes/Armas/UpgradedSpear.webp",
    "nombre": "Lanza mejorada",
    "tipo": "Melee, Distancia",
    "descripcion": "La lanza mejorada es un arma de combate formidable, así como una herramienta de caza y recolección muy útil. Como es una de las pocas armas ofensivas que se pueden usar mientras se corre, es un arma muy efectiva para hacer kite (golpear y correr), tambien esta arma se puede lanzar logrando un gran daño."
  },
  {
    "id": 10,
    "imagen": "imagenes/Armas/Chainsaw.webp",
    "nombre": "Motosierra",
    "tipo": "Melee",
    "descripcion": "La motosierra es una herramienta y arma única que no requiere resistencia para usar y solo requiere mantener presionado el botón de ataque para operar. Es propulsado por combustible, que se puede encontrar en varios puntos de la Península. Es una herramienta muy útil para cortar arboles y un arma formidable por su daño y su velocidad de ataque."
  },
  {
    "id": 11,
    "imagen": "imagenes/Armas/CraftedBow.webp",
    "nombre": "Arco artesanal",
    "tipo": "Distancia",
    "descripcion": "El arco artesanal dispara flechas, no tiene una cruz ni una función de zoom. Al mantener presionado el botón de ataque, el jugador estirará el arco y apuntará la flecha hacia adelante (sin una cruz). Al soltar el botón de ataque, se disparará la flecha hacia adelante. Aunque el disparar un arco apuntando requiera de mucha practica, el daño de las flechas va dependiendo de que tipo se use."
  },
  {
    "id": 12,
    "imagen": "imagenes/Armas/TurtleShell.webp",
    "nombre": "Caparazon de tortuga",
    "tipo": "Melee",
    "descripcion": "También se puede sostener y usar como un arma de golpe improvisada. Solo inflige poco daño a los enemigos y consume mucha energía, pero es extremadamente eficiente para bloquear, logrando bloquear el daño de todos los caníbales (excepto el de Cowman)."
  },
  {
    "id": 13,
    "imagen": "imagenes/Armas/Club.webp",
    "nombre": "Mazo",
    "tipo": "Melee",
    "descripcion": "Los mazos se pueden saquear de la mayoría de los mutantes normales masculinos, es un arma lenta, pero causa un daño significativo a los enemigos. Junto con el caparazón de tortuga y el Hacha Oxidada, el Club tiene el nivel de bloqueo más alto posible para un arma."
  },
  {
    "id": 14,
    "imagen": "imagenes/Armas/Dynamite.webp",
    "nombre": "Dinamita",
    "tipo": "Distancia",
    "descripcion": "Un palo arrojable/colocable de dinamita. Puede usarse para hacer estallar muchas cosas similares a la bomba. Se puede utilizar como arma y es eficaz contra cualquier tipo de enemigos. Puede volar fácilmente caníbales, mutantes, árboles, etc."
  },
  {
    "id": 15,
    "imagen": "imagenes/Armas/Molotov.webp",
    "nombre": "Molotov",
    "tipo": "Distancia",
    "descripcion": "El Molotov puede encenderse usando el encendedor y lanzarse en la dirección deseada. Si se lanza sobre un objeto sólido, explotará y creará una pequeña área de fuego durante un breve período de tiempo. Si se lanza sobre cualquier enemigo o animal, causará daño por quemaduras al objetivo."
  }


  ]
  
  return render(request, 'Armas.html',{"armas":armas})

def construccion(request):
  
  construcciones = [
  {
    "nombre": "Fogata basica",
    "imagen": "imagenes/Construcciones/BasicFire.webp",
    "materiales": [
      "7 Hojas",
      "2 Palos"
    ],
    "descripcion": "La fogata basica es más útil cuando el jugador está fuera de casa y necesita una protección fiable contra el frío o quiere cocinar carne rápidamente, pero esta fogata dura un corto periodo de tiempo."
  },
  {
    "nombre": "Fogata avanzada",
    "imagen": "imagenes/Construcciones/FirePit.webp",
    "materiales": [
      "7 Hojas",
      "4 Palos",
      "7 Rocas"
    ],
    "descripcion": "La fogata avanzada puede servir como fuente de luz, calor y puede usarse para cocinar carne, esta fogata en comparación a la otra, no se rompe, solo se apaga."
  },
  {
    "nombre": "Hoguera",
    "imagen": "imagenes/Construcciones/Bonfire.webp",
    "materiales": [
      "20 Hojas",
      "10 Palos",
      "5 Rocas"
    ],
    "descripcion": "La hoguera actualmente es el fuego más grande del juego, proporciona la mayor cantidad de luz y calor, pero no puede cocinar alimentos."
  },
  {
    "nombre": "Refugio de caza",
    "imagen": "imagenes/Construcciones/HuntingShelter.webp",
    "materiales": [
      "7 Hojas",
      "6 Rocas",
      "7 Troncos"
    ],
    "descripcion": "El propósito del refugio de caza es poder guardar el progreso del jugador y ser un lugar en el cual puedes dormir y recuperar vida, energía, etc. Después de un uso, este refugio se destruirá."
  },
  {
    "nombre": "Cabaña pequeña",
    "imagen": "imagenes/Construcciones/SmallCabin.webp",
    "materiales": [
      "13 Hojas"
    ],
    "descripcion": "La cabaña pequeña es un refugio que no tiene piso, aunque tiene una puerta y una ventana. Permite al jugador guardar y dormir. Dormir en la cabina pequeña restaurará la fatiga y podrás guardar el juego en el interior."
  },
  {
    "nombre": "Cabaña grande",
    "imagen": "imagenes/Construcciones/LogCabin.webp",
    "materiales": [
      "82+ Troncos"
    ],
    "descripcion": "Dormir en la cabina grande restaurará la fatiga y podrás guardar el juego en el interior. Dado que hay dos ventanas abiertas en las paredes, es muy probable que encender un fuego en el interior atraiga la atención no deseada de caníbales y mutantes."
  },
  {
    "nombre": "Jaula para conejos",
    "imagen": "imagenes/Construcciones/RabbitCage.webp",
    "materiales": [
      "13 Palos"
    ],
    "descripcion": "Una jaula de conejos es un edificio de almacenamiento y un objeto que le permite almacenar y criar hasta siete conejos en una jaula."
  },
  {
    "nombre": "Colector de agua",
    "imagen": "imagenes/Construcciones/WaterCollector.webp",
    "materiales": [
      "4 Palos",
      "1 Caparazón de tortuga"
    ],
    "descripcion": "El Colector de agua es una construcción que recoge agua de lluvia limpia y potable de la que se puede beber o recoger utilizando la olla vieja o el odre."
  },
  {
    "nombre": "Reserva de palos (pequeño)",
    "imagen": "imagenes/Construcciones/StickHolderSmall.webp",
    "materiales": [
      "6 Palos"
    ],
    "descripcion": "Después de acercarse al soporte del palo, el jugador puede almacenar palos de su inventario cuando quede espacio y recogerlos cuando quiera."
  },
  {
    "nombre": "Marcador",
    "imagen": "imagenes/Construcciones/StickMarker.webp",
    "materiales": [
      "2 Palos",
      "2 Rocas",
      "1 Tela"
    ],
    "descripcion": "Los marcadores de palo son construcciones que agregan un marcador al HUD para permitir a los jugadores marcar y recordar ubicaciones."
  },
  {
    "nombre": "Trineo de Troncos",
    "imagen": "imagenes/Construcciones/LogSled.webp",
    "materiales": [
      "21 Palos"
    ],
    "descripcion": "El trineo de troncos se puede utilizar para almacenar y transportar troncos, rocas, palos, torsos y cuerpos. El trineo de troncos es inmune a casi todo en el juego: caníbales, mutantes, ataques físicos, explosivos y posiblemente más."
  },
  {
    "nombre": "Casa del árbol (Alpina)",
    "imagen": "imagenes/Construcciones/AlpineTreeHouse.webp",
    "materiales": [
      "18 Palos",
      "29 Troncos",
      "1 Cuerda"
    ],
    "descripcion": "Esta construcción se crea en un árbol y es similar a la casa del árbol estándar, sin embargo, la casa del árbol Alpina ofrece un techo triangular, un balcón para observar el bosque y barandillas. Al igual que otros refugios, la casa del árbol alpino proporciona al jugador un área para dormir y guardar su progreso, al mismo tiempo que sirve como refugio seguro para escapar de los caníbales."
  },
  {
    "nombre": "Trampa de animales",
    "imagen": "imagenes/Construcciones/AnimalTrap.webp",
    "materiales": [
      "13 Palos"
    ],
    "descripcion": "Una trampa para animales es una construcción que te permite atrapar un conejo, un lagarto, una ardilla, un mapache o un jabalí a la vez sin matarlo."
  },
  {
    "nombre": "Casa del árbol",
    "imagen": "imagenes/Construcciones/TreeHouse.webp",
    "materiales": [
      "35 Troncos",
      "1 Cuerda (opcional)"
    ],
    "descripcion": "La casa del árbol es una casa, que como dice su nombre, se crea en el árbol, se puede usar para ahorrar y dormir. Se ingresa a la casa del árbol subiendo una cuerda y también se puede salir bajando."
  },
  {
    "nombre": "Gazebo",
    "imagen": "imagenes/Construcciones/Gazebo.webp",
    "materiales": [
      "60 Palos",
      "30+ Troncos"
    ],
    "descripcion": "No tiene otro propósito que el de decoración, ya que no se puede interactuar con él. Actualmente, el Gazebo requiere la mayor cantidad de palos de cualquier estructura hecha por jugadores. La cantidad final de troncos se determina si necesita cimientos adicionales y qué tan alto se coloca."
  }


  ]
  
  return render(request, 'Construcciones.html', {"construcciones":construcciones})

def consumibles(request):
  
  consumibles= [
    {
      "nombre": "Aloe",
      "imagen": "imagenes/Consumibles/Aloe.webp",
      "modo_normal": {
        "hambre": 5,
        "agua": 0,
        "vida": 2,
        "energia": 2
      },
      "modo_dificil": {
        "hambre": 5,
        "agua": 0,
        "vida": 2,
        "energia": 2
      }
    },
    {
      "nombre": "Amanita",
      "imagen": "imagenes/Consumibles/AmanitaMushroom.webp",
      "modo_normal": {
        "hambre": 5,
        "agua": 0,
        "vida": -2,
        "energia": 10
      },
      "modo_dificil": {
        "hambre": 5,
        "agua": 0,
        "vida": -30,
        "energia": 10
      }
    },
    {
      "nombre": "Bayas negras",
      "imagen": "imagenes/Consumibles/BlackBerries.webp",
      "modo_normal": {
        "hambre": 5,
        "agua": 10,
        "vida": 0,
        "energia": 10
      },
      "modo_dificil": {
        "hambre": 5,
        "agua": 10,
        "vida": 0,
        "energia": 10
      }
    },
    {
      "nombre": "Beber con manos",
      "imagen": "imagenes/Consumibles/Bloodied.webp",
      "modo_normal": {
        "hambre": 0,
        "agua": 10,
        "vida": -1,
        "energia": 0
      },
      "modo_dificil": {
        "hambre": 0,
        "agua": 5,
        "vida": -20,
        "energia": 0
      }
    },
    {
      "nombre": "Alcohol",
      "imagen": "imagenes/Consumibles/Booze.webp",
      "modo_normal": {
        "hambre": 2,
        "agua": 50,
        "vida": 15,
        "energia": -10
      },
      "modo_dificil": {
        "hambre": 2,
        "agua": 50,
        "vida": 15,
        "energia": -10
      }
    },
    {
      "nombre": "Pescado",
      "imagen": "imagenes/Consumibles/FishEdible.webp",
      "modo_normal": {
        "hambre": 61,
        "agua": 0,
        "vida": 0,
        "energia": 40
      },
      "modo_dificil": {
        "hambre": 61,
        "agua": 0,
        "vida": 0,
        "energia": 14
      }
    },
    {
      "nombre": "Cabeza",
      "imagen": "imagenes/Consumibles/Head.webp",
      "modo_normal": {
        "hambre": 10,
        "agua": 0,
        "vida": 0,
        "energia": 10
      },
      "modo_dificil": {
        "hambre": 10,
        "agua": 0,
        "vida": 0,
        "energia": 10
      }
    },
    {
      "nombre": "Carne cocinada",
      "imagen": "imagenes/Consumibles/IconMeatBurnt.webp",
      "modo_normal": {
        "hambre": 17,
        "agua": -10,
        "vida": 0,
        "energia": 10
      },
      "modo_dificil": {
        "hambre": 17,
        "agua": -40,
        "vida": 0,
        "energia": 3
      }
    },
    {
      "nombre": "Piernas",
      "imagen": "imagenes/Consumibles/Leg.webp",
      "modo_normal": {
        "hambre": 98,
        "agua": 20,
        "vida": 0,
        "energia": 80
      },
      "modo_dificil": {
        "hambre": 7,
        "agua": 0,
        "vida": -5,
        "energia": 4
      }
    },
    {
      "nombre": "Carne cruda",
      "imagen": "imagenes/Consumibles/Meat.webp",
      "modo_normal": {
        "hambre": 98,
        "agua": -5,
        "vida": 20,
        "energia": 80
      },
      "modo_dificil": {
        "hambre": 98,
        "agua": -20,
        "vida": 7,
        "energia": 28
      }
    },
    {
      "nombre": "Medicina",
      "imagen": "imagenes/Consumibles/Meds.webp",
      "modo_normal": {
        "hambre": 0,
        "agua": 0,
        "vida": 100,
        "energia": 0
      },
      "modo_dificil": {
        "hambre": 0,
        "agua": 0,
        "vida": 75,
        "energia": 0
      }
    },
    {
      "nombre": "Ostra",
      "imagen": "imagenes/Consumibles/Oyster.webp",
      "modo_normal": {
        "hambre": 15,
        "agua": 0,
        "vida": 3,
        "energia": 12
      },
      "modo_dificil": {
        "hambre": 14,
        "agua": 1,
        "vida": 4,
        "energia": 12
      }
    },
    {
      "nombre": "Carne de conejo",
      "imagen": "imagenes/Consumibles/RabbitMeat.webp",
      "modo_normal": {
        "hambre": 98,
        "agua": -5,
        "vida": 20,
        "energia": 80
      },
      "modo_dificil": {
        "hambre": 98,
        "agua": -20,
        "vida": 7,
        "energia": 28
      }
    },
    {
      "nombre": "Snack",
      "imagen": "imagenes/Consumibles/Snack.webp",
      "modo_normal": {
        "hambre": 25,
        "agua": 0,
        "vida": 5,
        "energia": 20
      },
      "modo_dificil": {
        "hambre": 25,
        "agua": 0,
        "vida": 5,
        "energia": 20
      }
    },
    {
      "nombre": "Bebida",
      "imagen": "imagenes/Consumibles/Soda.webp",
      "modo_normal": {
        "hambre": 0,
        "agua": 50,
        "vida": 0,
        "energia": 80
      },
      "modo_dificil": {
        "hambre": 0,
        "agua": 40,
        "vida": 0,
        "energia": 60
      }
    }
  ]



  return render(request, 'Consumibles.html', {"consumibles":consumibles})