from metalpy.perfis import TuboCir
from metalpy.material import Aco

#Definindo variáveis para conversão

in_to_cm = 2.54
cm_to_in = 0.394
kN_cm2_to_ksi = 1.45
kN_to_kips = 0.225

#Definição do Aço com as propriedades em kN/cm²

A500 = Aco(20000, 0.3, 31.7, 43.0, 0.6)

#Criando uma instancia do perfil TuboCir

tubo40 = TuboCir('HSS406.4X9.5', A500, und='cm', norma='AISC360')

#Respostas com Metalpy

A = tubo40.A * cm_to_in ** 2
esb = tubo40.esb



# Calculando o momento resistente de cálculo e obtendo os dados do cálculo

Lv = 192 * in_to_cm
Vrd, dados = tubo40.Vrdy(Lv = Lv, data=True)
Fcr = dados.Fcr * kN_cm2_to_ksi
Vrd = Vrd * kN_to_kips