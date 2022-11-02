# Final Project Proposal

**GitHub Repo URL**: TODO

###########################################
Benchmarking Energy Consumption of Buildings in Seattle

###########################################
Team Members: 
Aditi Kanaujia
Jeffrey Na
Nikita Khatwani
Ninad Bandewar
Pragnya Sridhar

###########################################
Problem description

Buildings contribute to 38% of global emissions as per the UN Environmental Global Status Report 2020. Hence, it is crucial for us to make efforts to reduce energy consumption. Each building’s energy usage is mentioned in its monthly bill. However, it is quite challenging to assess if this amount would be higher/lower than others or the set average (threshold) consumption value for say, the 2050 goal. This can be achieved using the benchmark data. To be specific, Seattle has State Policies to require all public, commercial, and multifamily buildings to complete the benchmarking report of energy consumption in the building. This helps various policy makers, consultants and designers take informed decisions about building retrofits and it assists with setting standards for new buildings as well. 

Given that energy is an important aspect for city planners and the government, data is maintained for each building in major cities every year. In Seattle alone, there are records for over 3,600 buildings for the year 2020 according to the Seattle government dataset. Manual inspection of such a large dataset is very difficult. There is a need to represent the data such that the users can choose the criteria they find important and gain insights from the data fitting those constraints. A dashboard can be used to meet this critical need. The existing dashboard of Seattle is informative, however, has scope for increased avenues for interaction and also, does not compare the relationship of various characteristics of the building with energy consumption. The available data set contains a couple of more unexplored features that could help answer conclusive questions and interactive techniques will aid in better comprehension of the performance in Seattle. It was also observed that the dataset contains missing values for the ENERGY STAR score, which rated building performance on a simple 1 - 100 scale, for about 25% of the buildings thus making the data represented incomplete.

In this regard, the motivation to develop a new Dashboard to show the distribution of energy consumption across buildings in Seattle incorporates more interactivity. Potential users of this dashboard include building occupants/owners, real estate developers, policy makers, consultants , designers, electricity board members and other interested parties. The dashboard can be used to identify energy efficient buildings to learn more about practices responsible for its efficiency and also to identify buildings that perform poorly. This will help the owners or other parties for further analysis and assess if the building must be retrofitted with newer green attributes like more energy efficient appliances, better heating/cooling systems, airtight construction, etc to reduce its  energy consumption. 

###########################################
Question

What are the trends in energy consumption among buildings in Seattle across five years? (2016-2020)
How does the energy efficiency of buildings relate to the characteristics of buildings?
What specific buildings in Seattle should be prioritized in terms of energy investment?

###########################################
Proposed solution

The proposed dashboard will allow the user to analyze the energy data trends of the building and its relationship with the different characteristics of the building from 2016-2020. In order to tackle the issue of completeness of data, we propose using a machine learning algorithm such as clustering to fill the empty energy star rating feature values with a value derived from buildings most similar to the building in question. Thus this dashboard will be built upon a more complete data set. Interactive time based visualizations will help understand the Energy Trends among buildings where several characteristics of the building can be used as filters. Interactive geographical visualizations exploring the correlation between the building’s energy use and its type, location, area, number of floors, age, electricity and gas usage will help answer the second question. This will allow us to get a list of the most inefficient buildings in Seattle with potential to get retrofitted at the end, thus helping us make decisions on energy investment and reducing total energy consumption in Seattle.
