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
  pennyroyal_infused_haymans_old_tom = "Pennyroyal-infused Hayman's Old Tom Gin" # instructions on pg. 281
  tanqueray_10 = "Tanqueray No. Ten Gin"
  bols_barrel_aged_genever = "Bols Barrel Aged Genever"
  bombay_london_dry = "Bombay London Dry Gin"
  beefeater_24 = "Beefeater 24 Gin"
  dorothy_parker = "Dorothy Parker Gin"
  peppercorn_infused_plymouth = "Szechuan Peppercorn-infused Plumouth Bin" # instructions on pg. 283
  snap_pea_infused_plymouth = "Snap pea-infused Plymouth Gin" # instructions on pg. 283
  bruichladdich = "Bruichladdich Botanist Gin"


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
  elixir_combier = "Exlixir Combier"
  
  # not mentioned in recommendation section
  cherry_heering = "Cherry Heering Liqueur"
  drambuie = "Drambuie" # honey spice liqueur with scotch base
  gabriel_curacao = "Gabriel Boudier Curacao" # blue
  maraska_maraschino = "Marasaca Maraschino Liqueur"
  massenez_peach_cream = "Massenez Creme de Peche Peach Liqueur"
  massenez_blackberry = "Massenez Creme de Mure Blackberry Liqueur"
  marie_mint_cream = "Marie Brizard White Creme de Menthe"
  marie_apricot = "Marie Brizard Apricot Liqueur"
  kronan_swedish_punsch = "Kronan Swedish Punsch"
  solerno_blood_orange = "Solerno Blood Orange Liqueur"
  creme_de_fraise = "Merlet creme de fraise des bois strawberry liqueur"
  rothman_creme_de_violette = "Rothamn & Winter Creme de Violette"
  dolin_genepy = "Dolin Genepy des Alpes Liqueur"


# Includes Amari, Aperitifs and Digestifs
class Amari(object):
  amaro_averna = "Amaro Averna"
  amaro_ciociaro = "Amaro CioCiaro"
  amaro_lucano = "Amaro Lucano"
  amaro_meletti = "Amaro Meletti"
  amaro_nardini = "Amaro Nardini"
  amaro_nanino = "Amaro Nanino Quintessentia"
  aperol = "Aperol"
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
  grapefruit_punt_e_mes = "Grapefruit-infused Punt e Mes"
  martini_sweet = "Martini Sweet Vermouth"


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
  ho = "House orange" # instructions on pg. 284
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
  verjus_blanc = "Fusion Verjus Blanc"
  
  creme_yvette = "Creme Yvette"
  ss = "simple syrup"
  acacia_honey_syrup = "acacia honey syrup" # instructions on pg. 286 in the book
  dry_champagne = "dry champagne"
  club_soda = "Club soda"
  tonic_water = "Tonic water"
  coconut_water = "Coconut water"
  cane_sugar_syrup = "cane sugar syrup"
  vanilla_syrup = "vanilla syrup" # instructions on pg. 277
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
  black_current_cordial = "American Fruits Black Current Cordial"
  grenadine = "Grenadine" # instructions on pg. 284
  donns_spices_2 = "Donn's spices #2" # instructions on pg. 284
  san_pellegrino_grapefruit = "San Pellegrino Pompelmo Grapefruit soda"
  orange_flower_water = "Orange flower water"
  zombie_mix = "Zombie mix" # instructions on pg. 284
  toasted_fennel_salt_rim = "toasted fennel salt rim" # instructions on pg. 283
  scarlet_glow_syrup = "scarlet glow syrup" # instructions on pg. 277
  
  avua_cachaca = "Avua amburana cachaca"
  boiron_kalamansi_puree = "Boiron Kalamansi puree"
  dons_hard_apple_cider = "Don's hard apple cider"


# G = Garnish
class G(object):
  lemon = "lemon"
  lime = "lime"
  orange = "orange"
  grapefruit = "Grapefruit"
  apple = "Apple"
  anjou_pear = "Anjou pear"
  green_grapes = "Green grapes"
  brandied_cherry = "Luxardo Marasche brandied cherry"
  cherry = "Cherry flag"
  cucumber = "Cucumber"
  mint = "Mint"
  curry_leaf = "Curry leaf"
  sage_leaf = "Safe leaf"
  basil_leaf = "Basil leaf"
  thai_basil_leaf = "Thai Basil leaf"
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


class Beer(object):
  green_flash_ipa = "Green Flash IPA"

