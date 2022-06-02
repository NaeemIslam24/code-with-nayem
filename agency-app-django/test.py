import random
def random_code():

    code = ['1','2','3','0','4','5','6','7']
   
    ran = "".join(random.choice(code) for x in range(6))
    return ran

r = random_code()
print(r)