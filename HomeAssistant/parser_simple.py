import re
import numpy as np

##
# we are expecting a command to be something of this structure:
# command [commandType] [commandItem]
# currently supported commands:
# play, search, pause, news, now playing, go
# currently supported commandType:
# search [genre|track|artist]
# go [from] commandItem_1 [to] commandItem_2 #


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
            elif(arr_of_string[i] == "news"):
                n = i
                break
            elif(arr_of_string[i] == "now"):
                if (arr_of_string[i+1] == "playing"):
                    n = i
                    break
            elif(arr_of_string[i] == "go"):
                # special case:
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
    elif(arr_of_string[indx] == "web"):
        return "web"
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


# returns command, commandType, commandItem
# command a string
# commandType a string
# commandItem can be string for all commands
# except go:
# a tuple of ( source location, destination location)
# both of which are string
#
# in failure of valid command parsing
# returns ("FAILURE", "", "")
def extractCommandFromText(text):
    # very simple normalization of text
    sentence = _normalize(text)
    # return items
    command = ''
    commandType = ''
    searchItem = ''

    # check if it is valid at all
    lst_of_string = [sentence][0].split()
    # if (len(lst_of_string) < 1):

    #     print('len choto')
    #     return ("FAILURE", commandType, searchItem)

    arr_of_string = np.array(lst_of_string)

    # get first command index
    cmdIndex = _find_first_command_index(arr_of_string)

    # has it any command at all?
    if (cmdIndex == -1):
        return("FAILURE", "", "")

    # set command
    if (arr_of_string[cmdIndex] == "now" and arr_of_string[cmdIndex+1] == "playing"):
        command = "nowplaying"
    else:
        command = arr_of_string[cmdIndex]

    # command type and search item
    if (command == "search"):
        commandType = _get_command_type(arr_of_string, cmdIndex)
        if (cmdIndex + 1 > np.size(arr_of_string) or commandType == "FAILURE"):
            return("FAILURE", "", "")
        searchItem = _search_item_after_command(arr_of_string, cmdIndex + 1)

    # go special case: go from <source> to <destination>
    elif (command == "go"):
        indx = cmdIndex + 1
        sz = np.size(arr_of_string)
        src = ""
        dest = ""

        if (indx > sz):
            return ("FAILURE", "", "")
        # go has from right after it so +2
        for indx in range(cmdIndex + 2, sz):
            if (arr_of_string[indx] == "to"):
                break
            src += ' ' + arr_of_string[indx]

        for sec_indx in range(indx + 1, sz):
            dest += ' ' + arr_of_string[sec_indx]

        if (len(src) == 0 or len(dest) == 0):
            return("FAILURE", "", "")

        searchItem = (src.strip(), dest.strip())

    else:
        if (arr_of_string[cmdIndex] == "now" and arr_of_string[cmdIndex+1] == "playing"):
            searchItem = _search_item_after_command(arr_of_string, cmdIndex+1)
        else:
            # command = arr_of_string[cmdIndex]
            searchItem = _search_item_after_command(arr_of_string, cmdIndex)

    return (command, commandType, searchItem)


# str="news abcd"
# # str = "asholei ki go from chandnichalk to china"
# # # # str= "vai please fly from ndc, motijheel dhaka to "
# print(extractCommandFromText(str))
