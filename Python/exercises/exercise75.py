def minion_game(string):
    # your code goes here
    0,1,2,3,4,5,6
    0-1,1-2,2-3,3-4,4-5,5-6
    0-2,2-4,4-6
    0-3,3-6
    
    vowelsDictionary = {
        'A':'A',
        'E':'E',
        'I':'I',
        'O':'O',
        'U':'U'
    }
    
    kevinsDictionary = {}
    kevinsDictionary['total'] = 0

    stevesDictionary = {}
    stevesDictionary['total'] = 0

    
    for i in range(len(string)+1):
        for j in range(len(string)+1):
            
            #  Don't want to go backwards
            if i > j:
                continue
            
            stringSlice = string[i:j]
            
            if len(stringSlice) == 0:
                continue
            
            #  Cheking to see if substring starts
            #  with vowel.
            if stringSlice[0] in vowelsDictionary:
                #  Checking to see if this substring
                #  was already found in Kevin's
                #  dictionary
                try:
                    kevinsDictionary[stringSlice] = kevinsDictionary[stringSlice] + 1
                    kevinsDictionary['total'] = kevinsDictionary['total'] + 1
                except:
                    kevinsDictionary[stringSlice] = 1
                    kevinsDictionary['total'] = kevinsDictionary['total'] + 1
            else:
                try:
                    stevesDictionary[stringSlice] = stevesDictionary[stringSlice] + 1
                    stevesDictionary['total'] = stevesDictionary['total'] + 1
                except:
                    stevesDictionary[stringSlice] = 1
                    stevesDictionary['total'] = stevesDictionary['total'] + 1

    

    #  Checking to see who has the greatest total.
    if kevinsDictionary['total'] > stevesDictionary['total']:
        print('Kevins ' + str(kevinsDictionary['total']))
    else:
        print('Stuart ' + str(stevesDictionary['total']))

if __name__ == '__main__':
    minion_game('BANANA')