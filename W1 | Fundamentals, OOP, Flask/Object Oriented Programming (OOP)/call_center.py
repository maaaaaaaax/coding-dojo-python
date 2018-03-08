class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print "Unique ID: {}, Caller Name: {}, Caller Phone Number: {}, Time of Call: {}, Reason for Call: {}".format(self.unique_id,self.caller_name,self.caller_phone_number,self.time_of_call,self.reason_for_call)
        return self

call1 = Call(000, "Max", "(123)456-7899", "08:00pm", "Wants free Apache Kafka support")
call2 = Call(001, "John", "(123)987-6543", "09:04pm", "Wants to know what Apache Kafka does")

call1.display()
print " "
call2.display()

# output is
# Unique ID: 0, Caller Name: Max, Caller Phone Number: (123)456-7899, Time of Call: 08:00pm, Reason for Call: Wants free Apache Kafka support
#
# Unique ID: 1, Caller Name: John, Caller Phone Number: (123)987-6543, Time of Call: 09:04pm, Reason for Call: Wants to know what Apache Kafka does

# when creating a new CallCenter, pass in a list of calls ie: [call1, call2]
class CallCenter(object):
    def __init__(self, calls_lst):
        self.calls_lst = calls_lst
        self.queue_size = len(calls_lst)
    # adds a new call to the end of the call list
    def add(self, call):
        self.calls_lst.append(call)
        self.queue_size = self.queue_size + 1
        return self

    # removes the call from the beginning of the list (index 0).
    def remove(self):
        self.calls_lst.pop(0)
        self.queue_size -= 1
        return self

    # prints the name and phone number for each call in the queue as well as the length of the queue.
    def info(self):
        for call in self.calls_lst:
            print "Name: {}, Phone Number: {}".format(call.caller_name,call.caller_phone_number)
        print "Queue size: {}".format(self.queue_size)
        return self

callcenter1 = CallCenter([call1, call2])
callcenter1.info()
