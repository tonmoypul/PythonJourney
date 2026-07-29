def apply_discount(price, discount):
  if not isinstance(price, (int, float)):
    return "The price should be a number"
  elif not isinstance(discount, (int, float)):
    return "The discount should be a number"
  elif price <=0:
    return "The price should be greater than zero"
  elif discount < 0 or discount >100:
    return "The discount should be between 0 and 100"
  
  real_discount = price * discount/100
  final_price = price - real_discount
  return final_price
  
print(apply_discount(50,20))