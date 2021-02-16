'''get text and replace some words with x'''

import tkinter

main = tkinter.Tk()
main.title("replace everything")
main.geometry("300x300")


def go():

    i = 0

    enter = text_entry.get("1.0", "end")
    word = word_entry.get("1.0", "end")

    replace_w = replace_entry.get("1.0", "end")
####################################################################################################

    enter_lastRMV = list(enter)

    enter_lastRMV.pop(-1)
    #enter_lastRMV.pop(-2)

    enter_temp  = "".join(enter_lastRMV)

####################################################################################################
    word_lastRMV = list(word)

    word_lastRMV.pop(-1)
#    word_lastRMV.pop(-2)


    word  = "".join(word_lastRMV)

####################################################################################################

    replace_lastRMV = list(replace_w)

    replace_lastRMV.pop(-1)
    #replace_lastRMV.pop(-2)

    replace_w  = "".join(replace_lastRMV)

####################################################################################################
    enter_list = enter_temp.split()

    arr_length = len(enter_list)

    for i in range(arr_length):     

        if str(enter_list[i]) == word:
            enter_list[i] = enter_list[i].replace(word, replace_w)
            
            
        enter_list[i] = enter_list[i] + " "


    file = open("text_replacer.txt", "w+")
    file.write("".join(enter_list))
    file.close()


text_entry = tkinter.Text(main, width=50, height=8)
word_entry = tkinter.Text(main, width=50, height=2)
replace_entry = tkinter.Text(main, width=50, height=2)

submit_btn = tkinter.Button(main, command=go, text="Replace!")
text_entry.grid(row=0, column=0)
word_entry.grid(row=1, column=0)
replace_entry.grid(row=2, column=0)
submit_btn.grid(column=0, row=5)

main.mainloop()
