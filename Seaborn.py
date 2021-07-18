`sns.set_style("dark")` :To set different themes for the plot

Seaborn has five different themes: (1)"darkgrid", (2)"whitegrid", (3)"dark", (4)"white", and (5)"ticks",
  
  

Use `plt.title(“shivam here”)` for giving title

Use `plt.figure(figsize=(10,10))` for size of plot

Use `plt.xlabel(“air”)` and `plt.ylabel(“wind”)` for labelling axes



`sns.lineplot(data=fifa_data)` :lineplot

`sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")` :Line Plot with specific columns
  
  

`sns.pairplot(data, hue=”something”)`:  for plotting multivariate analysis
  
  

`sns.countplot(data =diab_data, x= "Outcome")` : To know the proportion of particular outcome or any varibale
  
  

`sns.barplot(x=flight_data.index, y=flight_data['NK'])`     or

`sns.barplot(x=flight_data.index, data =flight_data, y=“NK”`)



`sns.heatmap(data=flight_data, annot=True)`

                        
  #SCATTER PLOTS

*`sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges’])` :Scatter plot*

*`sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges’])`. :Scatterplot with regression line*

*`sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])` : Scatter plot with colour coding according a data like Smoker*

`sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)` :Colour coded scatterplot with regression line

`sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])` :Categorical scatter
                                                        
                                                        
                                                        
                                                        #Histograms

`sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)` : Histogram

`sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)` :Smoothed Histogram

`sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")` :2D color coded Histogram
