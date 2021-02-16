import numpy as np

#Reciprocal lattice in (H,K,0) plane for Gd2PdSi3
lmbda=1.5
a_rcp=1.78042#a*
c_rcp=1.53248#c*
q=1/7
pi=np.pi
delta =0.04#unknown value. change it!

a_star = np.array([a_rcp,0,0])      # a* vector (parallel to the x axis at w=0)
b_star = np.array([a_rcp,0,c_rcp])     # b* vector

Ht = 1.0     # target H。好きな値に変えよう！
Kt = 0.0        # target K。好きな値に変えよう！

tau = Ht*a_star + Kt*b_star         # そのままベクトルの足し算が出来ます。tauはベクトル(np.array)です。
tau_length = np.linalg.norm(tau)    # np.linalg.norm( )　はnp.arrayで定義したベクトルの大きさを求める
theta = np.arcsin(lmbda*tau_length/4/pi)*180/pi   #in bragg's law
alpha = np.arctan2(tau[1],tau[0])*180/pi    # np.arctan2(y,x) は、 (x,y)の点についてx軸から測った角度を求める。tau[0]はtau vectorのx成分、tau[1]はy成分。
omega = theta+90.0-alpha

print("For Gd2PdSi3 in (H,K,0) plane")
print("target : (%f, %f, 0) in r. l. u."%(Ht,Kt))
print("tau = (%f, %f, %f) in A-1 unit"%(tau[0],tau[1],tau[2]))
print("|tau| = %f A-1"%(tau_length))
print("2theta = %f deg."%(theta*2))
print("Omega = %f deg"%(omega))
