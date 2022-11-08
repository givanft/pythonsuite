import sys
from datetime import datetime
from random import randint

ALPHABET: set = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


#==================
# main
def main() -> None:
#==================
    msg: str = ""
    match get_menu_choice():
        #''''''''''''''''''''''''''''''''''''
        case 1:
            msg = input("Message to be encrypted > ")

            if is_alphabet_only(msg) == False:
                sys.exit("ERROR: The message contains not alphabet characters.")

            encode_the_message(msg)
        #''''''''''''''''''''''''''''''''''''
        case 2:
            msg = input("Message to be decrypted > ")
            time_of_encode: str = input("Time of encode > ")

            try:
                dt: object = datetime.strptime(time_of_encode, '%d/%m/%Y, %H:%M:%S')
            except ValueError:
                sys.exit("Time of encode is wrong. Be sure its format like '%d/%m/%Y, %H:%M:%S'")

            decode_the_message(msg, dt)
        #''''''''''''''''''''''''''''''''''''
        case _:
            sys.exit()


#=================================
# get_menu_choice
def get_menu_choice() -> int:
#=================================
    """ 
    Get result of choice from main menu
 
    :param: None
    :type: None
    :raise: ValueError
    :return: 
        1: encode the message, 
        2: decode the message,
        0: close the tool
    :rtype: int
    """
    choice: int = 1

    print("Press 1 to encode a message.")
    print("Press 2 to decode a message.")
    print("Press any key to exit.")
    
    try:
        choice = int(input("Choice? > "))
    except ValueError:
        return 0
    
    if choice < 1 or choice > 2:
        return 0

    return choice


#==========================================
# is_alphabet_only
def is_alphabet_only(message: str) -> bool:
#==========================================
    """ 
    Check if the ecrypted message has only alphabet characters and a space
 
    :param: the encrypted message
    :type: str
    :raise: None
    :return: 'True' if there are not only alphabet characters and 'False' otherwise
    :rtype: bool
    """
    msg: str = ""
    for c in message:
        if c != ' ':
            msg += c

    return msg.isalpha()


#======================================================
# encode_the_message
def encode_the_message(message_to_encrypt: str) -> None:
#======================================================
    """ 
    Encode the message
 
    :param: 'message_to_encrypt' - A message to be encrypted
    :type: str
    :raise: None
    :return: None
    :rtype: None
    """
    time_of_encode = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    cipher_key = get_cipher_key(time_of_encode)

    cipher_abc = "".join(dict.fromkeys(cipher_key)) #remove duplicates
    
    # --------------------------------------------
    abc: list = list(ALPHABET)  # set copy of the original alphabet
    for c in cipher_abc:
        abc.remove(c)   # remove duplicates from original alphabet
    
    # --------------------------------------------
    for c in abc:
        cipher_abc += c # concatenate original alphabet with cipher one

    # --------------------------------------------
    # get dictionary => 
    #   key: original alphabet character
    #   value: a character from cipher alphabet
    abc_dict: dict = dict(zip(ALPHABET, list(cipher_abc)))

    # --------------------------------------------
    crypto_message: str = ""
    for c in message_to_encrypt:
        if c == ' ':
            crypto_message += str(randint(0,9))
        else:
            crypto_message += abc_dict[c.lower()]

    print(f"{crypto_message}")
    print(f"{time_of_encode}")


#=======================================
# decode_the_message
def decode_the_message(message_to_decrypt: str, time_of_encode: object):
#=======================================
    """ 
    Decode the message
 
    :param: 
        'message_to_decrypt' - A message to be decrypted,
        'time_of_encode' - Time of encode the message
    :type: str, object    
    :raise: None
    :return: None
    :rtype: None
    """
    cipher_key = get_cipher_key(time_of_encode)
    cipher_abc = "".join(dict.fromkeys(cipher_key))
    
    # --------------------------------------------
    abc: list = list(ALPHABET)  # set copy of the original alphabet
    for c in cipher_abc:
        abc.remove(c)   # remove duplicates from original alphabet
    
    # --------------------------------------------
    for c in abc:
        cipher_abc += c # concatenate original alphabet with cipher one

    # --------------------------------------------
    # get dictionary => 
    #   key: original alphabet character
    #   value: a character from cipher alphabet
    abc_dict: dict = dict(zip(list(cipher_abc), ALPHABET))
    pass

#======================================
# get_string_by_number
def get_string_by_number(num: int) -> str:
#======================================
    """ 
    Convert numeric value to string. Return one line. For example: 14 => fourteen, 49 => fortynine
 
    :param: number to be converted
    :type: str
    :raise: None
    :return: One line string
    :rtype: str
    """
    number_str_list: tuple = ("nil","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fifteen","twenty","thirty","forty","fifty")
    
    cipher: str = ""
    units: str = ""
    
    div: int = 0
    rem: int = 0
    
    if num < 10:
        cipher = number_str_list[num]
    elif 10 <= num < 20:
        match num:
            case 10 | 11 | 12 | 13:
                cipher = number_str_list[num]
            case 15:
                cipher = number_str_list[num-1]
            case _:
                rem = int(num % 10)
                suff :str = "teen"
                if rem == 8:
                    suff = "een"
                cipher = number_str_list[rem] + suff
    elif 20 <= num < 60:
        div = int(num / 10)
        match div:
            case 2:
                cipher = number_str_list[15]
            case 3:
                cipher = number_str_list[16]
            case 4:
                cipher = number_str_list[17]
            case 5:
                cipher = number_str_list[18]
        rem = int(num % 10)
        if rem != 0:
            units = number_str_list[rem]
    
    return cipher + units


#===========================
# get_cipher_key
def get_cipher_key(time_of_encode: str) -> str:
#===========================
    """ 
    Assemble the cipher key.
 
    :param: 'time_of_encode': Time of encode the message
    :type: str
    :raise: None
    :return: A string (the chiper key) formated like SSMMHHDDDWMM (DW - Day of week)
    :rtype: str
    """
    dt: object = datetime.strptime(time_of_encode, '%d/%m/%Y, %H:%M:%S')

    month_of_year: str = dt.strftime('%B').lower() 
    day_of_week: str = dt.strftime('%A').lower()
    
    # convert to int to avoid number line '00'
    day_of_month: str = get_string_by_number(int(dt.strftime('%d').lower()))
    hour :str = get_string_by_number(int(dt.strftime('%H').lower()))
    minute :str = get_string_by_number(int(dt.strftime('%M').lower()))
    second :str = get_string_by_number(int(dt.strftime('%S').lower()))

    return second + minute + hour + day_of_month + day_of_week + month_of_year


# ========================
if __name__ == "__main__":
    main()
