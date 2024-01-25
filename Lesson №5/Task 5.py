capitals = {"Russia":"Moscow","Belarus":"Minsk","Georgia":"Tiflis","Turkey":"Istanbul","Poland":"Warsaw"}
capitals["Russia"], capitals["Poland"] = capitals ["Poland"],capitals["Russia"]
capitals.pop("Belarus")
print (capitals)