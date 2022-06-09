from cpr.CPRDayBean import CPRDayBean


today_cpr_data = CPRDayBean()
today_cpr_data.calculateCPR_input_values(, 22857, 23092)
print(today_cpr_data.S1)
print(today_cpr_data.S2)
print(today_cpr_data.S3)
print(today_cpr_data.S4)

print()

print(today_cpr_data.R1)
print(today_cpr_data.R2)
print(today_cpr_data.R3)
print(today_cpr_data.R4)
