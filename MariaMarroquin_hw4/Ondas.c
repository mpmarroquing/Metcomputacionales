#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int extremos_sueltos(void);
int tambor(void);

int main(void){
	
	extremos_sueltos();
	tambor();
	//leer archivos
	FILE * c_i;
	FILE * datos = fopen("datos_cuerda_ef.dat","w");
	int t=129.0;
	int i;
	float * x = malloc(t*sizeof(float)); 
	float * y = malloc(t*sizeof(float)); 
	float * y_nuevo = malloc(t*sizeof(float)); 
	float * y_presente = malloc(t*sizeof(float)); 
	float * y_pasado = malloc(t*sizeof(float)); 
	
	
	c_i = fopen("cond_ini_cuerda.dat","r");
	
	for (i=0; i<t; i++){
		fscanf(c_i, "%f %f\n" , &x[i], &y[i]);
		
		}
	fclose(c_i);	
	

	double c=250.0;
	double dt=pow(10,-5);
	double dx=x[1]-x[0];
	int n=100000.0;
	int m=129.0;
	double r=c*(dt/dx);
	//printf("%f\n",dx);
	
	int j;
	int a;
	int s;
	
	//Avance (n=100000, parametro)	

		for (s=1; s<m-1; s++){
			y_nuevo[0] = y[0];
			y_nuevo[m-1] = y[m-1];	
			
			y_nuevo[s]= y[s] + (pow(r,2)/2)*(y[s+1]-2.0*y[s]+y[s-1]);
				
					}
					
				for(a=0; a<m; a++){	
					y_pasado[a]=y[a];
					y_presente[a]=y_nuevo[a];				
			
				}
			
		for (j=0;j<n;j++){
		
		fprintf(datos,"%f\n",y_nuevo[0]);
		
			for (s=1; s<m-1; s++){
				
				y_nuevo[s]=(2.0*(1.0-pow(r,2))*y_presente[s]-y_pasado[s]+pow(r,2)*(y_presente[s+1]+y_presente[s-1]));
				fprintf(datos,"%f\n",y_nuevo[s]);
			}
			
			for(a=0; a<m; a++){	
					y_pasado[a]=y_presente[a];
					y_presente[a]=y_nuevo[a];				
			
				}
		
		fprintf(datos,"%f\n",y_nuevo[m-1]);
		}
			
return 0;

	}

int extremos_sueltos(void){

	
	FILE * datos2 = fopen("datos_cuerda_es.dat","w");
	int T=129.0;
	int i;
	int s;
	int a;
	int j;
	float pi=3.1415;
	float l=0.64;
	double c=250.0;
	
	double dt=pow(10,-5);
	double dx=0.005;
	int n=100000.0;
	int m=129.0;
	double r=c*(dt/dx);
	float * y = malloc(T*sizeof(float)); 
	float * y_nuevo = malloc(T*sizeof(float)); 
	float * y_presente = malloc(T*sizeof(float)); 
	float * y_pasado = malloc(T*sizeof(float));
	
	
//cuerda con amplitud cero en t=0
	for (i=0; i<m; i++){
		y[i]=0.0;
		//printf("%f\n", y[i]); 
	}

//primera amplitud despues de 0
	for (s=1; s<m-1; s++){
			
			y_nuevo[s]= y[s] + (pow(r,2)/2)*(y[s+1]-2.0*y[s]+y[s-1]);
				
					}
					
				for(a=0; a<m; a++){	
					y_pasado[a]=y[a];
					y_presente[a]=y_nuevo[a];				
				}
			
			
//todas las demás amplitudes
		for (j=0;j<n;j++){
			
				
			y_nuevo[0] = y[0];
			fprintf(datos2,"%f\n",y_nuevo[0]);
			double t = j*dt;
			y_nuevo[m-1] = sin(((2*pi*c)/l)*t);
			fprintf(datos2,"%f\n",y_nuevo[m-1]);
		
			for (s=1; s<m-1; s++){
			
				
				y_nuevo[s]=(2.0*(1.0-pow(r,2))*y_presente[s]-y_pasado[s]+pow(r,2)*(y_presente[s+1]+y_presente[s-1]));
				fprintf(datos2,"%f\n",y_nuevo[s]);
				
			}
			
			for(a=0; a<m; a++){	
			
					
					y_pasado[a]=y_presente[a];
					y_presente[a]=y_nuevo[a];				
			
				}
			
			
		}
	

	return 0;
	}
	
int tambor(void){

	FILE * t_i;
	FILE * datos3 = fopen("datos_tambor.dat","w");
	t_i = fopen("cond_ini_tambor.dat","r");
	int t = 101.0;
	int i;
	int j;
	float matriz[t][t];
	float matriz_nueva[t][t];
	float matriz_presente[t][t];
	float matriz_pasado[t][t];
	
	//condiciones iniciales de perturbación
	for (i=0; i<t; i++){
		for (j=0; j<t; j++){
			fscanf(t_i, "%f\n" , &matriz[i][j]);
		}
			}
	fclose(t_i);
	
	
	
	float c=250.0;
	float l=0.5;
	double dt=pow(10,-5);
	double dx=0.005;
	double dy=0.005;
	int n=100000.0;
	int m=101.0;
	double rx=c*(dt/dx);
	double ry=c*(dt/dy);
	//printf("%f\n",dx);
	 
	int a;
	int s;
	
	//primera amplitud despues de 0
	for (s=1; s<m-1; s++){
			for(i=1; i<m-1; i++){
			
			matriz_nueva[s][i]= matriz[s][0] + (pow(rx,2)/2)*(matriz[0][i]-2.0*matriz[s][0]+matriz[0][i-1]) + matriz[0][i] + (pow(ry,2)/2)*(matriz[0][i+1]-2.0*matriz[0][i]+matriz[0][i+1]);
				
						}
					}
					
				for(a=0; a<m; a++){	
					for(j=0; j<m; j++){
						matriz_pasado[a][j]=matriz[a][j];
						matriz_presente[a][j]=matriz_nueva[a][j];				
				}
					}
			
			
	//todas las demás amplitudes
		for (j=0;j<n;j++){
			
				
			matriz_nueva[0][0] = matriz[0][0];
			matriz_nueva[m-1][m-1] = l;
			fprintf(datos3,"%f\n",matriz_nueva[0][0]);
		
			fprintf(datos3,"%f\n",matriz_nueva[m-1][m-1]);
		
			for (s=1; s<m-1; s++){
				for (i=0;i<n;i++){
				
				matriz_nueva[s][i]=(2.0*(1.0-pow(rx,2))*matriz_presente[s][i]-matriz_pasado[s][i]+pow(rx,2)*(matriz_presente[s+1][i+1]+matriz_presente[s-1][i-1])) + (2.0*(1.0-pow(ry,2))*matriz_presente[s][i]-matriz_pasado[s][i]+pow(ry,2)*(matriz_presente[s+1][i+1]+matriz_presente[s-1][i-1]));
				fprintf(datos3,"%f\n",matriz_nueva[s][i]);
				
			}
			
			for(a=0; a<m; a++){	
				for(j=0; j<m; j++){	
					
					matriz_pasado[a][j]=matriz_presente[a][j];
					matriz_presente[a][j]=matriz_nueva[a][j];				
			
					}
				}
			
			}
		}
	
	return 0;
}