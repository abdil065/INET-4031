import sys

print("Printing out User Data:")
for line in sys.stdin:
    if not line.startswith('#'):
        user_data = line.strip().split(':')
        username, password, userid, groupid = user_data
        print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
print("End of User Data")
