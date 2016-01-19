import operator

class Source(object):

  def __init__(self, name):
    self._name = name;

  def __repr__(self):
      return "Source [name: {0}]".format(str(self._name))


class BookSource(Source):

  def __init__(self, book_name, page):
    super(BookSource, self).__init__(book_name)
    self._page = page

  def __repr__(self):
      return "BookSource [name: {0}, page: {1}]".format(str(self._name), str(self._page))


class Comments(object):
  
  # have_made: bool, true if I've made it before
  # stars: int, 1-5
  # notes: string, any notes I have on it, regardless of whether I've made it or not
  # to_improve: string, things I could improve upon
  def __init__(self, have_made, stars, notes, to_improve):
    self._have_made = have_made
    self._stars = stars
    self._notes = notes
    self._to_improve = to_improve

  def __repr__(self):
    return "Comments [have_made: {0}, stars: {1}, notes: {2}, to_improve: {3}]".format(str(self._have_made), str(self._stars), str(self._notes), str(self._to_improve))


class Recipe(object):

  def __init__(self, name, source, ingredients, comments):
    self._name = name
    self._source = source
    self._ingredients = ingredients
    self._comments = comments

  def __repr__(self):
      return "\n* Recipe [name: {0}, source: {1}, ingredients: {2}, comments: {3}]".format(str(self._name), str(self._source), str(self._ingredients), str(self._comments))


# SN = Source Names
class SN(object):
  death_co_name = "Death & Co"
  internet = "Internet"
  ekon = "ekon" # recipes I made up


class Gin(object):
  beefeater = "Beefeater London Dry Gin"
  plymouth = "Plymouth Gin"
  tanqueray = "Tanqueray London Dry Gin"
  haymans = "Hayman's Old Tom Gin"
  ransom = "Ransom Old Tom Gin"
  bols_genever = "Bols Genever"
  anchor = "Anchor Distilling Company Junipero Gin"
  perrys = "Perry's Tot Navy-Strength Gin"
  
  # not in recommended section
  anchor = "Anchor Junipero Gin"
  fords = "Fords Gin"


# R = Rum
class R(object):
  cana_brava = "Cana Brave rum (Panama)"
  flor_de_cana = "Flor de Cana Extra-Dry White Rum (Nicaragua)"
  ron_del_barrilito_3 = "Ron del berrilito 3-star Rum"
  santa_teresa = "Santa Teresa 1796 Ron Antiguo de Solera Rum (Venezuela)"
  el_dorado_12 = "El Dorado 12-Year Rum (Guyana)"
  goslings = "Gosling's Black Seal Rum (Bermuda)"
  lemon_hart_151 = "Lemon Hart 151 Rum (Guyana)"
  scarlet = "Scarlet Ibis Rum (Trinidad)"
  appleton_vx = "Appleton Estate V/X Rum (Jamaica)"
  smiths = "Smith & Cross Rum (Jamaica)"
  barbancourt_white = "Barbancourt White Rhum (Haiti)"
  la_favorite_ambre = "La Favorite Rhum Agricole Ambre (Martinique)"
  la_favorite_blanc = "La Favorite Rhum Agricole Blanc (Martinique)"
  
  # not in the recommendations
  appleton_reserve = "Appleton Estate Reserve Rum"
  el_dorado_151 = "El Dorado 151 Rum"
  el_dorado_15 = "El Dorado 15-Year Rum"
  el_dorado_3 = "El Dorado 3-Year Rum"
  clement_creole = "Rhum Clement Creole Shrubb"
  barbancourt_3 = "Barbancourt 3-Star Rhum"
  lemon_hart_original = "Lemon Hart Original  Rum"


# T = Tequila
class T(object):
  siembra_blanco = "Siembra Azul Blanco Tequila"
  siete_blanco = "Siete Leguas Blanco Tequila"
  el_tesoro_platinum = "El Tesoro Platinum Tequila"
  el_tesoro_repasado = "El Tesoro Reposado Tequila"
  siete_reposado = "Siete Leguas Reposado Tequila"
  el_tesaro_anejo = "El Tesaro Anejo Tequila"

  # not in the recommendations
  tapatio_blanco = "Tapatio 110 Blanco Tequila"


class Mezcal(object):
  del_maguey_chichicapa = "Del Maguey Chichicapa Mezcal"
  del_maguey_crema = "Del Maguey Crema de Mezcal"
  del_maguey_vida = "Del Maguey Vida Mezcal"
  los_amantes_joven = "Los Amantes Joven Mezcal"


