mkdir Tolima
cd Tolima
touch PlotsTolima.py
grep March DatosTolima.dat > DatosMarzoP.txt
awk '{if ($1 ~ /^20/) print $5 " " $7; else print $4 " " $6}' DatosMarzoP.txt > DatosMarzo.txt
awk '{if ($1 ~ /^20/) print $5 " " $7; else print $4 " " $6}' DatosTolima.dat > GRF_vs_EQP.txt
tail -n +2 GRF_vs_EQP.txt > GRF_vs_EQ.txt

python PlotsTolima.py

rm DatosTolima.dat