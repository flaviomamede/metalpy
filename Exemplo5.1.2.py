from metalpy.perfis import PerfilILam
from metalpy.material import Aco

#Unidades para conversão
cm_to_in = 0.394
ft_to_cm = 30.48
cm_to_ft = 1/ft_to_cm
ksi_to_kN_cm2 = 0.6894
kN_to_kips = 0.225
kNcm_to_kipft = kN_to_kips * (1/ft_to_cm)

#Definição do Aço com as propriedades em ksi sendo convertidas para kN/cm²
E = 29000 * ksi_to_kN_cm2
fy = 50 * ksi_to_kN_cm2
fu = 65 * ksi_to_kN_cm2
v = 0.3

#Definindo um aço ASTM A992 em unidades de kN/cm²
A992 = Aco(E, v, fy, fu, 0.6)

#Definindo um perfil W360X122 com as propriedades em cm
W360X122 = PerfilILam('W360X122', A992, und='cm', norma='AISC360')

#Respostas com Metalpy
#Propriedades geométricas do perfil
A = W360X122.A * cm_to_in ** 2 #área do perfil
Wx = W360X122.Wx * cm_to_in**3 #módulo elástico em relação ao eixo X
Zx = W360X122.Zx * cm_to_in**3 #módulo plástico em relação ao eixo X
Wy = W360X122.Wy * cm_to_in**3 #módulo elástico em relação ao eixo Y
Zy = W360X122.Zy * cm_to_in**3 #módulo plástico em relação ao eixo X
Iy = W360X122.Iy * cm_to_in**4 #momento de inércia em relação ao eixo Y

# Calculando a força de tração resistente de cálculo de acordo com o ELU
# de escoamento da seção bruta
mp_Ntrd = W360X122.Ntrd_brt() * kN_to_kips

# Calculando o momento resistente Mx e obtendo os dados de cálculo
Cbx = 1.41
Lbx = 30 * ft_to_cm
Mrdx, dados_Mrdx = W360X122.Mrdx(Lb = Lbx, Cb = Cbx, data=True)
Mrdx = Mrdx * kNcm_to_kipft
Lp = dados_Mrdx.FLT.Lp * cm_to_ft
Lr = dados_Mrdx.FLT.Lr * cm_to_ft

# Calculando o momento resistente My
Mrdy = W360X122.Mrdy(Lb = 0, Cb=1) * kNcm_to_kipft

# Verificação a flexo-tração
Nsd = 174 / kN_to_kips
Msdx = 192 / kNcm_to_kipft
Msdy = 67.6 / kNcm_to_kipft

mp_verif = W360X122.verif_NM(Nsd, Msdx, Msdy, Lbx= 30 * ft_to_cm, Cb=1.41,\
klx=1, kly=Lbx, klz=1)