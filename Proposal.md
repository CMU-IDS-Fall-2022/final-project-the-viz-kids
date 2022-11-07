# Final Project Proposal

**GitHub Repo URL**: https://github.com/CMU-IDS-Fall-2022/final-project-the-viz-kids


Benchmarking Energy Consumption of Buildings in Seattle


Team Members: 
Aditi Kanaujia,
Jeffrey Na,
Nikita Khatwani,
Ninad Bandewar,
Pragnya Sridhar


### Problem description

Buildings contribute to 38% of global emissions as per the UN Environmental Global Status Report 2020. Hence, it is crucial for us to make efforts to reduce energy consumption. Each building’s energy usage is mentioned in its monthly bill. However, it is quite challenging to assess if this amount would be higher/lower than others or the set average (threshold) consumption value for say, the 2050 goal. This can be achieved using the benchmark data. To be specific, Seattle has State Policies to require all public, commercial, and multifamily buildings to complete the benchmarking report of energy consumption in the building. This helps various policy makers, consultants and designers take informed decisions about building retrofits and it assists with setting standards for new buildings as well. 

Given that energy is an important aspect for city planners and the government, data is maintained for each building in major cities every year. In Seattle alone, there are records for over 3,600 buildings for the year 2020 according to the Seattle government dataset. Manual inspection of such a large dataset is very difficult. There is a need to represent the data such that the users can choose the criteria they find important and gain insights from the data fitting those constraints. A dashboard can be used to meet this critical need. The existing dashboard of Seattle is informative, however, has scope for increased avenues for interaction and also, does not compare the relationship of various characteristics of the building with energy consumption. The available data set contains a couple of more unexplored features that could help answer conclusive questions and interactive techniques will aid in better comprehension of the performance in Seattle. It was also observed that the dataset contains missing values for the ENERGY STAR score, which rates building performance on a simple 1 - 100 scale, for about 25% of the buildings thus making the data represented incomplete.

In this regard, the motivation is to develop a new Dashboard to show the distribution of energy consumption across buildings in Seattle, incorporating more interactivity. Potential users of this dashboard include building occupants/owners, real estate developers, policy makers, consultants , designers, electricity board members and other interested parties. The dashboard can be used to identify energy efficient buildings to learn more about practices responsible for its efficiency and also to identify buildings that perform poorly. This will help the owners or other parties for further analysis and assess if the building must be retrofitted with newer green attributes like more energy efficient appliances, better heating/cooling systems, airtight construction, etc to reduce its energy consumption. 


### Question

1) What are the current trends in energy consumption of buildings in Seattle across five years?
2) How does the energy efficiency of buildings relate to the characteristics of buildings?
3) What specific buildings in Seattle should be prioritized in terms of energy investment?


### Proposed solution

The proposed dashboard will allow the user to analyze the energy data trends of the building and its relationship with the different characteristics of the building from 2016-2020. In order to tackle the issue of completeness of data, we propose using a machine learning algorithm such as clustering to fill the empty energy star rating feature values with a value derived from buildings most similar to the building in question. Thus this dashboard will be built upon a more complete data set. Interactive time based visualizations will help understand the Energy Trends among buildings where several characteristics of the building can be used as filters. Interactive geographical visualizations exploring the correlation between the building’s energy use and its type, location, area, number of floors, age, electricity and gas usage will help answer the second question. This will allow us to get a list of the most inefficient buildings in Seattle with potential to get retrofitted at the end, thus helping us make decisions on energy investment and reducing total energy consumption in Seattle.



# Sketches and Data Analysis
## Data Analysis:
(Ninad) - Where our dataset is from, what columns does it have and what it means

(Jeffrey) - What is energy star and what information does it give, how is it computed

(Jeffrey) - Comparing to our data - that table showing the different types of buildings and count of values

Given that energy score rating is a good metric to help even lay people understand and rate the buildings energy usage, it is worth mentioning in our dashboard. However, 25% of missing value is quite a big number of missing values and thus poses a problem we cannot ignore. In order to compute the metric using the formula from above, we do not have the monthly data of average usage for the last 12 months available.We thus intend to approximate this value using a Machine Learning algorithm to cluster the similar buildings together based on various features such as type of building, square footage, age of the building etc. Once the buildings are clustered, the missing value can be filled as the average of the cluster or the average usgae of the nearest k buildings. It is important to note and specify that this value is an approximation and we will also indicate the same in the dashboard while representing these values.

