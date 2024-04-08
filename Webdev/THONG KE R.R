# Trich xuất các thư viện cần thiết
library(stringr)
library(tidyr)
library(dplyr)
library(Metrics)
library(zoo)
library(ggplot2)
library(caret)
library(MASS)
library(reshape2)
library(mltools)
library(DescTools)
library(plotly)

#đọc dữ liệu và gán giá trị rỗng và "N/A" -> NA
All_GPUs <- read.csv("Downloads/All_GPUs.csv", na.strings = c("", "N/A"))

#chọn các cột quan trọng để thống kê
GPU_data <- All_GPUs[, c("Name", "Best_Resolution", "Core_Speed", "Manufacturer", "Memory", "Memory_Bandwidth", 
                         "Memory_Speed", "Release_Date")]

#in bang thong ke so bo cua data
print(summary(GPU_data))

#Kiem tra du lieu thieu
print(apply(is.na(GPU_data),2,sum))

#Kiem tra phan tram du lieu thieu
print(apply(is.na(GPU_data),2,mean))

#Doi voi Memory_Bandwidth va Memory_Speed, ta xoa bo cac gia tri NA
GPU_data <- subset(GPU_data, !is.na(Memory_Speed) & !is.na(Memory_Bandwidth))

#Doi voi Best_Resolution va Memory, ta thay cac gia tri NA bang median

#Tinh median cua Best_Resolution
median_best_resolution <- median(GPU_data$Best_Resolution, na.rm = TRUE)
#Thay cac gia tri NA trong Best_Resolution bang median
GPU_data$Best_Resolution <- ifelse(is.na(GPU_data$Best_Resolution), median_best_resolution, GPU_data$Best_Resolution)

#Tinh median cua Memory
GPU_data$Memory <- as.numeric(sub(" MB", "", GPU_data$Memory)
                              
median_memory <- median(GPU_data$Memory, na.rm = TRUE)
#Thay cac gia tri NA trong Memory bang median
GPU_data$Memory <- ifelse(is.na(GPU_data$Memory), median_memory, GPU_data$Memory)

#Kiem tra lai du lieu thieu
print(apply(is.na(GPU_data),2,sum))
