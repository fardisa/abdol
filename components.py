```python
import utils
from models import Model1, Model2

class Component1:
    def __init__(self, model1: Model1, model2: Model2):
        self.model1 = model1
        self.model2 = model2

    def execute(self):
        try:
            # Code to execute component
            pass
        except Exception as e:
            utils.log_error('components.py', 'Component1', str(e))

class Component2:
    def __init__(self, model1: Model1):
        self.model1 = model1

    def execute(self):
        try:
            # Code to execute component
            pass
        except Exception as e:
            utils.log_error('components.py', 'Component2', str(e))

if __name__ == "__main__":
    model1 = Model1()
    model2 = Model2()
    component1 = Component1(model1, model2)
    component1.execute()
    component2 = Component2(model1)
    component2.execute()
```