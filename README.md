# software-diagnosability-using-machine-learning

This project's aim is to find best software metrics for fault localization.
We provided jupyter notebook files and examples

You can find more explanations as comments in our code.

## FindingRank
This notebook file finds the rank, method count of each gzoltar project and gives them a target value between 0 and 1. It matches JD CallGraphs with spectra and matrices of buggy versions. It also 
finds CyclomaticComplexity of each project if the corresponding JDCallGraph is provided.
If it has incorrect spectra, matrix, JD CallGraph layout we discard that data.
Math file's buggy versions are handpicked.


*Note:* Currently Dstar's Ncf default power value is set to 1. Please change the value if you want to do some adjustments.

Unfortunately we don't have code for combining static_bug_test metrics with target values and dynamic metrics. Thererefore you
have to combine yourself. You can look at our example csv files to get an understanding.

## main
After generating your metric csv file, you can analyze it with machine learning methods in our code.
Currently we have implemented these machine learning methods

1.SVM

2.ExtraTrees

3.Adaboost(with DT)

4.NeuralNet

You can create your confusion matrices in our notebook as well. 



*Note:* Your target value name should be "percentage" for now. 

## ConfusionMatricesExample
This folder consists some of our results without Math project and also has our confusion matrix generator in brute force way.
