"""
Created on Sat Oct 3 2020
@author: natarajang
"""

def reorderLogFiles(logs):
    '''
    A function to sort log files based on letter and digit identifiers
    
    Parameters:
    ----------
    logs (list): array of space delimited strings
    
    Returns:
    --------
    list: Sorted list of letter-logs,
    and digit-logs in the order of appearance
    '''
    
    #Initialize digit-log and letter-log to be empty lists
    dig_log, let_log = [], []
    #Looping over the logs array
    for log in logs:
        #Split each entry by space
        #Peek at the first element after identifier
        if log.split()[1].isnumeric():
            #If the element is numeric, add to
            #digit-log list
            dig_log.append(log)
        else:
            #If element is non-numeric,
            #add to letter-log list
            let_log.append(log)
    return sorted(let_log, 
                  key = lambda x: (x.split()[1:],
                                   x.split()[0])) + dig_log
    #Code split at optimal places for easy reading


##Driver Code##
log_list = [['dig1 8 1 5 1','let1 art can','dig2 3 6','let2 own kit dig','let3 art zero'],
        ['g1 act car','a8 act zoo'],
        ['g1 act zoo','a1 act zoo'],
        ['6 r s','6 5 4','a3 ran car','6 50 4'],
        ['test1 5 6 7 9','test2 a a', 'test3 a']]
for logs in log_list:
    print('------------------------------------------------')
    print(reorderLogFiles(logs))
    print('------------------------------------------------')
