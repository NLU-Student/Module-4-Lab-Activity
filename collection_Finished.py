# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889
# variable authrs was mispelled  + quotations need to be change to single inside set
authors = {
    'Charles Dickens' : 1870,
    'William Thackeray' : 1863,
    'Anthony Trollope': 1882,
    'Gerard Manley Hopkins': 1889}
# deleted "date" in for loop and brack in line 16 and restructure line 19
for key, value in authors.items():
    print(key, " died in ", value)


