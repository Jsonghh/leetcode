class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []
        
        for log in logs:
            log_list = log.split(' ')
            if log_list[1].isdigit():
                digit_logs.append(log)
            else:
                log_list_order = tuple(log_list[1:])
                letter_logs.append(((log_list_order), log_list[0], log))
                
        letter_logs.sort()
        
        for i in range(len(letter_logs)):
            letter_logs.append(letter_logs.pop(0)[-1])
            
        return letter_logs + digit_logs                
        