# Data Engineering 1 Project Group 13

## Instances

docker swarm join --token SWMTKN-1-5t5tgg1juzbx9sosad14ivdpt8gg4effnczb30f4jd1sela6e2-7eebp378nhp6um1jnsd3h9xve 130.238.29.153:2377

p_g13_1: 130.238.29.153
p_g13_2: 130.238.29.154
p_g13_3: 130.238.29.77

## Notes
- the hostname of the instance gets used in 'docker node'. It doesnt parse the dot structure, so nodes have the same name. Changed instance names from p.g13.1 to p_g13_1, etc