
# coding: utf-8

# ### Read in the data

# In[1]:


import pandas
import numpy
import re
import random 
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
get_ipython().run_line_magic('matplotlib', 'inline')

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

data = {}

for f in data_files:
    d = pandas.read_csv("databank/{0}".format(f))
    data[f.replace(".csv", "")] = d


# ### Read in the surveys

# In[2]:


all_survey = pandas.read_csv("databank/survey_all.txt", delimiter="\t", encoding='windows-1252')
d75_survey = pandas.read_csv("databank/survey_d75.txt", delimiter="\t", encoding='windows-1252')

# Combine two data frames by rows
survey = pandas.concat([all_survey, d75_survey], axis=0)

# Change the column head to align with other data frame
survey["DBN"] = survey["dbn"]

# Identify and make a feature list of our interest
survey_fields = [
    "DBN", 
    "rr_s", 
    "rr_t", 
    "rr_p", 
    "N_s", 
    "N_t", 
    "N_p", 
    "saf_p_11", 
    "com_p_11", 
    "eng_p_11", 
    "aca_p_11", 
    "saf_t_11", 
    "com_t_11", 
    "eng_t_10", 
    "aca_t_11", 
    "saf_s_11", 
    "com_s_11", 
    "eng_s_11", 
    "aca_s_11", 
    "saf_tot_11", 
    "com_tot_11", 
    "eng_tot_11", 
    "aca_tot_11",
]
survey = survey.reindex(survey_fields, axis=1)
data["survey"] = survey

# Print results for verification
print(data['survey'].head(5))
data['survey'].shape


# ### Add DBN columns

# In[3]:


# Change the column head to align with other data frame
data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

# Set uniform field length to develop same size DBN value in the data frame
def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return "0" + string_representation

# Call function to set same size of  DBN prefix
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)

# Generate DBN field by combining two columns 
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]

# Print results for verification
data["class_size"]["DBN"].iloc[0:5]


# ### Convert columns to numeric

# In[4]:


# List of useful columns from the sat_result data frame 
cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']

# Convert the string data into numeric form, transfor errors into null
for c in cols:
    data["sat_results"][c] = pandas.to_numeric(data["sat_results"][c], errors="coerce")

# Combining three column valus into one and store it into a new column
data['sat_results']['sat_score'] = data['sat_results'][cols[0]] + data['sat_results'][cols[1]] + data['sat_results'][cols[2]]

# Display results for verification
data['sat_results']['sat_score'].iloc[0:5]


# ### Extract Latitude and Longiude from the Data

# In[5]:


# Function to extract latitude from the given string
def find_lat(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

# Function to extract longitude from the given string
def find_lon(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lon = coords[0].split(",")[1].replace(")", "").strip()
    return lon

# Extract latitude and longitude from the column at store them in new columns
data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)
data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

# Convert the extrated latitude and longitude into numeric form, transform errors into null
data["hs_directory"]["lat"] = pandas.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pandas.to_numeric(data["hs_directory"]["lon"], errors="coerce")

# Print results for verification
data['hs_directory'].head(5)


# ### Condense Datasets

# #### Data frame 'class_size'

# In[6]:


class_size = data["class_size"]

# Segregate the data frame from high school students under general education category
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]
print(class_size[["GRADE ", "PROGRAM TYPE"]].head(5))

# Consolidate the data frame for unique DBN field
class_size = class_size.groupby("DBN").agg('mean')

# Converting back DBN as index to column 
class_size.reset_index(inplace=True)
data["class_size"] = class_size

# Print data frame for verification
data['class_size'].head(5)


# #### Data frame 'demographics'

# In[7]:


# Seggregating the dataframe 'demographics' based on the 'schoolyear' to extract unique DBN
data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]

# Print for verification
data['demographics'].head(5)


# #### Data frame 'graduation'

# In[8]:


# Seggregating the dataframe 'graduation' for features useful to get unique DBN
data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]

# Print for verification
data["graduation"].head(5)


# ### Convert AP scores to numeric

# In[9]:


# Convert 'ap_2010' data frame columns to numeric format, transform errors into null
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for col in cols:
    data["ap_2010"][col] = pandas.to_numeric(data["ap_2010"][col], errors="coerce")
    
