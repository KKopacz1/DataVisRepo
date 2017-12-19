

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
```


```python
#import data from csv
city_csv = "city_data.csv"
ride_csv = "ride_data.csv"
city_df = pd.read_csv(city_csv)
ride_df = pd.read_csv(ride_csv)
```


```python
#view data frames
city_df.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
ride_df.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
pyber_summary = pd.merge(city_df, ride_df, on="city", how="left")
pyber_summary.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-19 04:27:52</td>
      <td>5.51</td>
      <td>6246006544795</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-04-17 06:59:50</td>
      <td>5.54</td>
      <td>7466473222333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-05-04 15:06:07</td>
      <td>30.54</td>
      <td>2140501382736</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-01-25 20:44:56</td>
      <td>12.08</td>
      <td>1896987891309</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
      <td>2016-08-09 18:19:47</td>
      <td>17.91</td>
      <td>8784212854829</td>
    </tr>
  </tbody>
</table>
</div>




```python
#find values for average fare and number of rides
bubble_plot_df_1 = pyber_summary.groupby(["type", "city"],as_index=True).mean()["fare"].to_frame().reset_index()
bubble_plot_df_2 = pyber_summary.groupby(["type", "city"],as_index=True).count()["ride_id"].to_frame().reset_index()
bubble_plot_df = pd.merge(bubble_plot_df_1, bubble_plot_df_2,
                         on=["type", "city"])
bubble_plot_df.head()
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
      <th>type</th>
      <th>city</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rural</td>
      <td>East Leslie</td>
      <td>33.660909</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rural</td>
      <td>East Stephen</td>
      <td>39.053000</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rural</td>
      <td>East Troybury</td>
      <td>33.244286</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rural</td>
      <td>Erikport</td>
      <td>30.043750</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rural</td>
      <td>Hernandezshire</td>
      <td>32.002222</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#set size of bubbles
size = 5*city_df.groupby(["type", "city"], as_index=True).sum()["driver_count"]
```


```python
#create scatter plot
sns.lmplot(x="ride_id", y="fare", data=bubble_plot_df,
          fit_reg=False, hue="type", legend_out=False,
          size=5,scatter_kws={"s": size, 'linewidths':1, 'edgecolor':'black'},
          palette=dict(Rural="gold", Suburban="lightskyblue", Urban="lightcoral"))
plt.legend(title="City Types", loc="best", markerscale=0.5, edgecolor="black")
plt.grid(linestyle="dotted")
plt.xlim(0,70)
plt.ylim(10,60)
plt.title("Pyber Ride Data (2016)", fontsize=15)
plt.xlabel("Number of Riders Per City")
plt.ylabel("Average Fare ($)")

plt.show()
```


![png](output_7_0.png)



```python
#total fares by city type
labels = ["Rural", "Suburban", "Urban"]
sizes = pyber_summary.groupby(["type"], as_index=False).sum()["fare"].tolist()
colors = ["gold", "lightskyblue", "lightcoral"]
explode = (0,0,0.2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct="%1.1f%%", shadow=True, startangle=120)
plt.axis("off")
plt.title("% of Fare by City Type", fontsize=15)
plt.show()
```


![png](output_8_0.png)



```python
#total rides by city
labels = ["Rural", "Suburban", "Urban"]
sizes = pyber_summary.groupby(["type"], as_index=False).count()["ride_id"].tolist()
colors = ["gold", "lightskyblue", "lightcoral"]
explode = (0,0,0.2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct="%1.1f%%", shadow=True, startangle=120)
plt.axis("off")
plt.title("% of Total Rides by City Type", fontsize=15)
plt.show()
```


![png](output_9_0.png)



```python
#total drivers by city type
labels = ["Rural", "Suburban", "Urban"]
sizes = pyber_summary.groupby(["type"], as_index=False).sum()["driver_count"].tolist()
colors = ["gold", "lightskyblue", "lightcoral"]
explode = (0,0,0.2)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
       autopct="%1.1f%%", shadow=True, startangle=120)
plt.axis("off")
plt.title("% of Total Rides by City Type", fontsize=15)
plt.show()
```


![png](output_10_0.png)

