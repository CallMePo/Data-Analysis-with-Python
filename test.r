library(readr)
data<-read.csv("D:/Data Visualization/Automobile.csv")
View(data)

data<-count(data['make']=='audi'])
View(data)
