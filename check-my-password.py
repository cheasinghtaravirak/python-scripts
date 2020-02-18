import requests
import hashlib
import sys

# query char is part of the real password. Do so for security reasons
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    respond = requests.get(url)
    if respond.status_code != 200:
        raise RuntimeError(f'Error fetching: {respond.status_code}, please check the api call again')
    return respond

def get_password_leaks_and_counts(response, key):
    #hashes are a tuple of a list of tail hash password and count ([hash-tail1, count1], [hash-tail2, count2], ...]
    hashes = (line.split(":") for line in response.text.splitlines()) #a generator
    for h, count in hashes:
        if h == key:
            return count
    return 0

def check_pwned_api(password):
    # check if password exists in api response
    # a way to create a sha1 password from a string
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # print(sha1password)
    # Extract first five characters and the tail of password
    first5_char, key = sha1password[:5], sha1password[5:] #key is a tail of hash
    # response.text is a list of hash passwords begin with first5-char with a count but only include the tail of hash
    response = request_api_data(first5_char)
    return get_password_leaks_and_counts(response, key)

def main(args):
    for password in args:
        count = check_pwned_api(password)
        if count:
            print(f'{password} was found {count} number of times. You should change your password.')
        else:
            print(f'{password} was not found. Don\'t worry.')
    return 'Done execution'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))



# check_pwned_api('00791BB54CC9122')
# res = request_api_data('CBFDA')
# check_pwned_api('123')
#password = '123'
#sha1password= '40BD001563085FC35165329EA1FF5C5ECBDBBEEF'
#head = '40BD0', tail = '01563085FC35165329EA1FF5C5ECBDBBEEF'

#Below has no head
#FF803FACF96FC5C8C5DF1308F2413BBC55F

# result = request_api_data('40BD0')
# print(result.text) #return a list of hash password with the head of 40BD0 but don't see the appendition