curl -0 http://www-bcf.usc.edu/~gareth/ISL/Credit.csv>Credit.csv

awk -F, '{print $2 " " $3 " " $4 " " $5 " " $6 " " $7 " " $12}' Credit.csv > DataCreditT.csv

tail -n +2 DataCreditT.csv > DataCredit.csv

rm DataCreditT.csv