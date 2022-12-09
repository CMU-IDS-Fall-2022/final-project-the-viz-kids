# Final Project Report

**Project URL**: https://github.com/CMU-IDS-Fall-2022/final-project-the-viz-kids
**Video URL**: TODO

Buildings contribute to 38% of global emissions as per the UN Environmental Global Status Report 2020. Hence, it is crucial for us to make efforts to reduce energy consumption. Each building’s energy usage is mentioned in its monthly bill. However, it is quite challenging to assess if this amount would be higher/lower than others or the set average (threshold) consumption value for say, the 2050 goal. This can be achieved using the benchmark data. To be specific, Seattle has State Policies to require all public, commercial, and multifamily buildings to complete the benchmarking report of energy consumption in the building. This helps various policy makers, consultants and designers take informed decisions about building retrofits and it assists with setting standards for new buildings as well.

## Introduction

## Related Work
Given that energy is an important aspect for city planners and the government, data is maintained for each building in major cities every year. In Seattle alone, there are records for over 3,600 buildings for the year 2020 according to the Seattle government dataset. Manual inspection of such a large dataset is very difficult. There is a need to represent the data such that the users can choose the criteria they find important and gain insights from the data fitting those constraints. A dashboard can be used to meet this critical need. The existing dashboard of Seattle is informative, however, has scope for increased avenues for interaction and also, does not compare the relationship of various characteristics of the building with energy consumption. The available data set contains a couple of more unexplored features that could help answer conclusive questions and interactive techniques will aid in better comprehension of the performance in Seattle. It was also observed that the dataset contains missing values for the Energy Star score, which rated building performance on a simple 1 - 100 scale, for about 25% of the buildings thus making the data represented incomplete.

In this regard, the motivation to develop a new Dashboard to show the distribution of energy consumption across buildings in Seattle incorporates more interactivity. Potential users of this dashboard include building occupants/owners, real estate developers, policy makers, consultants , designers, electricity board members and other interested parties. The dashboard can be used to identify energy efficient buildings to learn more about practices responsible for its efficiency and also to identify buildings that perform poorly. This will help the owners or other parties for further analysis and assess if the building must be retrofitted with newer green attributes like more energy efficient appliances, better heating/cooling systems, airtight construction, etc to reduce its  energy consumption.

## Methods
#### Dataset description
Where our dataset is from, what columns does it have and what it means
Benchmarking means measuring a building's energy use and then comparing it to the average for similar buildings. It allows owners and occupants to understand their building's relative energy performance and helps identify opportunities to cut energy waste. The dataset is a compilation of benchmarking datasets from the years of 2016 – 2020 except for 2018 (which is not publicly available, and we are attempting to acquire it by getting in touch with the administration). The data represents the buildings of Seattle which are required to provide information as stated by the Benchmarking laws of Seattle. For this project, multiple columns in the dataset have been scrapped as they do not provide any relevance to the data analysis. The columns that remain provide an insight into the following aspects of the building:

Name and Type of the Building
Geographical Location of the Building
Primary, Secondary and Tertiary Use of the Land and their respective Floor Areas
EnergyStar Rating
Electrical, Steam and Natural Gas Consumption
Weather Normalized Site and Source Energy Use Intensity (A metric to compare the buildings with either other similar typology of buildings in the city or the national set standard.
Validity and Compliance Status of the Data

Although all the categories mentioned above might not necessarily inform the visualizations, they would help in data analysis and help in weeding out “bad data”.

One of the most important columns in our dataset is Energy Star score, which allows users to quickly understand how the specific building is working. It uses 1-100, and a score of 50 represents median energy performance, while a score of 75 or higher indicates your building is even better than others. That is, the Energy Star score assesses how the building is performing as a whole based on actual, measured data. It is rated given its physical attributes, its operations, and how the people inside use it. To be specific, the input information includes its size, location, number of occupants, number of PCs, etc. Input details depend on the different property types in the ES list first, but there are five general steps to get the score rating: 1) Enter building data, 2) Compute the actual source EUI, 3) Compute the predicted source EUI, 4) Compute the energy efficiency ratio, 5) Assign a score via a lookup table.

However, our exploration of the 2020 dataset found that 1,002 building rows with missing Energy Star score values (~27% of total 3,628) were unfortunately included. From the captured table stated below, you could find the number of buildings by property type in the dataset with rated and missing values. It is said that the blue-colored types with missing values (~63% of total 1,002) would also be possibly rated since other buildings in the same type have been also rated, but we cannot be sure that non-colored and orange-colored rows could get rated. Because those are not included in the Energy Score(ES) list or the building type is null itself.

Given that Energy Star score rating is a good metric to help non-technical people understand and rate the building's energy usage, it is worth mentioning in our dashboard. However, 27% of missing value is quite a big number of missing values and thus poses a problem we cannot ignore. In order to compute the metric using the formula from above, we do not have the monthly data of average usage for the last 12 months available.We thus intend to approximate this value using a Machine Learning algorithm to cluster the similar buildings together based on various features such as type of building, square footage, age of the building etc. Once the buildings are clustered, the missing value can be filled as the average of the cluster or the average usage of the nearest k buildings. It is important to note and specify that this value is an approximation and we will also indicate the same in the dashboard while representing these values.

