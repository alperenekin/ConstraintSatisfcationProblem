#!/usr/bin/env python
# coding: utf-8

# In[102]:


import copy


def read_data(path):
    f = open(path, "r")
    data = {}
    for line in f:
        line = line.replace("\n", "")
        columns = line.split(",")
        data[columns[0]] = columns[1::]
    f.close()
    return data




def read_constraint(path):
    f = open(path, "r")
    data = []
    for line in f:
        line = line.replace("\n", "")
        line = line.replace("(", " ")
        line = line.replace(")", "")
        data.append(line)
    f.close()
    return data


def check_line_none(line):
    
    print("")
    

def split_condition(sentences):
    sep = []
    for i in sentences:
        sep.append(i.split(" "))
    return sep




class CSPNode:  
    def __init__(self, domain):
        
        self.domain = domain  
    
    def getDomain(self):
        return self.domain
    




def if_clause(node, sentence, index):
    # if breeds=greatDane then years=2006
    domain = node.getDomain()[index]
    first = sentence[1].split("=")
    second = sentence[-1].split("=")

    att = domain[first[0]]
    att2 = domain[second[0]]

    if (len(att) == 1):

        if (first[1] == att[0]):

            if (second[1] not in att2):
                return False

    if (len(att2) == 1):

        if (second[1] == att2[0]):

            if (first[1] not in att):
                return False
    return True


def ifnot_clause(node, sentence, index):
    # "if owners=Douglas then not dogs=Harley"
    domain = node.getDomain()[index]
    first = sentence[1].split("=")
    second = sentence[-1].split("=")

    att = domain[first[0]]  # Get owner what owners can be
    att2 = domain[second[0]]  # get dogs what dogs can be

    if (len(att) == 1):

        if (first[1] == att[0]):

            if (len(att2) == 1):

                if (att2[0] == second[1]):
                    return False

    return True


def ifeither_clause(node, sentence, index):
    
    # "if dogs=Riley then either owners=Douglas or breeds=bulldog"
    domain = node.getDomain()[index]
    first = sentence[1].split("=")
    second = sentence[-3].split("=")
    third = sentence[-1].split("=")
    att = domain[first[0]]  # Get owner what owners can be
    att2 = domain[second[0]]  # get dogs what dogs can be
    att3 = domain[third[0]]

    if len(att) == 1:

        if att[0] == first[1]:

            if(att2[0] == second[1] and att3[0] == third[1]):
                return False
            else:
                if (second[1] not in att2) and (third[1] not in att3):
                    return False
    if(len(second[1]) ==1):
        if(second[0] == att2[0]):
            if(first[1] not in att):
                return False
    if (len(third[1]) == 1):
        if (third[0] == att2[0]):
            if (first[1] not in att):
                return False

    return True


def check_equality(values1, values2):
    for i1 in values1:

        for i2 in values2:

            if (i1 == i2):
                return True
    return False


def check_bigger(values1, values2):
    # years(dogs=Riley) > years(dogs=Harley)

    for i1 in values1:

        for i2 in values2:

            if (i1 > i2):
                return True
    return False


def check_smaller(values1, values2):
    for i1 in values1:

        for i2 in values2:

            if (i1 < i2):
                return True
    return False


def check_plus(values1, values2, constant):
    for i1 in values1:

        for i2 in values2:

            if (int(i1) == int(i2) + constant):
                return True
    return False


def check_minus(values1, values2, constant):
    for i1 in values1:

        for i2 in values2:

            if (int(i1) == int(i2) - constant):
                return True
    return False


def numeric_clause(node, sentence, length_domain):
    cont = True
    domain = node.getDomain()

    key = sentence[0]
    first = sentence[1].split("=")
    second = sentence[4].split("=")
    key2 = sentence[3]
    # ['years', 'dogs=Molly', '=', 'years', 'breeds=pekingese', '+', '1'],
    for i in range(length_domain):

        if ((first[1] in domain[i][first[0]]) and (len(domain[i][first[0]]) == 1)):

            years = domain[i][key]
            if(len(years) == 1):
                for z in range(length_domain):

                    if ((second[1] in domain[z][second[0]]) and len(domain[z][second[0]]) == 1):  # Check whether they belong to the same node

                        years2 = domain[z][key2]
                        if years[0] == years2[0]:
                            return False
                        else:
                            if (len(sentence) == 5):

                                if (sentence[2] == "="):
                                    cont = check_equality(years, years2)

                                if (sentence[2] == ">"):
                                    cont = check_bigger(years, years2)

                                if (sentence[2] == "<"):
                                    cont = check_smaller(years, years2)

                            if (len(sentence) == 7):

                                if (sentence[-2] == "+"):

                                    cont = check_plus(years, years2, int(sentence[-1]))

                                if (sentence[-2] == "-"):
                                    cont = check_minus(years, years2, int(sentence[-1]))

                            if (cont == False):
                                return False
                            
    return cont