# Print for verification
print(data['ap_2010'].shape)
data["ap_2010"].head(5)


# ### Combine the Datasets

# In[10]:


combined = data["sat_results"]

combined = combined.merge(data["ap_2010"], on="DBN", how="left")
combined = combined.merge(data["graduation"], on="DBN", how="left")

# Print for verification
print(combined.shape)
combined.head(5)


# In[11]:


to_merge = ["class_size", "demographics", "survey", "hs_directory"]

for m in to_merge:
    combined = combined.merge(data[m], on="DBN", how="inner")

# Print for verification
print(combined.shape)
combined.head(5)


# ### Fill Up Null Values

# In[12]:


# Fill up the null values with the column average value
combined = combined.fillna(combined.mean())
combined = combined.fillna(0)

# Check for null values
print("Null Values in Combined Data Frame =", combined.isnull().sum().sum())


# ### Add a School District Column for Mapping

# In[13]:


def get_first_two_chars(dbn):
    return dbn[0:2]

combined["school_dist"] = combined["DBN"].apply(get_first_two_chars)

# Print for verification
combined["school_dist"].head(5)


# ### Find correlations

# In[14]:


correlations = combined.corr()
corr_satscore = correlations.corr()["sat_score"]
print(corr_satscore)


# ### Plot Correlations

# In[15]:


# Preparing a list of colors from matplotlib
colors_list = list(colors._colors_full_map.values())
random.shuffle(colors_list, random.random)

fig, ax = plt.subplots(figsize=(18, 12))
ax.bar(corr_satscore.index, corr_satscore, align='center', color=colors_list)
ax.set_xticklabels(corr_satscore.index, rotation=90)
ax.set_title("Correlation of Features with SAT Score")

plt.show()

We observe high correlations between SAT score and following factors:

o	Number of Students / Seats Filled
o	Average Class Size
o	The highest grade the school expects to serve eventually
o	Number of Teacher Respondents (-ve) 
o	SAT Critical Reading Average Score
o	Free Lunch Percent
o	Number of distinct programs available at the school (-ve)

It’s obvious to see how the ‘class-size’, ‘number of students’ and the ‘highest grade the school expects’ creates a competitive environment for the students to encourage them working hard to perform better in SAT.

The strong positive relationship of ‘SAT Critical Reading Average Score’ with the SAT score shows the impact of effective reading skills on the overall SAT performance. 

The positive correlation of ‘Free Lunch’ with SAT score tells the success story of government’s welfare program in the area of economically developing neighborhood and low-income immigrant regions. 

It is interesting to note that higher the number of teachers’ participation in survey for expectation about student’s academia negatively influence the overall student performance in SAT. 

The negative correlation of ‘Number of distinct programs available at the school’ with SAT score goes in reverse parity with the positive correlation of ‘class-size’ and ‘number of students’ factors above as more program diversity tends to reduce the class-size an number of students per course. 
# COMMENT ABOUT ABOVE SCATTER PLOT.

# ### Analyze Effect of Safety on SAT Score

# In[16]:


plt.scatter(combined['saf_s_11'], combined['sat_score'])
plt.title("Correlation Between Safety and SAT Score")
plt.show()


# There appears to be a positive correlation between safety and SAT score though not so strong. There are some schools that have high safety standard and achieve high SAT score and some schools with low safety standard got low SAT score. Majority of the school from the sample falls between the safety score of 6.0 to 7.5 with an average SAT score below 1500. 

# ### Map Safety Score by Districts

# In[17]:


m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

distr = combined.groupby("school_dist").mean()
distr.reset_index(inplace=True)

longitudes = (distr["lon"]).tolist()
latitudes = (distr["lat"]).tolist()
m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True, c=distr["saf_s_11"])
plt.show()


# Brooklyn seems to have better safety score compared to the same for the parts of Manhattan, Queens and Bronx region.  

# ### Evaluate Racial Performance in SAT

# In[18]:


# Listing the races of interest
races = ["white_per", "asian_per", "black_per", "hispanic_per"]
racial_per = combined[races]

# Extracting the coorelation value for the shortlisted races
value_ht = combined.corr()["sat_score"][races]

