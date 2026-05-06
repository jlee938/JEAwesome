# Grocery Store and Income Analysis

## Contribution

Joyce:

- Obtain Grocery dataset
  
- Cleaning Grocery dataset
  
- Helped merge two datasets
  
- Helped create data visualizations

Eric:

- Obtain Census data
  
- Cleaning Census data

- Helped merge two datasets

- Helped create data visualizations

- Help create files to organize dataframes 

## Summary

## Data Profile
**Grocery Store Dataset**

**Census Dataset**:

The original census dataset can be referenced in OriginalDataset/ChicagoZipMedian.csv and the cleaned version can be referenced in CleanedDataset/final_household_df_cleaned.csv.  The census dataset that was acquired directly from the U.S. Census Bureau S1901 Income in the Past 12 Months (in 2024 Inflation-Adjusted Dollars). It was manually filtered and selected by ZIP Code Tabulation Areas in Chicago (list of ZIP codes under Chicago is available on Google). Each column corresponded to a ZIP code under Chicago and the type of household (families, married couple, nonfamily household). Each row represents data for a specific ZIP code and household type, including the total number of households recorded. It shows the percentage of households that fall within various income brackets, ranging from 'Less than $10,000' to '$200,000 or more' In addition, the dataset provides both the median income and mean income (in dollars) for each group. 
There aren’t many strict legal barriers with this kind of dataset as it is directly acquired from the government. Despite this,  there are still some important ethical constraints to keep in mind. Since the project focuses on each ZIP code area, it has to be assured that the dataset won’t be used for bias and misrepresentation. This caution can prevent unintentionally reinforcing stereotypes about certain areas. 

**Merged Dataset**: 

## Data Licenses and Terms of Use

U.S. Census Bureau data is generally in the public domain, meaning it can be used and redistributed for both commercial and non-commercial purposes without copyright restrictions. However, there are still important conditions to follow, such as users are expected to properly cite the Census Bureau, avoid misrepresenting the data, and comply with confidentiality protections under Title 13 of the U.S. Code, which is to protect the confidentiality of individual responses.

## Data Quality

The final merged dataset contains 254 observations and 5 variables. It provides a snapshot of grocery store locations and the specific neighborhood’s economic data. This dataset can be referenced at `FinalDataset/merged_df.csv` After cleaning and merging, the dataset was relatively complete. One observation was missing values for `zip` and `median_income` (which will be discussed further soon). Despite one observation missing two values, the dataset’s level of completeness made the dataset suitable for exploratory analysis such as correlation analysis between store density and neighborhood income using a scatter plot as seen later in the report. 
The first strength of the dataset is its consistent formatting and standardization. The original data sources were successfully uniformed. For instance, store names were standardized to lowercase and all ZIP codes were consistent with five digit numbers. This standardization can prevent errors for future merging processes. 
The second characteristic of the data quality is its lack of redundancy and its uniqueness. With large datasets like the census and Grocery Dataset, there are prone to be duplicate entries. Despite this, the dataset had no duplicate observations. Outside of chain stores sharing the same name, every address functions as a unique identifier for the 254 records. 
The third strength of the dataset lies in its logical consistency and high degree of accuracy. To ensure the reliability of the economic indicators, all recorded ‘median_income’  values fall within a realistic and logical range of $31,905 to $147,357. An illogical value like $0 or negative amounts were not present in the dataset. Furthermore, all ZIP codes, excluding the missing observation,began with “60”, which confirms that all observation fell under the Illinois and Chicago area code. These factors confirm that the dataset displays a high level of accuracy and is suited for further interpretation. 
In terms of issues with the quality of the data, there are two changes that could be made to ensure and improve the data quality. One is the observation with missing values (`zip` and `median_income`). This missing variable was caused by a specific grocery store entry that was located outside of Chicago being present in the grocery store dataset. The grocery store with the missing `zip` and `median_income` values was Walmart located at 3320 south cicero avenue. On further inspection, it was found out that this address is not under the Chicago area. Because the neighborhood income data was precisely aimed and filtered to Chicago community areas, this out of area grocery store could not be matched with a corresponding income value from the census data. In order to ensure accuracy and integrity, and for future usages of this dataset, this grocery store entry will be omitted. The other issue is that it is difficult for the dataset to prove or be accessed for any type of timeliness. Since the dataset was merged from a census data and a dataset that was last updated on 6/13/25, proving the timeliness is difficult due to the lag in how demographic data is collected, updated, and estimated. 
Overall, the final dataset did have strengths when it comes to accuracy, completeness and consistency, but lacked in areas of timeliness. 

