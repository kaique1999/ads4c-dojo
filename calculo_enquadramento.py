def calculo_enquadramento(salario_base, base_calculo):
  
  base_calculo = salario_base
  if salario_base < 1903.98:
    return 0
  elif salario_base > 1903.98 and salario_base <= 2826.65:
    return round (base_calculo * 0.7)
  elif salario_base > 2826.65 and salario_base <= 3751.05:
    return round(base_calculo * 0.15)
  elif salario_base > 3751.05 and salario_base <= 4664.68:
    return round(base_calculo * 0.225)
  else:
    return round(base_calculo * 0.275)
