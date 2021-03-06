def f(w, x):
    return int((w[0]*x[0] + w[1]*x[1] + w[2]*x[2])>0)
  
def trained(w):
    flag=0
    for curTest in INPUTS:
        if not f(w,curTest) == curTest[3]:
            flag=1
    return not flag

    
def verifyNetwork(w, epochs):
    print("--done--")
    print (' Epochs = ', epochs)
    for curTest in TESTING:
        if f(w,curTest) == curTest[3]:
            print(" True " + str(f(w,curTest)) + " " + str(curTest))
        else:
            print(" False " + str(f(w,curTest)) + " " + str(curTest))
    print(" Line Generated: y= "+str(-1*round(w[0]/w[1],2))+"x + "+str(round(w[2]/w[1],2)))
    
def trainPerceptronsWeights():
    from random import random
    w = [(-2.0+4.0*random()) for a in range(3)]
    epochs=0
    from random import shuffle
    while epochs<TRIALS and not trained(w):
        shuffle(INPUTS)
        for x in INPUTS:
            y=f(w,x)
            t=x[3]
            if not y == t:
                w[0] = w[0] - ALPHA*(y-t)*x[0]
                w[1] = w[1] - ALPHA*(y-t)*x[1]
                w[2] = w[2] - ALPHA*(y-t)*x[2]
        epochs+=1
       
    print('epochs = ', epochs) 
    return w,epochs
            

#GLOBALS------------------------------------------------------------------------------------------------------------------
TRIALS = 1000000
ALPHA  = .1
INPUTS = [(0,4,-1,0),(4,0,-1,0),(2.01,2.01,-1,1)]
TESTING = INPUTS+[(4.1,0,-1,1),(0,4.1,-1,1)]
SMALL  = .4

#MAIN---------------------------------------------------------------------------------------------------------------------
def main():
    w, epochs = trainPerceptronsWeights()
    verifyNetwork(w, epochs)
    

if __name__ == '__main__': from time import clock; START_TIME = clock(); main(); print('--> Run Time = ', round(clock()-START_TIME, 2), 'seconds <--');
