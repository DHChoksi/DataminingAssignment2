# -------------------------------------------------------------------------
# AUTHOR: Dhruvi Choksi
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: worked for like 1-2 hours daily and
# -----------------------------------------------------------*/

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataSets = ['cheat_training_1.csv', 'cheat_training_2.csv']

for ds in dataSets:

    X = []
    Y = []

    df = pd.read_csv(ds, sep=',', header=0)   #reading a dataset eliminating the header (Pandas library)
    data_training = np.array(df.values)[:,1:] #creating a training matrix without the id (NumPy library)

    #transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
    #Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [2, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
    #be converted to a float.
    for instance in data_training:
        feature_vector = []
        feature_vector.append(1) if instance[0] == 'yes' else feature_vector.append(0)

        if instance[1] == 'Single':
            feature_vector.extend([1, 0, 0])
        elif instance[1] == 'Divorced':
            feature_vector.extend([0, 1, 0])
        else:
            feature_vector.extend([0, 0, 1])
        feature_vector.append(float(instance[2].replace('k', '')))
        X.append(feature_vector)

        Y.append(1) if instance[3] == 'yes' else Y.append(0)

        accuracies = []

        # 10 times loop tasks
        for i in range(10):

        #fitting the decision tree to the data by using Gini index and no max_depth
        clf = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=None)
        clf = clf.fit(X, Y)

        #read the test data and add this data to data_test NumPy
        df_test = pd.read_csv('cheat_test.csv', sep=',', header=0)
        data_test = np.array(df_test.values)[:,1:]

        correct_predictions = 0
        total_instances = len(data_test)
        for data in data_test:
            refund = 1 if data[0] == 'Yes' else refund = 0
            if data[1] == 'Single':
                single = 1
                divorced = 0
                married = 0
            elif data[1] == 'Divorced':
                single = 0
                divorced = 1
                married = 0
            else:
                single = 0
                divorced = 0
                married = 1
            taxable_income = float(data[2].replace('k', ''))

    #transform the original training classes to numbers and add them to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data by using Gini index and no max_depth
       clf = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=None)
       clf = clf.fit(X, Y)

       #plotting the decision tree
       tree.plot_tree(clf, feature_names=['Refund', 'Single', 'Divorced', 'Married', 'Taxable Income'], class_names=['Yes','No'], filled=True, rounded=True)
       plt.show()

       #read the test data and add this data to data_test NumPy
       #--> add your Python code here
       # data_test =

       for data in data_test:
           #transform the features of the test instances to numbers following the same strategy done during training, and then use the decision tree to make the class prediction. For instance:
           #class_predicted = clf.predict([[1, 0, 1, 0, 115]])[0], where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here

           #compare the prediction with the true label (located at data[3]) of the test instance to start calculating the model accuracy.
           #--> add your Python code here

       #find the average accuracy of this model during the 10 runs (training and test set)
       #--> add your Python code here

    #print the accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on cheat_training_1.csv: 0.2
    #--> add your Python code here




#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataSets = ['cheat_training_1.csv', 'cheat_training_2.csv']

for ds in dataSets:

    X = []
    Y = []

    df = pd.read_csv(ds, sep=',', header=0)   #reading a dataset eliminating the header (Pandas library)
    data_training = np.array(df.values)[:,1:] #creating a training matrix without the id (NumPy library)

    #transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
    #Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [2, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
    #be converted to a float.
    for instance in data_training:
        feature_vector = []
        if instance[0] == 'Yes':
            feature_vector.append(1)
        else:
            feature_vector.append(0)
        if instance[1] == 'Single':
            feature_vector.extend([1, 0, 0])
        elif instance[1] == 'Divorced':
            feature_vector.extend([0, 1, 0])
        else:
            feature_vector.extend([0, 0, 1])
        feature_vector.append(float(instance[2].replace('k', '')))
        X.append(feature_vector)

        if instance[3] == 'Yes':
            Y.append(1)
        else:
            Y.append(0)

    accuracies = []
    #loop your training and test tasks 10 times here
    for i in range(10):

        #fitting the decision tree to the data by using Gini index and no max_depth
        clf = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=None)
        clf = clf.fit(X, Y)

        #read the test data and add this data to data_test NumPy
        df_test = pd.read_csv('cheat_test.csv', sep=',', header=0)
        data_test = np.array(df_test.values)[:,1:]

        correct_predictions = 0
        total_instances = len(data_test)
        for data in data_test:
            if data[0] == 'Yes':
                refund = 1
            else:
                refund = 0
            if data[1] == 'Single':
                single = 1
                divorced = 0
                married = 0
            elif data[1] == 'Divorced':
                single = 0
                divorced = 1
                married = 0
            else:
                single = 0
                divorced = 0
                married = 1
            taxable_income = float(data[2].replace('k', ''))

            class_predicted = clf.predict([[refund, single, divorced, married, taxable_income]])[0]
            if class_predicted == 1 and data[3] == 'Yes':
                correct_predictions += 1
            elif class_predicted == 0 and data[3] == 'No':
                correct_predictions += 1

        accuracy = correct_predictions / total_instances
        accuracies.append(accuracy)

    avg_accuracy = sum(accuracies) / len(accuracies)
    print(f"Final accuracy when training on {ds}: {avg_accuracy}")
