# Variable Lookup加了上下文

# Adding variable lookup to the interpreter!

def eval_exp(tree, environment):
    nodetype = tree[0]
    if nodetype == "number":
        return int(tree[1])
    elif nodetype == "binop":
        left_value = eval_exp(tree[1], environment)
        operator = tree[2]
        right_value = eval_exp(tree[3], environment)
        if operator == "+":
            return left_value + right_value
        elif operator == "-":
            return left_value - right_value
    elif nodetype == "identifier":
        # ("binop", ("identifier","x"), "+", ("number","2"))
        # (1) find the identifier name
        # (2) look it up in the environment and return it
        return env_lookup(environment, tree[1])


# Here's some code to simulate env_lookup for now. It's not quite what we'll be
# using by the end of the course.

def env_lookup(env,vname): 
        return env.get(vname,None)

environment = {"x" : 2}
tree = ("binop", ("identifier","x"), "+", ("number","2"))
print eval_exp(tree,environment) == 4


# Evaluating Statements从表达式到语句

def eval_stmts(tree, environment):
    stmttype = tree[0]
    if stmttype == "assign":
        # ("assign", "x", ("binop", ..., "+",  ...)) <=== x = ... + ...
        variable_name = tree[1]
        right_child = tree[2]
        new_value = eval_exp2(right_child, environment)
        env_update(environment, variable_name, new_value)
    elif stmttype == "if-then-else": # if x < 5 then A;B; else C;D;
        conditional_exp = tree[1] # x < 5
        then_stmts = tree[2] # A;B;
        else_stmts = tree[3] # C;D;
        # Assume "eval_stmts(stmts, environment)" exists
        if eval_exp2(conditional_exp, environment) is True:
            eval_stmts(then_stmts, environment)
        else:
            eval_stmts(else_stmts, environment)

        
def eval_exp2(exp, env): #简化过后
        etype = exp[0] 
        if etype == "number":
                return float(exp[1])
        elif etype == "string":
                return exp[1] 
        elif etype == "true":
                return True
        elif etype == "false":
                return False
        elif etype == "not":
                return not(eval_exp2(exp[1], env))

def env_update(env, vname, value):
        env[vname] = value
        
environment = {"x" : 2}
tree = ("if-then-else", ("true", "true"), ("assign", "x", ("number", "8")), ("assign", "x", "5"))
eval_stmts(tree, environment)
print environment == {"x":8}
