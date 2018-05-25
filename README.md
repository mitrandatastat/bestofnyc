# Best Schools of NYC

This repository contains a data analysis project that shows us the top 10 best high schools and top 18 most cost-effective NYC neighborhoods. It also tells us a whole lot story about the impact of wide array of demographics on the overall student performance in SAT. 

### Objectives

Below is the list of questions for NYC region that we are looking to answer as a final outcome of this project:

* Is Scholastic Aptitude Test (SAT) a fair test in the diverse demographic region like New York City?

* How SAT score vary with race, income, gender, socioeconomic background and other wide array of factors?

* What are the top 10 best schools of NYC based on the average SAT score?

* What are the least expensive NYC neighborhoods with top 10 best schools?

* Which schools consist more than 60% of female students proportion and have average SAT score higher than 1700?

* Which are the schools with more than 95% and less than 10% of the Hispanic students?

* Which schools have low total enrollment and have low average SAT score?

### Goal Significance

Why do we need to determine whether SAT is a fair test or not? What advantage we could have by concluding upon the SAT test fairness with evidence? Below are the goals we can enlist: 

* This information will give us an idea about:  
	* How various factors play role in student’s performance in SAT score
	* How diverse the student mix within various NYC neighborhood?
	* How effectively different players of this game, i.e. teachers, parents, students, test system etc., contribute per their roles and responsibility
	* The school regions with strong/weak performances
	* Role of ethnicity, gender, income status and community environment over the test performance

* Based on the results, we could conclude whether:
	* How fair is the SAT system?
	* Which are the factors need to be addressed in case any flaw in the current system is identified?
	* The areas of NYC that should be given more attention in the event of future policy amendment. 

### Data

#### Data Source

New York City public data for student SAT score by high school and other relevant demographics is available at:
https://data.cityofnewyork.us/Education/2012-SAT-Results/f9bf-2cp4

The details of the property values in five distinct NYC suburbs is available in the .csv files listed below. This data is available for download at: 
http://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page

#### Data Lists

The data is available in the .csv file format. The detailed file data information is available in the referred links of the file name description.  

ap_2010.csv	:	Data on AP Test Results)

class_size.csv	: 	Data on class size

demographics.csv	:	Data on demographics

graduation.csv	:	Data on graduation outcomes

hs_directory.csv	:	A directory of high schools

sat_results.csv	: 	Data on SAT scores

survey_all.txt	:	Data on surveys from all schools

survey_75.txt	:	Data on surveys from New York City district 75

The raw property data for NYC is cleaned based on the most realistic per sq. ft. property rates in each of the five regions. In order to maintain trade-off between the computing and data diversity, the size of each data set is restricted to around 12000 entries. 
For more details, see the files listed below:

BK2017V11.csv	:	Sales Details for Properties in Brooklyn

BX2017V11.csv	:	Sales Details for Properties in Bronx

MN2017V11.csv	:	Sales Details for Properties in Manhattan

QN2017V11.csv	:	Sales Details for Properties in Queen

SI2017V11.csv	: 	Sales Details for Properties in Staten Island

#### Data Details

SAT scores by school - SAT scores for each high school in New York City

School attendance - Attendance information for each school in New York City

Class size - Information on class size for each school

AP test results - Advanced Placement (AP) exam results for each high school (passing an optional AP exam in a particular subject can earn a student college credit in that subject)

Graduation outcomes - The percentage of students who graduated, and other outcome information

Demographics - Demographic information for each school

School survey - Surveys of parents, teachers, and students at each school

### Highlights of the code. 

#### Software packages used:  

* Python
* Pandas
* Numpy
* Excel
* re
* random
* Matplotlib.pyplot 
* Matplotlib.colors

#### Overview:

