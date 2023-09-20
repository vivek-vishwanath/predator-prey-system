import matplotlib.pyplot as plt

# The duration over which the population changes
# 'h' in Euler's Method
time_scale = 0.0002

# The initial parameters

# Intrinsic Acorn Growth Rate
a_g = 20
# Rate of Acorn Consumption by Rodents
a_c = 0.1
# Efficiency of Converting Acorns into Rodent Biomass
c_r = 0.02
# Rate of Rodent Predation by Snakes
p_r = 0.03
# Mortality Rate of Rodents
m_r = 10
# Efficiency of Converting Rodents into Snake Biomass
c_s = 0.3
# Mortality Rate of Snakes
m_s = 60

# Initial Populations
acorns = 500
rodents = 100
snakes = 10

acorn_y = []
rodent_y = []
snake_y = []

for i in range(10000):
    # a_n+1 = a_n + da
    acorns += (a_g - a_c * rodents) * acorns * time_scale
    # r_n+1 = r_n + dr
    rodents += (c_r * acorns - p_r * snakes - m_r) * rodents * time_scale
    # s_n+1 = s_n + ds
    snakes += (c_s * rodents - m_s) * snakes * time_scale

    acorn_y.append(acorns)
    rodent_y.append(rodents)
    snake_y.append(snakes)

x = list(range(10000))

plt.plot(x, acorn_y)
plt.plot(x, rodent_y)
plt.plot(x, snake_y)
plt.show()
