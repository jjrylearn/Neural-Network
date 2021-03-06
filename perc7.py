from random import random, choice, shuffle
from time import clock
TRIALS = 900000
ALPHA = 0.25
#INPUTS = [(0,0,1,-1,0), (0,1,0,-1,1),(1,0,0,-1,1), (1,1,0,-1,1)] #OR GATE
#INPUTS = [(0,0,1,-1,0),  (0,1,0,-1, 1), (1,0,0,-1,1),(1,1,1,-1,0)] # XOR GATES
INPUTS =[(0,0,-1,0),(0,1,-1,1),(1,0,-1,1),(1,1,-1,0)]
SMALL = 0.4


def f(w,x):
    return int((w[0]*x[0] + w[1]*x[1] +  w[2]*x[2]) > 0 )

def yValue(x,w,v):
    h = [0,0,-1]
    h[0] = int((w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2])>0)
    h[1] = int((w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2])>0)
    y = int((v[0]+h[0] + v[1]*h[1] + v[2]*h[2]) > 0)
    return y
  

def trained(w,v):
    for x in INPUTS:
        y  = yValue(x,w,v)
        t = x[3]
        if y != t:
            return False
        print(y)
        print(t)
        print(y==t)
    return True


def verifyNetwork(epochs,w,v):
    print('--done--')
    print('Epochs = ' , epochs)
    for x in INPUTS:
        t= x[3]
        y = yValue(x,w,v)
        print('%5s'% (y == t) , '--->' , yValue(x,w,v),x)
    print('\n== Statistics ===')
    print(' x = %2d, %2d, %2d, %2d'%(x[0],x[1],x[2],x[3]))
    print('w = %5.2f,%5.2f'%(w[0][0],w[0][1]))
    print('    %5.2f,%5.2f'%(w[1][0],w[1][1]))
    print('    %5.2f,%5.2f'%(w[2][0],w[2][1]))
    print('v = %5.2f,    %5.2f,%5.2f'%(v[0],v[1],v[2]))
    print('y=',y)
    

def initializeWeights():
    w = [[-2.0+4.0*random() for a in range(2)] for n in range(3)]
    v = [-2.0+4.0*random() for a in range(3)]
    return w,v

def improveWeights(w,v):
    return initializeWeights()

def trainPerceptronsWeights():
    epochs= 0
    h = [0,0,-1]
    w,v =initializeWeights()

    
    while epochs < TRIALS and not trained(w,v):
        x = choice(INPUTS)
        h[0] = int((w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2])>0)
        h[1] = int((w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2])>0)
        epochs += 1
        print(epochs)
        w,v = improveWeights(w,v)
    print(trained(w,v))
    return epochs,w,v
    

def main():
    epochs,w,v = trainPerceptronsWeights()
    verifyNetwork(epochs,w,v)

if __name__ == '__main__':
    START_TIME = clock()
    main()
    print('---> Run Time=',round(clock() - START_TIME, 2), 'seconds <--');
    
