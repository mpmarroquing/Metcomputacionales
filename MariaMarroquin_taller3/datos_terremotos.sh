curl -0 https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv>all_month.csv
awk -F, '{print $2 " " $3}' all_month.csv > locations.txt 
tail -n +2 locations.txt > locationsY.txt
awk -F, '{print $5}' all_month.csv > magnitudes.txt
tail -n +2 magnitudes.txt > magnitudesY.txt
rm all_month.csv 