# Establish plot parameters
x_cor = [1,2,3,4]
random.shuffle(colors_list, random.random)
plt.bar(x_cor, value_ht, width=0.5, align="center", tick_label=races, color=colors_list)
plt.xlim(0,5)
plt.xticks(rotation=90)
plt.title("Correlation of Whites, Asians, Blacks and Hispanics with SAT Score")

plt.show()


# The whites and the Asians are found having strong positive correlation while the Blacks and the Hispanic are found having moderate negative correlation with the SAT score. 
# 
# This is due to the fact that the Hispanic and the Blacks might be coming from the immigrant families. The socio-economic factors, family support and surrounding environment play significant role in overall performance of the students. 

# ### Plot Correlation Between Hispanic Proportion & SAT Score

# In[19]:


plt.scatter(combined['hispanic_per'], combined['sat_score'])
plt.title("Correlation Between Hispanic Percent and SAT Score")

plt.show()


# There seems to be a moderately strong downward trend with the increase of Hispanic Population. Very small portion of population attains a SAT score of 1800 or more while majority falls under the score of 1500. 

# ### Dependency: Low Sat Score & Hispanic Percent

# In[20]:


low_sat_high_hisp = combined[combined["sat_score"] < 1400]
low_sat_high_hisp = low_sat_high_hisp[low_sat_high_hisp["hispanic_per"] > 40]
sat_sc = low_sat_high_hisp["sat_score"].values
hisp_per = low_sat_high_hisp["hispanic_per"].values

plt.scatter(sat_sc, hisp_per)
plt.xlabel("Sat Score")
plt.ylabel("Hispanic Percentage")
plt.title("Correlation Between Hispanic Percent (> 40%) and SAT Score (< 1400)")
print("Correlation Value =", low_sat_high_hisp.corr()["sat_score"]["hispanic_per"])


# Majority of the schools with Hispanic population in the range of 40% - 80% get average SAT score of around 1150. The results become clearly evident when plotted with 40% or more Hispanic Proportion for SAT score of 1400 or less. 
# 
# This is mainly due to the immigrant population along with the socio-economic and demographic factors.

# ### List Schools with Hispanic More Than 95%

# In[21]:


hisp_per_95 = combined[combined["hispanic_per"] > 95]
print(hisp_per_95["SCHOOL NAME"].unique())


# ### List  Schools with Hispanic Less Than 10%

# In[22]:


hisp_10_sat_1800 = combined[combined["hispanic_per"] < 10]
hisp_10_sat_1800 = hisp_10_sat_1800[hisp_10_sat_1800["sat_score"] > 1800]
print(hisp_10_sat_1800["SCHOOL NAME"].unique())


# ### Enlist Schools in NYC with Low Total Enrollment and Low SAT Score

# In[23]:


# Find the school with low enrolllment that get low SAT score
low_enrollment = combined[(combined['total_enrollment'] < 1000) & (combined['sat_score'] < 1000) ]

# Remove rows with invalid school name
low_enrollment = low_enrollment[low_enrollment['School Name'] != 0]

# Print for verification
low_enrollment['School Name']


# ### Plot Correlation Between Sat Score & Gender

# In[24]:


gender = ["male_per", "female_per"]
cor_val = combined.corr()["sat_score"][gender]
x_val = [1, 1.0070]
random.shuffle(colors_list, random.random)

plt.bar(x_val, cor_val, 0.005, align='center', tick_label=gender, color=colors_list)
plt.xlim(0.995,1.011)
plt.ylabel("Correlation Value")
plt.xticks(rotation=90)
plt.title("Correlation Between Gender and SAT Score")
plt.show()


# Female show very weak positive and male show very weak negative correlation for SAT score. This shows the relative performance of female and male students – which is more or less the same. 

# ### High SAT Score & High Female Percentage

# In[25]:


high_sat_n_fem = combined[combined["female_per"] > 50]
high_sat_n_fem = high_sat_n_fem[high_sat_n_fem["sat_score"] > 1500]
print("Schools with SAT > 1500 & Female > 50% =\n", high_sat_n_fem["SCHOOL NAME"].unique())
   
