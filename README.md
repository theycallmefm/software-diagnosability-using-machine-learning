# Exploring the Relationship between Design Metrics and Software Diagnosability using Machine Learning

The objective of a diagnosability analysis is to estimate the expected effort and preciseness of the bug localization process. The associated measurement cannot be defined in abstract, since faults are always revealed in a certain testing context. As we measure diagnosability at the design level, and since the measurement depends on the testing context, we need to qualify the testing context at the design level. 


Machine learning techniques have been used for various purposes in software engineering.

Purpose of this project is to find best software metrics for fault localization using machine learning methods.
We provided jupyter notebook files and examples

You can find more explanations of functions as comments in our code.

## FindingRank
This notebook  finds the rank, method count of each gzoltar project and gives them a target value between 0 and 1. It matches JD CallGraphs with spectra and matrices of buggy versions. It also 
finds CyclomaticComplexity of each project if the corresponding JDCallGraph is provided.
If it has incorrect spectra, matrix or JD CallGraph layout we discard that data.
Math file's buggy versions are handpicked.


*Note:* Currently Dstar's Ncf default power value is set to 1. Please change the value if you want to do some adjustments.

Unfortunately we don't have code for combining static_bug_test metrics with target values and dynamic metrics. Therefore you have to combine the data yourself. You can look at our example csv files to get an understanding.

## main
After generating your metric csv file, you can analyze it with machine learning methods in our code.
Currently we have implemented these machine learning methods

1.SVM

2.ExtraTrees

3.Adaboost(with DT)

4.NeuralNet

You can create your confusion matrices in our notebook as well. 

We have these example files which you can work on
chart_closure_lang_time_cyclomatic.csv
fulldata_wo_cyclomatic.csv


*Note:* Your target value name should be "percentage" for now. 

## ConfusionMatricesExample
This folder contains some of our results without Math project and also has our confusion matrix generator in brute force way.
