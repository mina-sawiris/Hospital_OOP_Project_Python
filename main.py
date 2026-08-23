import os
from controllers.main_controller import MainController
 
_PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(_PROJECT_ROOT, "data")
 
 
def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    app = MainController()
    app.run()
 
 
if __name__ == "__main__":
    main()

 