# W = Whiskey
class W(object):
  buffalo_bourbon = "Buffalo Trace Kentucky Straight Bourbon"
  elijah_bourbon = "Elijah Craig 12-Year Kentucky Straight Bourbon"
  old_grand_dad_114_bourbon = "Old Grand-Dad 114 Kentucky Straight Bourbon"
  old_overholt_rye = "Old Overhold Kentucky Straight Rye"
  rittenhouse_rye = "Rittenhouse Bonded 100-Proof Kentucky Straight Rye"
  compass_scotch = "Compass Box Asyla Blended Scotch"
  famous_grouse_scotch = "Famous Grouse Blended Scotch"
  knappogue_whiskey = "Knappogue Castle 12-Year Irish Whiskey"
  laphroaig_scotch = "Laphroaig 10-Year Islay Single-Malt Scotch"
  redbreast_whiskey = "Redbreast 12-Year Irish Whiskey"
  
  # not mentioned in recommendation section
  springbank_10_scotch = "Springback 10-Year Scotch"
  bakers_bourbon = "Baker's Bourbon"
  eagle_bourbon = "Eagle Rare 10-Year Bourbon"
  templeton_rye = "Templeton Rye"


class Brandy(object):
  acholado_pisco = "Campo de Encanto Acholado Pisco"
  hine_cognac = "Hine H VSOP Cognac"
  pierre_ferrand_1840_cognac = "Pierre Ferrand 1840 Cognac"
  pierre_ferrand_ambre_cognac = "Pierre Ferrand Ambre Cognac"
  lairds_apple = "Laird's Bottled-in-Bond Straight Apple Brandy"
  busnel_calvados = "Busnel Calvados Pays d'Auge VSOP"
  clear_creek_pear = "Clear Creek Pear Brandy"
  massenez_cherry = "G. E. Massenez Kirsch Cherry Brandy"
  massenez_peach = "G. E. Massenez Kirsch Pearch Brandy"
  

class Vodka(object):
  # there are no recommendations for vodka, but some recipes ask for them
  charbay = "Charbay Vodka"

# Other spirits
class OS(object):
  linie_aquavit = "linie Aquavit"
  krogstad_aquavit = "Krogstad Aquavit"
  emile_pernot_absinthe = "Emile Pernot Vieux Pontalier Absinthe"
  van_oosten = "Van Oosten Batavia Arrach" # can't quite figure out if it's an ingredient (pg. 37)
  
  # not in recommendations
  vieux_absinthe = "Vieux Pontarlier Absinthe"


# TODO: Liqueur is a Modifier, but haven't yet needed to make a base class for Modifier, may want to though to include the Other category? Although that would be a very weird inheritance! The other Category should also then just be a subclass of Modifiers. But doesn't make sense to keep a class empty.
class L(object):
  benedictine = "Benedictine"
  green_chartreuse = "Green Chartreuse"
  yellow_chartreuse = "Yellow Chartreuse"
  cointreau = "Cointreau"
  galliano = "Gualliano l'Authentico"
  grand_marnier = "Grand Marnier"
  kalani_coconut = "Kalani Ron De Coco Coconut Liqueur"
  luxardo = "Luxardo Maraschino Liqueur"
  marie_cacao_cream = "Marie Brizard White Creme de Cacao"
  rothman_apricot = "Rothman & Winter Orchard Apricot Liqueur"
  strega = "Strega"
  allspice_dram = "St. Elizabeth Allspice Dram"
  st_germain = "St-Germain"
  suze = "Suze Saveur d'Autrefois Liqueur"
  falernum = "John D. Taylor Velvet Falernum"
  
  # not mentioned in recommendation section
  cherry_heering = "Cherry Heering Liqueur"
  drambuie = "Drambuie" # honey spice liqueur with scotch base
  gabriel_curacao = "Gabriel Boudier Curacao" # blue
  maraska_maraschino = "Marasaca Maraschino Liqueur"
  massenez_peach_cream = "Massenez Creme de Peche Peach Liqueur"
  marie_mint_cream = "Marie Brizard White Creme de Menthe"


