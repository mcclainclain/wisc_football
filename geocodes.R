
library(tidyverse)
library(ggmap)

players = read_csv("players.csv")

readRenviron("./.Renviron")
register_google(Sys.getenv("MAPSAPIKEY"))

players_w_geocodes = mutate_geocode(players, Hometown)

write_csv(distinct(players_w_geocodes %>% select(Hometown, lon, lat)), "./geocodes.csv")
