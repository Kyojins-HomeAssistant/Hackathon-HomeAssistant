import re
import numpy as np

def _find_first_command_index(arr_of_string):
    n = -1
    if(np.size(arr_of_string) == 0):
        n = -1
    else:
        for i in range(0, np.size(arr_of_string)):
            if(arr_of_string[i] == "play"):
                n = i
                break
            elif(arr_of_string[i] == "search"):
                n = i
                break
            elif(arr_of_string[i] == "pause"):
                n = i
                break
            elif(arr_of_string[i] == "now"):
                if (arr_of_string[i+1] == "playing"):
                    n = i
                    break

    return n


def _search_item_after_command(arr_of_string, index):
    arrSize = np.size(arr_of_string)
    rtrn_str = ''
    for i in range(index + 1, arrSize):
        rtrn_str += arr_of_string[i] + ' '

    return rtrn_str.strip()


def _get_command_type(arr_of_string, indx):
    indx += 1
    if (arr_of_string[indx] == "genre"):
        return "genre"
    elif (arr_of_string[indx] == "artist"):
        return "artist"
    elif (arr_of_string[indx] == "track"):
        return "track"
    else:
        return "FAILURE"


def _normalize(sentence):
    sentence = sentence.lower()
    sentence = sentence.strip()
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # stop_words = set(stopwords.words('english'))
    lst = [sentence][0].split()
    sentence = ""
    for i in lst:
        # if not i in stop_words:
        sentence += i+' '

    sentence = sentence[:-1]
    # lst = [sentence][0].split()
    return sentence

def extractCommandFromText(text):
    # very simple normalization of text
    sentence = _normalize(text)
    # return items
    command = ''
    commandType = ''
    searchItem = ''
    # # first merge the two or more worded commands 🤲
    # sentence.replace("now playing", "nowplaying")
    # print(sentence)

    # check if it is valid at all
    lst_of_string = [sentence][0].split()
    if (len(lst_of_string) < 1):
        command = 'FAILURE'
        print('len choto')
        return ("FAILURE", commandType, searchItem)
    

    arr_of_string = np.array(lst_of_string)

    # get first command index
    cmdIndex = _find_first_command_index(arr_of_string)

    # set command
    if (arr_of_string[cmdIndex] == "now" and arr_of_string[cmdIndex+1] == "playing"):
        command = "nowplaying"
    else:
        command = arr_of_string[cmdIndex]

    # command type and search item
    if (command == "search"):
        commandType = _get_command_type(arr_of_string, cmdIndex)
        if (commandType == "FAILURE"):
            print('command type e error')
            return("FAILURE", "", "")
        searchItem = _search_item_after_command(arr_of_string, cmdIndex + 1)
    else:
        if (arr_of_string[cmdIndex] == "now" and arr_of_string[cmdIndex+1] == "playing"):
            searchItem = _search_item_after_command(arr_of_string, cmdIndex+1)
        else:
            # command = arr_of_string[cmdIndex]
            searchItem = _search_item_after_command(arr_of_string, cmdIndex)

    return (command, commandType, searchItem)
