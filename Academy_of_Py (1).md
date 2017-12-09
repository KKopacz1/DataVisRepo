

```python
import pandas as pd
```


```python
#load csv
schools_complete = "schools_complete.csv"
students_complete = "students_complete.csv"
```


```python
#read with pandas
schools_complete_pd = pd.read_csv(schools_complete, encoding="iso-8859-1", low_memory=False)
students_complete_pd = pd.read_csv(students_complete,encoding="iso-8859-1", low_memory=False)
```


```python
schools_complete_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_complete_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_schools = schools_complete_pd["School ID"].count()
total_schools
```




    15




```python
total_students = schools_complete_pd["size"].sum()
total_students
```




    39170




```python
total_budget = schools_complete_pd["budget"].sum()
total_budget
```




    24649428




```python
average_math_score = students_complete_pd["math_score"].mean()
average_math_score
```




    78.98537145774827




```python
average_reading_score = students_complete_pd["reading_score"].mean()
average_reading_score
```




    81.87784018381414




```python
number_passing_math = students_complete_pd["math_score"].loc[(students_complete_pd["math_score"] > 60)].count()
percent_passing_math = (number_passing_math/total_students)*100
percent_passing_math
```




    90.906305846310957




```python
number_passing_reading = students_complete_pd["reading_score"].loc[(students_complete_pd["reading_score"] > 60)].count()
percent_passing_reading = (number_passing_reading/total_students)*100
percent_passing_reading
```




    100.0




```python
overall_passing_rate = (percent_passing_math + percent_passing_reading)/2
overall_passing_rate
```




    95.453152923155471




```python
district_summary_pd = pd.DataFrame([[total_schools,
                               total_students,
                               total_budget,
                               average_math_score,
                               average_reading_score,
                               percent_passing_math,
                               percent_passing_reading,
                               overall_passing_rate]],
                             columns=["Total Schools",
                                     "Total Students",
                                     "Total Budget",
                                     "Average Math Score",
                                     "Average Reading Score",
                                     "Percent Passing Math",
                                     "Percent Passing Reading",
                                     "Overall Passing Rate"])
district_summary_pd
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>90.906306</td>
      <td>100.0</td>
      <td>95.453153</td>
    </tr>
  </tbody>
</table>
</div>




```python
#make distric dataframe
schools_complete_pd = schools_complete_pd.rename(columns={"name":
                                                         "school"})
school_summary = pd.merge(schools_complete_pd, students_complete_pd,
                         on="school",how="outer").groupby(["school"],
                                                         as_index=True)
```


```python
#calculate and storing per school budget info
school_type = school_summary["type"].unique().str.get(0)
total_school_budget = school_summary["budget"].unique().str.get(0)
total_school_students = school_summary.count()["Student ID"]
per_student_budget = total_school_budget/total_school_students
```


```python
#calculate and storing grades
school_math_score = school_summary.mean()["math_score"]
school_reading_score = school_summary.mean()["reading_score"]
count_percent_passing_math = students_complete_pd.loc[students_complete_pd["math_score"]>=70,:].groupby([students_complete_pd["school"]],as_index=True).count()["math_score"]
percent_passing_math_school=round(count_percent_passing_math*100/total_school_students,2)
count_percent_passing_reading = students_complete_pd.loc[students_complete_pd["reading_score"]>=70,:].groupby([students_complete_pd["school"]],as_index=True).count()["reading_score"]
percent_passing_reading_school = round(count_percent_passing_reading*100/total_school_students,2)
percent_overall_passing_school = (percent_passing_math_school + percent_passing_reading_school)/2
```


```python
#make new dataframe
school_summary_df = pd.DataFrame({"School Type": school_type,
                                 "Total_Students": total_school_students,
                                 "Total Budget": total_school_budget,
                                 "Per Student Budget": per_student_budget,
                                 "Percent Passing Math": percent_passing_math_school,
                                 "Percent Passing Reading": percent_passing_reading_school,
                                 "Overall Passing Rate": percent_overall_passing_school})
