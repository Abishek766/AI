def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    p_not_a = 1 - p_a
    p_b =(p_b_given_a * p_a)+(p_b_given_not_a * p_not_a)
    p_a_given_b = (p_b_given_a * p_a)/p_b

    return p_a_given_b
    

p_disease = 0.01
p_positive_disease = 0.99
p_no_disease = 0.05

person_disease_probability = bayes_theorem(p_disease,p_positive_disease,p_no_disease)
print(f"Probability of having disease if test is positive: {person_disease_probability:.4f}")
