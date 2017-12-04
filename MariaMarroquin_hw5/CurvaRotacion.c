#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int likelihood(float * V_obs, float * V_model);
int modelo(float R, float Mb, float Md, float Mh);


	
int main(void){
	
	
	FILE * datos = fopen ("modelo.txt","w");
	FILE * data = fopen("RadialVelocities.dat","r");
	int t = 300.0;
	float * R = malloc(t*sizeof(float));
	float * V_obs = malloc(t*sizeof(float));
	float * V_model = malloc(t*sizeof(float));
	float * Mb_walk = malloc(1000*sizeof(float));
	float * Md_walk = malloc(1000*sizeof(float));
	float * Mh_walk = malloc(1000*sizeof(float));
	float * l_walk = malloc(1000*sizeof(float));
	
	
	
	
	int i;
	int j;
	
	for (i=0; i<t; i++){
		fscanf(data, "%f %f\n", &R[i], &V_obs[i]);
		printf("%f %f\n",R[i],V_obs[i]);
	}
	fclose(data);
	
	Mb_walk[0] = drand48();
	Md_walk[0] = drand48();
	Mh_walk[0] = drand48();
	l_walk[0] = likelihood(V_obs, V_model);
	
	V_init=modelo(R,Mb_walk[0],Md_walk[0],Mh_walk[0])
	
	n = 1000;	//Numero de iteraciones
	
	for (j=0; j<n; j++){
	
		//definir Gaussiana
		Mb_prime = 
		Md_prime = 
		Mh_prime = 
		
		
		
		//revaluar el modelo
		V_init = modelo(R, Mb[j], Md[j], Mh[j]);
		V_prime = modelo(R, Mb_prime, Md_prime, Mh_prime);
		
		l_prime = likelihood(V_obs, V_prime);
		l_init = likelihood(V_obs, V_init);
		
		//definir alpha y beta
		
		float alpha = l_prime/l_init;
		if (alpha>=1.0){
		
			Mb_walk[j+1] = Mb_prime;
			Md_walk[j+1] = Md_prime;
			Mh_walk[j+1] = Mh_prime;
		
			}else{
				float beta = drand48();
					if(alpha>=beta) {
						Mb_walk[j+1] = Mb_prime;
						Md_walk[j+1] = Md_prime;
						Mh_walk[j+1] = Mh_prime;
					}else{
						Mb_walk[j+1] = Mb_walk[j];
						Md_walk[j+1] = Md_walk[j];
						Mh_walk[j+1] = Mh_walk[j];

					}		
		}
		printf("%f %f %f\n",Mb_walk[j],Md_walk[j],Mh_walk[j]);
		fprintf(datos,"%f\n",modelo(R,Mb_walk[j],Md_walk[j],Mh_walk[j]));
	}
	
	
return 0;
}


int likelihood(float * V_obs, float * V_model){
	
	int j;
	
	float sumaV = 0.0;
	for (j=0; j<300.0; j++){
		
		float * sum = malloc(300*sizeof(float));
		sum[j] = V_obs[j] + V_model[j]; 
	 	sumaV = sum[j] + sumaV;
	}
	
	float chi_s = (1.0/2.0)*pow((sumaV),2);
	
	return chi_s; 
}
	
int modelo(float R, float Mb, float Md, float Mh){	
	
	float model = 0.0;
	float bb = 0.2497;
	float bd = 5.16;
	float ad = 0.3105;
	float ah = 64.3;

	float A = pow(R,2) + pow(bb,2);
	float B = pow(R,2) + pow(bd + ad,2);
	float C = pow(R,2) + pow(ah,2);
	
	int j;
	
		model = (sqrt(Mb)*R)/pow(A,3/4) + (sqrt(Md)*R)/pow(B,3/4) + (sqrt(Mh)*R)/pow(C,1/4);
	
	
	return model;
}