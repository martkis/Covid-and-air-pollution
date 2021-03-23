library(data.table) 
library(dplyr)
library(stringi)
setwd("/home/kisiel/Covid-and-air-pollution/") 

dir_path <- "dane/danehistorycznepowiaty/"
files <- list.files(path=dir_path, pattern = "pow")

dane <- rbindlist(lapply(files, function(file){
  dt <- read.csv2(paste0(dir_path,"/",file), colClasses = "character", encoding = "latin1") #[,c(1:16)]
  
  }),use.names = TRUE, fill = TRUE)

dane <- dane %>% 
  filter(!(is.na(stan_rekordu_na))) %>%
  mutate(ow = substr(teryt,2,3))

dict <- read.csv2("dane/slownik_powiaty.csv", sep = ",", encoding = "windows-1250")
