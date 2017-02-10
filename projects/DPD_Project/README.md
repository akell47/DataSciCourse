
# Crime Forecasting
<br/>
### Decision Trees and Random Forrest

Understanding and modeling crime predictions helps validate police parole ground observations and inform residents and visitors to increase their personal safety awareness.
<br/>
This project is very much a data preprocessing and research design project.
<br/>
##### Original Project Idea Description notebook: <br/>
--->**https://github.com/akell47/DataSciCourse/blob/master/projects/DPD_Project/DPD_InitialProjectIdea.ipynb** <br/>
<br/>
There is much to improve to create a more logical and practical method of "crime prediction." I see what needs to be redone to improve the research design. The preprocessing and data combining processes are solid. Putting areas to improve up front here: <br/>
#### Areas to Improve
1. Where Block Groups intersected with the Index Grid
  - Block Groups that had a value of 0 were averaged with the adjacent Block Group's value. The resulting Grid Squares where that intersection occurred is then half the value. An example of where this is a problem is the Census Data on amount for rent for apartments. Thus Block Groups that contain all single-family parcels next to Block Groups that have apartments and have a number value for amount of rent are half the value on the grid that intersects.
  - Example of this: <br/> https://github.com/akell47/DataSciCourse/blob/master/projects/DPD_Project/Maps/DesignFlawCensusIndexGrid.JPG
2. The Index Grid needs to be the Data Frame not the Incident Points.
  - Data normalized / aggregated up to the Index Grid then predict over the Grid.
3. Grid Size
  - Also perhaps change the size of the index grid to get a count of points within a cell - Or make the grid size fitted to each crime target so that each grid is 0 or 1 for each crime target. Also need to think about this by the aggregated years or just one for the grid to be created on.
4. Improve Visualizations
  - Add more plots and charts
  - Make them interactive
  - Elaborate more on the visual trends and what it means for the model and for the research question(s). Current visualizations are just a sample.
  - Add time series maps, and hot spot maps.
5. Research and carefully decide what Census Data to use.
  - Current project has just a select few tables, mostly on Housing Characteristics.

## Data Sources and Data Scrubbing
Data is compiled from publically available datasets of four main data sources: <br/>

1. Incident Data
  - From Sandy Springs Open Data Site found link to Socrata Data on Incidents from City of Sandy Springs and City of Dunwoody that is a live feed from the Cities' Police Department.

2. Census Data
  - From the Census Select Demographic Data Geodatabase with shapefiles and Census Tables.
  - lots of manual joining in ArcMap
  - Census Meta Data Full Reference (open it in excel :P)<br/> https://github.com/akell47/DataSciCourse/blob/master/projects/DPD;_Project/Data/SelectDemographicMetadata.csv

3. Weather Data
 - From Weather Underground Historical Data
 - Data columns with mixed data types

4. Zoning Data
  - From City of Dunwoody Open Data Site and City of Dunwoody Open Data Site.
  - Each city classifies Zoning differently - much grouping was preformed in this section

<br/>
Data for this project was not a pre-cleaned dataset with columns that that were selected for one to learn on. The Data is from quite disparate sources and formats. I learned a lot of cleaning techniques and how to work through several preprocessing issues. I had numerical data with text in the cells, misspelled city names, and columns with too many values.  I did several intersections, dissolves, and joins with geoprocessing tools, cleaned the data and grouped data, and joined data on converted date fields. <br/>
##### Meta Data and Data Sources are documented in the Data Preprocessing notebook:<br/>
--->**https://github.com/akell47/DataSciCourse/blob/master/projects/DPD_Project/IncidentsPreprocessing.ipynb** <br/> (washing machine notebook) <br/>

## Research Design - Gridding data
An important concept in this research design is that of an Index Grid. The data from above is all "grouped up" to the Index Grid then the Index Grid is the Data Frame to make predictions on. As explained above the current project the Incident Points are the Data Frame data for the project. The data preprocessing, cleaning, joining, creating dummy variables, enumerating categories, and running it through Random Forest Classifier will all be the same process with the Index Grid data (but was done on the Incident Points).<br/>
Example: <br/>
https://github.com/akell47/DataSciCourse/blob/master/projects/DPD_Project/Maps/B25002e2_OccupiedHousingUnits.jpg

## Data Visualizations
The Visualizations are an example of just one or a few crime targets. Ideally I want to make these visualizations data with all the plots, and charts to be interactive.  Seems a little silly to have this super long scroll of all the possible visualizations. I want to create this section so that the plot type is the same but you can click on each crime type so you don't have to scroll down a long page.
##### Visualizations notebook: <br/>
--->**https://github.com/akell47/DataSciCourse/blob/master/projects/DPD_Project/IncidentTimeSeries.ipynb** <br/>
Currently you can see an interesting trend happening on Sundays.

## Fitting the Model - Machine Learning
##### Fitting the Model to Decision Trees and Random Forest notebook
(and a preprocessing specific to the algorithm): <br/>
--->**https://github.com/akell47/DataSciCourse/blob/master/projects/DPD_Project/Incidents_Model.ipynb**
Key Findings:
- Max Temperature and Hour of the Day had highest feature importance across all targets aka Incident types.


## Resources
Ideas are shared and code is copied.  The world is our resource. <br/>
This project was created with resources such as YouTube, Wikipedia, slack channels, StackOverflow, sklearn API, Google, and @bhajer.

<finish libraries list> <br/>

This report is excellent.
Covers a wide variety of crime prediction techniques and also debunks myths around crime forecasting.
http://www.rand.org/content/dam/rand/pubs/research_reports/RR200/RR233/RAND_RR233.pdf

## Threats to Open Data
https://www.theatlantic.com/business/archive/2017/02/real-life-consequences-hiring-freeze/516150/ <br/>
**A Bill** https://www.congress.gov/bill/115th-congress/senate-bill/103/text
```
(b) Notice.—The notice of the Department of Housing and Urban Development relating to the Affirmatively Furthering Fair Housing Assessment Tool, published in the Federal Register on December 31, 2015 (80 Fed. Reg. 81840; Docket No. FR–5173–N–07), and any successor notice or rule substantially similar to such notice shall have no force or effect.
```
```
Notwithstanding any other provision of law, no Federal funds may be used to design, build, maintain, utilize, or provide access to a Federal database of geospatial information on community racial disparities or disparities in access to affordable housing.
```
Great lets make unfair housing.<br/>
This is my data and research. <br/>
http://georgia-dca.maps.arcgis.com/apps/webappviewer/index.html?id=7556775c875a4cfcb372997cd9baa882 <br/>

**Open Data** is very important for the field of Data Science. Creating Legislative Action such as hiring freeze for scientists to enter Federal Government is not ok. Aiming to dismantle scientific data and research on earth sciences is an attack on the science community for all. Total nonsense to make a crisis for all the amazing diligent and hardworking people in public service sector. If anything Government need all the help it can get on bringing in new technology, and talented innovators - quite desperately in some areas. Government already has a difficult time competing with salaries in the private industry. Like user experience with apps that thrive and improve our quality of life, it is necessary for Government(s) to embrace modern technology for us to be a successful, beautiful, pleasurable, and welcoming place for businesses and families. In half a week this country lost a year's worth of talent. Innovation and business is not constrained to geographic boundaries, innovation will make space and salaries elsewhere. <br/>
### Amazing Data providers
* Data.gov
* HUD
* USGS
* EPA
* CDC
* NPS
* GPB
* NASA
* NOAA
* USFWS
* Census

<br/>
<br/>
