# Dataquest guided projects
Here I keep my guided projects from [dataquest](https://www.dataquest.io/).

Here is [my account](https://app.dataquest.io/profile/3axap92) as well.

## Python

### [1. Profitable App Profiles for the App Store and Google Play Markets (RU)](https://github.com/0ld-dancer/dq_projects/blob/main/1.%20Profitable%20App%20Profiles%20for%20the%20App%20Store%20and%20Google%20Play%20Markets/profitable_apps.ipynb)

 In this project I've been working as data analysts for a company that builds Android and iOS mobile apps. The main goal was to analyze data to help our developers understand what type of free apps are likely to attract more users. I used these two data sets from Kaggle: for [AppStore](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps) and for [GooglePlay](https://www.kaggle.com/lava18/google-play-store-apps).

 No libraries were usen in this project. Pure python only.

### [2. Exploring Hacker News Posts (RU)](https://github.com/0ld-dancer/dq_projects/blob/main/2.%20Exploring%20Hacker%20News%20Posts/hacker_news.ipynb)

 In this projest I've analyzed popularyty of two post types on [Hacker News](https://news.ycombinator.com/): ask and show. I've explored distribution of comments over time to find the best time for posting. The data set is also from [Kaggle](https://www.kaggle.com/hacker-news/hacker-news-posts).

 The `datetime` library was used.

### [3. Exploring Ebay Car Sales Data (RU)](https://github.com/0ld-dancer/dq_projects/blob/main/3.%20Exploring%20Ebay%20Car%20Sales%20Data/Exploring%20Ebay%20Car%20Sales%20Data.ipynb)

 I've been working with a dataset of used cars from the [German eBay classifieds](https://data.world/data-society/used-cars-data) in this guided project. The goal was to cleanse and examine this data in an attempt to find some relationship between price and brand or mileage.

 The first project with the `numpy` and `pandas`

### [4 .Best College Major (RU)](https://github.com/0ld-dancer/dq_projects/blob/main/4.%20Best%20College%20Major/College_majors.ipynb)

 In this project I've tried to find the best major according to future job hunting and salaries. tThe shares of women and men in different majors were also explored. The data set is provided by [American Community Survey](https://www.census.gov/programs-surveys/acs/).
 
 This project has a lot of plots built with the `matplotlib`.

### [5. Bachelors Degree Women-Men Gap (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/5.%20Bachelors%20Degree%20Women-Men%20Gap/gender_gap_plots.ipynb)

This project explores some of the `matplotlib` features that improve visual aesthetics of plots. I've built plots that show the gap changes between men and women over the years for each degree. The data set was collected by [The Department of Education Statistics](https://www.kaggle.com/sureshsrinivas/bachelorsdegreewomenusa).

### [6. Clean and Analyze Employee Exit Surveys (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/6.%20Clean%20and%20Analyze%20Employee%20Exit%20Surveys/Clean%20And%20Analyze%20Employee%20Exit%20Surveys.ipynb)

I've been working with the exit surveys from employees of [DETE](https://data.gov.au/dataset/ds-qld-fe96ff30-d157-4a81-851d-215f2a0fe26d/details?q=exit%20survey) and [TAFE](https://data.gov.au/dataset/ds-qld-89970a3b-182b-41ea-aea2-6f9f17b5907e/details?q=exit%20survey). I've tried to find some relationship between dissatisfaction and employee experience.

Libraries: `pandas`, `numpy` and `matplotlib`. 

### [7. Analyzing NYC High School Data (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/7.%20Analyzing%20NYC%20High%20School%20Data/Analyzing%20NYC%20High%20School%20Data.ipynb)

This project explores possible correlation between SAT score and the many different factors (like race or gender) scattered across the [files](https://www.kaggle.com/samaxtech/nyc-high-school-data).

Libraries: `pandas`, `numpy`, `re` and `matplotlib`.

### [8. Star Wars Survey (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/8.%20Star%20Wars%20Survey/Star%20Wars%20Survey.ipynb)

I've been working with the [FiveThirtyEight's survey](https://github.com/fivethirtyeight/data/tree/master/star-wars-survey) about Star Wars franchise in this project. I analyzed the rating of the episodes, for example, paired with fan status or gender. Also confirmed the favorite episode - "The Empire Strikes Back".

Libraries: `pandas`, `numpy` and `matplotlib`.

### [9. Popular Data Science Questions (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/9.%20Popular%20Data%20Science%20Questions/Popular%20Data%20Science%20Questions.ipynb)

In this scenario, I've been working for a company that creates data science content. The goal was to find what people want to learn about in data science by analyzing posts on **StackOverflow**. The data was received from [Stack Exchange Data Explorer (SEDE)](https://data.stackexchange.com/stackoverflow/query/new)

Libraries: `pandas` and `matplotlib`.

### [10. Predicting Car Prices (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/10.%20Predicting%20Car%20Prices/10.%20Predicting%20Car%20Prices.ipynb)

I've been predicting a car's market price by its attributes using [`KNeighborsRegressor()`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html) only in this project. I've implemented simple hyperameter variation and visualized the results.
The data set was provided by [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

Libraries: `pandas`, `numpy`, `matplotlib` and `sklearn`

### [11. Predicting House Sale Prices (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/11.%20Predicting%20House%20Sale%20Prices/11.%20Predicting%20House%20Sale%20Prices.ipynb)

I've developed the pipeline for linear regression modeling on [data](https://www.kaggle.com/hamzajabbarkhan/ames-housingtsv) for the city Ames, Iowa from, 2006 to 2010. It consist of three functions:
* `transorm_features()` - removes `NaN` values, creates new and drops useless columns, create dummies, etc.
* `select_features()` - selects hig-variance feature only, then finds k best from them.
*  `train_and_test()` - splits original data and implements k-fold cross validation.

Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn` and `sklearn`.

### [12. Predicting the stock market](https://github.com/0ld-dancer/dq_projects/tree/main/12.%20Predicting%20the%20stock%20market)

Basic script.

### [13. Predicting Bike Rentals (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/13.%20Predicting%20Bike%20Rentals/13.%20Predicting%20Bike%20Rentals.ipynb)

I've been working with the [data](http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset) on the number of bicycles people rent by the hour in the Washington, D.C in this project. The goal was to apply different ML methods (**linear regression, desition tree and random forest**) to track RMSE evaluation.

Libraries: `pandas`, `numpy`, `matplotlib` and `sklearn`.

### [14. A Handwritten Digits Classifier (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/14.%20A%20Handwritten%20Digits%20Classifier/digits_classifier.ipynb)

  I applied [`KNeighborsClassifier()`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) and [`MLPClassifier()`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html) to the built-n sklearn handwritten digits data set from [`load_digits()`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html). Explored how NN works with different hyperparameters and L2 regulariation. I used manually hyperparameters iteration and [`GridSearchCV()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html). Finally I visualized MLP weights.

### [15. Investigating Fandango Movie Ratings (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/15.%20Investigating%20Fandango%20Movie%20Ratings/fandango_ratings.ipynb)

 In this project I've been looking for some chahges in [Fandango's](https://www.fandango.com/) movie rating system after this [article](https://fivethirtyeight.com/features/fandango-movies-ratings/).
 
 But I've ended up only with rating comparison for popular movies releasen in 2015 and 2016 due to data sets from this [Github repository](https://github.com/mircealex/Movie_ratings_2016_17) weren't representative.

### [16. Finding the Best Markets to Advertise In (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/16.%20Finding%20the%20Best%20Markets%20to%20Advertise%20In/the_best_markets.ipynb)

 In this project I've been working in a e-learning company and looking for the best markets (countries) to advertise in. Two criterias for our searches were number of potential students and money spent on learning on average. As data set I've used [freeCodeCamp's 2017 New Coder Survey](https://www.freecodecamp.org/news/we-asked-20-000-people-who-they-are-and-how-theyre-learning-to-code-fff5d668969/) results.
 
### [17. Mobile App for Lottery Addiction (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/17.%20Mobile%20App%20for%20Lottery%20Addiction/lottery_addiction.ipynb)

 In this project I've been helping a medical institute with the app. Using combinations and probability formulas I've written functions that allow to:
* find the probability of winning the big prize with a single ticket
* check whether a certain combination has occurred in the Canada lottery
* find the probability for any number of of tickets between 1 and 13,983,816
* find the probability of having 2, 3, 4 or 5 winning numbers exactly

### [18. Spam Filter with Naive Bayes (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/18.%20Building%20a%20Spam%20Filter%20with%20Naive%20Bayes/spam_filter.ipynb)

 In this project I've created a simple spam filter using the multinomial Naive Bayes algorithm. The final accuracy is 98.56%.
 
 I've used the data set from [The UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection). It has 5,572 SMS messages classified by humans.

## SQL

### [1. Analyzing CIA Factbook Data Using SQL (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/SQL%20projects/1.%20Analyzing%20CIA%20Factbook%20Data%20Using%20SQL/Analyzing%20CIA%20Factbook%20Data%20Using%20SQL.ipynb)

I've been working with data from the [CIA World Factbook](https://www.cia.gov/the-world-factbook/) in this project. I've explored demographics and geographics of countries in this database to find some insights.

### [2. Answering Business Questions using SQL (ENG)](https://github.com/0ld-dancer/dq_projects/blob/main/SQL%20projects/2.%20Answering%20Business%20Questions%20using%20SQL/chinook_store.ipynb)

I've been working with the Chinook database (digital music shop) that is provided by SQLite in this project. I've analyzed the data and found most popular music genres, best sales agent, top sales countries and etc. Then I used the results to make some recommendations.