* Import files of different formats (.csv, .txt) and combine them to consolidate the data frame
* Understand the data and its relevance to the ultimate project goal
* Identify list of features and target feature for data analysis
* Combine various fields in the scattered data files and generate primary keys for database merge
* Format alternation for data frame column info
* Extract latitude and longitude of NYC schools and map them in basemap
* Condense various datasets to focus onto NYC High School Students SAT score info
* Clean the dataset for unwanted info and NaN values
* Review features correlation with the target column and visualize it through chart
* Various features verified for correlation with SAT score are:
	* Safety and Respect score based on student responses
	* Racial percentage
	* Hispanic proportion
	* Gender
	* AP Test Takers
	* Class size

* List schools with:
	* More than 95% Hispanic students
	* Less than 10% Hispanic Students
	* Low total enrollment and low SAT score
	* Higher SAT score and high female percentage
	* SAT score more than 1700 & female percent higher than 60%

* Correlation between Parent, Teacher and Student Responses to survey
* Find out the least expensive NYC neighborhoods for top 10 schools

### Map Safety Score by Districts

![output_36_1](https://user-images.githubusercontent.com/33802087/40557932-70d83e96-606f-11e8-85f3-cbf7c9dcdfa1.png)

### Visualize the results.

![output_29_0](https://user-images.githubusercontent.com/33802087/40557944-72d3708a-606f-11e8-89c4-eca9478e37a7.png)

![output_33_0](https://user-images.githubusercontent.com/33802087/40557931-70a6eb66-606f-11e8-874a-1a39a4a2f65b.png)

![output_39_0](https://user-images.githubusercontent.com/33802087/40557933-7108b526-606f-11e8-9efa-e6ff892ab393.png)

![output_42_0](https://user-images.githubusercontent.com/33802087/40557934-7133dc38-606f-11e8-8dce-79964ae43f90.png)

![output_45_1](https://user-images.githubusercontent.com/33802087/40557935-71604430-606f-11e8-9075-d5e235169e66.png)

![output_54_0](https://user-images.githubusercontent.com/33802087/40557936-718a7a5c-606f-11e8-9dd7-d4a4e9617213.png)

![output_57_1](https://user-images.githubusercontent.com/33802087/40557938-71bec046-606f-11e8-8fb7-4d2efd1c7a4b.png)

![output_61_0](https://user-images.githubusercontent.com/33802087/40557939-71ef7e8e-606f-11e8-83ae-9f80e891ede8.png)

![output_65_0](https://user-images.githubusercontent.com/33802087/40557940-721c8bf4-606f-11e8-8d5f-d5ce653bcbd6.png)

![output_72_1](https://user-images.githubusercontent.com/33802087/40557941-724b060a-606f-11e8-988b-f8c43a867fa4.png)

![output_75_1](https://user-images.githubusercontent.com/33802087/40557942-72790cc6-606f-11e8-8e30-a2ba06d5880e.png)

![output_78_1](https://user-images.githubusercontent.com/33802087/40557943-72a7f52c-606f-11e8-8f92-25a0e5ea3603.png)

### Tabular Results

#### Top 10 Best Schools in New York City

![image](https://user-images.githubusercontent.com/33802087/40558092-e9d1e072-606f-11e8-88bd-25f3d2bb32dd.png)

#### The Least Expensive NYC Neighborhoods with Top 10 Best Schools

![image](https://user-images.githubusercontent.com/33802087/40558104-f27474c4-606f-11e8-88b1-f4cfe777df95.png)

#### Schools with More Than 60% Female & Greater Than 1700 SAT Score

![image](https://user-images.githubusercontent.com/33802087/40558111-fcbbaa56-606f-11e8-95e2-ff1f9961d193.png)

#### Schools with More Than 95% Hispanic Students

![image](https://user-images.githubusercontent.com/33802087/40558120-fff40600-606f-11e8-84e9-181620abe04b.png)

#### Schools with Less Than 10% Hispanic Students

![image](https://user-images.githubusercontent.com/33802087/40558122-030d1ae8-6070-11e8-93b7-00f7f1c77cd7.png)

#### Schools with Low Total Enrollment for SAT & have Low Avg. SAT Score

![image](https://user-images.githubusercontent.com/33802087/40558131-0628585a-6070-11e8-91c9-1aa771ace0b5.png)


### Explain the results in a simple, concise and easy way. (non-technical audience)

The analysis and results give very useful info to shape our future planning based on:

* Student mix based on certain gender and/or ethnicity in various neighborhood

* Significance of various factors such as safety, racial mix, gender, female proportion, Advance Placement Testing system, classroom size, parents-student-teachers expectations for academia etc. over the SAT score

* School regions with strong/moderate/weak SAT performance

### Explain the results in the most technical way. (technical, data-scientist audience)

* We observe high correlations between SAT score and following factors:
	* Number of Students / Seats Filled
	* Average Class Size
	* The highest grade the school expects to serve eventually
	* Number of Teacher Respondents (-ve) 
	* SAT Critical Reading Average Score
	* Free Lunch Percent
	* Number of distinct programs available at the school (-ve)

	It’s obvious to see how the ‘class-size’, ‘number of students’ and the ‘highest grade the school expects’ creates a competitive but cohesive social environment for the students and encourage them working hard to perform better in SAT.

	The strong positive relationship of ‘SAT Critical Reading Average Score’ with the SAT score shows the impact of effective reading skills on the overall SAT performance. 

	The positive correlation of ‘Free Lunch’ with SAT score tells the success story of government’s welfare program in the area of economically developing neighborhood and low-income immigrant regions. 

	It is interesting to note that higher the number of teachers’ participation in survey for expectation about student’s academia negatively influence the overall student performance in SAT. 

	The negative correlation of ‘Number of distinct programs available at the school’ with SAT score goes in reverse parity with the positive correlation of ‘class-size’ and ‘number of students’ factors above as more program diversity tends to reduce the class-size and number of students per course. 

* Correlation: Safety & SAT Score:

  There appears to be a positive correlation between safety and SAT score though not so strong. There are some schools that have high safety standard and achieve high SAT score and some schools with low safety standard got low SAT score. Majority of the school from the sample falls between the safety score of 6.0 to 7.5 with an average SAT score below 1500. 

* Safety Map

  Brooklyn seems to have better safety score compared to the same for the parts of Manhattan, Queens and Bronx region.  

* Racial Correlation:

  The whites and the Asians are found having strong positive correlation while the Blacks and the Hispanic are found having moderate negative correlation with the SAT score. 

  This is due to the fact that the Hispanic and the Blacks might be coming from the immigrant families. The socio-economic factors, family support and surrounding environment play significant role in overall performance of the students. 

* Correlation between Hispanic Proportion and SAT score:

  There seems to be a moderately strong downward trend with the increase of Hispanic Population. Very small portion of population attains a SAT score of 1800 or more while majority falls under the score of 1500. Majority of the schools with Hispanic population in the range of 40% - 80% get average SAT score of around 1150. The results become clearly evident when plotted with 40% or more Hispanic Proportion for SAT score of 1400 or less. 

  This is mainly due to the immigrant population along with the socio-economic and demographic factors.

* Gender Correlation: 

  Female show very weak positive and male show very weak negative correlation for SAT score. This shows the relative performance of female and male students – which is more or less the same. 

* Relationship with Female Percentage:

  There exists moderately positive correlation between the female proportion and SAT score. While tested for pool of students having more than 50% female proportion and SAT score of greater than 1500, it is observed that around 40% - 65% of the total students attain SAT score in the range of 1000 – 1350. 

* Relationship with AP Test Takers:

  No correlation is found between the AP Test Takers and the SAT score. In fact, up to 40% of the total enrollment who took AP Test scored less than 1400 in SAT. There are few percent of students who took AP Test and secured SAT score of 1800 – 2000. 

  The data about students’ performance in AP Test Vs. SAT could give us more insight to further comment about the AP Test results predictive relevance for SAT score.

* Correlation with the Class Size:

  Moderately strong positive correlation has been observed between the class size and SAT score. Students’ SAT score slowly improves as the class size increases from 20 to 30 students. Majority of the students score between 1000 – 1400 irrespective of class size. However, there are few exceptional cases where the students score beyond 1800.  

  This clearly shows that performance of students in SAT is strongly impacted by his/her class size, higher student-teacher ratio and consequently the dense social environment -which collectively proves to be encouraging for the students.  

* Correlation for Difference between Parent-Student Survey Response:

  It appears that there is a moderately strong negative correlation between the difference in Parent-Student Survey Response and SAT Score. Hence, more similarity of parents and student’s opinion about the latter’s academic expectation, better would it be reflected in to the higher SAT score. In other words, more the disparity between parents and student’s responses for students’ academic expectation score, lower would be the SAT score.  

  This clearly indicates that parental involvement in student’s education results into a better SAT performance and vice versa. 

* Correlation for Difference between Parent-Teacher Survey Response:

  There exists weak negative relationship between the difference in parents and teachers’ survey response and SAT score. This indicates that difference of opinion between the parents and the teachers over the expectation of student’s academia has moderately reverse impact over student’s performance in SAT. In other words, less the differences between the parental and teacher’s opinion about student’s academic expectation, moderately better would be student’s performance in SAT. 

* Correlation for Difference between Teacher-Student Survey Response:

  No correlation is found between the difference in teachers’ and students’ survey response and SAT score. This indicates that difference of opinion between the teachers and students over the academic expectation for the students have no impact over student’s performance in SAT.

* Following information is deduced based on the analysis to answer our certain open-ended questions:
	* List of Schools with Hispanic More than 95%
	* List of Schools with Hispanic Less than 10%
	* List of Schools with Low Total Enrollment and Low Sat Score
	* List of Schools with High SAT score & High Female Percentage
	* List of School with more than 60% Female Percentage and SAT score higher than 1700
	* Top 10 Best Schools NYC based on SAT Score
	* List of Great Neighborhood (Least Expensive) in NYC for Top 10 Best Schools

### Conclusion

#### What we learn from this outcome. (non-technical audience)

* We understand the impact of various demographic, socio-economic, and current credit and grading system related factors over the performance of students in SAT examination. This helps us to determine and verify how this test maintains balance amongst these factors for overall fairness of test within the widely diverse community. 

* We are able to determine top 10 best schools based on their average SAT score.

* We shortlist the least expensive but situated with the top 10 best school neighborhood regions.

* We could identify the regions of NYC neighborhood where schools do not perform well and understand whether or not there exists any ethnic diversity [to consider] for policy improvement. 

* We learn the impact of similarity and disparity of students/teachers/parents’ opinion towards student’s academia over the SAT performance. This highlights the roles and responsibilities of various players of the game and its relative significance for the final outcome.

#### Technical significance of the results. (technical, data-science audience)

* We are able to know various critical factors that do/do not affect students’ performance in SAT examination. Based on this info, we can verify and validate how fare the current SAT system is for the diverse demographics like NYC. In case we found any flaws in the SAT system for unfair testing performances, we can get better idea about the causes to focus on and fix the system.

* We found the factor significance as summarized below:

  ![image](https://user-images.githubusercontent.com/33802087/40558389-cbc91e3c-6070-11e8-82d0-5b064a752467.png)


* Based on the correlations and its severity on students’ SAT score, we can mention that SAT is reasonably fair for the diverse NYC demographics. 

* We got answers to all of our open-ended questions enumerated in the objectives of the project. (See Results above for details)

### Suggestion for Further Development

#### How differently you would have done this project, if get a chance to do it again. Why?

In case of gotten second chance to do this project again, I would have gathered and used some more features such as:
	* Parents employment status
	* Average annual family income
	* Present residence status: Own/Rented, House/Apt. 
	* Family size
	* Number of siblings (elder/younger)
	* Details of student’s extracurricular activities
	* Participated in free / free and reduced lunch program
	* Student’s total years of enrollment with the same school
	* Past scholarship record
to determine each of these factors correlation with SAT score to further deepen our understanding about the fairness of the SAT system. 

#### Your suggestions for someone if s/he wants to further continue this work. 

Someone could pick one or more of the untouched data fields mentioned above, explore and gather additional features and continue this journey further to cherish more flavors in the analysis. 