#### Data Cleaning
As the first step to data cleaning, we start by listing all the unique property types in the entire dataset, sampled from the columns “LargestPropertyUseType”, “SecondLargestPropertyUseType” and “ThirdLargestPropertyUseType”. In doing so, it becomes evident that the building types are noisy and hence need cleaning.
For this, we create a dictionary, mapping the different noisy building types to their clean counterparts. 
A round of testing is then conducted to ensure all the building types are in an expected clean state, as the building type plays a very important role in predicting Energy Star score.

Finally for the purpose of visualization, we discard those data points where the location is missing as it cannot be represented on the map and thus analyzed further.

#### Data Processing (ML)
Missing Energy Score Values pose a problem to the dashboard. Since this metric cannot be computed given the data available, Machine Learning approaches are used to estimate this value for missing cases. Taking a brute force approach of assigning a mean calculated by clustering similar building types yields an informative value (often 50) as even within a building type, the values range from [1,100]. Thus ML is essential in solving this problem.

**Formulating the problem as an ML Problem:**
The problem at hand can be seen as a regression problem since the Energy Star Score is a continuous value between 1 and 100. It can be seen as a regression over the following features from our dataset. The following constitutes our feature set or X

Year built
Number of floors
Area of the Property
Type of Property
Source Energy Use Intensity (EUI)
GHG Emission
Energy Star Score serves as our labels or Y.

**Procedure:**
The first step to data processing is to identify rows in the dataframe that have Energy Star Score and that do not. This is of importance because in doing so, the rows for which data prediction is required can be collected. However, one kink to iron out is that there exits building types for which Energy Star Score has never been calculated and hence, is not applicable. It is essential to filter these building data types out.

For this, we start by creating two different datasets, one with rows with all energy star scores - df_energystar, and one with rows that have missing energy star score values - df_noenergystar. We then collect the unique building types in either dataframe in sets, to then be compared.

The next step is to filter out those rows from df_noenergystar that have the building type (first largest, second largest or third largest) as a building not mentioned in df_energystar. This implies that for this building, the energy star value has never been recorded and thus, is not applicable. An example of the same is Police Station. We do this filtering by first assigning these no energy star buildings a value of NA (as an identifier) and then removing those rows that have at least one building type (first, second or third largest) as NA. We now have our training data (df_energystar) and test data (df_noenergystar). 

With this crucial cleaning done, we undertake some more cleaning steps on the both train and test data, including -

Dropping rows that have SourceEUI less than 0
Dropping rows that have GHGEmissionIntensity less than 0
Dropping rows that have GHGEmissionIntensity greater than 10
Dropping rows that have Source and/or Site EUI less than 0
Dropping rows that have missing Source and/or Site EUI values
Dropping rows that have missing GFA values
Dropping rows that have missing LargestPropertyUseType values

Additionally, all the columns except the Type of Property are numeric in nature and can be used directly. In order to encode the relationship between two building types in the representation fed to the model, we tried two approaches.

_Approach One_
We initially obtain their BERT Encoding. For example, 'Multifamily Housing' and 'Residence Hall' are more similar than 'Multifamily Housing' and 'Hospital'. Thus we cleaned the Property Type column and encoded it using BERT. Finally, we concatenate the columns for X along with the BERT encoding and fed it to our model. 

_Approach Two_
While the results were satisfactory, we decided to venture into One Hot Encoding (OHE) as well, even though these encodings do not capture meaning and thus, relative distance between words. However, we create a special version of OHE where the embedding is not 0s and 1s but instead has the area of the building type (LargestPropertyTypeGFA, SecondLargestPropertyTypeGFA, ThirdLargestPropertyTypeGFA) in place of 1s. An embedding dictionary is created to store all the building types and their respective embeddings. For any building types that are NA, the area is set as 0.
This processing is done to both training and test data.

Post this processing, we commenced our ML model segment. The models we experimented with are-
* K Nearest Neighbors
* K Means 
* Linear Regression
* Support Vector Regressor
* Decision Tree
* Random Forest
* Extra Trees Regressor
* Ridge Regressor
* Multi Layer Perceptron

Out of all our experiments, the Extra Trees Regressor gave us the most favorable results which can be found listed in the results section.

#### Interaction Flow Modeling
To build an interaction flow based on the dataset we have, there were some steps to take in order. Firstly, we started with setting the key questions from the user’s normal perspective. Where is my building? How much is the energy efficiency of my building? What makes the energy efficiency of my building? Does my building need to get upgraded or not? After getting the questions, we needed to structure each chapter based on those bullets. Then, we should define the x-axis and y-axis to answer. For example, the specific years should be provided with the energy use pattern, or the property type could be adopted for filtering the efficiency of the building. Based on these settings, we did the visualization sketches to decide if it clearly helps to answer the questions.