## Data Cleaning

The data cleaning process was executed primarily using Python. First, the grocery store dataset underwent cleaning. An examination of the `zip` column revealed that several entries contained additional digits beyond the standard five. While these extra digits provide more geographic data, such detail was irrelevant to the project goal of generalizing neighborhoods. Furthermore, because five digit ZIP codes are the standard convention and matched the format of the census Data (reference: `OriginalDataset/ChicagoZipMedian.csv`), the grocery store ZIP codes were converted into strings and indexed to ensure only the first five numbers remained.
Next, the grocery store addresses were evaluated. Discrepancies were found where some addresses appeared in all capital letters while others followed standard English conventions and lower cases. To maintain consistency and increase the data quality, every string in the address column was converted to lower case. Additionally, the `location` and `last_updated` columns were removed as these variables did not align with the project objectives. Cleaned grocery dataset can be found at `CleanedDataset/grocery_df_cleaned.csv`
The census data cleaning followed. Every row outside of the median income range was removed. Since the original dataset provided multiple income brackets, the project plan specifically required a comparison of only the median for each ZIP code area. The dataset also included various demographic statuses: `Households`, `Families`, `Married-couple families`, and `Nonfamily households`. The decision was made to focus exclusively on `Households`. This status serves as a superior generalization and representation of an area, as it encompasses all individuals occupying a housing unit and reduces unnecessary complexity. The margin of error column was also deleted, as its inclusion would have added excessive complication to the final comparison.
Following these adjustments, the ZIP code headers were identified as being insufficiently tidy for a dataset merge. Headers such as `ZCTA560601 !!Households!!Estimate` contained trivial terms like “ZCTA” that hindered comparison. These headers were cleaned to ensure the ZIP code column contained only the five digit numbers. Finally, because the ZIP codes were originally listed across multiple columns, the dataset was deemed difficult to merge in its raw state. To resolve this, the `.melt()` function was utilized to reshape the data, placing all ZIP codes under a single `zip` attribute and all correspdoning income values to the ZIP codes under an `median_income` attribute. Cleaned dataset can be found at `CleanedDataset/final_household_df_cleaned.csv`.
After, `CleanedDataset/final_household_df_cleaned.csv` was merged onto `CleanedDataset/grocery_df_cleaned.csv` based on `zip`.  All the grocery stores that had `CLOSE` for their `new_status` were dropped from the dataset as it is irrelevant to the observation. The goal of the project is to observe how accessibility of grocery stores change based on income. Closed grocery stores do not provide any sort of information for our observation. The process of dropping all `CLOSED` further improves the data quality fits for our specific observations. The final merged and cleaned dataset can be found in `FinalDataset/merged_df.csv`. 
To easily visualize the distribution of grocery stores across various median incomes, the merged_df.csv was grouped by `median_income`. This process involved aggregating the data to calculate store frequency within each income level, then the grouped dataset was sorted in ascending order of `median_income`. This new grouped dataset helped later portions of the project when it came to observing any changes between grocery store frequency and median income level and creating visualizations. The grouped dataset can be located in `FinalDataset/number_of_stores_grouped_by_median.csv`. 

## Finding 

## Future Work

