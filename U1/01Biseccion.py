# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: BISECCION
# FECHA: 16 DE ENERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

'''
CAMBIAR EL CODIGO DE C++ A PYTHON 

#include <math.h>    // math.h
#include <iomanip>  // setprecision(), setw()
#include <iostream>
using namespace std;

double fnEcuacion(double valor) { return pow(valor, 2) - 2; }

int main(int argc, char const *argv[]) {
    double x1 = 1;
    double x2 = 2;
    double xm;
    double Es = 0.001;          // Error Standard o Absoluto
    double Er = abs(x2-x1);     // Error Relativo
    int i = 1;
    double it = round((log(x2 - x1) - log(Es)) / log(2));
    cout << it << endl;
    /*
    cout << "i" << "\t" << "x1" << "\t" << "x2" <<"\t" << "Er" <<"\t" << "xm"
         << "\t" << "fnEc(x1)" << "\t" << "fnEc(xm)" << endl;
    */     
    printf("i   |     x1    |     x2    |      Er   |     xm    |" \
           "   f(x1)   |   f(xm)   | f(x1) * f(xm) |\n");
    while (Er >= Es) {
        xm = (x1 + x2) / 2;
        /*
        cout << fixed << left << setprecision(4) << i << "\t" << x1 << "\t"
             << x2 << "\t" << Er << "\t" << xm << "\t" << fnEcuacion(x1) << "\t"
             << fnEcuacion(xm) << endl;
        */   
       printf("%3d |%10.4f |%10.4f |%10.4f |%10.4f |%10.4f |%10.4f \n",
               i, x1, x2, Er, xm,  fnEcuacion(x1), fnEcuacion(xm));
        if (fnEcuacion(x1) * fnEcuacion(xm) < 0) {
            x2 = xm;
        } else {
            x1 = xm;
        }
        Er = abs(x2 - x1);
        i = i + 1;
    }
    cout << xm << endl;
    return 0;
}
'''
#libreria
import math as ma

'''
pow => elevar
abs => valor absoluto
round => redondear

'''
x1 = 1
x2 = 2
xm = None #Ausencia de valor 
Es = 0.001 #Error Standard o Absoluto
Er = abs(x2-x1) #Error Relativo
i = 1
it = round((ma.log(x2 - x1) - ma.log(Es)) / ma.log(2))
print(it)

'''
ejemplo: C++
 cout << "i" << "\t" << "x1" << "\t" << "x2" <<"\t" << "Er" <<"\t" << "xm"
         << "\t" << "fnEc(x1)" << "\t" << "fnEc(xm)" << endl;
'''
#TABALA (columnas y filas)
print("i         |    x1     |    x2     |    Er    |    xm    |    f(x1)    |    f(xm)     |    f(x1) * f(xm)   |")

#Solución 
def potencia(num):
    return pow(num,2)-2

'''

Al no crear >potencia< la formula quedaria así 
=>  (((x1 * 2) - 2) * ((xm * 2) - 2) < 0): 

'''
while (Er >= Es): 
        xm = (x1 + x2) / 2
        print(i,round(x1,4), round(x2,4), round(Er,4), round(xm,4), round(potencia(x1),4), round(potencia(xm),4), round((potencia(x1)*potencia(xm)),4), sep= "\t|")
        if(potencia(x1)* potencia(xm) < 0):
            x2 = xm
        else:
            x1 = xm                                                  
        Er = abs(x2 - x1)
        i = i + 1 # O i += 1 

print("The result is: ", xm)