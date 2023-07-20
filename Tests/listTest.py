import numpy as np

def closest_value(input_list, input_value):

  arr = np.asarray(input_list)

  i = (np.abs(arr - input_value)).argmin()

  return arr[i]

if __name__ == "__main__" :

  list1 = [22, 12, 51, 23, 48, 16, 34, 61]

  num=int(input("Enter the value: "))

  val=closest_value(list1,num)

  print("The closest value to the "+ str(num)+" is",val)
