import re
def remove_punctuation(pattern,phrase):
    for pat in pattern:
        return(re.findall(pat,phrase))
        return('\n')
        
phrase = """
        - Встать! Суд идет!
        - Да здравствует наш суд, самый гуманный суд в мире!
        - Прошу садиться. Садитесь, садитесь
        - Спасибо, я постою.
        """
pattern=['[^!.,?-]+']
 
print("".join(remove_punctuation(pattern,phrase)))