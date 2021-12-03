print ("Hallo, welkom bij Ridda's snackbar")

name= input ("Wat is uw naam? \n" )

print ("\nHallo "+ name +", Dankuwel voor het binnenkomen bij ons café.\n" )

menu= "Patat,cola,kapsalon,Turske Pizza,Patat met, Redbull, Kroket, Frikandel, bitterballen, saté en Hotdogsrid\n"

print (name + " wat wilt u van ons menu?\nDit is wat wij serveren.\n" +menu )

order= input ()

if order == "" or order == "patat" or order == "cola" or order == "Kapsalon" or order == "turkse Pizza" or order == "Patat met" or order == "Redbull" or order == "Kroket" or order == "Frikandel" or order == "Bitterballen" or order == "Saté"or order == "Hotdogs" :

  print ("\nDat klinkt goed. "+ name +", We hebben dat genoteerd." +"\nHet is zo klaar.\n")
  print ("Dankuwel voor het wachten hier is uw " + order)

elif order != menu: 
     print ("Het spijt ons maar " +order+"\nserveren wij helaas niet")

print ("Fijne dag verder")