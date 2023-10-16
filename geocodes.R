
library(tidyverse)
library(ggmap)

players = read_csv("players.csv")

readRenviron("./.Renviron")
register_google(Sys.getenv("MAPSAPIKEY"))

# Individual cities that need adjustment for geocoding
players$Hometown[players$Hometown == "Montreal, Wis."] = "Montreal, Wisconsin"
players$Hometown[players$Hometown == "Howard, Kan."] = "Howard, Kansas"

players_w_geocodes = mutate_geocode(players, Hometown)


write_csv(distinct(players_w_geocodes %>% select(Hometown, lon, lat)), "./geocodes.csv")