## Results
#### Predicted Energy Star score
While we experimented with 9 models, the ones that gave us considerable results were Decision Trees, Random Forest Regressor and Extra Trees Regressor - 

| Model |Mean Train Scores|
---------------------
| Decision Trees | 0.452772194 |
| Random Forest Regressor | 0.718953426 |
| Extra Trees Regressor | 0.781048178 |

Since the Extra Trees Regressor performs the best, we also calculate the score for the validation dataset, which comes out to be 0.7420166382336816.

With these scores, we move onto prediction, where we simply pass the OHE encodings of the test data into the model and output the predicted Energy Star Score value.

#### Interactive data visualization
To illustrate the interaction flow as a result, we will give an example when walking through each chapter.

**Chapter 1**_
This application allows the user to effectively compare the selected building by filtering the unnecessary noise and data of buildings which cannot be compared with their own building’s characteristics. The application allows the user to filter the visualization with the parameters of Energy Use Intensity / Energy Score, Year of the Data provided, Zip Code, Area, Number of Floors and the year the building was built. This allows the user to create a meaningful comparison with other buildings in the similar type. As we go down through the filters, the filters dynamically change to accommodate the range specified earlier (Example: If there are no buildings with an area of 36,000 sq.ft which have more than 5 floors, the application will convey this information to the user). Then, let’s say that the user selects the one building which is located on 405 Olive Way, Seattle 98101.

**Chapter 2**
For now, it is possible for the user to analyze that building. So the selected building in this case is a hotel built in 1927, which has 12 floors, and it used 55.7 kBtus of energy per sq.ft of the building. In 2020, the building got rated 92 in terms of the Energy Star.
Then, how efficient is that building? To give a sense, there are three different levels of efficiency comparison: city level, neighborhood level, and building level. As a start, the user can compare the building with the average of all the buildings in the same property type in the city of Seattle. It is possibly said that the building used more or less energy than the city average from the specific year. Also, the building got rated with a more or less Energy Star score during the specific period. In this way, the user can easily compare the efficiency of the building with the city average based on the 5-year trend. Then the user can do the same thing at the neighborhood level. Now there is one more comparison along with the efficiency of the selected building, which refers to the energy sources used in the building. If the building consumed different types of energy sources, the side-by-side charts should be provided so that the user can compare the use pattern with the EUI and Energy Star score trend at the same time.

**Chapter 3**
In this section, we analyze the different characteristics of the selected building that affect its performance in comparison to the other buildings. The first sub question analyzes the performance of the program of the selected building in comparison to nine other best performing programs. This visualization shows where the selected program stands when compared to the best performing programs. The mean of the energy use intensity is taken for all the programs for the purpose of this visualization. For example, the program type of the selected building (hotel) at 405 Olive Way stands first in comparison and it seems to perform worse than any other programs like warehouse, worship facility, or etc. in the chart. 
The second sub question provides an option of 5 other characteristics that affect the performance of the building, namely, Zip Codes,Yearbuilt, Total Area, Number of Floors and Electricity usage. With regards to the Zip Code, this helps in understanding that the 98101 neighborhood, where the selected building is located, shows the 9th lowest EUI among all the neighborhoods having the hotels in the city of Seattle. Once you set another filter of YearBuilt, the selected characteristic of the building is compared against the performance of other 9 better performing buildings built in different years. Such comparison and filters of characteristics, can facilitate an understanding as to where the building lacks in terms of performance as compared to the better performing buildings in Seattle.


## Discussion
As mentioned earlier, the audience of this project can be a tenant, building owner, architect, policy maker, or etc. It is said that whoever can figure out not only the building-level efficiency but also the city-level efficiency when exploring this system. It will also enable users to get actions to reduce the energy consumption or to upgrade something in the building if needed through better comparisons with more buildings with larger data inputs based on the machine learning model provided. Going through a couple of different energy benchmarking maps from other cities such as New York City, Philadelphia, Chicago could have contributed to developing the user flow and interface of this system. The focus is whether the map can encourage the user to compare the building with ease and to think about savings. Given that the built year of the buildings in the dataset ranges from 1896 to 2019, the doable actions for the selected building should be strategic and impactful. This kind of learning from other cases could power this map interaction to be more intuitive.

## Future Work
An extension to this study can help provide an even deeper and detailed insight into the performance of the building stocks. One of the ways of getting more detailed analysis is to add other significant characteristics of the building to the data set and then conduct the analysis. This would include the physical properties of the building, materials used, type of HVAC system among other characteristics. The same study can also be expanded to other cities in the country to understand the performance of their building stocks. Post that, a comparison can be made over the comparison of the data of different cities so that the cities can learn about building efficiency from one another. An expansion of the data set in terms of the years for which the data is being provided will help in gaining a deeper understanding about the performances of the buildings. Thus an application to other cities, extension of the data set with added characteristics and years can help provide more detailed insights for the analysis demonstrated in this application. 
