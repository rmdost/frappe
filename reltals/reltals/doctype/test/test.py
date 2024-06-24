from frappe.model.document import Document

class test(Document):
    
# Validate hook save sai pahlay kam karta ha code ko run kr k 	
    def validate(self): 
# Loop laga k saray items ko variables ma daal dya ha 
        total = 0  
        total2 = 0
        for item in self.items:
            
            total += item.num
            total2 += item.num2
            
          
            self.result2 = total + total2
            self.result = total + total2
