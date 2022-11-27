# ALBERTI CIPHER DISK
#### Video Demo:  https://youtu.be/F7_hnQfNpII

## Description:

This project is going to be about encryption. I will demonstrate of usage the encryption method named like Alberti cipher disk.

## What does encryption means?

Encryption is the transformation of information into another form or code in such a way that only the user who has the secret key can access it.

## Alberti cipher disk.

The Alberti cipher has two mixed alphabets, and the key is constantly changing during encryption, so finding one letter does not allow further progress. Frequency analysis is also impossible, because the same letter is always encrypted in different ways.

## Main idea

The main idea is that each letter from the ordinary alphabet is going to be replaced by another letter from the cipher alphabet. The cipher alphabet based on a some key.

## Permutation cipher. The theory.

Let us suppose that we want to encrypt the message like this:
> Ivan Gorshenin took Introduction to Python
> 14-Nov-2022 09:01:07

Pay attention at the end of the message. It ended with date. This will be the key!

First of all what need to be done is to prepare the cipher alphabet. As I say before, the key for this purpose will be the date which we leave at the end of the message.

So, the key is:
> 14-Nov-2022 09:01:07

Then, we need to get some parameters from this date. They are: 
- Month of the year: 'november'
- Day of the month: 'fourteen’
- Day of the week: 'monday’
- Hours: 'nine’
- Minutes: 'one’
- Seconds: 'seven'

All this parameters must be translated to text (like shown above).

As a next step, we need to combine text in this order **SSMMHHDDDWM**. So we get the message like this:
>**SEVENONENINEFOURTEENMONDAYNOVEMBER**

In order to create a cipher alphabet we need to remove duplicates characters from this line. Start from S, so there is no S, next E – remove all E, do the same for V, N and so on.

When all duplicates are removed the remain line looks like this: 
>**SEVNOIFURTMDAYB**

This line will be beginner of our cipher alphabet.

Next step is to remove duplicates from original alphabet. Duplicates means – take a symbol from cipher alphabet and remove same from the original one. Start from S, then E and so on. When this step is done, the original alphabet will look like this:
>**CGHJKLPQWXZ**

Explanation: there are only symbols which are not included to the cipher alphabet!

And the last step, we need to fill cipher alphabet by remains symbols from the original one. Take it one by one from the start and place each symbol next to the symbols in cipher alphabet.

At the end of the procedure the cipher alphabet will look like this:
>**SEVNOIFURTMDAYBCGHJKLPQWXZ**

this based on the date: 14-Nov-2022 09:01:07.

Congratulation – now we can encode our message.

## Encode

To encode the source message we need to confront each symbol from the original alphabet with the cipher one:
>origin alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
>cipher alphabet: SEVNOIFURTMDAYBCGHJKLPQWXZ

As an example, encoding my name looks like this:
>IVAN => RPSY

So if we would have a physical disk Alberti then the first circle contains original alphabet, but second one – cipher alphabet.

At last it will look like this:

_There is the message to be encrypted:_
> Ivan Gorshenin took Introduction to Python
> 14-Nov-2022 09:01:07

_Encoded message to be send will be:_
>rpsy fbhjuoyry kbbm rykhbnlvkrby kb cxkuby
>14-Nov-2022 09:01:07

## Decode

To decode encrypted message you just need to confront each symbol from the cipher alphabet with the original one. 
>cipher alphabet: SEVNOIFURTMDAYBCGHJKLPQWXZ
>origin alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ

As an example, decoding my name looks like this:
>RPSY => IVAN

## Gratitude

Thank you CS50 for this great course!
