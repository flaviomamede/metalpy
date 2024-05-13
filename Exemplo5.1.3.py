from metalpy.perfis import TuboRet
from metalpy.material import Aco

#Definição do Aço com a propriedades em kN/cm²
VMB350 = Aco(20000, 0.3, 35, 45.0, 0.6)
L = 400 #cm

# Definindo um perfil do tipo tubo retangular TQ 220X220X16 com as
# propriedades em cm
TQ220X16 = TuboRet('TQ220X220X16', VMB350, und='cm', norma='NBR8800')

#Respostas com Metalpy
A = TQ220X16.A # área total do perfil
IX = TQ220X16.Ix # momento de inércia em relação ao eixo X
Iy = TQ220X16.Iy # momento de inércia em relação ao eixo Y
Wx = TQ220X16.Wx # módulo elástico em relação ao eixo X
Wy = TQ220X16.Wy # módulo elástico em relação ao eixo Y
Zx = TQ220X16.Zx # módulo plástico em relação ao eixo X
rx = TQ220X16.rx # raio de giração em relação ao eixo X
ry = TQ220X16.ry # raio de giração em relação ao eixo Y
J = TQ220X16.J # inércia a torção
esb_mesa = TQ220X16.esb_mesa # esbeltez das mesas
esb_alma = TQ220X16.esb_alma # esbeltez das almas

# Calculando as cargas criticas de flambagem através do método
# par_estabilidade()

Lx=400 
Ly=400
Lz=400
par_estabilidade = TQ220X16.par_estabilidade(klx=Lx, kly=Ly, klz=Lz)

Nex = par_estabilidade.Nex
Ney = par_estabilidade.Ney
Nez = par_estabilidade.Nez

# Calculando a força de compressão resistente de cálculo através do método
# Ncrd e obtendo os dados do cálculo

Ncrd, dados_Ncrd = TQ220X16.Ncrd(klx=Lx, kly=Ly, klz=Lz , data=True)
Q = dados_Ncrd.Q
ier = dados_Ncrd.ier
Chi = dados_Ncrd.Chi

#Calculando o momento resistênte de cálculo
Mrdx = TQ220X16.Mrdx()

# Verificação a flexo-compressão
Ncsd = -296.46
Mxsd = 7092
Mysd = 0

verif = TQ220X16.verif_NM(Ncsd, Mxsd, Mysd, klx=Lx, kly=Ly, klz=Lz)