# Includes Amari, Aperitifs and Digestifs
class Amari(object):
  amaro_averna = "Amaro Averna"
  amaro_ciociaro = "Amaro CioCiaro"
  amaro_meletti = "Amaro Meletti"
  amaro_nardini = "Amaro Nardini"
  amaro_nanino = "Amaro Nanino Quintessentia"
  aprol = "Aperol"
  campari = "Campari"
  cynar = "Cynar"
  fernet_branca = "Fernet-Branca"
  ramazzotti = "Ramazzotti"


# V = Vermouth
class V(object):
  carpano = "Carpano Antica Formula Vermouth" # sweet
  cocchi = "Cocchi Vermouth di Torino" # sweet
  dolin_blanc = "Dolin Blanc Vermouth"
  dolin_dry = "Dolin Dry Vermouth"
  dolin_rouge = "Dolin Rouge Vermouth"
  punt_e_mes = "Punt e Mes"
  
  # not mentioned in recommendation section
  house_sweet = "House sweet Vermouth" # instructions on pg. 284
  contratto = "Contratto Antica Formula Vermouth"
  carpano_coffee = "Coffee-infused Carpano Antica Formula Vermouth" # instructions on pg. 282


class Sherry(object):
  alvear_pale_cream = "Alvear Festival Pale Cream Montilla-Moriles"
  manzanilla = "La Gitana Manzanilla Sherry"
  solera = "Lustau East Indian Solera Sherry"
  amontillado = "Lustau Los Acros Amontillado Sherry"
  williams_dry = "Williams & Humbert Dry Sack Medium Sherry"
  barbadillo = "Barbadillo Principe Amontillado Sherry" # not in recommendation section


class Port(object):
  graham_reserve = "Graham's \"Six Grape\" Reserve Ruby Port"
  warre_tawny = "Warre's Otima Ten-Year Tawyny Port"


# AW = Aperitif Wines
class AW(object):
  bonal = "Bonal Gentiane-Quina"
  cocchi_americano = "Cocchi Americano"
  lillet_blanc = "Lillet Blanc"
  lillet_rouge = "Lillet Rouge"
  lillet_rose = "Lillet Rose"


# B = Bitters
class B(object):
  # lifting
  cherry_vanilla = "Bittercube cheery bark and vanilla bitters"
  celery = "Bitter Truth Celery bitters"
  tiki = "Bittermens 'Elemakule Tiki bitters"
  gapefruit = "Bittermens hopped grapefruit bitters"
  habanero = "Bittermens Hellfire habanero shrub"
  house_orange = "House orange" # instructions on pg. 284
  o = "Orange" # also binding
  
  # binding
  a = "Angostura"
  mole = "Bittermens Xocolatl mole bitters"
  bt = "Bitter Truth aromatic bitters"
  jt = "Bitter Truth Jerry Thomas' bitters"
  whiskey = "Fee Brothers whiskey barrel-aged bitters"
  house_peychauds = "House Peychaud's bitters" # instructions on pg. 284
  p = "Peychaud's"
  
  # not mentioned in recommendation section
  levender = "Scrappy's levender bitters"


# J = juice
class J(object):
  apple = "Apple"
  lemon = "Lemon"
  lime = "Lime"
  grapefruit = "Grapefruit"
  orange = "Orange"
  blood_orange = "Blood orange"
  pineapple = "Pineapple"
  cantaloupe = "Cantaloupe"
  carrot = "Carrot"
  celery = "Celery"
  red_pepper = "Red bell pepper"
  watermelon = "Watermelon"


class O(object):
  acid_phosphate = "Acid Phosphate" # adds acidity/sourness without sweetness that comes with citrus juice
  coco_lopez = "Coco lopez" # sugar sweetner
  pomegranate_molasses = "Pomegranet molasses"
  rose_water = "Rose water"
  verjus = "Verjus"
  
  creme_yvette = "Creme Yvette"
  simple_syrup = "simple syrup"
  acacia_honey_syrup = "acacia honey syrup" # instructions on pg. 286 in the book
  dry_champagne = "dry champagne"
  club_soda = "Club soda"
  cane_sugar_syrup = "cane sugar syrup"
  white_sugar_cube = "White sugar cube"
  passion_fruit_syrup = "Passion Fruit Syrup" # instructions on pg. 277
  cinnamon_bark_syrup = "Cinnamon Bark Syrup" # instructions on pg. 276
  ginger_syrup = "Ginger Syrup" # instructions on pg. 277
  orgeat = "Orgeat" # almond-based syrup, instructions on pg. 278
  demerara_syrup = "Demerara syrup" # instructions on pg. 277
  pendennis_mix = "Pendennis mix" # instructions on pg. 284
  agave_nectar = "Agave nectar"
  egg_white = "Egg white"
  egg_yolk = "Egg yolk"
  heavy_cream = "Heavy cream"
  lime_cordial = "Toby's lime cordial" # instructions on pg. 285
  grenadine = "Grenadine" # instructions on pg. 284
  donns_spices_2 = "Donn's spices #2" # instructions on pg. 284
  san_pellegrino_grapefruit = "San Pellegrino Pompelmo Grapefruit soda"
  orange_flower_water = "Orange flower water"
  zombie_mix = "Zombie mix" # instructions on pg. 284
  
  avua_cachaca = "Avua amburana cachaca"