# Plot the scatter diagram 
plt.scatter(combined["sat_score"], combined["female_per"])
plt.xlabel("Sat Score")
plt.ylabel("female_per")
plt.title("Correlation Between Female Percent (> 50%) and SAT Score (> 1500)")

print("\nCorrelation Value between SAT Score and Female Percentage =", high_sat_n_fem.corr()["sat_score"]["female_per"])


# There exists moderately positive correlation between the female proportion and SAT score. While tested for pool of students having more than 50% female proportion and SAT score of greater than 1500, it is observed that around 40% - 65% of the total students attain SAT score in the range of 1000 – 1350. 

# ### SAT Score > 1700 & Female Percentage > 60

# In[26]:


fem_60_sat_1700 = combined[(combined["sat_score"] > 1700) & (combined["female_per"] > 60)]
print("Schools with SAT > 1700 & Female > 60% =\n", fem_60_sat_1700["SCHOOL NAME"].unique())


# ### Relationship Between AP Test Takers & SAT Score

# In[27]:


combined["ap_per"] = combined["AP Test Takers "] / combined["total_enrollment"]
plt.scatter(combined["sat_score"], combined["ap_per"], color='r')
plt.xlabel("Sat Score")
plt.ylabel("AP Test Taker (% of Total Enrolled)")
plt.title("Correlation Between  AP Test Takers and SAT Score")
plt.show()

print("Corrleation value between SAT Score & Percent of AP Test Takers =", combined.corr()["sat_score"]["ap_per"])


# No correlation is found between the AP Test Takers and the SAT score. In fact, up to 40% of the total enrollment who took AP Test scored less than 1400 in SAT. There are few percent of students who took AP Test and secured SAT score of 1800 – 2000. 
# 
# The data about students’ performance in AP Test Vs. SAT could give us more insight to further comment about the AP Test results predictive relevance for SAT score.

# ### Relationship Between Class Size & SAT Score

# In[28]:


plt.scatter(combined["sat_score"], combined["AVERAGE CLASS SIZE"], color='b')
plt.xlabel("Sat Score")
plt.ylabel("Average Class Size")
plt.title("Correlation Between Class Size and SAT Score")
plt.show()

print("Corrleation value between SAT Score & Average Class Size =", combined.corr()["sat_score"]["AVERAGE CLASS SIZE"])


# Moderately strong positive correlation has been observed between the class size and SAT score. Students’ SAT score slowly improves as the class size increases from 20 to 30 students. Majority of the students score between 1000 – 1400 irrespective of class size. However, there are few exceptional cases where the students score beyond 1800.  
# 
# This clearly shows that performance of students in SAT is strongly impacted by his/her class size, higher student-teacher ratio and consequently the dense social environment -which collectively proves to be encouraging for the students.  

# ### Correlation Between Different in Parent, Teacher and Student Responses to Surveys with SAT Score

# #### Listing and Cleaning Data

# In[29]:


# short listing the relevant columns 
surv_col = ['aca_p_11', 'aca_t_11', 'aca_s_11', 'sat_score']
response = combined[surv_col]

# Cleaning the data with null values
response = response.dropna(axis=0, how='any')

# Making sure no null is left
response.isnull().sum().sum()


# #### Develop Survey Response Differrence Data

# In[30]:


# Developing the survey difference response data
response['aca_p_s'] = (response['aca_p_11'] - response['aca_s_11']).abs()
response['aca_p_t'] = (response['aca_p_11'] - response['aca_t_11']).abs()
response['aca_t_s'] = (response['aca_t_11'] - response['aca_s_11']).abs()

# Plot survey response difference
resp_cols = ['aca_p_s', 'aca_p_t', 'aca_t_s']

# Print for verfication
print(response[resp_cols].head())


# #### Correlation Between Parent-Student Survey Difference Response & SAT Score

# In[31]:


pss_cor0 = response.corr()[resp_cols[0]]["sat_score"]
print("\nCorrelation between Parent-Student Survey Response & SAT Score =", 
      pss_cor0)
plt.scatter(response[resp_cols[0]], response["sat_score"])
plt.title("Correlation for Difference between Parent-Student Survey Response and SAT Score")
plt.show()


