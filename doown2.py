import random
import time
MIN_OPERAND=2
MAX_OPERAND=15

OPERATOR=["+","-","*"]
total_problem=10

def genarate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATOR)
    expr=str(left)+" "+operator+" "+str(right)
    answer=eval(expr)
    return expr,answer
wrong=0
correct=0
input("press enter to start")
print("--------------------")
start_time=time.time()
for i in range(total_problem):
    expr,answer=genarate_problem()
    while True:
        gusse=input("problem #" + str(i+1) + ":"+expr+"=")
        if gusse==str(answer):
                
            break
        wrong+=1
end_time=time.time()
total_time=end_time-start_time
print("nice work you finish it in ",total_time,"seconds")
