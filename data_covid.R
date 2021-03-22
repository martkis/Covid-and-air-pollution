library(data.table) 

setwd("Pulpit/R/dane_covid/") 

#dt <- read.csv2("akutalne_dane_powiaty.csv", encoding = "cp-1250")
dir_path <- "danehistorycznepowiaty/"
files <- list.files(path=dir_path, pattern = "pow")

dane <- rbindlist(lapply(files, function(file){
  dt <- read.csv2(paste0(dir_path,"/",file), colClasses = "character", encoding = "latin1") #[,c(1:16)]
  
  }),use.names = TRUE, fill = TRUE)


