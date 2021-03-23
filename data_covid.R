rm(list = ls())
library(data.table) 
library(dplyr)
library(stringi)


dir_path <- "path"
files <- list.files(path=dir_path, pattern = "pow")

dane1 <- rbindlist(lapply(files, function(file){
  dt <- read.csv2(paste0(dir_path,"/",file), colClasses = "character", encoding = "UTF-8")  #[,c(1:16)]
  date <- substr(file,1,8)
  y <- substr(date,1,4)
  m <- substr(date,5,6)
  d <- substr(date,7,8)
  
  dt <- dt %>%
    mutate(stan_rekordu_na=paste0(y,"-",m,"-",d))
  
  }),use.names = TRUE, fill = TRUE)
#(dane, "dane1.csv")


dane <- read.csv2("dane/merge_data.csv", sep = ",", encoding = "UTF-8")

dict <- read.csv2("dane/slownik_powiaty.csv", sep = ",", encoding = "UTF-8")

dane <- dane %>% 
  filter(!(is.na(stan_rekordu_na))) %>%
  mutate(ow = substr(teryt,2,3))

dane <- dane %>% 
  mutate(teryt_num = substr(teryt,2,3))


