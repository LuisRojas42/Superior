clc
clear all
close all
warning off all
muestras = [0 0; 3 8; 2 2; 1 1; 5 3; 4 8; 6 3; 5 4; 6 4; 7 5]
clases = k_means(muestras, 3);