# G = Garnish
class G(object):
  lemon = "lemon"
  lime = "lime"
  orange = "orange"
  grapefruit = "Grapefruit"
  apple = "Apple"
  brandied_cherry = "Luxardo Marasche brandied cherry"
  cherry = "Cherry flag"
  cucumber = "Cucumber"
  mint = "Mint"
  curry_leaf = "Curry leaf"
  kaffir_lime_leaf = "Kaffir lime leaf"
  pear = "Pear"
  pineapple = "Pineapple"
  raspberry = "Raspberry"
  blackberry = "Blackberry"
  strawberry = "Strawberry"
  chocolate = "Chocolate"
  dark_chocolate = "Dark Chocolate"
  cinnamon = "Cinnamon"
  nutmeg = "Nutmeg"
  candied_ginger = "Candied ginger flag"


class RecipeBook(object):

  def __init__(self):
    no_comments = Comments(False, "", "", "")
    
    self._recipes = [Recipe("20th Century", BookSource(SN.death_co_name, 139), [Gin.beefeater, L.marie_cacao_cream, AW.cocchi_americano, J.lemon], no_comments),
      Recipe("Airmail", BookSource(SN.death_co_name, 139), [R.ron_del_barrilito_3, J.lime, O.acacia_honey_syrup, O.dry_champagne], no_comments),
      Recipe("Aviation", BookSource(SN.death_co_name, 139), [Gin.plymouth, L.luxardo, O.creme_yvette, J.lemon, O.simple_syrup, G.brandied_cherry], no_comments),
      Recipe("Bamboo", BookSource(SN.death_co_name, 140), [V.dolin_blanc, Sherry.barbadillo, O.cane_sugar_syrup, B.o, B.a, G.lemon], no_comments),
      Recipe("Bee's Knees", BookSource(SN.death_co_name, 140), [Gin.tanqueray, J.lemon, O.acacia_honey_syrup, B.levender, G.brandied_cherry], no_comments),
      Recipe("Blood and Sand", BookSource(SN.death_co_name, 140), [W.springbank_10_scotch, L.cherry_heering, V.house_sweet, J.orange, J.lemon, G.brandied_cherry], no_comments),
      Recipe("Bobby Burns", BookSource(SN.death_co_name, 140), [W.springbank_10_scotch, V.house_sweet, L.drambuie, G.lemon, B.a], no_comments),
      Recipe("Boulevardier", BookSource(SN.death_co_name, 140), [W.elijah_bourbon, V.house_sweet, Amari.campari, G.lemon], no_comments),
      Recipe("Brooklyn", BookSource(SN.death_co_name, 140), [W.rittenhouse_rye, V.dolin_dry, Amari.amaro_ciociaro, L.luxardo], no_comments),
      Recipe("Brown Derby", BookSource(SN.death_co_name, 140), [W.elijah_bourbon, J.grapefruit, J.lemon, O.acacia_honey_syrup, G.grapefruit], no_comments),
      Recipe("Caipirinha", BookSource(SN.death_co_name, 141), [J.lime, O.simple_syrup, O.white_sugar_cube, O.avua_cachaca], no_comments),
      Recipe("Champs-elysees", BookSource(SN.death_co_name, 141), [Brandy.pierre_ferrand_ambre_cognac, L.green_chartreuse, J.lemon, O.cane_sugar_syrup, B.a, G.lemon], no_comments),      
      Recipe("Charleston Cocktail", BookSource(SN.death_co_name, 141), [Gin.anchor, Brandy.massenez_cherry, V.dolin_dry, V.punt_e_mes, L.gabriel_curacao, L.maraska_maraschino], no_comments),
      Recipe("Cobra's Fang", BookSource(SN.death_co_name, 141), [R.appleton_reserve, R.el_dorado_151, L.massenez_peach_cream, OS.vieux_absinthe, J.lime, J.orange, O.passion_fruit_syrup, O.cinnamon_bark_syrup, O.ginger_syrup, B.a, G.mint, G.lime], no_comments),
      Recipe("Corpse Reviver #2", BookSource(SN.death_co_name, 141), [Gin.beefeater, L.cointreau, AW.lillet_blanc, OS.vieux_absinthe, J.lemon], no_comments),
      Recipe("Daiquiri", BookSource(SN.death_co_name, 141), [R.flor_de_cana, J.lime, O.cane_sugar_syrup, G.lime], no_comments),
      Recipe("Dark and Stormy", BookSource(SN.death_co_name, 142), [R.goslings, J.lime, O.ginger_syrup, O.club_soda, G.lime, G.candied_ginger], no_comments),
      Recipe("Diamondback", BookSource(SN.death_co_name, 142), [W.rittenhouse_rye, Brandy.lairds_apple, L.yellow_chartreuse], no_comments),
      Recipe("Fancy Tree", BookSource(SN.death_co_name, 142), [W.rittenhouse_rye, L.luxardo, B.a, B.house_orange, G.orange], no_comments),
      Recipe("Fitzerald", BookSource(SN.death_co_name, 142), [Gin.beefeater, J.lemon, O.simple_syrup, B.a, G.lemon], no_comments),
      Recipe("Flamenco", BookSource(SN.death_co_name, 142), [Sherry.amontillado, Gin.bols_genever, J.orange, J.lemon, O.orgeat, B.a], no_comments),
      Recipe("French 75", BookSource(SN.death_co_name, 143), [Gin.plymouth, J.lemon, O.cane_sugar_syrup, O.dry_champagne, G.lemon], no_comments),
      Recipe("French 95", BookSource(SN.death_co_name, 143), [W.buffalo_bourbon, J.lemon, O.cane_sugar_syrup, O.dry_champagne], no_comments),
      Recipe("Gimlet", BookSource(SN.death_co_name, 143), [Gin.perrys, O.lime_cordial, G.lime], no_comments),
      Recipe("Gin Fizz", BookSource(SN.death_co_name, 143), [Gin.beefeater, J.lemon, O.simple_syrup, O.egg_white, O.club_soda], no_comments),
      Recipe("Gin Rickey", BookSource(SN.death_co_name, 143), [Gin.beefeater, J.lime, O.simple_syrup, O.club_soda, G.lime], no_comments),
      Recipe("Grasshopper", BookSource(SN.death_co_name, 143), [G.mint, L.marie_mint_cream, L.marie_cacao_cream, O.heavy_cream, G.mint], no_comments),

      Recipe("Hanky-panky", BookSource(SN.death_co_name, 144), [Gin.fords, V.contratto, V.carpano,
      Amari.fernet_branca, G.lemon], no_comments),
      Recipe("Honeysuckle", BookSource(SN.death_co_name, 144), [R.flor_de_cana, J.lime,
      O.acacia_honey_syrup, G.lime], no_comments),
      Recipe("Jack Rose", BookSource(SN.death_co_name, 144), [Brandy.lairds_apple,
      Brandy.busnel_calvados, J.lemon, J.lime, O.grenadine, G.apple], no_comments),
      Recipe("La Rosita", BookSource(SN.death_co_name, 144), [T.el_tesoro_repasado, Amari.campari,
      V.cocchi, V.dolin_dry, B.a, G.orange], no_comments),
      Recipe("Last Word", BookSource(SN.death_co_name, 144), [Gin.beefeater, L.green_chartreuse,
      L.luxardo, J.lime], no_comments),
      Recipe("Lucien Gaudin", BookSource(SN.death_co_name, 144), [Gin.tanqueray, V.dolin_dry,
      Amari.campari, L.cointreau, G.lemon], no_comments),
      Recipe("Mai Tai", BookSource(SN.death_co_name, 144), [J.lime, R.el_dorado_15, R.appleton_vx,
      R.la_favorite_blanc, R.clement_creole, J.lime, O.orgeat, B.a, G.mint], no_comments),
      Recipe("Manhattan", BookSource(SN.death_co_name, 145), [W.rittenhouse_rye, V.house_sweet, B.a,
      G.brandied_cherry], no_comments),
      Recipe("Margarita", BookSource(SN.death_co_name, 145), [T.siembra_blanco, L.cointreau, J.lime,
      O.agave_nectar, G.lime], no_comments),
      Recipe("Martinez", BookSource(SN.death_co_name, 145), [Gin.haymans, Gin.ransom, V.house_sweet,
      L.luxardo, Brandy.massenez_cherry, B.house_orange, G.lemon], no_comments),
      Recipe("Martini", BookSource(SN.death_co_name, 145), [Gin.beefeater, V.dolin_dry,
      B.house_orange, G.lemon], no_comments),
      Recipe("Martini", BookSource(SN.death_co_name, 145), [Gin.tanqueray, V.dolin_dry,
      B.house_orange, G.lemon], no_comments),
      Recipe("Mexican Firing Squad", BookSource(SN.death_co_name, 145), [T.tapatio_blanco, J.lime,
      O.cane_sugar_syrup, O.grenadine, B.habanero, G.lime, G.cherry], no_comments),
      Recipe("Mint Julep", BookSource(SN.death_co_name, 147), [W.bakers_bourbon, O.simple_syrup,
      G.mint], no_comments),
      Recipe("Mojito", BookSource(SN.death_co_name, 147), [G.mint, O.simple_syrup, R.cana_brava,
      J.lime, B.a], no_comments),
      Recipe("Moscow Mule", BookSource(SN.death_co_name, 147), [Vodka.charbay, J.lime,
      O.ginger_syrup, G.lime, G.candied_ginger], no_comments),
      Recipe("Mudslide Flip", BookSource(SN.death_co_name, 147), [W.redbreast_whiskey,
      V.carpano_coffee, O.demerara_syrup, O.egg_yolk, O.heavy_cream, B.a, G.dark_chocolate], no_comments),
      Recipe("Negroni", BookSource(SN.death_co_name, 147), [Gin.tanqueray, Amari.campari,
      V.house_sweet, G.orange], no_comments),
      Recipe("Old-Fashioned", BookSource(SN.death_co_name, 147), [W.eagle_bourbon, O.demerara_syrup,
      B.a, B.bt, G.orange, G.lemon], no_comments),
      Recipe("Old Pal", BookSource(SN.death_co_name, 148), [W.rittenhouse_rye, Amari.campari,
      V.dolin_dry, G.lemon], no_comments),
      Recipe("Paloma", BookSource(SN.death_co_name, 148), [G.lime, T.el_tesoro_platinum,
      J.grapefruit, O.simple_syrup, O.san_pellegrino_grapefruit, G.lime], no_comments),
      Recipe("Pendennis Club Cocktail", BookSource(SN.death_co_name, 148), [Gin.plymouth,
      O.pendennis_mix, J.lime, B.house_peychauds, G.lime], no_comments),
      Recipe("Pina Colada", BookSource(SN.death_co_name, 148), [R.smiths, R.el_dorado_151,
      R.el_dorado_3, L.kalani_coconut, J.pineapple, J.lime, O.coco_lopez, B.a, G.mint], no_comments),
      Recipe("Ping-Pong Cocktail", BookSource(SN.death_co_name, 148), [Gin.plymouth, V.dolin_dry,
      V.punt_e_mes, B.house_orange, G.lemon], no_comments),
      Recipe("Pink Lady", BookSource(SN.death_co_name, 148), [Gin.plymouth, Brandy.lairds_apple,
      J.lemon, O.acacia_honey_syrup, O.grenadine, O.egg_white, G.brandied_cherry], no_comments),
      Recipe("Pisco Sour", BookSource(SN.death_co_name, 149), [Brandy.acholado_pisco, J.lemon,
      J.lime, O.simple_syrup, O.egg_white, B.a], no_comments),
      Recipe("Port au Prince", BookSource(SN.death_co_name, 149), [R.barbancourt_3, R.el_dorado_3,
      R.lemon_hart_151, L.falernum, J.lime, J.pineapple, O.grenadine, O.ginger_syrup, B.tiki,
      G.pineapple, G.brandied_cherry], no_comments),
      Recipe("Preakness", BookSource(SN.death_co_name, 149), [W.old_grand_dad_114_bourbon,
      V.carpano, L.benedictine, B.bt, G.orange], no_comments),
      Recipe("Queen's Park Swizzle", BookSource(SN.death_co_name, 150), [G.mint, O.simple_syrup,
      O.white_sugar_cube, R.cana_brava, J.lime, B.house_peychauds, B.a], no_comments),
      Recipe("Ramos Gin Fizz", BookSource(SN.death_co_name, 150), [Gin.plymouth, J.lemon, J.lime,
      O.simple_syrup, O.heavy_cream, O.egg_white, O.orange_flower_water, O.club_soda], no_comments),
      Recipe("Remember the Name", BookSource(SN.death_co_name, 150), [OS.vieux_absinthe,
      W.rittenhouse_rye, V.cocchi, L.cherry_heering, Brandy.massenez_cherry, G.lemon], no_comments),
      Recipe("Rob Roy", BookSource(SN.death_co_name, 150), [W.compass_scotch, V.carpano, B.a,
      G.brandied_cherry], no_comments),
      Recipe("Rum Julep", BookSource(SN.death_co_name, 150), [R.lemon_hart_151,
      R.lemon_hart_original, R.appleton_vx, L.falernum, O.donns_spices_2, J.orange, J.lime,
      O.acacia_honey_syrup, G.mint], no_comments),
      Recipe("Rusty Nail", BookSource(SN.death_co_name, 151), [W.springbank_10_scotch, L.drambuie,
      B.bt, G.lemon], no_comments),
      Recipe("Sazerac", BookSource(SN.death_co_name, 151), [OS.vieux_absinthe, W.rittenhouse_rye,
      Brandy.pierre_ferrand_1840_cognac, O.demerara_syrup, B.p, B.a, G.lemon], no_comments),
      Recipe("Scofflaw", BookSource(SN.death_co_name, 151), [W.templeton_rye, V.dolin_blanc,
      V.dolin_dry, J.lemon, O.grenadine], no_comments),
      Recipe("Sidecar", BookSource(SN.death_co_name, 151), [Brandy.pierre_ferrand_1840_cognac,
      L.cointreau, J.lemon, O.cane_sugar_syrup, G.orange], no_comments),
      Recipe("Singapore Sline", BookSource(SN.death_co_name, 151), [Gin.beefeater, L.cherry_heering,
      L.cointreau, L.benedictine, J.pineapple, J.lime, O.grenadine, B.a, G.pineapple,
      G.brandied_cherry], no_comments),
      Recipe("South Side", BookSource(SN.death_co_name, 151), [G.mint, Gin.beefeater, J.lime,
      O.cane_sugar_syrup, B.a], no_comments),
      Recipe("Stringer", BookSource(SN.death_co_name, 152), [Brandy.pierre_ferrand_1840_cognac,
      L.marie_mint_cream, O.simple_syrup, G.mint], no_comments),
      Recipe("Tailspin", BookSource(SN.death_co_name, 152), [Gin.beefeater, V.carpano,
      L.green_chartreuse, B.house_orange, G.lemon], no_comments),
      Recipe("Ti Punch", BookSource(SN.death_co_name, 152), [J.lime, O.cane_sugar_syrup,
      R.la_favorite_blanc], no_comments),
      Recipe("Tom Collins", BookSource(SN.death_co_name, 152), [Gin.beefeater, J.lemon,
      O.simple_syrup, O.club_soda, G.orange, G.cherry], Comments(True, 5, "refreshing, just a tad boozie", "don't forget the club soda")),
      Recipe("Toronto", BookSource(SN.death_co_name, 152), [W.rittenhouse_rye, Amari.fernet_branca,
      O.demerara_syrup, G.lemon], no_comments),
      Recipe("Vesper", BookSource(SN.death_co_name, 152), [Gin.plymouth, Vodka.charbay,
      AW.cocchi_americano, G.lemon], no_comments),
      Recipe("Vieux Carre", BookSource(SN.death_co_name, 153), [W.rittenhouse_rye,
      Brandy.pierre_ferrand_ambre_cognac, V.carpano, L.benedictine, B.a, B.house_peychauds, G.lemon], no_comments),
      Recipe("Ward 8", BookSource(SN.death_co_name, 153), [W.old_overholt_rye, J.lemon, J.orange,
      O.simple_syrup, O.pomegranate_molasses], no_comments),
      Recipe("Whiskey Sour", BookSource(SN.death_co_name, 153), [W.buffalo_bourbon, J.lemon,
      O.simple_syrup, O.egg_white, B.a, G.orange, G.cherry], no_comments),
      Recipe("Zombie Punch", BookSource(SN.death_co_name, 153), [R.appleton_vx,
      R.ron_del_barrilito_3, R.lemon_hart_151, O.zombie_mix, O.donns_spices_2, J.lime, B.a, G.mint], no_comments),

      Recipe("No name", BookSource(SN.death_co_name, 0), [], no_comments),
                   ]

  def __repr__(self):
      return "RecipeBook [recipes: {0}]".format(str(self._recipes))

  # Returns recipe in book, if exists. Otherwise, returns None.
  #
  # Args:
  #  recipe_name: string, must exactly match string names of recipes in ReccipeBook.
  def GetRecipe(self, recipe_name):
    for recipe in self._recipes:
      if recipe_name == recipe._name:
        return recipe
    return None