def allDifferent(node, sentence, length_domain):
    
    #['{boats=AlphaOne,sailors=VickyEstes,sailors=TaraCarroll}', 'are', 'all', 'different']
    
    s = sentence[0]
    s = s.replace("{", "")
    s = s.replace("}", "")
    s_att = s.split(",")
    
    first_clause = s_att[0].split("=")
    secondclause = s_att[1].split("=")
    thirdclause = s_att[2].split("=")

    domain = node.getDomain()
    cont_fs = True
    cont_st  = True
    cont_tf = True
    first_index = []
    second_index = []
    third_index = []
    for i in range(length_domain):

        if (first_clause[1] in domain[i][first_clause[0]] and len(domain[i][first_clause[0]]) == 1 ):
            first_index.append(i)

        if (secondclause[1] in domain[i][secondclause[0]] and len(domain[i][secondclause[0]]) == 1):
            second_index.append(i)

        if (thirdclause[1] in domain[i][thirdclause[0]] and len(domain[i][thirdclause[0]]) == 1):
            third_index.append(i)
    
    if(len(first_index) > 0):
        
        if(len(second_index) > 0):
            
            cont_fs = first_index[0] != second_index[0]
    if(len(second_index) > 0):
        
        if(len(third_index) > 0):
            
            cont_st = second_index[0] != third_index[0]
    
    if(len(third_index) > 0):
        
        if(len(first_index) > 0):
            
            cont_tf = first_index[0] != third_index[0]
            
    return (cont_tf and cont_st and cont_fs)



def oneof(node, sentence, length_domain):
    
    
    """{'days': ['270'], 'sailors': ['DebraDecker'], 'boatTypes': ['schooner'], 'boats': ['BayHawk']},
    one of {sailors=DebraDecker,days=270} corresponds to boats=BayHawk other boatTypes=schooner
    """
    first = sentence[2].split(",") #'{players=Lonnie,players=Steven}
    
    x_ = first[0].split("=") # [{players, Lonnie]
    y_ = first[1].split("=") #[players, Steven}] 
    
    z_ = sentence[5].split("=") #'years=2006'
    t_ = sentence[-1].split("=") # [teams,Dodgers]
    
    domain = node.getDomain()

    
    index_object = {}
    
    for i in  range(length_domain):
        
        if ((x_[1] in domain[i][x_[0][1::]]) and (len(domain[i][x_[0][1::]]) == 1)):
            
            index_object[x_[1]] = i
        
        if (((y_[1][0:-1]) in domain[i][y_[0]]) and (len(domain[i][y_[0]]) == 1)):
            
            index_object[y_[1][0:-1]] = i # Which subject it is
    
    if(len(index_object) != 2):
        return True
    if(index_object[x_[1]] == index_object[y_[1][0:-1]]):
        return False
    indexes = []
    indexes.append(index_object[x_[1]])
    indexes.append(index_object[y_[1][0:-1]])   
            
    if (( z_[1] in domain[indexes[0]][z_[0]] ) and (len(domain[indexes[0]][z_[0]]) == 1)):

        if((t_[1] not in domain[indexes[1]][t_[0]])):

            return False
        
    if ( ( t_[1] in domain[indexes[0]][t_[0]] ) and (len(domain[indexes[0]][t_[0]]) == 1)):

        if((z_[1] not in domain[indexes[1]][z_[0]])):
            
            return False
            
    if ( ( z_[1] in domain[indexes[1]][z_[0]] ) and (len(domain[indexes[1]][z_[0]]) == 1)):

        if((t_[1] not in domain[indexes[0]][t_[0]])):
            
            return False
            
    if ( ( t_[1] in domain[indexes[1]][t_[0]] ) and (len(domain[indexes[1]][t_[0]]) == 1)):

        if((z_[1] not in domain[indexes[0]][z_[0]])):
            
            return False
        
    return True
                
        
            
            
        
    
