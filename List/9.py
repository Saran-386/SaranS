years = ["January 2023","February 2024","March 2023”,"May 2025","April 2023","August 2024","September 2025","December 2023"]
sy=years.split(" ")
for i in sy:
    if (i!='2023'):
        sy[i]='2003'
    else:
        continue
print(sy)