list_ = ['nemo', 'bagas', 'charlie', 'alpha', 'nemo']
large = []

for i in range(10000):
    large.append('nemo')


def foundNemo(list_):
    for i in range(0, len(list_)):
        if list_[i] == 'nemo':
            print('Found Nemo')


foundNemo(large)  # O(n) --> Linear Time

print(large.count('nemo'))


def firstItem(list_):
    print(list_[0])


firstItem(list_)  # O(1) -> Constant Time


a = 'satu'

print(len(a))


# function funChallenge(input) {
#   let a = 10; O(1)
#   a = 50 + 3; O(1)

#   for (let i = 0; i < input.length; i++) { O(n)
#     anotherFunction(); O(n)
#     let stranger = true; O(n)
#     a++; O(n)
#   }
#   return a; O(1)
# }

# Big O = O(3 + 4n)