def globalConstraint(node, constraints):
    # constraints = node.getConstraints()

    domain = node.getDomain()
    cont = True
    length_domain = len(domain)
    for i in range(length_domain):

        for cons in constraints:

            sep = cons[0]
            if sep == "if":

                if (len(cons) == 4):
                    # print(cons)
                    cont = if_clause(node, cons, i)
                    # print("if clause", cont)

                if (len(cons) == 5):
                    cont = ifnot_clause(node, cons, i)
                    # print("ifnot_clause", cont)

                if (len(cons) == 7):
                    cont = ifeither_clause(node, cons, i)
                    # print(cons)
                    # print("ifeither_clause", cont)

            elif cons[len(cons) - 1] == "different":
                cont = allDifferent(node, cons, length_domain)
                
            elif cons[0] == "one":
                
                cont = oneof(node, cons, length_domain)
                
            else:

                cont = numeric_clause(node, cons, length_domain)

            
            if cont == False:
                return False
    return cont

def checkDomain(node,constraints,solution):
    count = 0
    domain = node.getDomain()
    keys = domain[0].keys()
    for i in range(len(domain)):
        for k in keys:
            if len(domain[i][k]) == 1:
                count += 1

    if count == 16:
        if globalConstraint(node, constraints):
            solution.append(node)
            return True
            

def createChild(node, attributes,solution, constraints):
    checkDomain(node, constraints, solution)
    domain = node.getDomain()
    length_domain = len(domain) 
    domain_keys = attributes
    
    for d in range(length_domain):

        for k in domain_keys:

            if (len(domain[d][k]) > 1):
                count = 0
                for ele in domain[d][k]:
                    element = ele
                    key = k
                    count += 1
                    if globalConstraint(node, constraints):
                        child_domain = copy.deepcopy(node.getDomain())
                        childNode = CSPNode(child_domain)
                        removeAttribute(childNode, key, element, d, length_domain)
                        createChild(childNode, domain_keys, solution, constraints)

                    if count == len(domain[d][k]):
                            return False


    return False

def removeAttribute(node, key, element, index, length_domain):

    domain = node.getDomain()

    for d in range(length_domain):

        if d != index:
            if (element in domain[d][key]):

                
                node.getDomain()[d][key].remove(element)

        else:

            domain[d][key] = [element]

    return True


def writeSolution(solution):
    
    
    if(len(solution) > 1):
        
        
        sorted_list = sorted(solution[1].getDomain(), key=lambda k: k[list(solution[0].getDomain()[0].keys())[0]]) 

        columns = list(sorted_list[0].keys())

        char_columns = 0
        for i in range(len(columns)):

            if(i == len(columns) - 1):
                sep = " "
            else:
                sep = " | "
            char_columns += len(columns[i])
            print(columns[i], end = sep )

        print("\n" + char_columns * "-" + "---" * len(columns) )
        for x in range(len(sorted_list)):

            for y in range(len(columns)):

                if(y == len(columns) - 1):
                    sep = " "
                else:
                    sep = " | "
                print(sorted_list[x][columns[y]][0], end = sep)

            print("")
    else:
        
        print("Solution is not found")

        
          
 


# In[109]:


def main():
    
    while(True):
        print("The problems available in this directory: 1 2 3 (Enter Q for exit)")
        directery_user = input("Choose a problem ")
        if(directery_user not in ["1", "2", "3"]):
            
            if(directery_user.capitalize() == "Q" ):
                print("Exit is successful")
                break
            else:
                
                print("Enter by input option")
        
        else:
            data_name = "data-"+ directery_user +".txt"
            constraint_name = "clues-"+ directery_user +".txt"
            print("")
            print("Here is the solution to the problem defined in "+data_name+" and "+constraint_name+".\n")
            data = read_data(data_name)
            domain = []
            for i in range(len(data)):
                domain.append(copy.deepcopy(data))
            constraint_file = read_constraint(constraint_name)
            constraints = split_condition(constraint_file)
            keys = data.keys()
            rootNode = CSPNode(domain)
            child_domain = copy.deepcopy(rootNode.getDomain())
            solution = []
            childNode = CSPNode(child_domain)
            createChild(childNode, keys, solution, constraints)
            writeSolution(solution)


# In[110]:


if __name__ == "__main__":
    
    main()


# In[56]:





# In[ ]:




