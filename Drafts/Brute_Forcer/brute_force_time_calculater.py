# 0.14953255653381348 Seconds für ein Durchlauf
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tHOW Secure is Your Password?")
password = input("Your Password:\t\t")
letters = password.count("")
loops_count = letters * letters
final_time = loops_count ** 0.14953255653381348
minutes = final_time / 60
hours = minutes / 60
days = hours / 24
months = days / 30
years = days / 12
combinations = 55296 ** letters
print(f"A brute Forcer would have to try that many combinations:\n {combinations:,}")
print(f"\n\n\nIt would take:")
print(f"Seconds: {round(final_time)}")
print(f"Minutes: {round(minutes)}")
print(f"Hours: {round(hours)}")
print(f"Days: {round(days)}")
print(f"Months: {round(months)}")
print(f"Years: {round(years)}")