# TODO: add logic about what type of substitutions I can actually do.
def CanMakeRecipe(existing_ingredients, subs_allowed, num_missing_allowed, recipe_ingredients):
  # thought about using set differences but with subsitutions it's not really any less code anyway
  subs_made = 0
  for ingredient in recipe_ingredients:
    if ingredient not in existing_ingredients:
      if not subs_allowed or subs_made == num_missing_allowed:
        return False
      subs_made += 1
  return True


# ingredients = list of ingredients that I have
# subs_allowed = bool, true = allowed to make substitutions. TODO: define substitution rules
# num_missing_allowed = int, number of allowed ingredients to be missing
def WhatCanIMake(existing_ingredients, subs_allowed, num_missing_allowed):
  recipes_can_make = []
  for recipe in book._recipes:
    if CanMakeRecipe(existing_ingredients, subs_allowed, num_missing_allowed, recipe._ingredients):
      recipes_can_make.append(recipe)
  return recipes_can_make


book = RecipeBook()
my_pantry = [Gin.beefeater, W.buffalo_bourbon, R.goslings, L.cointreau, L.luxardo, L.grand_marnier, L.st_germain, Amari.campari, V.dolin_dry,
V.dolin_blanc, O.egg_white, O.egg_yolk, O.club_soda, O.dry_champagne, G.lemon, G.lime, G.orange, J.lemon, J.lime, J.orange,  B.a,
B.o, B.p, O.simple_syrup, O.ginger_syrup]
i_can_make = WhatCanIMake(my_pantry, False, 0)
print "I can make {0} recipes: {1}".format(len(i_can_make), i_can_make)