## Sketches:
### Question 01: What are the current trends in energy consumption of buildings in Seattle across five years?
#### Sub-Question 01: What is the trend in energy consumption over the last 5 years for the chosen building types such as hospitals, hotels etc?
This would potentially help us evaluate which building types have improved their energy efficiency. This will help electricity providers analyse which types of buildings need more energy, the government can identify the types of buildings that have improved their energy efficiency, thus allocating the resources to the ones laging behind on this front.

![4](https://github.com/CMU-IDS-Fall-2022/final-project-the-viz-kids/blob/main/image-4.png)

#### Sub-Question 02: What is the trend in energy consumption over the last 5 years for the chosen buildings?
This would help building associations analyse and compare their performance with their neighbours and thus implement more efficient practices. It would also help the government identify the buildings which have shown signifiacnt imporvement in their energy efficiency, thus granting them a small tax emption or reduced electricity prices.

![5](https://github.com/CMU-IDS-Fall-2022/final-project-the-viz-kids/blob/main/image-5.png)


#### Sub-Question 03: What is the trend in total and average energy consumption over the last 5 years for chosen neighborhoods? 
The total energy sketch would help energy providers analyse the energy consumption of various neighborhoods. This would provide insight on which neighborhoods are developing rather rapidly and might need more infrastructure to support the increased need than the others.
The average energy sketch would help the local governments compare their constituents to the others to implement more sustainable practices.

![6](https://github.com/CMU-IDS-Fall-2022/final-project-the-viz-kids/blob/main/image-6.png)

#### Sub-Question 04: What is the trend in usage of electricity vs natural gas over the last 5 years? Is there any relationship?
This would be particularly useful to the Government to understand how much natural gas they must be importing in subsequent years. Given that natural gas is limited, electricity is more widely used. Thus we expect to observe a decreasing trend in natural gas and an increasing trend in electricity. 

![7](https://github.com/CMU-IDS-Fall-2022/final-project-the-viz-kids/blob/main/image-7.png)

### Question 02 :  How does the energy efficiency of buildings relate to the characteristics of buildings?

#### Sub-Question 01 : What is the location of buildings in Seattle based on their energy performance with respect to other characteristics of the building?

The question is addressed via the map of the city as the base. With reference to the sketch below, buildings are being color coded on the map based on their energy performance. This map allows the user to interactively filter the buildings through the different characteristics available in the benchmarking data sets. For example,  a user can filter to see the performance of buildings built between the years 1950 - 1980 and their location on the map. Since all the filters will be linked to one another, they can also see the range of other characteristics like area, energy star score, GHG emissions of these filtered buildings. The eneryg scale on the right also provides a reference to see where the selected building might stand on the scale and its reference to an ideal efficient building as per standards. 

![1](https://user-images.githubusercontent.com/98651122/200193459-a9e8496c-3a51-4b7d-bafd-83e86ddd320e.jpg)


### Question 03 : What specific buildings in Seattle should be prioritized in terms of energy investment?

#### Sub-Question 01.a : What is the energy comparison of the top 10 least efficient buildings within a specific program type in Seattle ?

 it is important to compare buildings wihtin their program type to identify which buildings should be prioritized for retrofits/improvements since different program types have different energy standards requirements. A bar chart is chosen to answer this question where the user gets to decide which building type would they like to analyse. The chart plots the energy performance (EUI) of the top 10 least efficient buildings within that specific program against a bar of the most efficient energy performance expected by the standard. This helps put their performances in perspective of the goal that these buildings are needed to achieve. In addition , a map is linked to this graph to also show the location of these 10 buildings, incase of any insightful available learnings about the corelatoin between location and performance. 

![2](https://user-images.githubusercontent.com/98651122/200192850-9fcdf41a-552d-4c2c-a108-21daaadf4883.jpg)

#### Sub-Question 01.b : What is the location of these 10 least efficient buildings in Seattle ?
![3](https://user-images.githubusercontent.com/98651122/200193261-a04eb7ec-5a57-4cfc-a821-19aade114ded.jpg)

