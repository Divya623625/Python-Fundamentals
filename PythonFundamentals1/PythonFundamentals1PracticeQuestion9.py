# Q9. Ask the user for: Principal(P), Rate(R), Time(T). Convert all to float and compute Simple interest: (SI=P*R*T)/100
Principal=input("Enter the Principal: ")
Rate=input("Enter the Rate: ")
Time=input("Enter the time: ")
Principal, Rate, Time=float(Principal), float(Rate), float(Time)
SI=Principal*Rate*Time/100
print(SI)