school_summary_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>School Type</th>
      <th>Total Budget</th>
      <th>Total_Students</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>74.305</td>
      <td>628.0</td>
      <td>66.68</td>
      <td>81.93</td>
      <td>District</td>
      <td>3124928</td>
      <td>4976</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>95.585</td>
      <td>582.0</td>
      <td>94.13</td>
      <td>97.04</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>73.365</td>
      <td>639.0</td>
      <td>65.99</td>
      <td>80.74</td>
      <td>District</td>
      <td>1884411</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>73.805</td>
      <td>644.0</td>
      <td>68.31</td>
      <td>79.30</td>
      <td>District</td>
      <td>1763916</td>
      <td>2739</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>95.265</td>
      <td>625.0</td>
      <td>93.39</td>
      <td>97.14</td>
      <td>Charter</td>
      <td>917500</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>73.805</td>
      <td>652.0</td>
      <td>66.75</td>
      <td>80.86</td>
      <td>District</td>
      <td>3022020</td>
      <td>4635</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>94.380</td>
      <td>581.0</td>
      <td>92.51</td>
      <td>96.25</td>
      <td>Charter</td>
      <td>248087</td>
      <td>427</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>73.500</td>
      <td>655.0</td>
      <td>65.68</td>
      <td>81.32</td>
      <td>District</td>
      <td>1910635</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>73.640</td>
      <td>650.0</td>
      <td>66.06</td>
      <td>81.22</td>
      <td>District</td>
      <td>3094650</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>95.270</td>
      <td>609.0</td>
      <td>94.59</td>
      <td>95.95</td>
      <td>Charter</td>
      <td>585858</td>
      <td>962</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>73.295</td>
      <td>637.0</td>
      <td>66.37</td>
      <td>80.22</td>
      <td>District</td>
      <td>2547363</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>94.860</td>
      <td>600.0</td>
      <td>93.87</td>
      <td>95.85</td>
      <td>Charter</td>
      <td>1056600</td>
      <td>1761</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>95.290</td>
      <td>638.0</td>
      <td>93.27</td>
      <td>97.31</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>1635</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>95.205</td>
      <td>578.0</td>
      <td>93.87</td>
      <td>96.54</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>2283</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>94.970</td>
      <td>583.0</td>
      <td>93.33</td>
      <td>96.61</td>
      <td>Charter</td>
      <td>1049400</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>




```python
#sort top performing schools
top_performing_schools = school_summary_df.sort_values("Overall Passing Rate", ascending=False).head()
top_performing_schools
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>School Type</th>
      <th>Total Budget</th>
      <th>Total_Students</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>95.585</td>
      <td>582.0</td>
      <td>94.13</td>
      <td>97.04</td>
      <td>Charter</td>
      <td>1081356</td>
      <td>1858</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>95.290</td>
      <td>638.0</td>
      <td>93.27</td>
      <td>97.31</td>
      <td>Charter</td>
      <td>1043130</td>
      <td>1635</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>95.270</td>
      <td>609.0</td>
      <td>94.59</td>
      <td>95.95</td>
      <td>Charter</td>
      <td>585858</td>
      <td>962</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>95.265</td>
      <td>625.0</td>
      <td>93.39</td>
      <td>97.14</td>
      <td>Charter</td>
      <td>917500</td>
      <td>1468</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>95.205</td>
      <td>578.0</td>
      <td>93.87</td>
      <td>96.54</td>
      <td>Charter</td>
      <td>1319574</td>
      <td>2283</td>
    </tr>
  </tbody>
</table>
</div>




```python
#bottom performing school
bottom_performing_schools = school_summary_df.sort_values("Overall Passing Rate", ascending=True).head()
bottom_performing_schools
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Overall Passing Rate</th>
      <th>Per Student Budget</th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>School Type</th>
      <th>Total Budget</th>
      <th>Total_Students</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>73.295</td>
      <td>637.0</td>
      <td>66.37</td>
      <td>80.22</td>
      <td>District</td>
      <td>2547363</td>
      <td>3999</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>73.365</td>
      <td>639.0</td>
      <td>65.99</td>
      <td>80.74</td>
      <td>District</td>
      <td>1884411</td>
      <td>2949</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>73.500</td>
      <td>655.0</td>
      <td>65.68</td>
      <td>81.32</td>
      <td>District</td>
      <td>1910635</td>
      <td>2917</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>73.640</td>
      <td>650.0</td>
      <td>66.06</td>
      <td>81.22</td>
      <td>District</td>
      <td>3094650</td>
      <td>4761</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>73.805</td>
      <td>644.0</td>
      <td>68.31</td>
      <td>79.30</td>
      <td>District</td>
      <td>1763916</td>
      <td>2739</td>
    </tr>
  </tbody>
</table>
</div>