As mentioned above in the Findings section, this project highlighted that analyzing food accessibility through a single variable, such as median household income, may not be sufficient to capture the full picture we were originally trying to find. The findings demonstrated that the relationship is far more complex and not strongly correlated. Learning to avoid oversimplified assumptions when working with real world data and problems 
This project also highlighted several key principles learned in the IS 477 course. Specifically, the Data Quality Dimension module emphasized their true implication when implementing or creating a dataset. It also served as a reminder of the usefulness and utility of APIs. For the longest time, API’s were not something valued when obtaining datasets online. Before, the decision was always to download a CSV file manually or scrap a dataset using BeautifulSoup if a downloading option was not available. This project taught that APIs are crucial when a project requires the most up to date results and to meet the Data Quality Dimension: Timeliness and 
Accuracy. Furthermore, the increased timeliness and results using API, in turn, can significantly increase the accuracy of the analysis. 
Based  on the lessons learned from the project, it was learned that the Data Quality Dimensions are, “moderately, codependent.” As the census dataset lacked timeliness, it was learned that this could also impact the final merged dataset and the final analysis accuracy. A census dataset that is updated every decade lacks timeliness and in return might reflect inaccurate median income results when the analysis or dataset is used to represent current conditions. 

Several precautions could be taken in the future in order to improve the project. One key refinement would be integrating a comprehensive Chicago median income dataset that offers annual, non-estimated updates and reporting contrary to the dataset acquired from census. As discussed in the Data Quality section and previous paragraph, the final merged dataset lacked heavily when it comes to timeliness. This problem mainly stemmed from the fact that one of the dataset used is updated every decade. For this reason it was also concluded that API will not be utilized for acquiring the census data as it isn’t often updated. If there were an alternative dataset that provided timely updates on the median income of each Chicago ZIP code area, it could improve the final merged dataset’s timeliness and accuracy, resulting in a better overall analysis that is more representative of current conditions. The same could be implied for the Grocery Dataset, as it wasn’t updated since last year. Using an alternative dataset that is updated more timely could have yielded better results. 
One other change that can be made in the future is to consider additional variables than just “income median” and area. There are many factors and nuances outside of income that might lead to food insecurity and lack of grocery store accessibility. Some factors might include, population density, transportation access, store size, and distance to the nearest grocery store. Moving beyond ZIP codes and median incomes and considering these factors may yield better insights on food insecurity and grocery store accessibility. 

## Challenges

One major challenge this project faced, as mentioned earlier, was the lack of timeliness in the two dataset used and the limited data pool selection. These two datasets were mainly selected due to the scarcity of alternative data sources and the high cost of creating a specific, primary dataset that could accurately support the project observations, goals and analysis. Another challenge involved obtaining an API dataset from the census website. Multiple errors were encountered despite following all the necessary processes. Once obtained, the large dataset proved very difficult to tidy and conform to the Accuracy, Consistency and Completeness Data  Quality Dimensions. Ultimately, the attempt to retrieve an API dataset from the census was deemed trivial, as the underlying dataset would not be updated for a decade. 

Another challenge lies in geographic granularity. Using ZIP codes as the unit of analysis can introduce distortions, as ZIP codes vary widely in both physical size and population density. Larger ZIP codes may contain more grocery stores, while smaller or more densely populated ZIP areas may have less. 

Another key challenge is the geographic specificity of the dataset. Both the grocery store dataset and the census data are explicitly focused on Chicago, which means the findings and analysis are highly localized. As a result, any conclusions or findings from this analysis may not be generalizable and applicable to areas outside of Chicago. As cities and countries vary in density, transportation and economic and financial distribution, these could influence grocery store accessibility. Because the dataset was filtered and cleaned specifically for Chicago ZIP codes, applying the same analysis to other areas with these varying factors without any adjustment made, most likely might produce inaccurate and misleading results. 

Beyond the data analysis itself, the project presented several technical challenges. Getting ourselves re-familiarized with GitHub after not using it for a great period of time created some delay. Furthermore, a hardware malfunction on one of our devices complicated efforts during the merging and cleaning coding stages.

## Reproducing 


## Reference
U.S. Census Bureau. Income by Zip Code Tabulation Area. American Community Survey 5-Year Estimates 
https://data.census.gov/chart?q=Income+by+Zip+code+tabulation+area&g=050XX00US17031_860XX00US


U.S. Census Bureau. Terms of Service 

https://www.census.gov/data/developers/about/terms-of-service.html


U.S. Census Bureau. License Information and Disclaimer

http://census.gov/data/software/x13as/disclaimer.html


