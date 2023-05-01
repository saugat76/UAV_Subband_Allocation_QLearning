import subprocess

#Run the script for multiple levels of information exchange from level 1 to level 4
for i in range(1, 4):
    print('#######################################################')
    print('####  Running the code for Level:', i, "info exchange  ####")
    print('#######################################################')
    p = subprocess.run(["python", "uav_env.py"])
    g = subprocess.run(["python", "main.py", "--info-exchange-lvl", str(i), "--num-episode", str(450)])

# ## Running for level 3 with different distance values
# for i in range(0,1000, 250):
#     print('###########################################################')
#     print('####  Running the code for distance threshold:', i, " with Level: 2 ####")
#     print('###########################################################')
#     p = subprocess.run(["python", "uav_env.py"])
#     g = subprocess.run(["python", "main.py", "--info-exchange-lvl", str(2), "--num-episode", str(800), "--wandb-track", "True", "--uav-dis-th", str(i), "--learning-rate", str(3.5e-4)])