```python
#math scores by grade
school_grade_grouped = students_complete_pd.groupby([students_complete_pd["school"],
                                                    students_complete_pd["grade"]],
                                                   as_index=False)
math_scores_per_grade = school_grade_grouped["math_score"].mean()

school_names_math = []
math_grade_9th_grade = []
math_grade_10th_grade = []
math_grade_11th_grade = []
math_grade_12th_grade =[]

for school in math_scores_per_grade["school"].unique():
    school_name=school
    school_names_math.append(school_name)
    index=school_names_math.index(school)
    math_grade_9th_grade.insert(index,round(math_scores_per_grade.loc[(math_scores_per_grade["school"]==school) &
                                                                     (math_scores_per_grade["grade"]=="9th"),"math_score"].values[0],2))
    math_grade_10th_grade.insert(index,round(math_scores_per_grade.loc[(math_scores_per_grade["school"]==school) &
                                                                     (math_scores_per_grade["grade"]=="10th"),"math_score"].values[0],2))
    math_grade_11th_grade.insert(index,round(math_scores_per_grade.loc[(math_scores_per_grade["school"]==school) &
                                                                     (math_scores_per_grade["grade"]=="11th"),"math_score"].values[0],2))
    math_grade_12th_grade.insert(index,round(math_scores_per_grade.loc[(math_scores_per_grade["school"]==school) &
                                                                     (math_scores_per_grade["grade"]=="12th"),"math_score"].values[0],2))

math_by_grade_df = pd.DataFrame({"School Name": school_names_math,
                                "9th Grade": math_grade_9th_grade,
                                "10th Grade": math_grade_10th_grade,
                                "11th Grade": math_grade_11th_grade,
                                "12th Grade": math_grade_12th_grade,})

math_by_grade_df.set_index("School Name", inplace=True)

math_by_grade_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
      <th>9th Grade</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
      <td>77.08</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
      <td>83.09</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
      <td>76.40</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
      <td>77.36</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
      <td>82.04</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
      <td>77.44</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
      <td>77.03</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
      <td>83.63</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
      <td>83.42</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
      <td>83.59</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
      <td>83.09</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
      <td>83.26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#reading scores by grade
school_grade_grouped_2 = students_complete_pd.groupby([students_complete_pd["school"],
                                                    students_complete_pd["grade"]],
                                                   as_index=False)
reading_scores_per_grade = school_grade_grouped_2["reading_score"].mean()

school_names_reading = []
reading_grade_9th_grade = []
reading_grade_10th_grade = []
reading_grade_11th_grade = []
reading_grade_12th_grade =[]

for school in reading_scores_per_grade["school"].unique():
    school_name=school
    school_names_reading.append(school_name)
    index=school_names_reading.index(school)
    reading_grade_9th_grade.insert(index,round(reading_scores_per_grade.loc[(reading_scores_per_grade["school"]==school) &
                                                                     (reading_scores_per_grade["grade"]=="9th"),"reading_score"].values[0],2))
    reading_grade_10th_grade.insert(index,round(reading_scores_per_grade.loc[(reading_scores_per_grade["school"]==school) &
                                                                     (reading_scores_per_grade["grade"]=="10th"),"reading_score"].values[0],2))
    reading_grade_11th_grade.insert(index,round(reading_scores_per_grade.loc[(reading_scores_per_grade["school"]==school) &
                                                                     (reading_scores_per_grade["grade"]=="11th"),"reading_score"].values[0],2))
    reading_grade_12th_grade.insert(index,round(reading_scores_per_grade.loc[(reading_scores_per_grade["school"]==school) &
                                                                     (reading_scores_per_grade["grade"]=="12th"),"reading_score"].values[0],2))

reading_by_grade_df = pd.DataFrame({"School Name": school_names_reading,
                                "9th Grade": reading_grade_9th_grade,
                                "10th Grade": reading_grade_10th_grade,
                                "11th Grade": reading_grade_11th_grade,
                                "12th Grade": reading_grade_12th_grade,})

reading_by_grade_df.set_index("School Name", inplace=True)

reading_by_grade_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10th Grade</th>
      <th>11th Grade</th>
      <th>12th Grade</th>
      <th>9th Grade</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
      <td>81.30</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
      <td>83.68</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
      <td>81.20</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
      <td>80.63</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
      <td>83.37</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
      <td>80.87</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
      <td>83.68</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
      <td>81.29</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
      <td>81.26</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
      <td>83.81</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
      <td>80.99</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
      <td>83.73</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
      <td>83.94</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
      <td>83.83</td>
    </tr>
  </tbody>
</table>
</div>




```python
#score by school size
bins = [0, 1750, 3500, 5000]
label_value = ["Small (Less Than 1750)", "Medium (1750-3500)", "Large (3500-5000)"]

school_summary_df["Total_Students"]=pd.cut(school_summary_df["Total_Students"], bins, labels=label_value)
size_school_summary = school_summary_df.groupby("Total_Students", as_index=False).mean()

size_school_summary.set_index("Total_Students", inplace=True)

size_school_summary=size_school_summary[["Average Math Score",
                                        "Average Reading Score"
                                        "Percent Passing Math"
                                        "Percent Passing Reading"
                                        "Overall Passing Rate"]]

size_school_summary
```


```python
#Scores by School Type

school_type_summary=school_summary_df.groupby("School Type",as_index=False).mean()

school_type_summary.set_index("School Type",inplace=True)

school_type_summary=school_type_summary[["Percent Passing Math",
                                        "Percent Passing Reading",
                                        "Overall Passing Rate"]]

school_type_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percent Passing Math</th>
      <th>Percent Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>93.620000</td>
      <td>96.586250</td>
      <td>95.103125</td>
    </tr>
    <tr>
      <th>District</th>
      <td>66.548571</td>
      <td>80.798571</td>
      <td>73.673571</td>
    </tr>
  </tbody>
</table>
</div>