# Given a recipe name, find ingredients not in my pantry.
#
# TODO: would be good to not have to have an exact name on the drink name (e.g. regex, lower case
# all).
#
# Args:
#  recipe_name: string, must exactly match string names of recipes in RecipeBook.
#  existing_ingredients: list of ingredients I already have
def FindMissingIngredients(recipe_name, existing_ingredients):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  missing_ingredients = []
  for ingredient in recipe._ingredients:
    if ingredient not in existing_ingredients:
      missing_ingredients.append(ingredient)
  return missing_ingredients


# TODO: would be nice to have the drink_name as a flag
drink_name = "French 75" #"Dark and Stormy"
missing_ingredients = FindMissingIngredients(drink_name, my_pantry)
print "Missing ingredients for {0} are: {1}".format(drink_name, missing_ingredients)


def PrintIngredients(recipe_name):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  print "Ingredients for {0} are: {1}".format(recipe_name, recipe._ingredients)


PrintIngredients(drink_name)

# Prints a sorted map of ingredient to # recipes used in in order of most-used first.
# TODO: right now it prints in reverse order, fix that.
# TODO: This function is a decent approximation for what ingredients I want, but isn't good enough.
# This doesn't optimize for actually being able to make more drinks. What I really want is a
# function that will tell me which ingredient I should buy that will let me make the most number of
# new drinks given my existing ingredients. For example, tiki drinks require multiple rums, if I
# only get the most used rum in all of the drinks that will not be enough for me to be able to make
# those drinks, unless I also have those other rums, or want to do substitutions.
def PrintMostUsedIngredients():
  ingredient_frequency = {}
  for recipe in book._recipes:
    for ingredient in recipe._ingredients:
      if ingredient in ingredient_frequency:
        ingredient_frequency[ingredient] += 1
      else:
        ingredient_frequency[ingredient] = 1
  ingredients_sorted_by_freq = sorted(ingredient_frequency.items(), key=operator.itemgetter(1))
  print "Most used ingredients are: {0}".format(str(ingredients_sorted_by_freq))

PrintMostUsedIngredients()

