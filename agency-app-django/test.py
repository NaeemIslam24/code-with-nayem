import random
# def random_code():

#     code = ['1','2','3','0','4','5','6','7']
   
#     ran = "".join(random.choice(code) for x in range(6))
#     return ran

# r = random_code()
# print(r)


def hello():
        number_list = [x for x in range(10)]
        code_string = "".join(str(item) for item in number_list)
        return code_string

print('this is a test.....', hello())