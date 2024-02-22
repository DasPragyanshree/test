import datetime
import time
import os


#spt_tool_path="C:\FedEx\SPT Files 20231110 - Write _No_Revenue\FedEx SPT - Accenture MasterCopy_Export v 0.5.xlsb"
#
# # # In[3]:
# # if __name__=="__main__":
# #     parser=argparse.ArgumentParser()
# #     #parser.add_argument("log_file_path", help="Pass the file name")
# #     parser.add_argument("file_name",help="Pass the file name")
# #     args = parser.parse_args()
#
#
#
#
# date = datetime.datetime.now().strftime("%Y%m%d")
# #log_path=args.file_name
# log_path="C:\FedEx\SPT Files 20231110 - Write _No_Revenue\FedEx SPT - Accenture MasterCopy_Export v 0.5.xlsb"
# print(log_path)
# #print(log_path.split('\\'))
# # log_path = log_path[:log_path.rfind('\\')+1]
# #print(log_path[:log_path.rfind('/')-2])
# print(log_path.split('\\'))
# file_path =('\\'.join(log_path.split('\\')[:-1]))
# file_path = os.path.normpath(file_path)
# print(os.path.join(file_path, 'temp.txt'))
# # print(file_path)
# # # # input("Press Enter to continue\n")
# # print(file_path+"\\"+"test.txt")
# # # print(os.getcwd())
#
# #C:\FedEx

def number_to_words(number):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number == 0:
        return "zero"

    if number < 10:
        return units[number]
    elif 10 < number < 20:
        return teens[number - 10]
    elif number < 100:
        return tens[number // 10] + ("-" + units[number % 10] if number % 10 != 0 else "")
    elif number < 1000:
        # if number % 100 != 0:
        #     num_1000=number_to_words(number % 100)
        # else:
        #    ""
        return units[number // 100] + " hundred" + (" and " + number_to_words(number % 100) if number % 100 != 0 else "")
        #return units[number // 100] + " hundred" + (" and " + num_1000)

user_input = int(input("Enter a number: "))
word_representation = number_to_words(user_input)
print(f"Word representation: {word_representation}")

