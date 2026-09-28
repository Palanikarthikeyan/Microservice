'''employee details'''

emp_name = 'Mr.ABC'
eid = 101
ecost = 1300.42
elogin = True
print(f"Emp name is:{emp_name}  ID:{eid}\n") 

Emp_info1 = [emp_name,eid,ecost,elogin] # list
print(Emp_info1)
print(f'Emp name is:{Emp_info1[0]} ID:{Emp_info1[1]}') # from given list - fetch nth item

Emp_info2 = (emp_name,eid,ecost,elogin) # tuple
print(Emp_info2)
print(f"Emp name is:{Emp_info2[0]} ID:{Emp_info2[1]} Basic pay:{Emp_info2[2]}") # from given tuple - fetch nth item

Emp_info3 = {'eid':eid,'ename':emp_name,'ecost':ecost,'eLogin':elogin} # dict 
print(Emp_info3)
print(f'Emp name is:{Emp_info3['ename']} ID:{Emp_info3["eid"]}') # from given dict - fetch nth item