# It appears that there is a moderately strong negative correlation between the difference in Parent-Student Survey Response and SAT Score. Hence, more similarity of parents and student’s opinion about the latter’s academic expectation, better would it be reflected in to the higher SAT score. In other words, more the disparity between parents and student’s responses for students’ academic expectation score, lower would be the SAT score.  
# 
# This clearly indicates that parental involvement in student’s education results into a better SAT performance and vice versa. 

# #### Correlation Between Parent-Teacher Survey Difference Response & SAT Score

# In[32]:


pss_cor1 = response.corr()[resp_cols[1]]["sat_score"]
print("\nCorrelation between Parent-Teacher Survey Response & SAT Score =", 
      pss_cor1)
plt.scatter(response[resp_cols[1]], response["sat_score"])
plt.title("Correlation for Difference between Parent-Teacher Survey Response and SAT Score")
plt.show()


# There exists weak negative relationship between the difference in parents and teachers’ survey response and SAT score. This indicates that difference of opinion between the parents and the teachers over the expectation of student’s academia has moderately reverse impact over student’s performance in SAT. In other words, less the differences between the parental and teacher’s opinion about student’s academic expectation, moderately better would be student’s performance in SAT. 

# #### Correlation Between Teacher-Student Survey Difference Response & SAT Score

# In[33]:


pss_cor2 = response.corr()[resp_cols[2]]["sat_score"]
print("\nCorrelation between Teacher-Student Survey Response & SAT Score =", 
      pss_cor2)                  
plt.scatter(response[resp_cols[2]], response["sat_score"])
plt.title("Correlation for Difference between Teacher-Student Survey Response and SAT Score")
plt.show()


# No correlation is found between the difference in teachers’ and students’ survey response and SAT score. This indicates that difference of opinion between the teachers and students over the academic expectation for the students have no impact over student’s performance in SAT.

# ### Find out neighborhoods with Best Schools

# #### Determine Top 10 Best School in NYC Based On SAT Score

# In[34]:


# Find the top 10 school based on the SAT score
good_schools = combined[combined['sat_score'] > 1750]
good_schools = good_schools.groupby('DBN').agg('max').sort_values(by='sat_score', ascending=False)
good_schools[['boro', 'sat_score', 'SCHOOL NAME', 'CSD', 'zip']].head(10)


# #### Gathering NYC Property Value Information

# In[35]:


cols = ['Borough', 'CD', 'SchoolDist', 'ZipCode', 'BldgClass', 'price_sf', 'Address', 'OwnerName']
brk_data = pandas.read_csv(r"databank/nyc_property/BK2017V11.csv", usecols = cols)
brx_data = pandas.read_csv(r"databank/nyc_property/BX2017V11.csv", usecols = cols)
mnh_data = pandas.read_csv(r"databank/nyc_property/MN2017V11.csv", usecols = cols)
qns_data = pandas.read_csv(r"databank/nyc_property/QN2017V11.csv", usecols = cols)
snr_data = pandas.read_csv(r"databank/nyc_property/SI2017V11.csv", usecols = cols)
prop_val = pandas.concat([brk_data, brx_data, mnh_data, qns_data, snr_data], axis=0)

# Print for verification
print(prop_val.shape)
prop_val.head(10)


# ### Finding Top 10 Cost Effective Properties for NYC School Neighborhood (2 Deals/School)

# #### Define functions to seggregate residential class

# In[36]:


# Filter data frame for select residential building class 
def usage(char):
    usg = ['A', 'B', 'C', 'D', 'R']
    if char in usg:
        return 1
    else:
        return 0


# #### Define Function to Extract Neighborhood  Details

# In[37]:


