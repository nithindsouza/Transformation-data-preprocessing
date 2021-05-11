
library(readr)
calories <- read.csv("C:\\Users\\hp\\Desktop\\DataSets\\calories_consumed.csv")

str(calories)
attach(calories)
boxplot(calories)
qqnorm(calories$Weight.gained..grams.)
qqnorm(calories$Calories.Consumed)

#transformation to make Weight.gained..grams. variable normal
qqnorm(log(Weight.gained..grams.))
qqline(log(Weight.gained..grams.))

#transformation to make workex variable normal
qqnorm(log(Calories.Consumed))
qqline(log(Calories.Consumed))
