'''
The purpose of this script is to demonstrate multinomial Naive Bayes. We will be performing Naive Bayes on lists that represent email messages. Each list is a message that is either 
spam or friendly message. We start with Training Data in a list. For the sake of example, we keep the message short. We first count the number of words in each category.
Then we count the number of desired data in the inbox and divide byt he total number of words. We do the same for the spam. Then we calculate the prior probability and the final
probability that the desired combinations of words are in each mailbox.
'''

messages = [["Inbox", "Dear", "Friend", "How", "are", "you"],
            ["Inbox", "Dear", "Friend", "Where", "are", "you"],
            ["Inbox", "Dear", "Friend", "Dinner", "tonight?"],
            ["Inbox", "Dear", "Friend", "What", "is", "up"],
            ["Spam", "Dear", "Friend", "Buy", "our", "product!"],
            ["Spam", "Hello", "Team", "Deadline", "is", "near"],
            ["Spam", "Purchase", "Yours", "Today!"],
            ["Inbox", "Hello", "Jen", "Are", "you", "free"],
            ["Spam", "Don't", "forget", "to", "order", "today!"],
            ["Spam", "Dear", "Recipient", "claim", "your", "product", "Friend!"],
            ["Inbox", "Dear", "Friend", "How", "are", "you"],
            ["Inbox", "Dear", "Friend", "Dinner", "tomorrow?"]
            ]
messages_length = len(messages)

#Words in normal messages
inbox_words = 0
spam_words = 0
for m in messages:
    if "Inbox" in m:
        inbox_words += len(m)
    else:
        spam_words += len(m)

#Words in spam messages

#probablility that we see any of the desired words in inbox messages
dear_words_i = 0
friend_words_i = 0
dinner_words_i = 0

for i in range(len(messages)):
    if "Dear" in messages[i] and "Inbox" in messages[i]:
        dear_words_i += 1
    if "Friend" in messages[i] and "Inbox" in messages[i]:
        friend_words_i += 1
    if "Dinner" in messages[i] and "Inbox" in messages[i]:
        dinner_words_i += 1

p_dear_inbox = dear_words_i/inbox_words
p_friend_inbox = friend_words_i/inbox_words
p_dinner_inbox = dinner_words_i/inbox_words

#probablility that we see any of the desired words in spam messages
dear_words_s = 0
friend_words_s = 0
dinner_words_s = 0

for i in range(len(messages)):
    if "Dear" in messages[i] and "Spam" in messages[i]:
        dear_words_s += 1
    if "Friend" in messages[i] and "Spam" in messages[i]:
        friend_words_s += 1
    if "Dinner" in messages[i] and "Spam" in messages[i]:
        dinner_words_s += 1

p_dear_spam = dear_words_s/spam_words
p_friend_spam = friend_words_s/spam_words
p_dinner_spam = dinner_words_s/spam_words


#Calculate prior Probabilities
number_inbox = 0
number_spam = 0

for m in messages:
    if "Inbox" in m:
        number_inbox += 1
    else:
        number_spam += 1

prior_inbox = number_inbox/messages_length
prior_spam = number_spam/messages_length

#Calculate the probability that a message that contians Dear, Friend is normal
prob_that_dear_friend_is_inbox = prior_inbox * p_dear_inbox * p_friend_inbox

#Probability that a message that contains Dear, Friend is Spam
prob_that_dear_friend_is_spam = prior_spam * p_dear_spam * p_dear_inbox

print("The probablilty that a message that contains Dear and Friend will go to your inbox is: {0} \nThe probability that a message that contains Dear and Friend will go to your spam is: {1}".format(prob_that_dear_friend_is_inbox, prob_that_dear_friend_is_spam))