# Define function to extract the neighborhood details
def find_property(data, df):
    sch_dst = data[0]
    zip_code = data[1]
    df = df[(df['ZipCode'] == zip_code) & (df['SchoolDist'] == sch_dst)]
    
    count = 0
    j = 0
    k = 0
    m = df.shape[0]
    inp_vals = [([0] * 5) for i in range(2)]
    
    if (m == 0):
        inp_vals[j][k] = data[3]
        inp_vals[j][k+1] = "No Resi. Property Found"
        inp_vals[j][k+2] = "N/A"
        inp_vals[j][k+3] = "N/A"
        inp_vals[j][k+4] = data[2]
        j += 1
        k = 0
        
    elif (m == 1):
        i = 0
        inp_vals[j][k] = data[3]
        inp_vals[j][k+1] = df['Address'].iloc[i]
        inp_vals[j][k+2] = df['OwnerName'].iloc[i]
        inp_vals[j][k+3] = df['price_sf'].iloc[i]
        inp_vals[j][k+4] = data[2]
        j += 1
        k = 0

    else:
        for i in range(m):
            if (count < 2):
                inp_vals[j][k] = data[3]
                inp_vals[j][k+1] = df['Address'].iloc[i]
                inp_vals[j][k+2] = df['OwnerName'].iloc[i]
                inp_vals[j][k+3] = df['price_sf'].iloc[i]
                inp_vals[j][k+4] = data[2]
                j += 1
                k = 0
                count += 1
            elif (count >= 2):
                break
    return inp_vals


# #### Top 10 Cost Effective Neighborhood Properties in NYC for Best Schools (2 choices / school)

# In[38]:


# Set up the data frame per ascending property prices, building class and location zip code
sorted_property = prop_val.sort_values(by=['price_sf', 'BldgClass', 'ZipCode'])
sorted_property['ZipCode'] = pandas.to_numeric(sorted_property['ZipCode'], errors = 'coerce')

# Seggregate data based on the building class for residential properties
sorted_property['Usage'] = sorted_property['BldgClass'].str[:1].apply(usage)
sorted_property = sorted_property[sorted_property['Usage'] == 1]

# Removing null values from the data frame
sorted_property = sorted_property.dropna()

# Extracting Top 10 Best Neighbordhood Data
neighbor = [([0]*5) for i in range(20)]
j = 0
for i in range(10):
    first_row, second_row = find_property(good_schools[['CSD', 'zip', 'SCHOOL NAME', 'boro']].iloc[i], sorted_property)
    for k in range(5):
        neighbor[j][k] = first_row[k]
        neighbor[j+1][k] = second_row[k]
    j += 2

# Set up neighbor data frame for output
cols = ['Borough', 'Property Address', 'Owner', 'Price/Sq Ft', 'Neighborhood School']
great_deal = pandas.DataFrame(columns=cols)

# Feed the final output in the data frame
for i in range(len(neighbor)):
        great_deal[cols[0]] = ([x[0] for x in neighbor])
        great_deal[cols[1]] = ([x[1] for x in neighbor])
        great_deal[cols[2]] = ([x[2] for x in neighbor])
        great_deal[cols[3]] = ([x[3] for x in neighbor])
        great_deal[cols[4]] = ([x[4] for x in neighbor])

# Removing data with missing values and resetting the index
great_deal = great_deal[great_deal['Borough'] != 0]
great_deal.reset_index(inplace=True, drop=True)

# Print the final results results
print("\nList of Least Expensive Neighborhood With Great Schools: \n")
great_deal


# ### Conclusion
•	We are able to know various critical factors that do/do not affect students’ performance in SAT examination. Based on this info, we can verify and validate how fare the current SAT system is for the diverse demographics like NYC. In case we found any flaws in the SAT system for unfair testing performances, we can get better idea about the causes to focus on and fix the system.

•	We understand the impact of various demographic, socio-economic, and current credit and grading system related factors over the performance of students in SAT examination. This helps us to determine and verify how this test maintains balance amongst these factors for overall fairness of test within the widely diverse community. 

•	We are able to determine top 10 best schools based on their average SAT score.

•	We shortlist the least expensive but situated with the top 10 best school neighborhood regions.

•	We could identify the regions of NYC neighborhood where schools do not perform well and understand whether or not there exists any ethnic diversity [to consider] for policy improvement. 

•	We learn the impact of similarity and disparity of students/teachers/parents’ opinion towards student’s academia over the SAT performance. This highlights the roles and responsibilities of various players of the game and its relative significance for the final outcome.

•	Based on the correlations and its severity on students’ SAT score, we can mention that SAT is reasonably fair for the diverse NYC demographics. 