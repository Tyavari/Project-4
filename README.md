# NYC Residential Property Sale Price Predction Model

This application is deployed via Heroku at: 

This application acts as a tool to any user (property appraiser, potential buyer/seller, realtor) who would like to get a ballpark figure of what a property may sell for in NYC. 

The model uses 2016-2017 NYC data to learn, and requires a set of inputs from the user in order to make a prediction (zip code, neighborhood, building type, number of units, year built, and square footage).

Initial Cleaning and Initial Cleaning2 are Python notebooks that take raw data (NYC_Sales.csv) and clean it by dropping rows with incomplete data, standardizing string and numeric formats, trimming the number of columns down to include only relevant features.
NYC_Sales_clean.csv is an intermediate output of cleaned data.

LinearExam notebook is a look into linear regression - each relevant feature is plotted against the variable we are trying top predict (sales price) in a scatter plot, giving us a better idea of which features may be significant to the model and which are likely to be irrelevant or contribute noise. 

NN_RealEstate notebook is an attempt at implementing a neural network for the model. It plays with taking additional cleaning steps, such as binning categorical data to only have individual one-hot encoding for the top 25 most popular values in each category (e.g. top 25 neighborhoods). In an effort to optimize the neural network, we tried different variations of activation functions, number of hidden layers, number of neurons per layer, and number of training epochs. This model type peaked at 25% accuracy, using no hidden layers (one input and one output layer), tanh activation functions, 4 and 3 neurons per layer, mean-squared error as the loss function, adam optimizer, and 125 training epochs.


NYC_Sales_Model notebook takes the cleaned data and uses pd.get_dummies() to encode categorical data, StandardScaler to scale the data, and a Python library to split the data into training and testing sets (20% test). LinearRegression model is used on unscaled data for an 18% accuracy score.
Various version of RandomForest are used as well, including some with extra trees and some with boosting. 
Ultimately, the best performing model was a Random Forest with 100 estimators, using unscaled data, with a 25.8% accuracy score. This is the version of the model used in our deployment. 
This notebook also includes some Python code needed for formatting of data and HTML code for our Flask app.

App.py is the Flask server app. This allows us to deploy the app locally. It imports the Random Forest model, and uses HTML and JavaScript/Bootstrap to read in user input (form2.html) and get a model prediction of sales price (summary.html). 

