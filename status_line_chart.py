import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
sns.set_style('white')

frame_len = 100000

fig = plt.figure(figsize=(9,6))

def animate(i):
    data = pd.read_csv('status.csv')
    y1 = data['win']
    y2 = data['draw']
    y3 = data['loss']

    #if len(y1)<=frame_len:
    plt.cla()
    plt.plot(y1, label='win')
    plt.plot(y2, label='draw')
    plt.plot(y3, label="loss")
#     else:
#         plt.cla()
#         plt.plot(y1[-frame_len: ], label='win')
#         plt.plot(y2[-frame_len: ], label='draw')
#         plt.plot(y3[-frame_len: ], label='loss')
                        
    
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000,repeat=True
                )
plt.show()
