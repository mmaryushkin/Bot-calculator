class Stack():
    
    def __init__(self, stack: list):
        self.stack = stack
    
    def push(self, e):
        """ добавление элемента в стэк """
        
        self.stack.append(e)
    
    def get_last(self):
        """ Достать последний элемент из стэка """
        
        return self.stack.pop()
    
    def is_empty(self):
        """ Проверка наличия элементов в стэке """
        
        return len(self.stack) == 0
    
    def top(self):
        """ 'Верхушка' стэка - последний элемент
        В отличие от метода get_last - элемент остается в стеке """
        
        return self.stack[-1]
